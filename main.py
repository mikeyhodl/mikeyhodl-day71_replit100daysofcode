# password = "baldy1"
# password = hash(password)
# print(password)

# # This will output a really long number

# from replit import db

# userName = "mike"
# password = "owish"
# password = hash(password)
# db[userName] = password # Stores the hashed password in the database under the username key 'david'

# print(password)

# from replit import db

# print(db["mike"])

# from replit import db

# ask = input("Password >") # Get the input
# ask = hash(ask) # Hash the input

# if ask == db["mike"]: #compare hash of input to stored hash.
#   print("Login successful")
# else:
#   print("Login failed")

# from replit import db

# password = "...password..&*&^%$%#$%^*()."
# salt = 10221

# newPassword = f"{password}{salt}" # append the salt
# newPassword = hash(newPassword) # hash the lot

# print(newPassword)


# from replit import db

# password = "mikee"
# salt = 10221
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)
# print(newPassword)

# password = "mikee"
# salt = 39820
# newPassword = f"{password}{salt}"
# newPassword = hash(newPassword)
# print(newPassword)


# from replit import db

# ans = input("Password >") # Get the input
# salt = db["mikee"]["salt"] # Get the salt from the database.
# newPassword = f"{ans}{salt}"
# newPassword = hash(newPassword) # Hash the concatenated string

# if newPassword == db["owinoo"]["password"]: #compare hash of newPassword to stored hash.
#   print("Login successful")

import os, time, random
from replit import db

def createUser():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username in keys:
    print("ERROR: Username exists")
    return

  salt = random.randint(1000, 9999)
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)
  
  db[username] = {"password": newPassword, "salt": salt}

  print("User added")

def login():
  time.sleep(1)
  os.system("clear")
  username = input("Username: ")
  password = input("Password: ")
  keys = db.keys()
  if username not in keys:
    print("ERROR: Username does not exists")
    return

  salt = db[username]["salt"]
  newPassword = f"{password}{salt}"
  newPassword = hash(newPassword)

  if db[username]["password"]==newPassword:
    print("Logged in")
  else:
    print("Username or password incorrect")


while True:
  menu = input("1: New User\n2: Login\n> ")
  if menu == "1":
    createUser()
  elif menu == "2":
    login()
  else:
    keys = db.keys()
    for key in keys:
      print(db[key])