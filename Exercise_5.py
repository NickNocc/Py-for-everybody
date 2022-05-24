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