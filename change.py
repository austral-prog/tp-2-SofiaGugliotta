def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(f"{expense}")
    print("Dinero")
    print(f"{money}")
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(f"int({money} - {expense})")
    print("Centavos:")
    print(f"int(float {money} - {expense} - int({money} - {expense}) *100)")
