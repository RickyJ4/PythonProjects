import random
from game_data import data

score = 0
is_guessed = True
user_b = random.choice(data)


while is_guessed:

    user_a = user_b
    user_b = random.choice(data)
    while user_a == user_b:
        user_b = random.choice(data)

    def format_account(account):
        username = account["name"]
        user_description = account["description"]
        user_country = account["country"]
        return f"Compare A : {username}, {user_description},{user_country}"

    def followers(compare,username_a,username_b):
        score = 0
        if compare == "a":
            if username_a>  username_b:
                return True
            else:
                return False
        elif compare == "B":
            if username_b > username_a:
                return True
            else:
                return False

    user_a = random.choice(data)
    user_b = random.choice(data)
    print(f"Compare A : {format_account(user_a)} ")
    print("vs")
    print(f"Compare A : {format_account(user_b)} ")

    compare = input("Whose got more followers A or B :").lower()

    username_a = user_a["follower_count"]
    username_b = user_b["follower_count"]
    is_correct = followers(compare,username_a,username_b)

    if is_correct == True:
        score = score +1
        print(f"Correct your current score is ; {score}")
    else:
        print(f"Incorrect your final score was: {score}")
        is_guessed = False

