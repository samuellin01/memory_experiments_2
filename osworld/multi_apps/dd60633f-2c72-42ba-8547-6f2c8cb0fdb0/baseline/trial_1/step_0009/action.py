import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('head -30 /home/user/gpt_dev_pure_code.py\n'), shell=True, check=True)
import time; time.sleep(0.05)