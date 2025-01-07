secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

enter_number = int(input(""))

while enter_number!=777:
    print("Ha ha! You're stuck in my loop!")
    enter_number = int(input("So, what is the secret number?\n"))

print(f"{enter_number}\nWell done, muggle! You are free now.")