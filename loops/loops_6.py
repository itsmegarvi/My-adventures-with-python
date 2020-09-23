# QUESTION: Calculate income tax for the given income by adhering to the below rules
#Taxable Income	Rate (%)
#First $10,000	0
#Next $10,000	10
#The remaining	20

def tax_calculator(income):
    if income <= 10000:
        print ("Tax is zero.")
    elif income <= 20000:
        tax = (income - 10000) * 10 / 100
        print(int(tax))
    else:
        t = income - 20000
        a = income - t - 10000
        tax = (t * 20/100) + (a * 10/100)
        print(int(ta))

tax_calculator(45000)
