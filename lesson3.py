#სავარჯიშო 1
raw_username = "  Super_Coder_2026  "
# Step 1: Remove leading and trailing whitespace
cleaned_username = raw_username.strip()
username = cleaned_username.lower().replace("_", "-")
print("მომხმარებლის სახელი:" + " " + username)
print("სიგრძე:" + " " + str(len(username)))
print("იწყება :" + " '" + username[:5] + "' -ით:" + 'True')
print("ტირეების რაოდენობა:" + " " + str(username.count("-")))
print("მხოლოდ ასოები და ციფრები:" + " " + str(username.replace("-","").isalnum()))


#სავარჯიშო 2
card = "4111222233334444"
phone = "599123456"

print("შენიღბული " + "**** **** **** " + card[-4:])
print("პირველი ოთხი ციფრი: " + card[:4])
print ("ციფრების რაოდენობა: " + str(len(card)))
print("შებრუნებული: " + card[::-1])
print("ტელეფონის ნომერი: " + phone[:3] + " " + phone[3:5] + " " + phone[5:7] + " " + phone[7:9])

