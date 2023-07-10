hrs = input("Enter Hours:")
rte = input("Enter Rate:")

try:
    hours = float(hrs)
    rate = float(rte)

except:
    print("Error! Please enter numeric input")
    quit()
print(hours, rate)

if hours <= 40:
 print(hours * rate)

else:
 print(40 * rate + (hours - 40) * (rate * 1.5))
