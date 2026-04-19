"""
Imprecisão dos pontos flutuantes
"""
import decimal

numero_1 = decimal.Decimal(0.1)
numero_2 = decimal.Decimal(0.7)
resultado = numero_1 + numero_2

print(resultado)
print(f"{resultado:.2f}")
print(round(resultado, 2))
