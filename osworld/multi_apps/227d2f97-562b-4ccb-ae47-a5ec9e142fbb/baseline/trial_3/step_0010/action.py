import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('XCF_FILE=$(ls ~/Desktop/*.xcf) && echo "$XCF_FILE"'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('\n'), shell=True, check=True)
import time; time.sleep(0.05)