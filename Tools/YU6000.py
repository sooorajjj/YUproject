#!/usr/bin/python -tt
import sys
import subprocess
from sys import platform as _platform
import time


def fastboot_function(device, usb_attrs, flash_script_path, sp_flash_tool_path):

	cmd1 = 'fastboot'+usb_attrs+'getvar product'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)
	time.sleep(2)

	if len(scan1) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif scan1.find('ZAL1860_PLATFORM') >= 0:
		print('Yureka S ('+device+')')

		if _platform == 'linux' or _platform == 'linux2':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')

		elif _platform == 'darwin':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')

		elif _platform == 'win32':
			print('Found '+_platform+'\n'+'')
			sp_flash_tool_module = os.path.join(sp_flash_tool_path, 'flash_tool.exe')
			arg1 = ' -d ' + sp_flash_tool_path+ '\MTK_AllInOne_DA.bin'
			arg2 = ' -s ' + flash_script_path + '\MT6753_Android_scatter.txt'
			arg3 = ' -c firmware-upgrade'
			os.system(sp_flash_tool_module + arg1 + arg2 + arg3)
			
		else :
			print('Unable to recognise this OS')


	else :
		print('Device Not '+device+', \nExit!')


if __name__ == '__main__':

	fastboot_function(sys.argv[0], sys.argv[1], sys.argv[5], sys.argv[8])
