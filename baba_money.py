

"""
pv = p * (pow((1 + r/100/n),n * t))

print(pv)
"""




def compound_interest():
    p =  float(input("What's the principle "))
    r = float(input("Whats the rate "))
    n = int(input("How many periods "))
    t =  int(input('how many payments per period'))
    
    balance = p * (pow((1 + r/100/n),n*t))
    ci = balance - p
    print('Your balance at the end of the period will be $',round(balance,2),| "\n")
    print('You earned $', round(ci,2), 'during the 1 year period.')
    roi = (ci/balance) * 100
    print('This is ', round(roi,2), '% return on investment')

compound_interest()
