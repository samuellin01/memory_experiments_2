import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('echo "set number" >> ~/.vimrc\n'), shell=True, check=True)
import time; time.sleep(0.05)