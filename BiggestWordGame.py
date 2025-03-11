import os
import platform

# Letters and Points
letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", " "]
points = []
letter_to_points = {}

# Players
player_and_points = {}
player_and_words = {}

# Game Handlers
match = {
  "match_type": "",
  "match_rounds": "",
  "words_per_round": "",
  "player_count": 0,
}

# Function that adds player to match dictionary and player and points and words dict
def set_player(player):
  player_and_points[player] = 0
  player_and_words[player] = []
  print(f"{player} Joined")
  match["player_count"] += 1

# Word points function (Calculates the score of a word)
def score_word(word):
  point_total = 0
  for letter in word:
    if letter.upper() in letter_to_points.keys():
      point_total += letter_to_points[letter.upper()]
  return point_total

# Add Word Player (Adds word to the player and words dict)
def add_word(player, word):
    if player not in player_and_words:
        player_and_words[player] = []
    # Add the word to the player's list
    player_and_words[player].append(word)

# Update Points Total
def update_point_totals():
    for key, words in player_and_words.items():
        player_points = 0
        for word in words:
            player_points += score_word(word)
        player_and_points[key] = player_points

# Show Ranking
def show_ranking():
  update_point_totals()
  ranking = sorted(player_and_points.items(), key= lambda x: x[1], reverse=True)
  for key, value in ranking:
    print(f"- {key}: {value}")

#----------------------------------------------------
###GAME

# Setting Players
while True:
  os.system('cls' if platform.system() == 'Windows' else 'clear')
  print("==============================================")
  print("")
  print("          Wellcome to the Word game!          ")
  print("")
  print("==============================================")

  player = str(input("Type player name ('done' to continue): "))
  if player.lower() == "done" and match["player_count"] != 0:
    break
  elif player.lower() != "done":
    set_player(player)

# Setting Match Settings
while True: #Match Type
  os.system('cls' if platform.system() == 'Windows' else 'clear')
  print("==============================================")
  print("")
  print("                  Match Type:                 ")
  print("")
  print(" [1] - Every Letter Count as 1 ")
  print(" [2] - Uncommon Letters are better ")
  print("")
  print("==============================================")

  match_type = input("Choose your match type ('1' or '2'): ")
  if match_type in ["1", "2"]:
    match["match_type"] = int(match_type)
    break

while True: #Match Rounds
  os.system('cls' if platform.system() == 'Windows' else 'clear')
  print("==============================================")
  print("")
  print("                 Match Rounds:                ")
  print("")
  print("==============================================")
  try:
    match["match_rounds"] = int(input("Type the ammount of rounds you want: "))
    break
  except ValueError:
    continue

if match["match_type"] == 1:
  points = [1 for i in range(27)]
elif match["match_type"] == 2:
  points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letter_to_points = {key: value for key, value in zip(letters, points)}

while True: #Match Rounds
  os.system('cls' if platform.system() == 'Windows' else 'clear')
  print("==============================================")
  print("")
  print("                  Round Words:                ")
  print("")
  print("==============================================")
  try:
    match["words_per_round"] = int(input("Type the ammount of words you want each round: "))
    break
  except ValueError:
    continue

##Starting Game
words_used = []
for round in range(match["match_rounds"]):
  if round != 0: 
    print("\n                 Round Ranking:")
    show_ranking()
    input("\nPress ENTER to start next round")

  os.system('cls' if platform.system() == 'Windows' else 'clear')
  print("==============================================")
  print("")
  print(f"                 Round: {round+1}                ")
  print("")
  print("==============================================")

  for word_in_round in range(match["words_per_round"]):
    for player in player_and_points.keys():
      while True:
        word = input(f"{player}, type your word: ")
        if word not in words_used and word.isalpha():
          words_used.append(word)
          add_word(player, word)
          break
        elif not word.isalpha():
            print("Please enter alphabetic characters only.")
        else:
          print(f"{word} was already used")
print("\n==============================================")
print("")
print("                 Final Ranking:")
show_ranking()
print("")
print("==============================================")
