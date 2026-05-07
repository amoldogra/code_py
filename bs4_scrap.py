import urllib.request
from bs4 import BeautifulSoup

URL = "https://www.projecthoneypot.org/list_of_ips.php"
with urllib.request.urlopen(URL) as response:
    html = response.read().decode('utf-8')
soup = BeautifulSoup(html, 'html.parser')
print(soup)

ip_addresses = []
for row in soup.select("table.manmx tr")[1:]:
    ip_cell = row.select_one('td a.bnone')
    if ip_cell:
        ip_addresses.append(ip_cell.text.strip())

for ip in ip_addresses:
    print(ip)



