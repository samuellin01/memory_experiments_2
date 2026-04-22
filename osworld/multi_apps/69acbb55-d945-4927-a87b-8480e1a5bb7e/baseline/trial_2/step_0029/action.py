import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('du -sh /tmp/* 2>/dev/null | sort -rh | head -10\n'), shell=True, check=True)
import time; time.sleep(0.05)