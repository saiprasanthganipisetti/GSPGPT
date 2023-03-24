import os
import openai

openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
while True:
  ask = input("Enter your question : ")
  print()
  if ask == "break":
    print("Thank you for using GSPGPT")
    break
  response = openai.Completion.create(
    model="text-davinci-003",
    prompt=ask,
    temperature=0.9,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
  )
  print(response["choices"][0]["text"])
  print()