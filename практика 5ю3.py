dollars_in_rubles = 95.5
def convert_dollars_in_rubles(amount_dollars):
     return amount_dollars * dollars_in_rubles
dollars = float(input("Введите сумму в долларах:"))
rubles = convert_dollars_in_rubles(dollars)
print(f"In Dollars = {dollars}, In Rubles = {rubles}")
