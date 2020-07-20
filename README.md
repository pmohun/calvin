# calvin

## What is it?

**calvin** is a Python library designed to improve the developer experience when working with pretrained language models. **calvin** provides premade prompts for interacting with language models like GPT-3. It simplifies the learning curve by providing easy to use examples and sample text to get started. Additionally, it has the broader goal of becoming **the most comprehensive repository of quality prompts for interacting with language models.**

It is named after [Susan Calvin](https://en.wikipedia.org/wiki/Susan_Calvin), Chief Robopsycologist of US Robots from Asimov's novels. 

## Main Features

- A json file with quickstart prompts and hyperparameter settings for common prompts
- A wrapper for the OpenAI API

## Where to get it
The source code is currently hosted on GitHub at:
https://github.com/philmohun/calvin

## Dependencies
- [OpenAI](https://pypi.org/project/openai/)

## How to use this library

- Clone locally (pip coming soon) and launch from root directory
- ```from calvin import calvin # import package``` 
- ```calvin = calvin.Calvin("xx-yy-zz") # set API key```
- ```response = calvin.generate(calvin.prompts['philosopher'][0]).json()['choices'][0]['text'] # generate response using preset "philosopher" prompt" ```

To see other prompts:
- ``` calvin.list_prompts() ```
