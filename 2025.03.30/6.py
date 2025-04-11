list1 = input('Введите 1-й список: ').split(" ")
list2 = input('Введите 2-й список: ').split(" ")

range1 = range(0, len(list1)+1)

slice_length = len(list2)
result = 0

for i in range1:
    if list1[i:i+slice_length] == list2:
        result = 1
        break
       
if result == 1:
    print('да')
else:
    print('нет')
    
# Введите 1-й список: 3 55 78 754 1345
# Введите 2-й список: 78 754
# да

# Введите 1-й список: 1 2 3 4 5 6
# Введите 2-й список: 2 4
# нет

