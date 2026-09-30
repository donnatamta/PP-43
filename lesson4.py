# #სავარჯიშო 1
age = int(input("გთხოვთ შეიყვანოთ თქვენი ასაკი: "))
if age >= 18:
    print("შესვლა დაშვებულია") 
elif age >= 12 and age < 17:
    input = str(input("მშობელთან ერთად ხართ? (კი/არა)"))
if input == "კი": 
    print("შესვლა დაშვებულია")
elif input == "არა":
    print("შესვლა აკრძალულია")
if age < 12:
    print("შესვლა აკრძალულია")

#სავარჯიშო 2
first_number = int(input("პირველი რიცხვი: "))
second_number = int(input("მეორე რიცხვი: "))
third_number = int(input("მესამე რიცხვი: "))
biggest_number = first_numberა

if second_number > biggest_number:
    biggest_number = second_number

if third_number > biggest_number:
    biggest_number = third_number

print("უდიდესი რიცხვია:", biggest_number)