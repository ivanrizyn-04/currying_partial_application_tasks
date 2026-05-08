# -*- coding: utf-8 -*-
"""
Карування та часткове застосування у Python

У файлі виконано 17 завдань:
- приклади звичайних функцій;
- карування;
- часткове застосування через functools.partial;
- validators;
- formatting;
- pricing pipeline;
- короткі пояснення та результати виконання.
"""

from functools import partial
from typing import Callable, Iterable


def print_title(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


# =============================================================================
# Завдання 1. Звичайна функція з кількома аргументами
# =============================================================================

print_title("Завдання 1. Звичайна функція з кількома аргументами")


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def power(base, exponent):
    return base ** exponent


print("add(2, 3) =", add(2, 3))
print("add(10, 5) =", add(10, 5))

print("multiply(4, 5) =", multiply(4, 5))
print("multiply(7, 8) =", multiply(7, 8))

print("power(2, 3) =", power(2, 3))
print("power(5, 2) =", power(5, 2))

print("\nПояснення:")
print("Ці функції не є карованими, бо кожна приймає всі аргументи одразу за один виклик.")
print("add приймає 2 аргументи за один виклик.")
print("multiply приймає 2 аргументи за один виклик.")
print("power приймає 2 аргументи за один виклик.")


# =============================================================================
# Завдання 2. Аналіз функцій
# =============================================================================

print_title("Завдання 2. Аналіз функцій")


def discount(price, percent):
    return price * (1 - percent)


def convert(amount, rate):
    return amount * rate


def greet(greeting, name):
    return f"{greeting}, {name}!"


def discount_curried(percent):
    return lambda price: price * (1 - percent)


def convert_curried(rate):
    return lambda amount: amount * rate


def greet_curried(greeting):
    return lambda name: f"{greeting}, {name}!"


discount_10_from_curried = discount_curried(0.10)
usd_to_uah_from_curried = convert_curried(40)
hello = greet_curried("Hello")

discount_10_partial = partial(discount, percent=0.10)
usd_to_uah_partial = partial(convert, rate=40)
hello_partial = partial(greet, "Hello")

print("discount(100, 0.10) =", discount(100, 0.10))
print("discount_10_from_curried(100) =", discount_10_from_curried(100))
print("discount_10_partial(100) =", discount_10_partial(100))

print("convert(100, 40) =", convert(100, 40))
print("usd_to_uah_from_curried(100) =", usd_to_uah_from_curried(100))
print("usd_to_uah_partial(100) =", usd_to_uah_partial(100))

print('greet("Hello", "Alice") =', greet("Hello", "Alice"))
print('hello("Alice") =', hello("Alice"))
print('hello_partial("Alice") =', hello_partial("Alice"))

print("\nПояснення:")
print("discount, convert, greet не є карованими, бо приймають два аргументи одразу.")
print("До всіх трьох можна застосувати часткове застосування.")
print("Після фіксації одного параметра отримуємо нову функцію, яка очікує решту параметрів.")
print("Карований варіант повертає функцію після отримання першого аргументу.")


# =============================================================================
# Завдання 3. Карування функції додавання
# =============================================================================

print_title("Завдання 3. Карування функції додавання")


def add_curried(a):
    def inner(b):
        return a + b

    return inner


print("add_curried(2)(3) =", add_curried(2)(3))
print("add_curried(10)(5) =", add_curried(10)(5))

add10 = add_curried(10)
print("add10(7) =", add10(7))
print("add10(100) =", add10(100))

print("\nПояснення:")
print("add_curried(10) повертає функцію inner, яка запам'ятовує a = 10.")


# =============================================================================
# Завдання 4. Карування множення
# =============================================================================

print_title("Завдання 4. Карування множення")


def multiply_curried(a):
    def inner(b):
        return a * b

    return inner


print("multiply_curried(2)(8) =", multiply_curried(2)(8))
print("multiply_curried(5)(6) =", multiply_curried(5)(6))

numbers = [1, 2, 3, 4, 5]

double = multiply_curried(2)
triple = multiply_curried(3)

doubled_numbers = list(map(double, numbers))
tripled_numbers = list(map(triple, numbers))

print("Початковий список:", numbers)
print("Подвоєні значення:", doubled_numbers)
print("Потроєні значення:", tripled_numbers)


# =============================================================================
# Завдання 5. Карування функції з трьома аргументами
# =============================================================================

print_title("Завдання 5. Карування функції з трьома аргументами")


def volume(length, width, height):
    return length * width * height


def volume_curried(length):
    def second(width):
        def third(height):
            return length * width * height

        return third

    return second


print("volume(2, 3, 4) =", volume(2, 3, 4))
print("volume_curried(2)(3)(4) =", volume_curried(2)(3)(4))

box_base = volume_curried(2)(5)
print("box_base(10) =", box_base(10))
print("box_base(20) =", box_base(20))

print("\nПояснення:")
print("box_base фіксує length = 2 і width = 5, тому очікує тільки height.")


# =============================================================================
# Завдання 6. Карування рядкових операцій
# =============================================================================

print_title("Завдання 6. Карування рядкових операцій")


def message(prefix, name):
    return f"{prefix}: {name}"


def message_curried(prefix):
    def inner(name):
        return f"{prefix}: {name}"

    return inner


error_message = message_curried("ERROR")
warning_message = message_curried("WARNING")
info_message = message_curried("INFO")

print(error_message("File not found"))
print(warning_message("Low memory"))
print(info_message("Process started"))

print("\nПояснення:")
print("message_curried створює спеціалізовані функції для різних типів повідомлень.")


# =============================================================================
# Завдання 7. Часткове застосування через functools.partial
# =============================================================================

print_title("Завдання 7. Часткове застосування через functools.partial")

add5 = partial(add, 5)
add10_partial = partial(add, 10)

print("add5(3) =", add5(3))
print("add10_partial(7) =", add10_partial(7))

print("\nПояснення:")
print("partial фіксує частину аргументів звичайної функції.")
print("Карована функція спочатку спеціально написана так, щоб повертати інші функції.")
print("partial не змінює саму функцію add, а створює новий callable з уже заданими параметрами.")


# =============================================================================
# Завдання 8. Часткове застосування для конвертації валют
# =============================================================================

print_title("Завдання 8. Часткове застосування для конвертації валют")


def convert_currency_simple(amount, rate):
    return amount * rate


usd_to_uah = partial(convert_currency_simple, rate=40)
eur_to_uah = partial(convert_currency_simple, rate=43)

print("usd_to_uah(100) =", usd_to_uah(100))
print("eur_to_uah(100) =", eur_to_uah(100))
print("usd_to_uah(250) =", usd_to_uah(250))

print("\nПояснення:")
print("Через partial зафіксовано курс валюти, а сума залишається змінним аргументом.")


# =============================================================================
# Завдання 9. Часткове застосування для обчислення знижки
# =============================================================================

print_title("Завдання 9. Часткове застосування для обчислення знижки")


def apply_discount(price, percent):
    return price * (1 - percent)


discount_10 = partial(apply_discount, percent=0.10)
discount_20 = partial(apply_discount, percent=0.20)
discount_50 = partial(apply_discount, percent=0.50)

prices = [100, 250, 999]

print("Ціни:", prices)
print("Знижка 10%:", list(map(discount_10, prices)))
print("Знижка 20%:", list(map(discount_20, prices)))
print("Знижка 50%:", list(map(discount_50, prices)))


def apply_discount_curried(percent):
    return lambda price: price * (1 - percent)


discount_10_curried = apply_discount_curried(0.10)

print("Карований варіант 10% для 250:", discount_10_curried(250))

print("\nПорівняння:")
print("partial зручний, коли вже є звичайна функція apply_discount(price, percent).")
print("Карування зручне, якщо функція одразу проєктується у функціональному стилі.")


# =============================================================================
# Завдання 10. Часткове застосування для логування
# =============================================================================

print_title("Завдання 10. Часткове застосування для логування")


def log(level, message):
    return f"[{level}] {message}"


log_info = partial(log, "INFO")
log_warning = partial(log, "WARNING")
log_error = partial(log, "ERROR")

print(log_info("Application started"))
print(log_warning("Disk space is low"))
print(log_error("Cannot connect to database"))

print("\nПояснення:")
print("Фіксується рівень логування, а текст повідомлення передається пізніше.")


# =============================================================================
# Завдання 11. Реалізувати двома способами
# =============================================================================

print_title("Завдання 11. Power: карування та partial")


def power_curried(exponent):
    def inner(base):
        return base ** exponent

    return inner


square_curried = power_curried(2)
cube_curried = power_curried(3)

square_partial = partial(power, exponent=2)
cube_partial = partial(power, exponent=3)

power_numbers = [2, 3, 4, 5]

print("Числа:", power_numbers)
print("Квадрати через currying:", list(map(square_curried, power_numbers)))
print("Куби через currying:", list(map(cube_curried, power_numbers)))
print("Квадрати через partial:", list(map(square_partial, power_numbers)))
print("Куби через partial:", list(map(cube_partial, power_numbers)))

print("\nПитання до студента:")
print("Який варіант читається простіше? Часто partial, якщо функція вже існує.")
print("Який варіант дає більше контролю? Карування, бо ми самі визначаємо порядок викликів.")
print("Який підхід ближчий до класичного FP? Карування.")


# =============================================================================
# Завдання 12. Побудова перевірок validators
# =============================================================================

print_title("Завдання 12. Побудова перевірок validators")


def greater_than(limit, value):
    return value > limit


def greater_than_curried(limit):
    def inner(value):
        return value > limit

    return inner


validator_numbers = [5, 10, 15, 50, 100, 150]

greater_than_10 = greater_than_curried(10)
greater_than_100 = greater_than_curried(100)

print("Числа:", validator_numbers)
print("Перевірка > 10:", list(map(greater_than_10, validator_numbers)))
print("Перевірка > 100:", list(map(greater_than_100, validator_numbers)))
print("filter > 10:", list(filter(greater_than_10, validator_numbers)))
print("filter > 100:", list(filter(greater_than_100, validator_numbers)))

print("\nПояснення:")
print("Карування дозволяє створювати готові validators, які зручно передавати у filter.")


# =============================================================================
# Завдання 13. Формування повідомлень
# =============================================================================

print_title("Завдання 13. Формування повідомлень")


def format_message(prefix, suffix, text):
    return f"{prefix}{text}{suffix}"


def format_message_curried(prefix):
    def with_suffix(suffix):
        def with_text(text):
            return f"{prefix}{text}{suffix}"

        return with_text

    return with_suffix


html_bold = format_message_curried("<b>")("</b>")
markdown_bold = format_message_curried("**")("**")
parentheses = format_message_curried("(")(")")

texts = ["Python", "FP", "Currying"]

print("HTML bold:", list(map(html_bold, texts)))
print("Markdown bold:", list(map(markdown_bold, texts)))
print("Дужки:", list(map(parentheses, texts)))

print("\nПояснення:")
print("Ми зафіксували prefix і suffix, тому нові функції очікують лише text.")


# =============================================================================
# Завдання 14. Functional Pricing Engine
# =============================================================================

print_title("Завдання 14. Functional Pricing Engine")


def add_tax(price, tax):
    return price * (1 + tax)


def add_tax_curried(tax):
    return lambda price: price * (1 + tax)


def apply_discount_for_engine(price, discount):
    return price * (1 - discount)


def apply_discount_curried_for_engine(discount):
    return lambda price: price * (1 - discount)


def convert_currency(price, rate):
    return price * rate


def convert_currency_curried(rate):
    return lambda price: price * rate


def add_fee(price, fee):
    return price + fee


def add_fee_curried(fee):
    return lambda price: price + fee


engine_prices = [100, 250, 400, 999]

# Спеціалізовані функції через partial:
tax_20 = partial(add_tax, tax=0.20)
discount_10_engine = partial(apply_discount_for_engine, discount=0.10)
usd_to_uah_engine = partial(convert_currency, rate=40)
fee_50 = partial(add_fee, fee=50)


def run_pipeline(value, steps: Iterable[Callable]):
    result = value
    for step in steps:
        result = step(result)
    return result


pricing_pipeline = [
    discount_10_engine,
    tax_20,
    fee_50,
    usd_to_uah_engine,
]

final_prices = [run_pipeline(price, pricing_pipeline) for price in engine_prices]

print("Початкові ціни:", engine_prices)
print("Фінальні ціни:", final_prices)

print("\nДеталізація для кожної ціни:")
for price in engine_prices:
    after_discount = discount_10_engine(price)
    after_tax = tax_20(after_discount)
    after_fee = fee_50(after_tax)
    final = usd_to_uah_engine(after_fee)
    print(
        f"{price} -> після знижки {after_discount} -> після податку {after_tax} "
        f"-> після збору {after_fee} -> у UAH {final}"
    )

print("\nПояснення:")
print("Часткове застосування використано у tax_20, discount_10_engine, usd_to_uah_engine, fee_50.")
print("Карування можна було б використати у відповідних curried-функціях.")
print("Для цього кейсу partial зручніший, бо базові функції вже мають звичайний формат price + параметр.")


# =============================================================================
# Завдання 15. Прочитати та пояснити
# =============================================================================

print_title("Завдання 15. Прочитати та пояснити")


def curry_add(a):
    return lambda b: a + b


add7 = curry_add(7)
print("add7(5) =", add7(5))

print("\nПояснення:")
print("curry_add(7) повертає lambda b: 7 + b.")
print("add7 пам'ятає число 7 завдяки замиканню.")
print("Замикання — це ситуація, коли внутрішня функція зберігає доступ до змінних зовнішньої функції.")
print("У цьому прикладі lambda зберігає доступ до a = 7.")


# =============================================================================
# Завдання 16. Визначити тип підходу
# =============================================================================

print_title("Завдання 16. Визначити тип підходу")


def multiply_for_analysis(a, b):
    return a * b


double_by_partial = partial(multiply_for_analysis, 2)


def multiply_curried_for_analysis(a):
    return lambda b: a * b


def add_for_analysis(a, b):
    return a + b


print("double_by_partial(10) =", double_by_partial(10))
print("multiply_curried_for_analysis(2)(10) =", multiply_curried_for_analysis(2)(10))
print("add_for_analysis(2, 3) =", add_for_analysis(2, 3))

print("\nВизначення:")
print("double = partial(multiply, 2) — це часткове застосування.")
print("multiply_curried(a): return lambda b: a * b — це карування.")
print("add(a, b): return a + b — це ні карування, ні часткове застосування.")


# =============================================================================
# Завдання 17. Власний приклад використання
# =============================================================================

print_title("Завдання 17. Власний приклад використання")

print("Задача:")
print("Є список замовлень. Потрібно створити фільтри за мінімальною сумою та форматери статусів.")


orders = [
    {"id": 1, "total": 120, "status": "new"},
    {"id": 2, "total": 850, "status": "paid"},
    {"id": 3, "total": 1500, "status": "paid"},
    {"id": 4, "total": 75, "status": "cancelled"},
]


# Приклад карування: створення фільтрів
def order_total_greater_than_curried(limit):
    def inner(order):
        return order["total"] > limit

    return inner


expensive_order = order_total_greater_than_curried(500)
very_expensive_order = order_total_greater_than_curried(1000)

print("Замовлення дорожчі за 500:", list(filter(expensive_order, orders)))
print("Замовлення дорожчі за 1000:", list(filter(very_expensive_order, orders)))


# Приклад partial: форматування повідомлень про замовлення
def format_order_message(prefix, order):
    return f"{prefix} Order #{order['id']}: {order['total']} UAH, status={order['status']}"


format_admin_order = partial(format_order_message, "ADMIN")
format_customer_order = partial(format_order_message, "CUSTOMER")

print("Повідомлення для адміністратора:")
print(list(map(format_admin_order, orders)))

print("Повідомлення для клієнта:")
print(list(map(format_customer_order, orders)))

print("\nПояснення:")
print("Карування доречне для побудови фільтрів, бо ми фіксуємо limit і отримуємо predicate-функцію.")
print("partial доречний для форматування, бо ми фіксуємо prefix у вже готовій функції.")


# =============================================================================
# Загальний висновок
# =============================================================================

print_title("Загальний висновок")

print("Карування — це перетворення функції з кількома аргументами у ланцюжок функцій,")
print("де кожна функція приймає один аргумент і повертає наступну функцію.")
print()
print("Часткове застосування — це створення нової функції шляхом фіксації частини")
print("аргументів уже існуючої функції.")
print()
print("Головна різниця:")
print("- карування змінює спосіб структурування функції: f(a, b) -> f(a)(b);")
print("- partial просто фіксує частину аргументів: partial(f, a) -> нова функція;")
print("- карування ближче до класичного функціонального програмування;")
print("- partial часто практичніший у Python, якщо функції вже написані у звичайному стилі.")
