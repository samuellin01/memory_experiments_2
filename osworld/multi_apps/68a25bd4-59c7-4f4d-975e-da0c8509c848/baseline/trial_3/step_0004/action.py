import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('wget -O /home/user/paper01.pdf https://arxiv.org/p'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('df/1810.04805\n'), shell=True, check=True)
import time; time.sleep(0.05)