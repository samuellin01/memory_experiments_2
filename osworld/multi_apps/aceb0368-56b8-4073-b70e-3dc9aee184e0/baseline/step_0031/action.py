import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('1\t1\t0\t1\t1\t0\t1\t0\t1\t1\t70\n'), shell=True, check=True)
import time; time.sleep(0.05)