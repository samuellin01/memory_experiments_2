import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cat 1.txt 2.txt 3.txt 4.txt 5.txt\n'), shell=True, check=True)
import time; time.sleep(0.05)