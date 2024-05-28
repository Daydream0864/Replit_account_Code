mon = float(1000)
#prozent = float(0.05)

#for prozent in range(10):
 # result = mon * prozent
 # print(result)



################
loan = float(1000)
apr = float(0.05)

#for i in range(10):
 # loan = loan * (1 + apr)
 # print(round(loan,2))

for k in range(10):
  loan = loan*( 1 + 0.05)
  print(round(loan,3))


######  A=P*(1 +rn)**nt      (can be)

  # - A is the final amount
  # - P is the principal amount
  # - r is the annual interest rate
  # - n is the number of times the interest is compounded per year
  # - t is the number of years



 # In this formula, the variable t represents the number of years, and the variable n represents the number of times the interest is compounded per year. If the period is one year, then n would be equal to 1.

#The 1 in the expression (1 + apr) represents the principal amount of the loan. The principal amount is the amount of money that is borrowed or invested. In the context of compound interest, the principal amount is the initial amount of money that is invested or borrowed.

#The expression (1 + apr) is used to calculate the interest rate for one period. The interest rate is calculated by adding the annual percentage rate (APR) to 1. For example, if the APR is 5%, the interest rate for one period would be 1 + 0.05 = 1.05. This means that the value of the loan will increase by 5% after one period.

#The expression loan = loan * (1 + apr) is equivalent to loan += (loan * apr). Both expressions calculate the interest for one period and add it to the current value of the loan. This is known as compound interest.