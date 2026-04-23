import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la ~/Desktop/src_clip.gif 2>/dev/null && echo '), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('"GIF EXISTS" || echo "GIF NOT YET"\n'), shell=True, check=True)
import time; time.sleep(0.05)