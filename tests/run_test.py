import os
import subprocess

os.makedirs("report",exist_ok=True)
subprocess.run(["pytest","--junitxml=report/result.xml"])