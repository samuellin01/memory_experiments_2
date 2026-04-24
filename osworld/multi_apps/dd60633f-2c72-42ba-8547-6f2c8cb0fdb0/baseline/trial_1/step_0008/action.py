import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat /home/user/gpt_dev_pure_code.py | head -100\n'), shell=True, check=True)
import time; time.sleep(0.05)