""" We are sinking! The nearest ship got our SOS call, 
    but they replied in pure gobbledygook! Are ye savvy enough to decode the message, 
    or will we be sleepin' with the fish tonight? All hands on deck!

    Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform 
    Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven

    Flag format: TFCCTF{RESUL7-H3R3} """

str = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"

words = str.split(' ')

specials = {
    "One": "I", "Two": 2, "Three": "E", "Four": "A",
    "Five": 5, "Six": 6, "Seven": "T", "Eight": 8,
    "Nine": 9, "Zero": "O", "Dash": '-'
}

for w in words:
    print(specials.get(w, w[0]), end="")