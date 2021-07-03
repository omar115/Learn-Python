import subprocess

filename = r'/home/omar/git_workspace/Learn-Python/bot/testA.py'

while True:

    p = subprocess.Popen('python '+filename, shell=True).wait()

    if p!=0:
        continue
    else:
        break