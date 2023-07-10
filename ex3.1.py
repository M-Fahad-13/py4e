hrs = input("Enter Hours:")
hours = float(hrs)
rte = input("Enter Rate:")
rate = float(rte)

if hours <= 40:
 print(hours * rate)

else:
 print(40 * rate + (hours - 40) * (rate * 1.5))
