import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Carrot & Ginger Soup\tFood\tExpense\t-5.70\t=E10+D11\n'), shell=True, check=True)
import time; time.sleep(0.05)