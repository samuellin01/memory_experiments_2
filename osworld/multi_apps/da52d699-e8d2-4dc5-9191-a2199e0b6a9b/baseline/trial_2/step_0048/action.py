import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('The Andromeda Strain Michael Crichton'), shell=True, check=True)
import time; time.sleep(0.05)