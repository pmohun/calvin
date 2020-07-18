import openai, requests, os, json

f = open('prompts.json')
data = json.load(f)

def list_prompts():
  print(list(data.keys());

r = requests.get("https://api.openai.com/v1/engines/davinci/completions/browser_stream", 
  headers=headers,
  stream=True,
  params={
    "prompt": 'Once upon a time',
    "max_tokens": 3,
})
for line in r:
  print(line)
