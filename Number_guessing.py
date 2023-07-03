import random

number_of_times = input("How many times do you wanna play this game: ")

if number_of_times > 0
  secret_number = random.randint(1,99)
  input_number = input("Enter any number: ")
  if input_number == secret_number:
    print("CONGRATS!! YOU WON! ")
    number_of_times += 1
  else:
    print(NO > Try again... )
    number_of_times += 1
