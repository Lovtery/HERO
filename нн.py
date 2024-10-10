name = input("введите имя вашего героя ")
age = int(input("введите возраст вашего героя "))
hero = input(f"{name} герой? ") == ("true/false")
if hero == "true": age += 1
else:
    print(f"вашему герою {age}")