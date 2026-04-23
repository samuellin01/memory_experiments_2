import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote("paste -d',' file1.csv file2.csv | awk -F',' 'NR==1"), shell=True, check=True)
import time; time.sleep(0.05)
import subprocess, shlex; subprocess.run(f'xdotool type --delay 12 -- ' + shlex.quote('{print $1" "$2} NR>1{print $1" "$2}\' > output.csv\n'), shell=True, check=True)
import time; time.sleep(0.05)