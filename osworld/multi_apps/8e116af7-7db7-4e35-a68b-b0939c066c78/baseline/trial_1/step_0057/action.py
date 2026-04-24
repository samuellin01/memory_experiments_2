import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Bank Transfer\tBanking\tExpense\t-3670\t=E9+D10\n'), shell=True, check=True)
import time; time.sleep(0.05)