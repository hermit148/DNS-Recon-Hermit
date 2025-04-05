#!/bin/bash

# Update system
sudo apt update -y && sudo apt upgrade -y

# Install essential DNS utilities
sudo apt install -y dnsutils whois curl jq git

# Install subfinder (for subdomain enumeration)
git clone https://github.com/projectdiscovery/subfinder.git
cd subfinder/v2/cmd/subfinder || exit
go build
sudo mv subfinder /usr/local/bin/
cd ../../../..
rm -rf subfinder

# Install Amass (another powerful subdomain tool)
sudo apt install -y amass

# Install dnsrecon (for DNS record enumeration)
sudo apt install -y dnsrecon

# Install dig (already included in dnsutils, but ensuring it's there)
sudo apt install -y bind9-dnsutils

# Install Nmap (useful for additional network scans)
sudo apt install -y nmap

# Verify installations
echo "\n[+] Installed Tools:\n"
which dig && dig -v
which subfinder && subfinder -version
which amass && amass -version
which dnsrecon && dnsrecon -h | head -n 2
which nmap && nmap --version

echo "\n[+] All tools installed successfully!"
