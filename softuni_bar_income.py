import re
pattern = r'[^\|\$\%\.]*\%(?P<name>[A-Z][a-z]+)\%[^\|\$\%\.]*\<(?P<product>[\w]+)\>[^\|\$\%\.]*\|(?P<count>[0-9]+)' \
          r'\|[^\|\$\%\.]*(?P<price>\b[0]\.?\d+|[1-9][0-9]*\.?\d+\b)\$[^\|\$\%\.]*'

customer_list = dict()
total_income = 0
command = input()

while command != 'end of shift':
    matches = re.finditer(pattern, command)
    for match in matches:
        cust = match.group('name')
        product = match.group('product')
        count = int(match.group('count'))
        price = float(match.group('price'))
        customer_list[cust] = {"Product": product, "Total": (count*price)}
        total_income += customer_list[cust]['Total']
        print(f"{cust}: {customer_list[cust]['Product']} - {customer_list[cust]['Total']:.2f}")
    command = input()

print(f"Total income: {total_income:.2f}")
