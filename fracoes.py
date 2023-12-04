import fractions

p1 = 4
q1 = 3
p2 = 3
q2 = 5

x = fractions.Fraction(p1,q1)
y = fractions.Fraction(p2,q2)
soma = x + y
mult = x * y
print(f'A soma das frações {x} e {y} é igual a {soma}.')
print(f'O produto das frações {x} e {y} é igual a {mult}.')
