import re


# Numeros enteros pares
def validate_a(value: str) -> bool:
    my_string = r"[-+0]?(\d*[02468])+$"
    return re.search(my_string, value) is not None


# Numeros pares sin cero significativos
def validate_b(value: str) -> bool:
    my_string = r"(^[-+]?)([1-9]\d{0,}[02468]$|(^[1-9]+[02468]$|^[2468]$))"
    return re.search(my_string, value) is not None


# Variable de Python
def validate_c(value: str) -> bool:
    my_string = r"\_|\w+\_|[a-z0-9]+$"
    return (my_string, value) is not None


# Cadenas del tipo {a^nbc^n/n,m > 0}
def validate_d(value: str) -> bool:
    my_string = r"[a]+b{1}[c]+"
    return re.search(my_string, value) is not None


# Direcciones IPv4
def validate_e(value: str) -> bool:
    my_string = r"^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$"
    return re.search(my_string, value) is not None


# Direcciones IPv4 con puerto
def validate_f(value: str) -> bool:
    my_string = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])(.(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])){3}(:(6553[0-5]|655[0-2][0-9]|65[0-4][0-9]{2}|6[0-4][0-9]{3}|[0-5]?([0-9]){0,3}[0-9]))?$"
    return re.search(my_string, value) is not None


# Numeros de VISA
def validate_g(value: str) -> bool:
    my_string = r"^4[0-9]{13,16}$"
    return re.search(my_string, value) is not None


if __name__ == '__main__':
    my_chain = "-0258"
    print(validate_b(my_chain))
