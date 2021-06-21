def validate(num):
    if num < 1 or num > 9:
        print("out of range")
    elif num != int(num):
        print("not an integer")
    else:
        print("just right")
        return True
    return False


print(validate(-5))
print(validate(15))
print(validate(5.2))
print(validate(5))
