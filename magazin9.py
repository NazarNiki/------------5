prices = {
    "sword": 10,
    "armor": 15,
    "amulet of wind power": 500
}

# Вводим количество денег у пользователя
money = float(input("Сколько у вас денег? $"))

# Вводим название товара
product = input("Какой товар вы хотите купить? ")

# Проверяем, хватает ли денег на товар
if product in prices:
    if money >= prices[product]:
        print(f"Вы можете купить {product} за ${prices[product]}.")
        money -= prices[product]
        print(f"У вас осталось ${money}.")
    else:
        print("Извините, у вас недостаточно денег.")
else:
    print("Этого товара нет в магазине.")