import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('cp ~/Desktop/*.xcf /tmp/image.xcf && ls -la /tmp/i'), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('mage.xcf\n'), shell=True, check=True)
import time; time.sleep(0.05)