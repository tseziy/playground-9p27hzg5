import subprocess
import os

script_path = os.path.join('battle1-project', 'universe.py')
respone = subprocess.check_output("py " + (script_path)).decode('utf-8').rstrip()
if respone == '1':
    print('TECHIO> success true')
else:
    print('TECHIO> success false')