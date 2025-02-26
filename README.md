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

- ```bash-s, --subdomain```: Run subdomain brute-forcing on the specified domain.
- ```bash-d, --directory```: Run subdirectory brute-forcing on the specified base URL.
- ```bash-w, --wordlist``` : Path to the wordlist file for brute-forcing.

## Note

### Key Points:
1. **Installation**: Explains how to clone the repo and install dependencies.
2. **Usage**: Details on how to run the tool in subdomain and subdirectory brute-forcing modes.
3. **Command-Line Options**: A breakdown of the available options for the user.
4. **Example**: Simple usage examples for both modes.
5. **Error Handling**: Basic error-handling explanation for interruptions and incorrect file handling.
6. **License**: Mentions the MIT license for open-source projects. You can change it based on your own preference.

## Author

#### Georgi-0d

