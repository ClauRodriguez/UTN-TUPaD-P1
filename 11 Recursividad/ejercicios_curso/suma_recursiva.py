#obtener la suma de numeros de una lista de forma recursiva

lista = [1,2,3,4,5,6,7,8,14]

def sum_list(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sum_list(list[1:])
    

print(sum_list(lista))

