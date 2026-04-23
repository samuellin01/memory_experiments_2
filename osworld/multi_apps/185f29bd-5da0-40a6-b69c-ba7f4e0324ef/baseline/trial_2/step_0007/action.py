import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find ~/ -name "*.xlsx" -o -name "*.pdf" 2>/dev/nul'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('l\n'), shell=True, check=True)
import time; time.sleep(0.05)