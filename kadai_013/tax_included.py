def tax_included(price, tax):
  return price + (price * tax)

result = tax_included(100, .1)
print(result)