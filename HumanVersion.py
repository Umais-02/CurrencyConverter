print("Currency Converter")
pkr = float(input("Enter amount in PKR: "))

print("Choose currency:")
print("1. USD")
print("2. Pounds")
print("3. Turkish Lira")

choice = int(input("Enter your choice: "))

if choice == 1:
    usd = pkr/277.38
    print("PKR", pkr, "=", usd, "USD")
elif choice == 2:
    pounds = pkr/374.20
    print("PKR", pkr, "=", pounds, "Pounds")
elif choice == 3:
    lira = pkr / 6.50
    print("PKR", pkr, "=", lira, "Turkish Lira")
else:
    print("Invalid choice.")