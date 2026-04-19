#check if number is a factor of a number or not
mainnum = int(input("What is the number you want to test?:"))
factornum = int(input("What is the factor you want to test?: "))

if mainnum % factornum == 0:
    print(f"{factornum} is a factor of {mainnum}")
else:
    print(f"{factornum} is not a factor of {mainnum}")


