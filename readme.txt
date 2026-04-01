#follow the instructions at to access the graphic card
https://github.com/intel/ipex-llm/blob/main/docs/mddocs/Quickstart/llama_cpp_quickstart.md


#to know if I have assigned a gpu 
Go to https://console.cloud.google.com/iam-admin/quotas
Filter by GPUs (All Regions)

#run a sample nlm as in https://www.youtube.com/watch?v=GKIUmb99HQc
sudo apt-get install zstd
curl -fsSL https://ollama.com/install.sh | sh
gcloud beta run deploy --image ollama/ollama --gpu 1 --port 11434 --region us-east4
OLLAMA_HOST=<service URL from above> ollama run deepseek-r1:7b

OLLAMA_HOST=https://ollama-70516613071.us-east4.run.app ollama run deepseek-r1:7b
OLLAMA_HOST=https://ollama-70516613071.us-east4.run.app ollama run qwen3-coder:30b --FAILS

OLLAMA_HOST=https://ollamaraul-70516613071.us-east4.run.app ollama pull gemma2:2b
OLLAMA_HOST=https://ollamaraul-70516613071.us-east4.run.app ollama run llama3.3:70b "who are you?"

OLLAMA_HOST=https://ollamaraul-70516613071.us-east4.run.app ollama run glm-4.7-flash:latest "who are you?"

OLLAMA_HOST=https://ollamaraul-70516613071.us-east4.run.app ollama run qwen3-coder:30b-a3b-q4_K_M "who are you?"

##to run opencode with the remote openllama
OLLAMA_HOST=https://ollamaraul-70516613071.us-east4.run.app ollama launch opencode



curl https://ollamaraul-70516613071.us-east4.run.app/api/chat -d '{
  "model": "qwen3-coder:30b",
  "messages": [{ "role": "user", "content": "Solve: 25 * 25" }],
  "stream": false
}' | jq '.message.content'



curl https://ollamaraul-70516613071.us-east4.run.app/api/chat -d '{
  "model": "qwen3-coder:30b",
  "messages": [
    { 
      "role": "user", 
      "content": "given the following table:create table customer_metric(zone string, region string, club string, customer_cnt integer) write a single sql to to answer to answer the following question: get the total number of customers divided by: zones, regions" 
    }
  ],
  "stream": false,
   "system": "You are a SQL generator for snowflake. Only output the first raw SQL code. No conversational text, no explanations, no markdown formatting. the output should be able execute just as it is"
}' | jq '.message.content'

curl https://ollamaraul-70516613071.us-east4.run.app/api/chat -d '{
  "model": "qwen3-coder:30b",
  "messages": [
    { 
      "role": "user", 
      "content": "given the following table:create table customer_metric(zone string, region string, club string, customer_cnt integer) write a single sql to to answer to answer the following question: give me the region with the most customers" 
    }
  ],
  "stream": false,
   "system": "You are a SQL generator for snowflake. Only output the first raw SQL code. No conversational text, no explanations, no markdown formatting. the output should be able execute just as it is"
}' | jq '.message.content'

given the following table:create table customer_metric(zone string, region string, club string, customer_cnt integer); can you create a set of natural language sentences a human can use to ask for the sum of customer_cnt?

given the following table:"create table customer_metric(zone string, region string, club string, customer_cnt integer)" create an sql to retrive the total number of customers divided by: zones, regions


.\llama-cli.exe -m mistral-7b-instruct-v0.1.Q4_K_M.gguf -n 32 --prompt "Once upon a time..." -c 1024 -t 8 -e -ngl 99 --color -no-cnv

######to redeploy: in the console click in open editor and copy the dockerfile and download_model.sh the run the following commands
gcloud artifacts repositories delete raulrepository --project=llamacpp-487220 --location=us-east4

gcloud artifacts repositories create raulrepository \
        --repository-format=docker \
        --location=us-east4 \
        --description="Rauls repository" \
        --async

gcloud artifacts repositories list
gcloud artifacts repositories describe raulrepository --project=llamacpp-487220 --location=us-east4

#gcloud auth configure-docker us-east4-docker.pkg.dev
#gcloud builds submit --tag docker.pkg.dev/llamacpp-487220/us-east4-docker.pkg.dev/ollamaraul

gcloud builds submit --tag us-east4-docker.pkg.dev/llamacpp-487220/raulrepository/ollamaraul

gcloud run services add-iam-policy-binding  --member=mendozra1972@gmail.com  --role=run.admin --region=us-east4 --project=llamacpp-487220

gcloud iam service-accounts add-iam-policy-binding  70516613071@cloudbuild.gserviceaccount.com \
  --member=serviceAccount:mendozra1972@gmail.com \
  --role roles/iam.serviceAccountUser
  --project=$PROJECT \
  --region=$REGION

###to deploy the service use: or redeploy the existing one
container image url:
us-east4-docker.pkg.dev/llamacpp-487220/raulrepository/ollamaraul:latest

container port:11434

Container name: ollamaraul-1

memory:32GiB
CPU 8
GPU NVIDIA L4
number of gpus 1
no zonal redundancy
revision scaling min 0 max 1
#networking
serve this version immediatelly true

curl -H "Content-Type: application/json" http://localhost:11434/api/chat -d '{
  "model": "llama3.2:1b",
  "messages": [{
    "role": "user",
    "content": "Hello there!"
  }],
  "stream": false
}'


curl -H "Content-Type: application/json" http://localhost:11434/api/chat -d '{
  "model": "premai_io/prem-1b-sql-fp16",
  "prompt": "### Schema: CREATE TABLE schools (id INT, name VARCHAR, phone VARCHAR, open_date DATE); ### Question: List phone numbers of schools opened after 2000-01-01; ### SQL:",
  "stream": false
}'


curl -H "Content-Type: application/json" http://localhost:11434/api/chat -d '{
  "model": "nemotron-3-nano:30b",
  "messages": [{
    "role": "user",
    "content": "### Schema: CREATE TABLE schools (id INT, name VARCHAR, phone VARCHAR, open_date DATE); ### Question: List phone numbers of schools opened after 2000-01-01; ### SQL:"
  }],
  "stream": false
}'


