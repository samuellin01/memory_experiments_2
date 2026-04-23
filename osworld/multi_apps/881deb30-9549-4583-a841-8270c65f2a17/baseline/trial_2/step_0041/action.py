import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('libreoffice --calc ~/Documents/Fundings/ecs/ECS_Pa'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ss_Rate_by_School_and_Year.csv &\n'), shell=True, check=True)
import time; time.sleep(0.05)