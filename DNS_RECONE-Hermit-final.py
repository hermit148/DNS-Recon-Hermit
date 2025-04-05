import subprocess
import os
import time

def print_logo():
    logo = """
    ██╗  ██╗███████╗██████╗ ███╗   ███╗██╗████████╗
    ██║  ██║██╔════╝██╔══██╗████╗ ████║██║╚══██╔══╝
    ███████║█████╗  ██████╔╝██╔████╔██║██║   ██║   
    ██╔══██║██╔══╝  ██╔══██╗██║╚██╔╝██║██║   ██║   
    ██║  ██║███████╗██║  ██║██║ ╚═╝ ██║██║   ██║   
    ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝   ╚═╝   

                      [ DNS-RECONE By HeRM!T ---:) ]
    """
    print(logo)

def get_domain():
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    return domain

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout.strip()
    except Exception as e:
        return f"Error running command: {e}"

def loading_message(task):
    print(f"[+] {task} in progress", end="", flush=True)
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print(" Done!")

def verify_dns_issue(issue, command, expected_output):
    result = run_command(command)
    if expected_output in result:
        return f"[!] WARNING: {issue} is still an issue!\n{result}\n"
    return f"[✓] {issue} is now fixed."

def dns_zone_transfer(domain):
    loading_message("Checking Zone Transfer")
    ns_command = f"dig NS {domain} +short"
    name_servers = run_command(ns_command).split("\n")

    if not name_servers or name_servers == [""]:
        return "[✓] No name servers found or Zone Transfer not possible."

    for ns in name_servers:
        ns = ns.strip()
        if ns:
            transfer_command = f"dig AXFR {domain} @{ns}"
            transfer_result = run_command(transfer_command)
            if "Transfer failed" not in transfer_result:
                return f"[!] WARNING: Zone Transfer possible on {ns}\n{transfer_result}\n"

    return "[✓] Zone Transfer not allowed. This is good!"

def subdomain_enum(domain):
    loading_message("Enumerating Subdomains")
    command = f"subfinder -d {domain}"
    result = run_command(command)
    return f"[!] Subdomains found:\n{result}" if result else "[✓] No subdomains found."

def check_spf_dkim_dmarc(domain):
    loading_message("Checking Email Security (SPF, DKIM, DMARC)")
    spf = run_command(f"dig TXT {domain} | grep 'v=spf1'")
    dkim = run_command(f"dig TXT default._domainkey.{domain}")
    dmarc = run_command(f"dig TXT _dmarc.{domain}")

    warnings = []
    if not spf:
        warnings.append("[!] WARNING: No SPF record found. Email spoofing possible!")
    if not dkim:
        warnings.append("[!] WARNING: No DKIM record found. Email integrity at risk!")
    if not dmarc:
        warnings.append("[!] WARNING: No DMARC record found. Email phishing protection missing!")

    return "\n".join(warnings) if warnings else "[✓] SPF, DKIM, and DMARC are properly configured."

def open_resolver_check():
    loading_message("Checking Open Resolver")
    result = run_command("dig +short test.openresolver.com TXT")
    return verify_dns_issue("Open Resolver detected! Risk of DNS amplification attacks", "dig +short test.openresolver.com TXT", "open resolver")

def check_dnssec(domain):
    loading_message("Checking DNSSEC")
    result = run_command(f"dig +dnssec {domain}")
    return verify_dns_issue("DNSSEC not enabled. Susceptible to DNS spoofing!", f"dig +dnssec {domain}", "ad:")

def main():
    print_logo()
    domain = get_domain()

    results = {
        "Zone Transfer": dns_zone_transfer(domain),
        "Subdomains": subdomain_enum(domain),
        "Email Security (SPF, DKIM, DMARC)": check_spf_dkim_dmarc(domain),
        "Open Resolver Check": open_resolver_check(),
        "DNSSEC Check": check_dnssec(domain)
    }

    output_filename = f"{domain}-result.txt"
    with open(output_filename, "w") as file:
        for section, result in results.items():
            file.write(f"=== {section} ===\n{result}\n\n")
    
    print(f"\n[+] Results saved to {output_filename}")
    
if __name__ == "__main__":
    main()
