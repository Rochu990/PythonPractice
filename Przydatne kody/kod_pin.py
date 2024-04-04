def validate_pin(pin):

    pin_1 = "0123456789"
    pin_1List = list(pin_1)

    pin = list(pin)

    y = True

    if len(pin) != 4 and len(pin) != 6:
        y = False
    else:
        for x in pin:
            if x not in pin_1List:
                y = False
    return y


print(validate_pin("1234"))
