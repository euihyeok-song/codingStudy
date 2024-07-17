def solution(price, money, count):
    charge = 0
    change_price = price
    
    for i in range(count):
        change_price = price * (i+1)
        charge += change_price
    
    return charge-money if charge > money else 0