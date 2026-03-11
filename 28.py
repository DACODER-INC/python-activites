cyclist1 = 10
cyclist2 = 20
cyclist3 = 30
mean = (cyclist1 + cyclist2 + cyclist3) / 3
print("The mean speed of the three cyclists is: " + str(mean) + " km/h")
if cyclist1 > mean and cyclist2 > mean and cyclist3 > mean:
    print("All three cyclists are faster than the mean speed.")
elif cyclist1 > mean and cyclist2 > mean:
    print("Cyclist 1 and Cyclist 2 are faster than the mean speed.")
elif cyclist1 > mean and cyclist3 > mean:
    print("Cyclist 1 and Cyclist 3 are faster than the mean speed.")
elif cyclist2 > mean and cyclist3 > mean:
    print("Cyclist 2 and Cyclist 3 are faster than the mean speed.")
elif cyclist1 > mean:
    print("Cyclist 1 is faster than the mean speed.")
elif cyclist2 > mean:
    print("Cyclist 2 is faster than the mean speed.")
elif cyclist3 > mean:
    print("Cyclist 3 is faster than the mean speed.")
else:
    print("No cyclist is faster than the mean speed.")
