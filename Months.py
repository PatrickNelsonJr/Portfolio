#This code is used to output a month of the year associated with a number input of 1-12



num =int(eval(input("Enter a number 1-12 and I will return the name of the month associated with that number: ")))

if num==1:  print("January")
elif num==2:    print("February")
elif num==3:    print("March")
elif num==4:    print("April")
elif num==5:    print("May")
elif num==6:    print("June")
elif num==7:    print("July")
elif num==8:    print("August")
elif num==9:    print("September")
elif num==10:   print("October")
elif num==11:   print("November")
elif num==12:   print("December")
else:
    print("You did not input a number 1-12")

