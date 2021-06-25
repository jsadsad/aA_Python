GUEST_LIST = {"Kurt": "Germany", "Julia": "France", "Ito": "Japan", "Katherine": "England", "Sam": "Argentina"}

# Write your function, here.
def greeting(name):
    if name not in GUEST_LIST:
        return "Hi! I'm a guest."
    return f"Hi! I'm {name} from {GUEST_LIST[name]}."


print(greeting("Kurt"))  # > "Hi! I'm Kurt from Germany."
print(greeting("Sam"))  # > "Hi! I'm Sam from Argentina."
print(greeting("Monty"))  # > "Hi! I'm a guest."
