from type_checker import type_checked

@type_checked
def multiply(s: str, x: int) -> str:
    return s * x

print(multiply('a', 4))