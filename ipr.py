# A simple domain/subdomain resovler to ip address uing 8.8.8.8 and 1.1.1.1 as dns servers 
# Make sure you have a file named a.txt in the same directory as the script, containing the list of domain/subdomains you want to resolve. After running the script, the resolved IP addresses will be written to the output.txt file in the desired format.
# Command : python3 ipr.py 
# Make sure in the same directory there is a.txt with subdomain/domains names ,single entery per line.

import socket

def resolve_domains(input_file, output_file):
    dns_servers = ['8.8.8.8', '1.1.1.1']
    
    with open(input_file, 'r') as f:
        domains = f.read().splitlines()

    resolved_domains = []
    
    for domain in domains:
        for dns_server in dns_servers:
            try:
                ip_info_list = socket.getaddrinfo(domain, None, socket.AF_INET)
                ip_addresses = [ip_info[4][0] for ip_info in ip_info_list]
                if ip_addresses:
                    resolved_domains.append((domain, ip_addresses))
                break
            except socket.gaierror:
                pass  # If domain couldn't be resolved, try the next DNS server

    with open(output_file, 'w') as f:
        for domain, ip_addresses in resolved_domains:
            for ip in ip_addresses:
                f.write(f"{domain},{ip}\n")

if __name__ == "__main__":
    input_file = "a.txt"
    output_file = "output.txt"
    resolve_domains(input_file, output_file)
    print("DNS resolution complete. Check output.txt for results.")

