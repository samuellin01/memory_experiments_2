import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('rm file1.csv file2.csv && libreoffice --calc ~/Des'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ktop/output.csv &\n'), shell=True, check=True)
import time; time.sleep(0.05)