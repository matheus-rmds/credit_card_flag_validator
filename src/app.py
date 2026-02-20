"""
Credit Card Flag Validator

Identifies credit card types based on their number prefixes using regex patterns.
Supports: Visa, MasterCard, American Express, Discover, Hipercard, and Elo.

Example:
    validate_credit_card("4532123456789010")  # Returns 'Visa'
"""

import re

# Card type patterns - easily extensible by adding new entries
CREDIT_CARD_PATTERNS = {
    "Visa": r"^4\d+$",
    "MasterCard": r"^(5[1-5]|2[2-7])\d+$",
    "American Express": r"^3[47]\d+$",
    "Discover": r"^(6011|65|64[4-9])\d+$",
    "Hipercard": r"^6062\d+$",
    "Elo": r"^(4(011|312|389)|50(18|20|38)|5893|65\d{2}|723[1-3])\d+$",
}


def validate_credit_card(card_number):
    """
    Identify credit card type from card number.
    
    Removes spaces/hyphens, validates format, and matches against card patterns.
    
    Args:
        card_number: Credit card number (str or int)
        
    Returns:
        Card type: 'Visa', 'MasterCard', 'American Express', 'Discover', 
                   'Hipercard', 'Elo', 'Invalid', or 'Unknown'
    """
    # Normalize card number by removing spaces and hyphens
    card_number = str(card_number).replace(" ", "").replace("-", "")
    
    # Validate that the input contains only digits
    if not card_number.isdigit():
        return "Invalid"
    
    # Check each card pattern against the normalized card number
    for card_type, pattern in CREDIT_CARD_PATTERNS.items():
        if re.match(pattern, card_number):
            return card_type
    
    # No pattern matched
    return "Unknown"


def run_validation_tests():
    """Run test cases to verify the credit card validator works correctly."""
    test_cases = [
        ("4532123456789010", "Visa"),
        ("5425233010103442", "MasterCard"),
        ("378282246310005", "American Express"),
        ("6011111111111117", "Discover"),
        ("6062123456789012", "Hipercard"),
        ("4011123456789012", "Elo"),
        ("5018123456789012", "Elo"),
        ("7231123456789012", "Elo"),
        ("1234567890123456", "Unknown"),
        ("4532-1234-5678-9010", "Visa"),  # With hyphens
        ("5425 2330 1010 3442", "MasterCard"),  # With spaces
        ("abc123", "Invalid"),  # Invalid format
    ]
    
    print("=" * 70)
    print("CREDIT CARD FLAG VALIDATOR - TEST RESULTS")
    print("=" * 70)
    print()
    
    passed = 0
    failed = 0
    
    for card_number, expected_type in test_cases:
        result = validate_credit_card(card_number)
        status = "OKAY " if result == expected_type else "ERROR"
        
        if result == expected_type:
            passed += 1
        else:
            failed += 1
        
        print(f"{status} | Card: {card_number:25} | Expected: {expected_type:18} | Got: {result}")
    
    print()
    print("=" * 70)
    print(f"Total: {len(test_cases)} | Passed: {passed} | Failed: {failed}")
    print("=" * 70)


if __name__ == "__main__":
    run_validation_tests()
