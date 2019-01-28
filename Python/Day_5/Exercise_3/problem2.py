'''
3. Write a python program to assign grades to students at the end of the year. The program
must do the following
a. Ask for a student number.
b. Ask for the student's tutorial mark.
c. Ask for the student's test mark.
d. Calculate whether the student's average so far is high enough for the student to be permitted
to write th examination. If the average (mean) of the tutorial an test marks is lower than
40%, the student should get automatically F grade and the program should print th grade
and exit without performing the following steps.
e. Ask for student's examination mark
f. Calculate the student's final mark. The tutorial and test marks should count for 25%
of the final mark each, and the final examination should count for remaining 50%.
g. Calculate the student's grade, according to the following table

80 <= mark <= 100   A
70 <= mark < 80     B
60 <= mark < 70     C
50 <= mark < 60     D
mark < 50           E
'''

tutorial_mark = int(input("Enter tutorial marks: "))
test_mark = int(input("Enter test marks: "))
tutorial_test_average = (tutorial_mark+test_mark) / 2

if tutorial_test_average >= 40:
   examination_mark = int(input("Enter examination marks: "))
   final_mark = (examination_mark / 2) + (tutorial_mark / 4) + (test_mark / 4)
else:
    print("F Grade")