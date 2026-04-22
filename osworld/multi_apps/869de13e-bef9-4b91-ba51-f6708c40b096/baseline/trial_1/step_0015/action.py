import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mv 2-if-for-array assign1-data_python3 Projects/\n'), shell=True, check=True)
import time; time.sleep(0.05)