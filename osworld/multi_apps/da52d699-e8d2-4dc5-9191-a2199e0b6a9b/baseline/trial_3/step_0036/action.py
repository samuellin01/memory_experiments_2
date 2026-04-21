import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('2001 A Space Odyssey Arthur C Clarke'), shell=True, check=True)
import time; time.sleep(0.05)