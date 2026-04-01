from atlassian import Confluence
import base64
import re
from bs4 import BeautifulSoup
import os

"""
confluence = Confluence(
    url='https://mendozra1972.atlassian.net',
    token= os.environ.get("CONFLUENCE_API_TOKEN")
    cloud=True
)
"""

URL = 'https://mendozra1972.atlassian.net/wiki'

USERNAME = "mendozra1972@gmail.com"
PASSWORLD =  os.environ.get("CONFLUENCE_API_TOKEN")

mixed = USERNAME + ":" + PASSWORLD
mixed_b64 = base64.b64encode(mixed.encode()) #.decode()
print( mixed_b64 )

confluence = Confluence(
    url=URL, 
    username=USERNAME, 
    password=PASSWORLD,
    cloud=True
)


if( confluence ):
    print("confluece")
else:
    exit(1)  

spaces = confluence.get_all_spaces()
slist = spaces['results']
for s in slist:
    print(s['key'], s['name'], s['type'])

# List pages for space "metricsv1"
pages = confluence.get_all_pages_from_space("metricsv1", start=0, limit=50)
print("\nPages in 'metricsv1':")
for p in pages:
    print(p['id'], p['title'])
    page = confluence.get_page_by_id(p['id'], expand='body.storage')
    content = page['body']['storage']['value']
    soup = BeautifulSoup(content, 'html.parser')
    text = soup.get_text(separator='\n')

    # Extract description
    desc_match = re.search(r'description[:\s]+(.+)', text, re.IGNORECASE)
    description = desc_match.group(1).strip() if desc_match else 'N/A'

    # Extract group by
    group_match = re.search(r'group\s+by[:\s]+(.+)', text, re.IGNORECASE)
    group_by = group_match.group(1).strip() if group_match else 'N/A'

    # Extract all case # entries by splitting at each "case N:" boundary
    case_blocks = re.split(r'(?=case\s+\d+\s*:)', text, flags=re.IGNORECASE)
    cases = [block.strip() for block in case_blocks if re.match(r'case\s+\d+\s*:', block.strip(), re.IGNORECASE)]

    print(f"\n[Page] {p['title']}")
    print(f"  Description : {description}")
    print(f"  Group By    : {group_by}")
    print(f"  Cases ({len(cases)}):")
    for c in cases:
        print(f"    - {c.strip()}")
    print("---")

print("\nEND.")