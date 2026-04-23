import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gimp -i -b \'(python-fu-eval RUN-NONINTERACTIVE 0 "'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('exec(open(\'/tmp/gifmaker.py\').read())")\' 2>&1 &\n'), shell=True, check=True)
import time; time.sleep(0.05)