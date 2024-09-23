import os
import random

# Configura el mes y año deseado
año = 2024
mes = 9  # Octubre

for i in range(100):
    d = str(i) + ' days ago'
    # El día se calculará aleatoriamente en el mes de octubre
    rand_day = random.randint(1, 31)
    
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
        
    os.system('git add test.txt')
    os.system(f'git commit --date="{año}-{mes:02d}-{rand_day:02d} 17:51:00 -0500" -m "Commit {i}"')

# Intenta hacer push
push_result = os.system('git push -u origin main')

# Verifica si el push fue exitoso
if push_result != 0:
    print("El push falló. Revisa si hay conflictos.")
