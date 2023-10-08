manga:str=input("Do you prefer Jujutsu Kaisen or Naruto : ").lower()
  
if manga=="jujutsu kaisen":
  print(f"\nYou prefer \033[32m{manga}\033[0m, you are in the present.")
elif manga=="naruto":
  print(f"\nYou like \033[32m{manga}\033[0m, you are a nostagic.")
else:
  print(f"I don't know this \033[33m{manga}\033[0m but it must to be fun!")