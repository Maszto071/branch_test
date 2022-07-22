import random

def multiply(x):
    # first-class usage
    return lambda n:n*x

def power(x):
    #another one
    return lambda n:n**x

def create_3_ele_list(random_l:list):
    for i in range(3):
        random_l.append(random.random())
    return random_l

def apply_f_c_fnc(fnc):
    return list(map(fnc, random_l))


if __name__ == '__main__':
    multiply_do = multiply(2)
    power_do = power(2)
    random_l = create_3_ele_list([])
    mulit_l = apply_f_c_fnc(multiply_do)
    power_l = apply_f_c_fnc(power_do)
    print(mulit_l, power_l)
