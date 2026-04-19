salas = [
    ["Rodernilson", "Valmiresclaudio"], 
    ["Terezenalopis", "Sr Nilson"], 
    ["Abravanelson", "Torenereza"]
]

for i, sala in enumerate(salas):
    print("\n===========================")
    print(f"Sala {i} | {sala}")
    print("===========================\n")

    for i, pessoa in enumerate(sala):
        print(f"Aluno {i} | {pessoa}")

