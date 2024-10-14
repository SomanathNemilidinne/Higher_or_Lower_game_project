import random
logo = """
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = """
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""
import game_data
print(logo)
first_choice = random.choice(game_data.data)
print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
print("\n" * 1)
score = 0
continuation = True
while continuation:
    print(vs)
    second_choice = random.choice(game_data.data)
    while second_choice == first_choice:
        second_choice = random.choice(game_data.data)
    print(f"Against B: {second_choice['name']}, a {second_choice['description']}, from {second_choice['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B' :  ").upper()
    if user_choice == "A" and first_choice["follower_count"] > second_choice["follower_count"] or user_choice == "B" and second_choice["follower_count"] > first_choice["follower_count"]:
        score += 1
        print("\n" * 30)
        print(logo)
        print(f"You're right! Current score: {score}")
        first_choice = second_choice
        print(f"Compare A: {first_choice['name']}, a {first_choice['description']}, from {first_choice['country']}")
    elif user_choice == "B" and first_choice["follower_count"] > second_choice["follower_count"] or user_choice == "A" and second_choice["follower_count"] > first_choice["follower_count"]:
        print("\n" * 30)
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        continuation = False
    else:
        print("Wrong input! DUMBO, Try again with both your eyes open.")
