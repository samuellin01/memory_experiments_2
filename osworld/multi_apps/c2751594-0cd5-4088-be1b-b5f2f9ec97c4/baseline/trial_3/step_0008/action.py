import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('ls -la attached_file_extracted/word/media/\n'), shell=True, check=True)
import time; time.sleep(0.05)