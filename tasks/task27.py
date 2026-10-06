def calculate_discount(order_amount, threshold, discount_percent):
    if order_amount < 0:
        raise ValueError("Сумма заказа не может быть отрицательной")

    if order_amount >= threshold:
        discount = order_amount * discount_percent / 100
    else:
        discount = 0

    final_price = order_amount - discount

    return final_price


# Примеры проверки
print(calculate_discount(9000, 10000, 10))   # Скидки нет
print(calculate_discount(10000, 10000, 10))  # Скидка на границе порога
print(calculate_discount(15000, 10000, 10))  # Скидка 10%
