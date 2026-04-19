"""
enumerate - enumera iteraveis (índices)
"""

lista = ["Macarrao", "Cebola", "Molho"]
lista.append("Milho")


for i, item in enumerate (lista):
    print(f"{i + 1} | {item}")