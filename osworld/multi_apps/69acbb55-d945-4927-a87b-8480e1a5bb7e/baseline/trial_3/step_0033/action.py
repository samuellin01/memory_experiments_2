import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('df -h / && du -sh ~/.local/lib/python3.10/site-pac'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('kages/ 2>/dev/null && du -sh /tmp/ 2>/dev/null\n'), shell=True, check=True)
import time; time.sleep(0.05)