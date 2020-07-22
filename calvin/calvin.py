import json
import requests

# #                                               # #
#   calvin - abstraction module over openai's API   #
# #                                               # #


# Define module-scoped variables
engine = None
api_key = None
headers = {}
prompts = {}

# Define organization specific variables for future language models
organizations = {
  'openai': {
    #TODO: Change to base_url and add suffix within methods
    'url': 'https://api.openai.com/v1/engines/{engine}/completions',
    'engine': 'davinci',
    'headers': {
      "Content-Type": "application/json",
      "Authorization": "Bearer {api_key}"
    }
  }
}


# Initialize module
def initialize(_api_key, _org = 'openai'):
  # Define global variables to update outside scope of function
  global organizations, engine, url, headers, prompts, api_key

  engine = organizations[_org]['engine'] #TODO: add parameter to allow user to instantiate with different engine than davinci
  url = organizations[_org]['url'].format(engine=engine)
  headers = organizations[_org]['headers']
  prompts = json.load(open("./calvin/prompts.json"))
  api_key = _api_key

  # set API key in headers
  headers['Authorization'] = headers['Authorization'].format(api_key = _api_key)

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

def test_gen(_prompt):

  global api_key
  
  url = f"https://api.openai.com/v1/engines/{engine}/completions"
  headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {_api_key}"
  }

# Create Completion POST
# Create a completion. This is the main endpoint of the API.
# Returns new text as well as, if requested, the probabilities over each alternative token at each position.

def generate(_prompt, input = "", _predefined = False, _temperature = 0.5, _max_tokens = 50, _top_p = 1, _n = 1, _prompt_index = 0):
  
  global engine, headers, prompts, url, prompts
  
  if _predefined == True:
    try:
      if _prompt in prompts:
        payload = prompts[_prompt][_prompt_index]
        response = requests.post(url, headers, json=payload)
    except:
      print('Prompt not found in prompt list.')
  else:
    payload = {
      "prompt": _prompt,
      "max_tokens": _max_tokens,
      "temperature": _temperature,
      "top_p": _top_p,
      "n": _n
    }
    response = requests.post(url, headers, json=payload)

  try:
    if response.ok:
      print(f"JSON: {response.json()}")
      return response.json()
    else:
      return response.raise_for_status()
  except Exception as e:
    print(e)
    

def create_completion(payload):
  global headers, url

  response = requests.post(url, headers, json=payload)

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
  global headers, url

  url = url + '/search'
  response = requests.post(url, headers, json=payload)

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
