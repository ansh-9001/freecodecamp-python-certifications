def apply_discount(price,discount):
    if type(price) != int and type(price) != float:
        return 'The price should be a number'
    else:
        if type(discount) != int and type(discount) != float:
            return 'The discount should be a number'
        else:
            if price <= 0:
                return 'The price should be greater than 0'
            else:
                if discount < 0 or discount > 100:
                    return 'The discount should be between 0 and 100'
                else:
                    discount_value = price*(discount/100)
                    discounted_price = price - discount_value
                    return discounted_price

