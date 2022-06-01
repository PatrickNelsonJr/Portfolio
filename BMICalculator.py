#This logic is used to calculate a person's BMI(Body Mass Index)
#BMI is used as a quick screening tool for determining obesity/body fatness
#BMI formula: (weight/height^2) where weight MUST be in kilograms(kgs) and height MUST be given in meters(m)
print('Hello! Welcome to the BMI calculator! \n Congratulations on choosing to monitor your health.') 
print(' ')
print('Please refer to the following categories below for your BMI results: \n Underweight BMI: greater than 18.5\n Normal BMI: 18.5 - less than 25\n Overweight BMI: 25-less than 30\n Obesity BMI: 30 of higher')
print(' ')
weight=float(input('Please enter your weight in kilograms: '))
print('Thank you!')
height=float(input('Now please enter your height in meters: '))

BMI=(weight/height**2)
category ='undefined'
if BMI<18.5:
     category=('Underweight')
elif BMI>=18.5 and BMI<25:
    category=('Normal')
elif BMI>=25 and BMI<30:
    category=('Overweight')
elif BMI>=30:
    category('Obesity')

print('Your BMI is: '+str(BMI))
print('Your BMI Category is: '+ str(category))

    
