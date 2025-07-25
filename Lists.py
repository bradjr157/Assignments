my_list = []
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
print(my_list)

my_list = [10, 20, 30, 40]
my_list.insert(1, 15)
print(my_list)

my_list.extend([50, 60, 70])
print(my_list)

my_list.remove(70) 
print(my_list)

my_list.sort()
print(my_list)

value = 30
index = my_list.index(value)
print(f"Value {value} found at index: {index}")


