print("Uh, oh, you've been given a", "\033[31m", "warning", "\033[0m", "for being a bad, bad person.")

name:str=input("What's your name? : ")
superpower:str=input("Your superpower : ")
manga:str=input("What's manga do you prefer? : ")
live:str=input("Where do you live? : ")

print(f"Welcome \033[32m{name}\033[0m, you have the young that like \033[33m{manga}\033[0m and live in \033[34m{live}\033[0m. I like your superpower:\033[31m{superpower}")