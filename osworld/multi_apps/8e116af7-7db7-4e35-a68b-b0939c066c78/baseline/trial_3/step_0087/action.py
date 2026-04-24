import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Grocery Shopping\tGroceries\tExpense\t-186.93\t=E8+D9\n'), shell=True, check=True)
import time; time.sleep(0.05)