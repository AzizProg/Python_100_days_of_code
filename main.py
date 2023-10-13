print("Welcome in the jungle ")
choice:str=input("Manga and Anime, what do you prefer?").lower()
if choice=="manga":
    print("Nice , you a right fan")
    manga:str=input("Manga's name :").lower()
    if manga=="jujutsu kaisen" or "naruto" or "one piece" or "dragon ball":
      print("You an old fan")
    else:
      print(f"I don't know {manga} but it must to be fun ! ")
elif choice=="anime":
  print("Gooood! you must to like animations")
  anime:str=input("Your anime name").lower()
  if anime=="jujutsu kaisen" or "naruto" or "one piece" or "dragon ball":
    print("You an old fan")
  else:
    print(f"I don't know {anime} but it must to be fun ! ")
else:
  print("I see that you don't like anime or manga")