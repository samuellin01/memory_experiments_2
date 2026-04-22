import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('du -sh /home/user/.local/lib/python3.10/site-packa'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ges/* 2>/dev/null | sort -rh | head -20\n'), shell=True, check=True)
import time; time.sleep(0.05)