import json
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

url = "https://ollamaraul-70516613071.us-east4.run.app/api/generate"

print(os.getcwd())

with open("./src_ollama/tables.csv") as f:
    _tables = f.read()

CONTENT_PREFIX = "with the list of table.field type:\n" + _tables

CONTENT_METRIC = """
Please create and sql that:

for each: fact_lead_interaction.club_id, fact_lead_interaction.lead_src_id, '1' as case_number; select the count(fact_lead_interaction.LEAD_SRC_ID) on:
from fact_lead_interaction: 
    include only those with dim_crm_metadata.TYPE_DESC='LEAD_INTERACTION_TYPE' and dim_crm_metadata.CRM_METADATA_TYPE in ('Kiosk Walk-In','Manual Walk-In','Appointment Show','BeBack Appointment Show','BeBack') use dim_crm_metadata.CRM_METADATA_SRC_NUM to join with fact_lead_interaction.LEAD_INTERACTION_TYPE_SRC_ID 
    include only those fact_lead_interactions with no previous CREATE_SRC_DATE_UTC or at least 60 days have passed since the last CREATE_SRC_DATE_UTC for the same club_id and lead_src_id previous to the current CREATE_SRC_DATE_UTC
    exclude those with fact_lead_interaction.lead_src_id is null
    exclude the EMPLOYEE_SRC_ID = '100'
    exclude those DIM_LEAD.LEAD_TYPE_DESC in ('Buddy','Gympass') 
    exclude those in fact_tmp_membership   
    find the related dim_customer using customer_src_num then join dim_subscription_new using the customer_id and if the dim_suscription_new.corporate_code in dim_complimentary_corporate_code.CORPORATE_CODE is true exclude them
    
    
"""

CONTENT_END = """
avoid the use of inner queries use CTEs instead
"""

CONTENT = CONTENT_PREFIX + CONTENT_METRIC + CONTENT_END

payload = {
    "model": "qwen3-coder:30b",
    "prompt": CONTENT,
    "think": False,
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

data = json.loads(response.text)
#print(json.dumps(data, indent=2))

content = data.response
start = content.find("```sql\n")
if start != -1:
    start += len("```sql\n")
    end = content.find("```\n", start)
    if end == -1:
        end = content.find("```", start)
    sql = content[start:end]
    print(sql)
