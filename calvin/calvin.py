import openai, requests, os, json

def prompt_list():
  f = open('prompts.json')
  data = json.load(f)
  print(list(data.keys()))
  return data

def create(prompt, data):
  #text = input()
  response = openai.Completion.create(engine="davinci", prompt=data[prompt][0]['prompt'], max_tokens=150)
  output = response["choices"][0]['text']

if __name__ == "__main__":
  data = prompt_list
  print(type(data))
  print('Please input a prompt: ')
  prompt = input()
  create(prompt, data)