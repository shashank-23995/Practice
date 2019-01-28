weight = int(input("Enter weight of the parcel: "))

if weight <= 1000:
	if weight <= 300:
		cost = 5
	else:
		cost = 5 + 2 * round((weight-300)/100)

	print("Your parcel will cost Rs. %d"% cost)
else:
	print("maximum weight for small parcel is exceeded")
	print("Use large parcel service instead")
