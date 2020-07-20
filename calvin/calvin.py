import openai
import requests
import os
import json
import argparse
import sys
import tqdm


import json
import requests

# calvin - abstraction layer over openai's API
class Calvin:

  # Constructor
  def __init__(self, api_key, engine="davinci"):
    self.engine = engine
    self.headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
      }
    self.prompts = json.load(open("./calvin/prompts.json"))

  # Change engine setting
  def set_engine(self, engine):
    self.engine = engine

  # List Engines GET
  # Lists the currently available engines, and provides basic information about each option such as the owner and availability.
  def list_engines(self):
    url = "https://api.openai.com/v1/engines"
    response = requests.get(url, headers=self.headers)
    print(response.text)

    return response.text

  # Retrieve Engine GET
  # Retrieves an engine instance, providing basic information about the engine such as the owner and availability.
  def retrieve_engine(self):
    url = f"https://api.openai.com/v1/engines/{self.engine}"
    response = requests.get(url, headers=self.headers)
    print(response.text)

    return response.text

  # Create Completion POST
  # Create a completion. This is the main endpoint of the API.
  # Returns new text as well as, if requested, the probabilities over each alternative token at each position.
  def create_completion(self, payload):
    url = f"https://api.openai.com/v1/engines/{self.engine}/completions"
    response = requests.post(url, headers=self.headers, json=payload)
    print(response.text)

    return response

  # Search POST
  # Perform a semantic search over a list of documents.
  def search(self, payload):
    url = f"https://api.openai.com/v1/engines/{self.engine}/search"
    response = requests.post(url, headers=self.headers, json=payload)
    print(response.text)

    return response.text

  # Test function to confirm it works
  def test_create_completion(self):
    payload = {
      "prompt": "Once upon a time",
      "max_tokens": 5,
      "temperature": 1,
      "top_p": 1,
      "n": 1
    }

    self.create_completion(payload)

  # Import premade prompts from json
  def load_json(self):
    f = open("./calvin/prompts.json")
    data = json.load(f)
    return data

  # List available prompts
  def list_prompts(self):
    data = self.prompts
    print(list(data.keys()))
    return data



def create(prompt, data):
  #text = input()
  response = openai.Completion.create(engine="davinci", prompt=data[prompt][0]['prompt'], max_tokens=150)
  output = response["choices"][0]['text']

stop = "\n-"

def main(prompt):

  # TODO: add check for API key from class 'Calvin'
  openai.api_key = Calvin.headers['Authorization']
  data = json.load(open("prompts.json"))
  parser = argparse.ArgumentParser(description=None)
  parser.add_argument(
      "-v",
      "--verbose",
      action="count",
      dest="verbosity",
      default=0,
      help="Set verbosity.",
  )
  parser.add_argument("-n", "--number", type=int, default=10)
  parser.add_argument("-e", "--engine", default="davinci")
  parser.add_argument("-b", "--best_of", type=int)
  parser.add_argument("-m", "--max_batch", type=int, default=25)
  args = parser.parse_args()

  n = args.number
  batches = []
  while n > 0:
      take = min(n, args.max_batch)
      batches.append(take)
      n -= take

  choices = []
  for b in tqdm.tqdm(batches):
      completion = openai.Completion.create(
          prompt=prompt,
          n=b,
          engine=args.engine,
          max_tokens=300,
          stop=stop,
          temperature=data[prompt][0]['temperature'],
          logprobs=0,
      )
      choices += completion.choices

  def score(a):
      return sum(a.logprobs.token_logprobs) / len(a.logprobs.token_logprobs)

  choices = sorted(choices, key=lambda a: -score(a))
  for i, choice in enumerate(choices):
      print(f"======")
      print(choice.text.strip())

  return 0

if __name__ == "__main__":
    prompt = input('Enter prompt: ')
    sys.exit(main(prompt))