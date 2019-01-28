# Here's what can happen if we put our weekdaye in a mutable list

WEEKDAYS = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def print_funny_weekday_list(weekdays):
    weekdays[5] = 'Caturday' # this is going to modify the orignal list
    print(weekdays)

print_funny_weekday_list(WEEKDAYS)
print(WEEKDAYS) #oops