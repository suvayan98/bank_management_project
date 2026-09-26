import random as r

def ramdom_no(y):
    
    if y.lower() == "cust_id":
        total="CUST0"
        for i in range (4):
            no1=r.randint(0,9)
            total+=str(no1)
        return total


    elif y.lower() == "ifse_no":
        total="SPB000"
        for i in range (5):
            no1=r.randint(0,9)
            total+=str(no1)
        return total
