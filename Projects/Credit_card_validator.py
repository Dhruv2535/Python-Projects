import re

def validate_credit_card(card_number):
    # Remove any spaces or dashes from the card number
    card_number = re.sub(r'[ -]', '', card_number)

    # Check if the card number is valid using the Luhn algorithm
    if not re.match(r'^\d{16}$', card_number):
        return False
    sum = 0
    for i, digit in enumerate(reversed(card_number)):
        digit = int(digit)
        if i % 2 == 0:
            sum += digit
        else:
            sum += sum_of_double_digit(digit * 2)
    return sum % 10 == 0

def sum_of_double_digit(digit):
    return sum(map(int, str(digit)))

import tkinter as tk

def on_submit():
    card_number = card_number_var.get()
    if validate_credit_card(card_number):
        result_var.set("Valid")
    else:
        result_var.set("Invalid")

root = tk.Tk()
root.title("Credit Card Validator")

card_number_var = tk.StringVar()
card_number_entry = tk.Entry(root, textvariable=card_number_var)
card_number_entry.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

result_var = tk.StringVar()
result_var.set("Enter a card number")
result_label = tk.Label(root, textvariable=result_var)
result_label.pack()

root.mainloop()
