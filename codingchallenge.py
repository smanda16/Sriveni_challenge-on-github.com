import re

def validate_credit_card(card):
    # Check if card starts with 4, 5, or 6 and has only digits and optional hyphens
    if re.match(r'^[456]\d{3}(-?\d{4}){3}$', card):
        # Remove hyphens to get continuous string of digits
        digits_only = ''.join(card.split('-'))
        # Check if no digit is repeated consecutively 4 or more times
        if not re.search(r'(\d)\1{3,}', digits_only):
            return 'Valid'
    return 'Invalid'

if _name_ == "_main_":
    n = int(input().strip())
    for _ in range(n):
        card_number = input().strip()
        print(validate_credit_card(card_number))