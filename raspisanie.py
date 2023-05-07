def array_input(n):
    if n:
        return list(map(int, input().split()))
    input()
    return []
t = int(input('Введите количество учителей занятых этим предметом '))
print('Введите номера занятых учителей')
T = array_input(t)
r = int(input('Введите количество занятых кабинетов '))
print('Введите номера занятых кабинетов ')
R = array_input(r)
t1 = int(input('Введите количество свободных учителей '))
print('Введите номера свободных учителей')
T1 = array_input(t1)
r1 = int(input('Введите количество свободных кабинетов '))
print('Введите номера свободных кабинетов')
R1 = array_input(r1)

set_T, set_R, set_T1, set_R1 = set(T), set(R), set(T1), set(R1)
T, R, T1, R1 = list(set_T), list(set_R), list(set_T1), list(set_R1)
if set_R1.issubset(set_R) or set_T.intersection(set_T1):
    print(-1)
else:
    r_min = min(list(set_R1.difference(set_R)))
    R.append(r_min)
    R.sort()
    set_T.update(set_T1)
    T = list(set_T)
    print('Обновлённое количество занятых учителей ' ,len(T))
    print('Обновлённые имена занятых учителей ',T)
    print('Обновлённое количество занятых кабинетов ' ,len(R))
    print('Обновлённые номера занятых кабинетов '.join(list(map(str, R))))