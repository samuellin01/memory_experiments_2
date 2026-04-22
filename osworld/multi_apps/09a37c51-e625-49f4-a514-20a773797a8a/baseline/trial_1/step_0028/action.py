import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la ~/.u2net/ 2>/dev/null; echo "---"; pip3 sho'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('w rembg 2>/dev/null | head -3\n'), shell=True, check=True)
import time; time.sleep(0.05)