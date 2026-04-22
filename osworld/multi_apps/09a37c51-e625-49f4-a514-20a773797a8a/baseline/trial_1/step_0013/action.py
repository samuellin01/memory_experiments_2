import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pip3 install onnxruntime 2>&1 | tail -5\n'), shell=True, check=True)
import time; time.sleep(0.05)