import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('happy-extension v0.0.1'), shell=True, check=True)
import time; time.sleep(0.05)