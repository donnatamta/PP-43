
#სავარჯიშო 1
temp = input("გთხოვთ შეიყვანოთ ტემპერატურა ცელსიუსში: ")
print("თქვენი ტემპერატურა ფარენჰეიტშია: " , (float(temp) * 9 / 5) + 32)

#სავარჯიშო 2
total_seconds = input("გთხოვთ შეიყვანოთ დრო წამებში: ")
hours = int(total_seconds) // 3600
minutes = (int(total_seconds) % 3600) // 60
seconds = int(total_seconds) % 60
print(f"თქვენი დროა: {hours} საათი, {minutes} წუთი, {seconds} წამი")

#სავარჯიშო 3
check = float(input("გთხოვთ შეიყვანოთ თანხა: "))
tips_percent = int(input("გთხოვთ შეიყვანოთ ჩაის თანხის პროცენტი: "))
persons = int(input("გთხოვთ შეიყვანოთ ადამიანების რაოდენობა: "))
print("ჩაის თანხა იქნება: " , (check * tips_percent / 100))
print("სულ გადასახდელი: " ,  (check + (check * tips_percent / 100)))
print("თქვენი თითოეული ადამიანის ჩაის თანხა იქნება: " , round((check + (check * tips_percent / 100)) / persons, 2))
