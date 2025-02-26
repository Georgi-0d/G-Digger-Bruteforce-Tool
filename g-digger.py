import asyncio
import sys
import aiohttp
import dns.asyncresolver
from colorama import Fore, init
import argparse
from argparse import RawTextHelpFormatter
import time
from concurrent.futures import ThreadPoolExecutor

init(autoreset=True)

print(Fore.RED + r"""   
   _____            _____ _____ _____  _____ ______ _____  
  / ____|          |  __ \_   _/ ____|/ ____|  ____|  __ \ 
 | |  __   ______  | |  | || || |  __| |  __| |__  | |__) |
 | | |_ | |______| | |  | || || | |_ | | |_ |  __| |  _  / 
 | |__| |          | |__| || || |__| | |__| | |____| | \ \ 
  \_____|          |_____/_____\_____|\_____|______|_|  \_\

                                                           """)

DNS_TIMEOUT = 1
CONCURRENT_LIMIT = 50

semaphore = asyncio.Semaphore(CONCURRENT_LIMIT)

async def check_subdomain(domain, subdomain):
    full_domain = f"{subdomain}.{domain}"
    resolver = dns.asyncresolver.Resolver()
    resolver.timeout = 1
    resolver.lifetime = 1
    resolver.nameservers = ['8.8.8.8', '8.8.4.4']

    try:
        answers = await resolver.resolve(full_domain, "A")
        ips = [ip.to_text() for ip in answers]
        print(f"{Fore.GREEN}[+] Found: {full_domain} -> {', '.join(ips)} (IPv4)")
    except (dns.resolver.NXDOMAIN, dns.resolver.NoAnswer, dns.exception.Timeout, dns.resolver.YXDOMAIN):
        pass
    except Exception as e:
        print(f"{Fore.RED}[!] Error resolving {full_domain}: {e}")

def check_subdomain_thread(domain, subdomain):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(check_subdomain(domain, subdomain))

async def brute_force_subdomains(domain, wordlist_path, threads=100):
    try:
        with open(wordlist_path, "r") as file:
            subdomains = file.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Wordlist file '{wordlist_path}' not found.")
        return

    with ThreadPoolExecutor(max_workers=threads) as executor:
        tasks = []
        for subdomain in subdomains:
            task = executor.submit(check_subdomain_thread, domain, subdomain)
            tasks.append(task)

        for task in tasks:
            task.result()

async def check_subdirectory(url, subdirectory):
    full_url = f"{url}/{subdirectory}"
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(full_url) as response:
                if response.status == 200:
                    print(f"{Fore.GREEN}[+] Found: {full_url}")
        except Exception as e:
            pass

async def brute_force_directories(base_url, wordlist_path):
    try:
        with open(wordlist_path, "r") as file:
            subdirectories = file.read().splitlines()
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Wordlist file '{wordlist_path}' not found.")
        return

    tasks = []
    for subdirectory in subdirectories:
        task = check_subdirectory(base_url, subdirectory)
        tasks.append(task)

    for i in range(0, len(tasks), 10):
        chunk = tasks[i:i + 10]
        await asyncio.gather(*chunk)
        await asyncio.sleep(0.1)

def main():
    parser = argparse.ArgumentParser(
        description='Subdomain and Subdirectory Bruteforce Tool',
        formatter_class=RawTextHelpFormatter,
        epilog="Example:\n"+Fore.RED+" For subdomains: python g-digger.py -s google.com -w wordlist.txt "+Fore.GREEN+"\n For subdirectories: python g-digger.py -d https://google.com -w wordlist.txt"
    )
    parser.add_argument(
        '-s', '--subdomain',
        help='Subdomain bruteforce mode. Specify domain (e.g., example.com).'
    )
    parser.add_argument(
        '-d', '--directory',
        help='Subdirectory bruteforce mode. Specify base URL (e.g., https://example.com).'
    )
    parser.add_argument(
        '-w', '--wordlist',
        required=True,
        help='Path to the wordlist file.'
    )

    args = parser.parse_args()

    try:
        start_time = time.time()
        if args.subdomain:
            print(f"{Fore.YELLOW}[*] Starting subdomain bruteforce for {args.subdomain}...")
            asyncio.run(brute_force_subdomains(args.subdomain, args.wordlist, threads=50))
        elif args.directory:
            print(f"{Fore.YELLOW}[*] Starting subdirectory bruteforce for {args.directory}...")
            asyncio.run(brute_force_directories(args.directory, args.wordlist))
        else:
            print(f"{Fore.RED}[*] Please specify a mode. Use --help for usage instructions.")

        end_time = time.time()
        elapsed_time = end_time - start_time
        print("")
        print(f"{Fore.GREEN}[*] Time taken: {elapsed_time:.3f} seconds")
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}[*] Operation canceled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"{Fore.RED}[*] Error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
