number = input("What is Your Number?:")
numbercount = len(number)
sum = 0
for i in number:
    sum = sum + int(i) ** numbercount

if sum == int(number):
    print("You have an armstrong number")
else:
   print("You dont have an armstrong number")
