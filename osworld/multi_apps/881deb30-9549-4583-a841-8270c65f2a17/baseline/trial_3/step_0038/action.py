import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('libreoffice --calc /home/user/Documents/Fundings/e'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cs/ecs_pass_rates.csv &\n'), shell=True, check=True)
import time; time.sleep(0.05)