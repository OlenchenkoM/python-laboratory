print("Оленченко Максим Андрійович \n Лабораторна робота №1 \n Варіант 15"
      " Завдання №2 Проаналізувати дані про вік людини.")

n = (input("Введіть вік людини: "))

while(n.isdigit() == False) : n = (input(
    "Ви ввели не правильну форму заповнення. Введіть точніший вік людини. "))

n = int(n)

if n <= 6 :
    print("Ця людина є дошкільником. ")

elif 6 < n <= 18 :
    print("Ця людина є учнем. ")

elif 18 < n <= 65 :
    print("Ця людина є працівником. ")

elif n > 65 :
    print("Ця людина є пенсіонером. ")