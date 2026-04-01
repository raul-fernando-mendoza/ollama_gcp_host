import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://ollamaraul-70516613071.us-east4.run.app/api/chat"

with open("tables.csv") as f:
    _tables = f.read()

CONTENT_PREFIX = "with the list of table.field type:\n" + _tables

CONTENT_METRIC = """
Please create and sql that:

for each: customer_id, 1 as case_number; select the subscription_id from:
the latest dim_subscription_new with the latest effective_date and subscription_type = ‘Membership’ and is_current_record = true
"""

CONTENT_END = """
avoid the use of inner queries use CTEs instead
"""

CONTENT = CONTENT_PREFIX + CONTENT_METRIC + CONTENT_END

payload = {
    "model": "qwen3-coder:30b",
    "messages": [
        {
            "role": "user",
            "content": CONTENT,
        }
    ],
    "stream": False,
    "system": (
        "You are a SQL generator for snowflake. "
        "Only output the first raw SQL code. "
        "No conversational text, no explanations, no markdown formatting. "
        "the output should be able execute just as it is"
    ),
}

response = requests.post(url, json=payload, verify=False)
response.raise_for_status()

data = response.json()
#print(json.dumps(data, indent=2))

content = data["message"]["content"]
start = content.find("```sql\n")
if start != -1:
    start += len("```sql\n")
    end = content.find("```\n", start)
    if end == -1:
        end = content.find("```", start)
    sql = content[start:end]
    print(sql)
