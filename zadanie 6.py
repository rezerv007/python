#6
a = int(input("Введите результаты первого дня в км "))
b = int(input("Введите общий результат в км "))
result_days = 1
result_km = a
while result_km < b:
        a = a + 0.1 * a
        result_days += 1
        result_km = result_km + a
print(f"Вы достигнете желаемого показателя на %.d день" % result_days)