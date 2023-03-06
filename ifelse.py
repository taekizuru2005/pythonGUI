#ตรวจสอบเกรด
grade = int(input("input your grade: "))

if grade >= 80:
    print("Grade: A")
elif grade >= 70:
    print("Grade: B")
elif grade >= 60:
    print("Grade: C")
elif grade >= 50:
    print("Grade: D")
else:
    print("Grade: F")

print('\n')
#ตรวจสอบ username and password
username = str(input("Username: "))
password = str(input("Password: "))

if username == "admin" and password == "Ad13n@23t":
    print("Welcome, admin")
else:
    print("You are not admin.")

print('\n')
#คำนวน BMI
height = int(input("Height (cm): ")) / 100 #รับค่าเป็นหน่วย cm และแปลงเป็น m โดยนำไปหาร 100
weight = int(input("Weight (kg): "))
bmi = weight / (height * height)
bmi = float('%.2f' %(bmi)) #แปลงเป็นทศนิยม2ตำแหน่ง

print("BMI is " + str(bmi))
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal weight")
else:
    print("Underweight")



