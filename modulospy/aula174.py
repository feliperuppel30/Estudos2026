import os
import shutil

HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplo')
NOVA_PASTA =os.path.join(DESKTOP, 'nova_pasta')


shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)