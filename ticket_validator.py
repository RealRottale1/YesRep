# ticket_validator.py -- start with stubs, no logic

def validate_ticket(code):
    if (not (type(code) is str)):
        raise TypeError
    if (len(code) == 8):
        f = ''.join(code[0::2])
        s = ''.join(code[2::9])
        if (type(f) is str) and (type(int(s)) is int):
            return True
    return False

def get_ticket_tier(code):
    try:
        if validate_ticket(code):
            if code[0] != "T" and code[1] != "K":
                raise ValueError
            s = ''.join(code[2])
            firstDigit = int(s)
            print(s)
            if firstDigit <= 3:
                return "General"
            elif firstDigit <= 6:
                return "VIP"
            elif firstDigit <= 9:
                return "Platinum"
    except:
        raise ValueError

def calculate_total(prices, discount=0):
    if not (type(prices) is list):
        raise TypeError
    if not prices:
        raise ValueError
    if discount < 0 or discount > 1:
        raise ValueError
    return round(sum(prices) * (1-discount), 2)
    
