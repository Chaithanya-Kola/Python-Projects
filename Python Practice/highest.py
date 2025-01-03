science = int(input("Enter your Science marks :"))
maths = int(input("Enter your maths marks :") )
social = int(input("Enter your social marks :"))
subject = ""
if (science >= maths) and (science >= social) : 
    largest = science 
    subject = "science"
elif (maths >= science) and (maths >= social) :
    largest = maths
    subject = "maths"
else:
    largest= social 
    subject = "social"

print("your highest marks are in  {} : {}".format(subject ,largest))