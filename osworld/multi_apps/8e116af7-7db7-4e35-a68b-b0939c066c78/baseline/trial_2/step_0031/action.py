import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('echo "=== RECEIPT 0 ===" && cat /tmp/r0.txt && ech'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('o "=== RECEIPT 1 ===" && cat /tmp/r1.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)