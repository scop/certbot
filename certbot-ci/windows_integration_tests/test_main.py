import subprocess
import sys
import os
import clr

from System.Management.Automation import PowerShell


def test_it():
    root_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

    # Build the installer
    # installer_build_script = os.path.join(root_path, 'windows-installer', 'construct.py')
    # subprocess.check_call([sys.executable, installer_build_script])

    # Run the installer
    # installer_path = os.path.join(root_path, 'windows-installer', 'build',
    #                               'nsis', 'certbot-beta-installer-win32.exe')
    # subprocess.check_call([installer_path, '/S'])

    # Assert certbot can be run from PATH
    subprocess.check_call(['certbot', '--version'])

    # Assert certbot renew task is installed

