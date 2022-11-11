import subprocess

respone = subprocess.check_output("py /project/target/universe.py").decode('utf-8').rstrip()
if respone == '1':
    print('TECHIO> success true')
else:
    print('TECHIO> success false')
    