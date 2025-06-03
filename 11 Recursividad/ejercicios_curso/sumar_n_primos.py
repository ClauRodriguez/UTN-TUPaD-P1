#suma recursiva de n primos



def es_primo(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def sum_n_primos(num):
    if num == 1:
        return 0
    elif es_primo(num):
        return num + sum_n_primos(num - 1)
    else:
        return sum_n_primos(num - 1)
    


print(sum_n_primos(8))