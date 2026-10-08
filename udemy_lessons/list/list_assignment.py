import random
#assingnment 1
pos_int = [x for x in range(1,21)]
print(pos_int)


#assingnment 2
print(pos_int[0])
print(pos_int[int(len(pos_int)/2)])
print(pos_int[-1])

#assignment 3
print(pos_int[0:4])
print(pos_int[-5:])
print(pos_int[5:15])

#assingnment 4
pos_ten = [x**2 for x in range(1,11)]
print(pos_ten)

#assignment 5
even = [x for x in pos_int if x%2==0]
print(even)

#assingnment 6
#.sample for unique, .choices for dup
ran_num = random.sample(range(1,101), k=10)
ran_num.sort()
print(ran_num)
ran_num.sort(reverse=True)
print(ran_num)

#assignment 7
matrix = [[x for x in random.sample(range(1,11), k=3)] for r in range(3)]
matrix_str = ", ".join(map(str, matrix))
print("matrix: " + matrix_str)
print(matrix[1][2])

#assignment 8
student = {'Eko': 89, 'Bambang': 66, 'Jonah': 77}
sort_value = sorted(student.values())
inv_student = {v:k for k, v in student.items()}
print(f'inv: {inv_student}')
sorted_student = {}
for val in sort_value:
    if val in inv_student.keys():
        sorted_student[inv_student.get(val)] = val
print(sorted_student)

#assignment 9
matrix_2 = [[y for y in random.sample(range(1, 11), k=3)] for r in range(3)]
def transpose(matrix):
    """
    Method to transpose a matrix.\n
    :param matrix: nested lists of numbers
    :type matrix: list
    :return: transposed matrix
    :rtype: nested lists"""
    row_count = len(matrix[0])
    col_count = len(matrix)
    trans_result = list()
    for x in range(0, row_count):
        temp = list()
        for y in range(0, col_count):
            #switching x with y since its a transpose
            temp.append(matrix_2[y][x])
        trans_result.append(temp)
    return trans_result
print(f"pre-transposed: {matrix_2}")
print(f"after: {transpose(matrix_2)}")


#assignment 10
original_list = [[x for x in random.sample(range(1, 11), k=3)] for r in range(2)]
def splatt(lists=[]):
    """
    Method to convert nested lists into single list.\n
    :param lists: nested lists
    :type lists: list
    :return: single list
    :rtype: list
    """
    flattened = lists[0]
    if len(lists) <= 0:
        return None
    for i in range(1, len(lists)):
        for i2 in range(0, len(lists[i])):
            flattened.append(lists[i][i2])
    return flattened        
print(f"fat lists: {original_list}")
print(f"flattened! {splatt(original_list)}")

#assignment 11
int_pos = [x for x in range(1, 11)]
print(f"list manipulation: {int_pos}")
int_pos.remove(2)
int_pos.remove(4)
int_pos.remove(6)
int_pos.insert(4, 99)
print(f"after list manipulation: {int_pos}")

#assignment 12
zip_candidate_1 = [x for x in random.sample(range(1,11), k=5)]
zip_candidate_2 = [y for y in random.sample(range(1,11), k=5)]
print(f"Zip candidate 1: {zip_candidate_1}")
print(f"Zip candidate 2: {zip_candidate_2}")
print(f"Zipped! {list(zip(zip_candidate_1, zip_candidate_2))}")

#assignment 13
normal_list = [x for x in random.sample(range(1, 100), k=5)]
def esrever(regular_list=[]):
    """
    Function to reverse order list.\n
    :param regular_list: single list
    :type regular_list: list
    :return: None
    :rtype: None"""
    if isinstance(regular_list, list):
        return regular_list.sort(reverse=True)

print(f"Regular list: {normal_list}")
esrever(normal_list)
print(f"Reversed! {normal_list}")

#assignment 14
rotate_candidate = [x for x in random.sample(range(1, 100), k=6)]
def rotate(regular_list, i) -> list:
    """
    Method to rotate list position.\n
    :param regular_list: target list
    :type regular_list: list
    :param i: amount of member to be rotated.
    :type i: int
    :return: list with rotated position
    :rtype: list"""
    return regular_list[i:] + regular_list[:i]
print(f"list: {rotate_candidate}")
print(f"rotated! {rotate(rotate_candidate, 2)}")

#assignment 15
intersect_candidate_1 = [x for x in random.choices(range(1, 11), k=5)]
intersect_candidate_2 = [y for y in random.choices(range(1, 11), k=5)]
def intersect(list1, list2) -> list:
    """
    Method to display intersected values between two lists.\n
    :param list1: target list
    :param list2: target list
    :type list1: list
    :type list2: list
    :return: intersected values
    :rtype: list"""
    result = []
    for item in list1:
        if item not in result and item in list2:
            result.append(item)
    return result
print(f"candidate 1: {intersect_candidate_1}")
print(f"candidate 2: {intersect_candidate_2}")
print(f"1 and 2 intersect! {intersect(intersect_candidate_1, intersect_candidate_2)}")