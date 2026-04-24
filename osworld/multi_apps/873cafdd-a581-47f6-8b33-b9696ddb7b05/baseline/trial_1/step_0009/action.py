import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('https://chromewebstore.google.com/search/Speechify'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('%20Text%20to%20Speech%20Voice%20Reader\n'), shell=True, check=True)
import time; time.sleep(0.05)