import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cd ~ && git clone https://github.com/kevinboone/tx'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('t2epub.git\n'), shell=True, check=True)
import time; time.sleep(0.05)