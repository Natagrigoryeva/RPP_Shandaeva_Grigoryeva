# Задание 1.1
print ('Введите первое число')
a = input()
print ('Введите второе число')
b = input()
print ('Введите третье число')
c = input()

print ('Минимальное число: ', min(a,b,c))

# Задание 1.2
print ('Введите первое число')
a = int(input())
print ('Введите второе число')
b = int(input())
print ('Введите третье число')
c = int(input())
if 1 <= a <= 50:
    print (a, '- входит в промежуток [1; 50]');
if 1 <= b <= 50:
    print (b, '- входит в промежуток [1; 50]');
if 1 <= c <= 50:
    print (c, '- входит в промежуток [1; 50]');


# Задание 1.3
print ('Введите число')
m = float(input())
for i in range(1, 11):
    print (i*m);

# Задание 1.4 (1)
print('Введите числа и дважды нажмите ENTER')
a = int(input('-->> '))
list = []
b = 0
while True:
    try:
        list.append(a)
        b = b + a
        a = int(input('-->> '))
    except:
        break;
print(b)

# Задание 1.4 (2)
print('Введите числа и дважды нажмите ENTER')
a = int(input('-->> '))
list = []
b = 0
while True:
    try:
        list.append(a)
        b = b + 1
        a = int(input('-->> '))
    except:
        break;
print(b);

