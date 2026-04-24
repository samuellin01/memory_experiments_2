import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls ~/Documents/Novels/4th\\ Year\\ in\\ Tsinghua/\n'), shell=True, check=True)
import time; time.sleep(0.05)