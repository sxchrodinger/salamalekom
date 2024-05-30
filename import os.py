import os
from random import randint

for day in range(1, 366):  # Mengubah 365 menjadi 366 untuk mewakili tahun 2024
    
    for commit in range(0, randint(1, 10)):
        d = str(day) + ' days ago'
        with open('file.txt', 'a') as file:
            file.write(d + '\n')
        os.system('git add .')
        os.system(f'git commit --date="{d}" -m "commit {day}-{commit}"')

os.system('git push -u origin main')
