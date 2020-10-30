st = input('what is the starting capital: ')
a = input('how many months do you want to calculate for: ')
p = input('what is the monthly percentage to calculate from: ')

def rates(st, a, p):
    for i in range(1, int(a) + 1):
        st = float(st) + float(st) * float(p)/100
        print('Return after month {}: {} '.format(i, st))
        i += 1
        
        
rates(st, a, p)        
