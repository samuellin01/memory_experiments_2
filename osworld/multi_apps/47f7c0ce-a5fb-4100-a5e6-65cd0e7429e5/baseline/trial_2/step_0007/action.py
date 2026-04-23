import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('find /home/user -name "*.pptx" -o -name "*.ppt" -o'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote(' -name "*.odp" 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)