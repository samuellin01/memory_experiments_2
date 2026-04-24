import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("McDonald's Restaurant\tFood\tExpense\t-8.10\t=E12+D13\n"), shell=True, check=True)
import time; time.sleep(0.05)