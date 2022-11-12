import subprocess
import os
from universe import main

#print(os.path.abspath(os.curdir))
#respone = subprocess.check_output("python3 universe.py").decode('utf-8').rstrip()
respone = main()
if respone == '1':
    print('TECHIO> success true')
else:
    print('TECHIO> success false')