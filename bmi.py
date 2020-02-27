print("Welcome in BMI Calculator")
choose = int(input("Do you wish to enter: \n1 - metric units or\n2 - imperial units\n(1/2): "))

if choose == 1:
    height = float(input("Please enter your height input meters (decimals): "))
    weight = int(input("Please enter your weight input kg: "))
    bmi = weight/(height**2)

    if bmi <= 18.5:
        print("Your BMI is ", bmi," which means you are underweight.")

    elif bmi > 18.5 and bmi < 25:
        print("Your BMI is ", bmi," which means you are normal.")

    elif bmi > 25 and bmi < 30:
        print("Your BMI is ", bmi," overweight.")
    elif bmi > 30:
        print("Your BMI is ", bmi," which means you are obese.")

    else:
        print("There is an error with your input")
        print("Please check you have entered whole numbers and decimals were asked.")

elif choose == 2:
    height = int(input("Please enter your height input inputches(whole number): "))
    weight = int(input("Please enter your weight input pounds(whole number): "))
    bmi = (weight*703)/(height**2)

    if bmi <= 18.5:
        print("Your BMI is ", bmi," which means you are underweight.")

    elif bmi > 18.5 and bmi < 25:
        print("Your BMI is ", bmi," which means you are normal.")

    elif bmi > 25 and bmi < 30:
        print("Your BMI is ", bmi," which means you are overweight")

    elif bmi > 30:
        print("Your BMI is ", bmi," which means you are obese.")
    else:
        print("There is an error with your input")
        print("Please check you have entered whole numbers and decimals were asked.")
else:
    print("Wrong choice")