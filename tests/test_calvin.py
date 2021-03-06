import calvin

# Arrange, Act, Assert

def test_calvin(api_key, engine):
  print("\nBegin Testing Calvin Module ...\n")
  
  print("\nTesting initialize method...\n")
  # Initialize calvin module
  calvin.initialize(api_key, engine)

  print("\nTesting module-scoped globals...\n")
  # Get module-scoped globals & validate them
  calvin_api_key, calvin_engine, calvin_headers, calvin_prompts = calvin.get_globals()
  assert(calvin_api_key == api_key)
  assert(calvin_engine == engine)
  assert(calvin_headers["Content-Type"] == "application/json")
  assert(calvin_headers["Authorization"] == f"Bearer {calvin_api_key}")

  print("\nTesting engine repsonse...\n")
  # Make API to get list of engine
  engines_response = calvin.list_engines()

  print("\nTesting current module engine response...\n")
  # Assert current module engine exists in response
  assert(any(engine["id"] == calvin_engine for engine in engines_response["data"]))

  print("\nTesting setting a new engine...\n")
  # Make API to set a new engine and subsequently retrieve the engine
  calvin_engine = "ada"
  calvin.set_engine(calvin_engine)
  engine_response = calvin.retrieve_engine()

  print("\nTesting current engine matches retrieved engine...\n")
  # Assert current module engine matches retrieved engine
  assert(engine_response["id"] == calvin_engine)

  print("\nTesting complete prompt method...\n")
  # Make API to complete test prompt
  response_1 = calvin.complete_prompt(prompt="Once upon a time", max_tokens=5, temperature=1, top_p=1, n=1)
  assert(type(response_1) is dict)
  assert(type(response_1["id"]) is str)
  assert(type(response_1["choices"]) is list)
  assert(type(response_1["choices"][0]["text"]) is str)

  print("\nTesting complete predefined method (no custom prompt)...\n")
  # Make API to complete predefined prompt (no custom prompt added)
  response_2 = calvin.complete_predefined_prompt(prompt_key="philosopher")
  assert(type(response_2) is dict)
  assert(type(response_2["id"]) is str)
  assert(type(response_2["choices"]) is list)
  assert(type(response_2["choices"][0]["text"]) is str)

  print("\nTesting complete predefined method (custom prompt)...\n")
  # Make API to complete predefined prompt (custom prompt added)
  response_3 = calvin.complete_predefined_prompt(prompt_key="philosopher", index=0, prompt="without a reason the story took a left turn which no one would predicted.")
  assert(type(response_3) is dict)
  assert(type(response_3["id"]) is str)
  assert(type(response_3["choices"]) is list)
  assert(type(response_3["choices"][0]["text"]) is str)

  print("\nFinish Testing Calvin Module\n")
