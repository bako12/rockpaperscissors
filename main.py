import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
while True:
  user_input = input("type Rock/Paper/Scissors or Q to quit:  ").lower()
  if user_input == "q":
    break
  elif user_input not in options:
    continue
  random_number = random.randint(0, 2)
  # Rock: 0 , Paper: 1 , Scissors: 2.
  computer_pick = options[random_number]
  print("The computer picked " + computer_pick)
  if (user_input == "rock" and computer_pick == "scissors") or (
      user_input == "scissors"
      and computer_pick == "paper") or (user_input == "paper"
                                        and computer_pick == "rock"):
    user_wins += 1
    print("Congrats you won!")
  elif user_input == computer_pick:
    print("its a draw")
    continue
  else:
    computer_wins += 1
    print("wooomp wooomp computer won go cry")

print("You won " + str(user_wins) + " times and the computer won " +
      str(computer_wins) + " times!!")
print("Ciaoo")
print("wazzap github")
