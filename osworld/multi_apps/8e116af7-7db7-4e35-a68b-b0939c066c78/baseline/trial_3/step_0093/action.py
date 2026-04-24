import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('Repair Services\tRepair\tExpense\t-154.06\t=E11+D12\n'), shell=True, check=True)
import time; time.sleep(0.05)