# A simple domain/subdomain resovler to ip address uing 8.8.8.8 and 1.1.1.1 as dns servers 
# Make sure you have a file named a.txt in the same directory as the script, containing the list of domain/subdomains you want to resolve. After running the script, the resolved IP addresses will be written to the output.txt file in the desired format.
# Command : python3 ipr.py 
# Make sure in the same directory there is a.txt with subdomain/domains names ,single entery per line.

import dns.resolver

def resolve_domain(domain):
    resolver = dns.resolver.Resolver()
    resolver.nameservers = ['8.8.8.8', '1.1.1.1']
    
    try:
        result = resolver.query(domain, 'A')
        ip_addresses = ', '.join(str(ip) for ip in result)
        return ip_addresses
    except dns.resolver.NXDOMAIN:
        return "Domain not found"
    except dns.resolver.Timeout:
        return "Timeout"
    except Exception as e:
        return str(e)

input_filename = "a.txt"
output_filename = "output.txt"

with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
    for line in input_file:
        domain = line.strip()
        ip_addresses = resolve_domain(domain)
        output_line = f"{domain}, {ip_addresses}\n"
        output_file.write(output_line)

print("IP addresses resolved and written to output.txt.")

