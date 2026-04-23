import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find /home/user -name "*.odp" -o -name "*.pptx" -o'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' -name "*.ppt" 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)