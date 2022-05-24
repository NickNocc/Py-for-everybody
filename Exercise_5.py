# hourInput = input('Enter your hours worked: ')
# rateInput = input('Enter your rate per hour: ')
# hourFloat = float(hourInput)
# rateFloat = float(rateInput)

# if hourFloat > 40:
#     print('Overtime')
#     reg = hourFloat * rateFloat
#     overtime = (hourFloat - 40.0) * (rateFloat * 0.5)
#     totalPay = reg + overtime
# else:
#     print('Normal')
# try:
#     totalPay = hourFloat * rateFloat
# except:
#     totalPay = -1
# print("Your pay is:", totalPay)

def computerPay(hours, rate) :
    try: 
        hoursFloat = float(hours)
    except:
        hoursFloat = -1
    try:
        rateFloat = float(rate)
    except:
        rateFloat = -1
    if hoursFloat > 40:
        regPay = hoursFloat * rateFloat
        print(regPay)
        overtimePay = (hoursFloat - 40) * (rateFloat * 0.5)
        print(overtimePay)
        return print(regPay + overtimePay)
    else:
        return print(hoursFloat * rateFloat)

computerPay(50, 15)