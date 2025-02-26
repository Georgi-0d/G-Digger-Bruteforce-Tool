# Subdomain and Subdirectory Bruteforce Tool

A powerful tool for brute-forcing subdomains and subdirectories of a given domain or website. This tool helps security researchers and penetration testers identify hidden subdomains and directories that may not be publicly listed.

## Features

- **Subdomain Bruteforce**: Discover subdomains of a given domain using a wordlist.
- **Subdirectory Bruteforce**: Find hidden directories within a specified base URL.
- **Asynchronous Requests**: Fast and efficient due to asyncio and aiohttp for non-blocking network calls.
- **Color-Coded Output**: Easy-to-read output with color coding using `colorama`.
- **Customizable**: Supports custom wordlists for brute-forcing subdomains and subdirectories.

## Installation

To use this tool, you need Python 3.6+ installed.

### Clone the repository

```bash
git clone https://github.com/yourusername/subdomain-subdirectory-bruteforce.git
cd subdomain-subdirectory-bruteforce
```

## Install Dependencies

```bash
pip3 install -r requirements.txt
```

## Usage

### Subdomain Bruteforce:

- Use the **-s** or **--subdomain** option followed by the domain.
- Use the **-w** or **--wordlist** option for adding wordlist.

```bash
python3 g-digger.py -s google.com -w wordlist.txt
```

### Subdirectory Bruteforce:

- Use the **-d** or **--directory** option followed by the base URL.
- Use the **-w** or **--wordlist** option for adding wordlist.

```bash
python3 g-digger.py -d https://google.com -w wordlist.txt
```

## Command-Line Options:

- ```-s, --subdomain```: Run subdomain brute-forcing on the specified domain.
- ```-d, --directory```: Run subdirectory brute-forcing on the specified base URL.
- ```-w, --wordlist``` : Path to the wordlist file for brute-forcing.

## Note

**This tool is intended for educational and ethical security testing purposes only. Always have proper authorization before performing penetration testing on any network or website.**

## Author

#### Georgi-0d

