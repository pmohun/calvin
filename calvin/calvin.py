import openai
import requests
import os
import json
import argparse
import sys
import tqdm


def load_json():
  f = open('../prompts.json')
  data = json.load(f)
  return data

def prompt_list():
  data = load_json()
  print(list(data.keys()))
  return data

def create(prompt, data):
  #text = input()
  response = openai.Completion.create(engine="davinci", prompt=data[prompt][0]['prompt'], max_tokens=150)
  output = response["choices"][0]['text']

stop = "\n-"

def main(prompt):
    data = load_json()
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