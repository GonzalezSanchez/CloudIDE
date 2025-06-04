import subprocess

with open('requirements.txt') as f:
    packages = f.read().splitlines()

'''
for package in packages:
    subprocess.check_call(['pip', 'install', package])
'''


# Skip empty lines and comments
for package in packages:
    package = package.strip()
    if package and not package.startswith('#'):
        subprocess.check_call(['pip', 'install', package])