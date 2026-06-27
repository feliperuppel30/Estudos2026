

import os
from itertools import count

caminho = 'D:\\projeto2026\\exemploimgs'
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter= next(counter)
    print(f'contador: {the_counter}')
    print(root)
    print(dirs)
    print(files)