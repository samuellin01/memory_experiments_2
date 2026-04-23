import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('head -5 file1.csv && echo "---" && head -5 file2.c'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('sv\n'), shell=True, check=True)
import time; time.sleep(0.05)