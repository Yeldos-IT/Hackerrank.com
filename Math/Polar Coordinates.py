import cmath
z = input().strip()
pol = cmath.polar(complex(z))
print(pol[0])
print(pol[1])