hourInput = input('Enter your hours worked: ')
rateInput = input('Enter your rate per hour: ')
hourFloat = float(hourInput)
rateFloat = float(rateInput)

if hourFloat > 40:
    print('Overtime')
    reg = hourFloat * rateFloat
    overtime = (hourFloat - 40.0) * (rateFloat * 0.5)
    totalPay = reg + overtime
else:
    print('Normal')

totalPay = hourFloat * rateFloat

print("Your pay is:", totalPay)
