def exponent(base , exp ):
    product = 1
    while exp > 0 :
        product *= base
        exp -= 1
    return product
