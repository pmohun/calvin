import json
import requests

# #                                             #   #
#   Calvin - abstraction module over openai's API  #
# #                                             #   #


# Defile module-scoped variables
engine = "davinci"
headers = {}
prompts = {}


# Initialize module
def initialize(_api_key, _engine):
  global engine, headers, prompts

  if _engine:
    engine = _engine

  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {_api_key}"
  }

  prompts = json.load(open("./calvin/prompts.json"))

# Change engine setting
def set_engine(_engine):
  global engine
  engine = _engine

# List Engines GET
# Lists the currently available engines, and provides basic information about each option such as the owner and availability.
def list_engines():
  global headers

  url = "https://api.openai.com/v1/engines"
  response = requests.get(url, headers=headers)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()

# Retrieve Engine GET
# Retrieves an engine instance, providing basic information about the engine such as the owner and availability.
def retrieve_engine():
  global headers

  url = f"https://api.openai.com/v1/engines/{engine}"
  response = requests.get(url, headers=headers)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()

# Create Completion POST
# Create a completion. This is the main endpoint of the API.
# Returns new text as well as, if requested, the probabilities over each alternative token at each position.
def create_completion(payload):
  global headers

  url = f"https://api.openai.com/v1/engines/{engine}/completions"
  response = requests.post(url, headers=headers, json=payload)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()

def complete_prompt(prompt):
  payload = {
    "prompt": prompt,
    "max_tokens": 5,
    "temperature": 1,
    "top_p": 1,
    "n": 1
  }

  create_completion(payload)

def complete_predefined_prompt(prompt_key, index=0):
  global prompts

  if prompts[prompt_key] in prompts:
    create_completion(prompts[prompt_key][index])

  return "Unable to access predefined prompt."


# Search POST
# Perform a semantic search over a list of documents.
def search(payload):
  global headers

  url = f"https://api.openai.com/v1/engines/{engine}/search"
  response = requests.post(url, headers=headers, json=payload)

  if response.ok:
    print(f"JSON: {response.json()}")
    return response.json()
  else:
    return response.raise_for_status()

# Test function to confirm it works
def test_create_completion():
  payload = {
    "prompt": "Once upon a time",
    "max_tokens": 5,
    "temperature": 1,
    "top_p": 1,
    "n": 1
  }

  create_completion(payload)



"""
Example completion request payload
{
  "prompt": "Once upon a time",
  "max_tokens": 5,
  "temperature": 1,
  "top_p": 1,
  "n": 1,
  "stream": false,
  "logprobs": null,
  "stop": "\n"
}
"""