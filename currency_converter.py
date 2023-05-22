value = float(input())
in_curr = input()
out_curr = input() 

dict = {'BGN': 1, 'USD': 1.79549, 'EUR': 1.95583, 'GBP': 2.53405}

def currency_converter (value,in_curr,out_curr):
    return((dict[in_curr] / dict[out_curr]) * value)
