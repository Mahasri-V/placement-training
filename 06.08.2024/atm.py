def atm_simulation(balance, withdrawal_amount):
    if withdrawal_amount <= balance:
        return "Transaction successful"
    else:
        return "Insufficient funds"

print(atm_simulation(1000, 700)) 
print(atm_simulation(2000, 300))  
print(atm_simulation(1500, 1500))
