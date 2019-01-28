'''
1. Write a program which uses a nested for loop to populate a three dimensional list 
representing a calendar: the top level list should contain a sub-list for each month,
and each month should contain four weeks. Each week should be an empty list
'''
MONTHS = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']
WEEKS = ['SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY']

calendar = []

# for m_index, m in enumerate(MONTHS):
#     calendar[m_index] = m
#     for w_index, w in enumerate(WEEKS):
#         calendar[m_index][w_index] = w

for m in MONTHS:
    calendar.append(m)
    for w in WEEKS:
        calendar[m].append(w)
         
print("Printing calendar\n\n")
print(calendar)