print("TIP calculator")
print("____________")
#####################
myBill = float(input("how much did you spend?: "))
tip = int(input("what percentage do you wanna want to spend: "))
numberOfPeople = int(input("How many people?: "))




answer = myBill / numberOfPeople
answerR =  (tip/100 * answer) + answer
print("You all owe", answerR)
###########################################
#myBill = float(input("What was the bill?: "))
#numberOfPeople = int(input("How many people?: "))
#tip = int(input("What percent tip do you want to leave: 15, 18, or 20 percent?"))
#
#
#bill_with_tip = tip / 100 * myBill + myBill
#bill_per_person = bill_with_tip / numberOfPeople
#final_amount = round(bill_per_person, 2)
#
#
#print("You all owe", final_amount)