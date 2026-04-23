import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la ~/Desktop/file1.xlsx ~/Desktop/file2.ods\n'), shell=True, check=True)
import time; time.sleep(0.05)