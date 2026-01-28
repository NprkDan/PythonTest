def main():
    """Główna pętla programu FizzBuzz."""
    for i in range(1, 101):
        # Sprawdzamy najpierw podzielność przez obie liczby (15)
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        # Potem pojedyncze warunki
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        # Jeśli żaden warunek nie jest spełniony, drukujemy liczbę
        else:
            print(i)

if __name__ == "__main__":
    main()