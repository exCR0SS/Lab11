def dec_to_bin(n):
    if n == 0:
        return "0"
    elif n % 2 == 0:
        return dec_to_bin(n // 2) + "0"
    else:
        return dec_to_bin(n // 2) + "1"