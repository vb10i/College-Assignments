sales_earning = int(input("enter the earnings from sales: "))
if sales_earning >= 100000:
    Basic = 4000
    print("Basic is: ", Basic)
    HRA = .2*4000
    print("HRA: ", HRA)
    DA = 11*4000
    Conveyance = 500
    print("Conveyance is: ", Conveyance)
    Incentive = .1*sales_earning
    print("Incentive is: ", Incentive)
    Bonus = 1000
    print("Bonus is: ", Bonus)
    Total_salary = Basic + HRA + DA + Conveyance + Incentive + Bonus 
    print("Total Salary is: ", Total_salary)
else:
    Basic = 4000
    print("Basic is: ", Basic)
    HRA = .1*4000
    print("HRA is: ", HRA)
    DA = 11*4000
    Conveyance = 500
    print("Conveyance is: ", Conveyance)
    Incentive = .4*sales_earning
    print("Incentive is: ", Incentive)
    Bonus = 500
    print("Bonus is: ", Bonus)
    Total_salary = Basic + HRA + DA + Conveyance + Incentive + Bonus 
    print("Total Salary is: ", Total_salary)