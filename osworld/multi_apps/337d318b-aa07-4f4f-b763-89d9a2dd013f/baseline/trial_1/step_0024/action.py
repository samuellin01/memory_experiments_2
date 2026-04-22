import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mkdir -p ~/Desktop/problematic && mv ~/Desktop/"In'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('voice # 243729.pdf" ~/Desktop/problematic/\n'), shell=True, check=True)
import time; time.sleep(0.05)