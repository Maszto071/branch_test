import random

def multiply(x):
    return lambda n:n*x

def create_3_ele_list(random_l:list):
    for i in range(3):
        random_l.append(random.random())
    return random_l

def multiply_all_ele():
    list(map(first_class, random_l))


if __name__ == '__main__':
    first_class = multiply(2)
    random_l = create_3_ele_list([])
    multiply_all_ele()
    print(random_l)