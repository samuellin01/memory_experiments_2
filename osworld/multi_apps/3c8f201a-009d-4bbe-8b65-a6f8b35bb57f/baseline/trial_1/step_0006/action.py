import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la ~/Desktop/compressed.jpeg\n'), shell=True, check=True)
import time; time.sleep(0.05)