import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('python3 /tmp/fix_ecs.py\n'), shell=True, check=True)
import time; time.sleep(0.05)