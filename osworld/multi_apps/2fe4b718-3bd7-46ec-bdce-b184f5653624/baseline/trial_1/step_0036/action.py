import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gimp -i --batch-interpreter python-fu-eval -b "exe'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('c(open(\'/tmp/make_gif.py\').read())" &\n'), shell=True, check=True)
import time; time.sleep(0.05)