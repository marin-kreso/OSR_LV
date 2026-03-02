def total_euro(hours, pay_rate):
    return hours * pay_rate

hours = int(input("Radni sati: "))
pay_rate = float(input("eura/h: "))

result = total_euro(hours, pay_rate)
print("Ukupno:", result, "eura")