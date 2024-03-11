import os
import subprocess

dir = './tests'
files = [f for f in os.listdir(dir) if os.path.isfile(
    os.path.join(dir, f)) and f.endswith('.grh')]

for file in files:
    subprocess.run(
        ['./pce', 'MC', os.path.join(dir, file), '0.5', 'output.txt'])
    input()
