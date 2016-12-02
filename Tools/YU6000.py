#!/usr/bin/python -tt
import sys
import subprocess
from sys import platform as _platform
import time


def fastboot_function(device, usb_attrs, flash_script_path):

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
		else :
			print('Unable to recognise this OS')


	else :
		print('Device Not '+device+', \nExit!')


if __name__ == '__main__':

	fastboot_function(sys.argv[0], sys.argv[1], sys.argv[5])