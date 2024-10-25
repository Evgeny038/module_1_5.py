immutable_var = tuple([1,2,'Apple'])
print(immutable_var)
#immutable_var = tuple([1,2,'Apple']) =1
#print(immutable_var)
# я не понял 3 пункт задачи. Но вроде кортеж нельзя изменить, т.к. не удается назначить вызов функции
mutable_list = list([5,3, 'Peach'])
print(mutable_list)
print(type(mutable_list))  #это я для себя проверил
mutable_list [5][5] = 200
print(mutable_list)
#НЕ ПОЛУЧИЛОСЬ. НУЖНА КОНСУЛЬТАЦИЯ