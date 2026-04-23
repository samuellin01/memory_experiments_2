import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la ~/Desktop/src_clip.gif 2>&1; ps aux | grep '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('gimp | grep -v grep\n'), shell=True, check=True)
import time; time.sleep(0.05)