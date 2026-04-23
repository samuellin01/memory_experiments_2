import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('~/miniconda3/bin/conda init bash\n'), shell=True, check=True)
import time; time.sleep(0.05)