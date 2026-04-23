import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('wc -l file1.csv file2.csv\n'), shell=True, check=True)
import time; time.sleep(0.05)