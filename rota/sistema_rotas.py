
company1 = float(input('Type the KM of company 1:'))
company2 = float(input('Type the KM of company 2:'))

print(f'The distancie between them is{abs(company1 -company2)} KM')

cost = (abs(company1 - company2)*5)
print(f'The delivery cost is R$({cost:.2f})')