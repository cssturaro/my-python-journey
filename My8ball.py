import random

name = input("Type your name: ")

responses = [
  "Yes, definitely",
  "It is decidedly so",
  "Without a doubt",
  "Reply hazy, try again",
  "Ask again later",
  "Better not tell you now",
  "My sources say no",
  "Outlook not so good",
  "Very doubtful"
  ]

while True:
  question = input(f'{name}, Type your question (or type "exit" to quit): ')
  
  if question.lower() == 'exit':
    break

  random_number = random.randint(1, 9)
  print(responses[random_number - 1])
