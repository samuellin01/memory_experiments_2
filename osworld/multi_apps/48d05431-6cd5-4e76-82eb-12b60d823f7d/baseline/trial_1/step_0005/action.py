import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('wget https://repo.anaconda.com/miniconda/Miniconda'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh\n'), shell=True, check=True)
import time; time.sleep(0.05)