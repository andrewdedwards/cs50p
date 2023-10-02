price = int(50)
amt_paid = int(0)

while amt_paid < price:
    print(f"Amount Due: {price - amt_paid}")
    payment = int(input("Insert Coin: "))
    if payment == 5 or payment == 10 or payment ==25: #How do I clean this up?
        amt_paid += payment
    
print(f"Change Owed: {amt_paid - price}")