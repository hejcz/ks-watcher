import sys
import os

if len(sys.argv) != 2:
    print('pass one of: check, update, track')

opt = sys.argv[1]

if opt == 'update':
    os.system('poetry run python3 kswatcher/update.py')
elif opt == 'check':
    os.system('poetry run python3 kswatcher/check.py')
   
