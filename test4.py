grades = [10, 20 , 30, 50]
grades1 = [100, 80 , 20, 50]

def avg_calc (list_g):
    sum =0 
    for i in range(len(list_g)):
        sum += list_g[i]
    avg_g = sum/len(list_g) 
    return avg_g 

res_grade = avg_calc(grades)
res_grade1 = avg_calc(grades1)
print(res_grade) 
print(res_grade1)


def test_func(a, b, c=10):
    s = a**b+c
    print(s)
    
test_func(a = int(input()), b=4, c=12)


hours = 20 
rate = 15

def calc_payment(h, r):
    n_h_limit = 16
    if h>n_h_limit:
        o_h = h-n_h_limit
        n_h = 16
    else:
        o_h=0
        n_h = h
    
    return n_h*r+o_h*(r*2)

print(calc_payment(hours, rate))