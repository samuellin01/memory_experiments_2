import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('which conda 2>/dev/null; find /home /opt /root -na'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('me "conda" -type f 2>/dev/null | head -20\n'), shell=True, check=True)
import time; time.sleep(0.05)