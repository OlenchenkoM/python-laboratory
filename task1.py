import math
const = math.pi

print("Оленченко Максим Андрійович \n Лабораторна робота №1 \n Варіант 15"
      " Завдання №1 Обчислити, скільки потрібно банок фарби")

a = (input("Введіть діаметр бака "))

while(a.isdigit() == False) : a = (input("Ви ввели не правильну форму заповнення."
                                         " Введіть точніше діаметр баку. "))
a = float(a)

b = (input("Введіть висоту бака. "))

while(b.isdigit() == False) : b = (input(
    "Ви ввели не правильну форму заповнення. Введіть точніше висоту бака. "))

b = float(b)

c = (input(
    "Введіть площу, яку можна"
    " забарвити однієї банкою фарби "))
m = 0
while m == 0:
    while(c.isdigit() == False) : c = (input("Ви ввели не правильну форму заповнення. Введіть точніше висоту бака. "))
    c = float(c)
    while c <= 0.0: c = (input("Це число не може дорівнювати нулю. Введіть інше число "))
    m = 1


d = float((2*const*(a/2)*b)/c)
print("Кількість банок що потрібна =", d)
