from game_data import data
import random
from art import vs
from art import logo
from replit import clear

random1 = random.choice(data)
random2 = random.choice(data)

score = 0
if random1 == random2:
  random2 = random.choice(data)
play = True
while play == True:
  
  random3 = random.choice(data)

  if random2 == random3:
    random3 = random.choice(data)

  print(logo)
  if score > 0:
    print(f'Correct; Current score is {score}')
  print(f"Compare A: {random1['name']}, a {random1['description']}, from {random1['country']}. ")
  print(random1["follower_count"])
  print(vs)
  print(f"Against B: {random2['name']}, a {random2['description']}, from {random2['country']}. ")
  print(random2["follower_count"])
  ask = input('Who has more followers? A or B: ')
  

  answer = ''
  if random1['follower_count'] > random2["follower_count"]:
    answer = 'a'
  elif random2["follower_count"] > random1['follower_count']:
    answer = 'b'
  if ask.lower() == answer:
    score += 1
    random1 = random2
    random2 = random3
    clear()
  else:
    print(f'Sorry that was incorrect; final score is {score}.')
    play = False




  
  





