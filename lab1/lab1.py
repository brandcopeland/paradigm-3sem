import sys
import cmath


# Функция для ввода коэфицентов и проверки на ошибки
def get_coefficient(prompt, coef_name):
    while True:
        try:
            coef = float(input(prompt))
            return coef
        except ValueError:
            print(f"Некорректное значение для коэффициента {coef_name}. Повторите ввод.")


# Функция для вычисления корней уравнения
def solve_biquadratic(a, b, c):
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = cmath.sqrt((-b + cmath.sqrt(discriminant)) / (2 * a))
        root2 = -root1
        root3 = cmath.sqrt((-b - cmath.sqrt(discriminant)) / (2 * a))
        root4 = -root3
        return root1, root2, root3, root4
    elif discriminant == 0:
        root = cmath.sqrt(-b / (2 * a))
        return root, -root
    else:
        return ()


# Функция поиска действительных корней
def findTrueRoots(roots):
    trueRoots = []
    for root in roots:
        # Проверка на действительность и на дубликатность ( 0 и -0)
        if (root.imag == 0) and (str(root.real) != "-0.0"):
            trueRoots.append(root.real)
    return trueRoots


def printTrueRoots(trueRoots):
    if len(trueRoots) == 4:
        print(
            f"Уравнение имеет четыре действительных корня: {trueRoots[0]}, {trueRoots[1]}, {trueRoots[2]}, {trueRoots[3]}")
    elif len(trueRoots) == 3:
        print(f"Уравнение имеет три действительных корня: {trueRoots[0]}, {trueRoots[1]}, {trueRoots[2]}")
    elif len(trueRoots) == 2:
        print(f"Уравнение имеет два действительных корня: {trueRoots[0]}, {trueRoots[1]}")
    elif len(trueRoots) == 1:
        print(f"Уравнение имеет один действительный корень: {trueRoots[0]}")
    else:
        print("Уравнение не имеет действительных корней.")


def main():
    # Проверка ввода из консоли и получение аргументов
    if len(sys.argv) == 4:
        try:
            a = float(sys.argv[1])
            b = float(sys.argv[2])
            c = float(sys.argv[3])
        except ValueError:
            print("Некорректные коэффициенты в командной строке. Пожалуйста, введите их с клавиатуры.")
            a = get_coefficient("Введите коэффициент A: ", "A")
            b = get_coefficient("Введите коэффициент B: ", "B")
            c = get_coefficient("Введите коэффициент C: ", "C")
    else:
        a = get_coefficient("Введите коэффициент A: ", "A")
        b = get_coefficient("Введите коэффициент B: ", "B")
        c = get_coefficient("Введите коэффициент C: ", "C")
    # Получение корней
    roots = solve_biquadratic(a, b, c)
    # Вывод ответа
    trueRoots = findTrueRoots(roots)
    printTrueRoots(trueRoots)


if __name__ == "__main__":
    main()
