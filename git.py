import os
import random

# Configura el mes y año deseado
año = 2024
mes = 9  # Octubre

for i in range(17):
    d = str(i) + ' days ago'
    # El día se calculará aleatoriamente en el mes de octubre
    rand_day = random.randint(1, 31)
    with open('test.txt', 'a') as file:
        file.write(d + '\n')
    os.system(f'git add test.txt')
    os.system(f'git commit --date="{año}-{mes:02d}-{rand_day:02d} 17:51:00 -0500" -m "Commit {i}"')
os.system('git push -u origin main')

#git commit --amend --no-edit --date="Fri Nov 6 20:00:00 2015 -0600"
#git fetch origin master
#git rebase origin/master
