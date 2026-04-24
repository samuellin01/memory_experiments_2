import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('head -5 ~/Desktop/stock.csv\n'), shell=True, check=True)
import time; time.sleep(0.05)