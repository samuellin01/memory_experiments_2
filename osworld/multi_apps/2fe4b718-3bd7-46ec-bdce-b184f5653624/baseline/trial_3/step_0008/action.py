import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/frames/ | wc -l && ls ~/Desktop/frame'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('s/ | head -20\n'), shell=True, check=True)
import time; time.sleep(0.05)