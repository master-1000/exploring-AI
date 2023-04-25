def remove_duplicates(lst):

    unique_lst = set(lst)
    return list(unique_lst)

lista_com_duplicatas = [1, 2, 3, 3, 4, 5, 5, 6]
lista_sem_duplicatas = remove_duplicates(lista_com_duplicatas)
print(lista_sem_duplicatas)