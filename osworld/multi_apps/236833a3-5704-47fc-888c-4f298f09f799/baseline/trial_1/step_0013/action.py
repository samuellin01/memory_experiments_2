import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('huggingface.co/papers?date=2024-03-01\n'), shell=True, check=True)
import time; time.sleep(0.05)