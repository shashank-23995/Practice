python_students = []
name_list = []
score_list = []
runner_up = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    name_list.append(name)
    score_list.append(score)

min_value = min(score_list)
while min(score_list) == min_value:
    index = score_list.index(min_value)
    score_list.remove(min_value)
    del name_list[index]

min_value = min(score_list)
while min(score_list) == min_value:
    index = score_list.index(min_value)
    runner_up.append(name_list[index])
    score_list.remove(min_value)
    del name_list[index]

runner_up.sort()
for i in runner_up:
    print(i)
# print(name_list)
# print(score_list)

# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     temp_student = []
#     temp_student.append(name)
#     temp_student.append(score)
#     python_students.append(temp_student)
# print(python_students)
# print(min(python_students))