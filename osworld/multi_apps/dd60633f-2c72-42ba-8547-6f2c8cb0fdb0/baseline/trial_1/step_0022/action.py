import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('grep -n "class GPT\\|GPTLanguageModel" /home/user/g'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('pt_dev_pure_code.py | head -5\n'), shell=True, check=True)
import time; time.sleep(0.05)