import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('The Shining Stephen King'), shell=True, check=True)
import time; time.sleep(0.05)