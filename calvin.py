import openai, requests, os, json

def list_prompts():
  f = open('prompts.json')
  data = json.load(f)
  print(list(data.keys());
  return data

def create(prompt, data):
  text = input()
  response = openai.Completion.create(engine="davinci", prompt=data[prompt][0]['prompt'] + text, max_tokens=150)
  output = response["choices"][0]['text']

if __name__ == 'main':
  data = list_prompts
  print('Please input a prompt: ')
  prompt = input()
  create(prompt, data)