import os
import requests

API_KEY = os.getenv("SECURITYTRAILS_API_KEY")
domain = input("Enter the domain name: ")

all_domains = []
page = 1
limit = 1000  # Adjust based on API docs

while True:
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {"APIKEY": API_KEY}
    params = {"page": page, "limit": limit}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print("Error:", response.status_code, response.text)
        break
    data = response.json()
    subdomains = data.get("subdomains", [])
    if not subdomains:
        break
    for sub in subdomains:
        all_domains.append(f"{sub}.{domain}")
    print(f"Page {page} done, added {len(subdomains)} domains")
    page += 1

output_file = f"{domain}_domains.txt"
with open(output_file, "w") as f:
    for d in all_domains:
        f.write(d + "\n")

print(f"All domains saved to {output_file}")

