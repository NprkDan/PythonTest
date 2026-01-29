active = True

while active:
    print("\n--- Menu Kalkulatora ---")
    option = int(input("Wybierz 1 (+), 2 (-), 3 (*), 4 (/), lub 0 by wyjść: "))

    if option == 0:
        print("Zamykanie programu...")
        active = False  # To kończy pętlę
    
    elif option in (1, 2, 3, 4):
        num1 = float(input("Podaj pierwszą liczbę: "))
        num2 = float(input("Podaj drugą liczbę: "))

        if option == 1:
            print(f"Wynik: {num1 + num2}")
        elif option == 2:
            print(f"Wynik: {num1 - num2}")
        elif option == 3:
            print(f"Wynik: {num1 * num2}")
        elif option == 4:
            if num2 != 0:
                print(f"Wynik: {num1 / num2}")
            else:
                print("Błąd: Nie dziel przez 0!")
    else:
        print("Nieprawidłowa opcja, spróbuj ponownie.")