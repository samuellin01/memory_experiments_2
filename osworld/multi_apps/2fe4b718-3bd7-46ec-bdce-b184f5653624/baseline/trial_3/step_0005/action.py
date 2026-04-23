import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Desktop/frames/ | head -20 && echo "---" && l'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('s ~/Desktop/frames/ | wc -l\n'), shell=True, check=True)
import time; time.sleep(0.05)