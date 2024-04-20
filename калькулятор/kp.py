import math
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите число.")

def solve_linear(a, b):
    x = -b / a
    return f"x = {x}"

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Корней нет"
    elif discriminant == 0:
        x = -b / (2*a)
        return f"x = {x}"
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"x1 = {x1}, x2 = {x2}"

def solve_cubic(a, b, c, d):
    f = lambda x: a*x**3 + b*x**2 + c*x + d
    df = lambda x: 3*a*x**2 + 2*b*x + c
    x0 = 0
    root = newton_method(f, df, x0)
    return f"Корень: {root}" if root is not None else "Метод не сходится"

def solve_rational(a, b, c, d, e, x0, epsilon=1e-7, max_iter=100):
    f = lambda x: (a*x**2 - b*x + c) / (d*x**2 - e)
    df = lambda x: (2*a*x - b) / (d*x**2 - e)
    root = newton_method(f, df, x0, epsilon, max_iter)
    return f"Корень: {root}" if root is not None else "Метод не сходится"

def solve_bicubic(a, b, c, d, e, f, x0, epsilon=1e-7, max_iter=100):
    g = lambda x: a*x**4 + b*x**3 + c*x**2 + d*x + e
    dg = lambda x: 4*a*x**3 + 3*b*x**2 + 2*c*x + d
    root = newton_method(g, dg, x0, epsilon, max_iter)
    return f"Корень: {root}" if root is not None else "Метод не сходится"

def solve_irrational(a, b, c, d, e, x0, epsilon=1e-7, max_iter=100):
    f = lambda x: (a*x**2 - b*x + c) / (d*x**2 - e)
    df = lambda x: (2*a*x - b) / (d*x**2 - e)
    root = newton_method(f, df, x0, epsilon, max_iter)
    return f"Корень: {root}" if root is not None else "Метод не сходится"

def newton_method(f, df, x0, epsilon=1e-7, max_iter=100):
    x = x0
    for _ in range(max_iter):
        x_new = x - f(x) / df(x)
        if abs(x_new - x) < epsilon:
            return x_new
        x = x_new
    return None

def main():
    try:
        while True:
            print("Выберите тип уравнения:")
            print("1. Линейное уравнение")
            print("2. Квадратное уравнение")
            print("3. Кубическое уравнение")
            print("4. Биквадратное уравнение")
            print("5. Рациональное уравнение")
            print("6. Иррациональное уравнение")
            print("0. Выход")
            choice = input("Введите номер: ")

            if choice == '0':
                break

            clear_console()

            while True:
                if choice == '1':
                    a = input_float("Введите a: ")
                    b = input_float("Введите b: ")
                    print(solve_linear(a, b))
                    back_choice = input("Нажмите '1' для возврата к меню или '0' для выхода: ")
                    if back_choice == '0':
                        break
                    elif back_choice == '1':
                        break

                elif choice == '2':
                    a = input_float("Введите a: ")
                    b = input_float("Введите b: ")
                    c = input_float("Введите c: ")
                    print(solve_quadratic(a, b, c))
                    back_choice = input("Нажмите '1' для возврата к меню или '0' для выхода: ")
                    if back_choice == '0':
                        break
                    elif back_choice == '1':
                        break

                # Добавьте аналогичные блоки для остальных типов уравнений

                else:
                    print("Неверный выбор. Попробуйте еще раз.")
                    break

    except KeyboardInterrupt:
        print("\nПрограмма была прервана пользователем.")

if __name__ == "__main__":
    main()




