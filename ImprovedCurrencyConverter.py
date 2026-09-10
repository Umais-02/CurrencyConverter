from decimal import Decimal, InvalidOperation


CURRENCY_RATES = {
    "1": ("USD", Decimal("277.38")),
    "2": ("Pounds", Decimal("374.20")),
    "3": ("Turkish Lira", Decimal("6.50")),
    "4": ("Euro", Decimal("310.50")),
    "5": ("AED", Decimal("75.00")),
}


def get_valid_amount():
    while True:
        try:
            amount = input("Enter amount in PKR: ").strip()
            if not amount:
                raise ValueError("Amount cannot be empty.")
            return Decimal(amount)
        except (InvalidOperation, ValueError) as e:
            print(f"Invalid amount. Please enter a valid number. ({e})")


def show_menu():
    print("\nCurrency Converter")
    print("Choose a currency to convert PKR into:")
    for key, (name, _) in CURRENCY_RATES.items():
        print(f"{key}. {name}")
    print("0. Exit")


def convert_pkr_to_currency(amount_pkr: Decimal, rate: Decimal) -> Decimal:
    return amount_pkr / rate


def main():
    print("Welcome to the improved currency converter!\n")

    while True:
        show_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            print("Thank you for using the converter. Goodbye!")
            break

        selected_currency = CURRENCY_RATES.get(choice)
        if selected_currency is None:
            print("Invalid choice. Please select a valid option.")
            continue

        currency_name, rate = selected_currency
        amount_pkr = get_valid_amount()
        converted_amount = convert_pkr_to_currency(amount_pkr, rate)

        print(
            f"{amount_pkr:.2f} PKR = {converted_amount:.2f} {currency_name}"
        )

        again = input("Do you want to convert another amount? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thank you for using the converter. Goodbye!")
            break


if __name__ == "__main__":
    main()
