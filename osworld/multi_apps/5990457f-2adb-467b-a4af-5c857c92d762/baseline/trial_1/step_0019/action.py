import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('curl -s "https://scholar.google.com/citations?user'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('=WLN3QrAAAAAJ" | head -100\n'), shell=True, check=True)
import time; time.sleep(0.05)