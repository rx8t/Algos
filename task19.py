with open("task19_test", "r") as f:
    parag_counts = 0
    in_parag = False
    for line in f:
        if line.strip():
            if not in_parag:
                parag_counts +=1
                in_parag = True
        else:
            in_parag = False
print("Количество абзацей в файле: " + str(parag_counts))