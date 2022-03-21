


import subprocess


def cmd():
    subprocess.check_call(['git', 'pull'])
    subprocess.check_call(['cd', '../coocoowa/'])
    subprocess.check_call(['git', 'restore', '.'])
    subprocess.check_call(['git', 'apply', '../MyPatch/patch.diff'])
    subprocess.check_call(['python3', 'script/build.py', '--mod', 'Gb', '-d', '1', '--path', '/home/gene/Android/Sdk/build-tools/28.0.3', '-v', '9.0.0_9000000'])

if __name__ == '__main__':
    cmd()