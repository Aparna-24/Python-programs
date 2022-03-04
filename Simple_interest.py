#using functions keyword arguments
def si(p=100, n=13, r=4, t=3):
    amount=p*(1+r/100)**t
    print("amount is", amount)
    ci=amount-p
    print('compound interest is', ci)

si(200, 1, 5, 2)
si()
