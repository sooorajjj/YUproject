#!/usr/bin/python -tt
import sys
import subprocess
import time
import os


def validation(device, flash_script_path):
	cmd1 = 'adb devices'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)
	time.sleep(6)

	cmd2 = 'adb shell mount /system && adb shell grep -m 1  "^ro.product.model=" /system/build.prop'
	scan2 = str(subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan = scan2[17:] #len(scan)-2
	print(substr_scan +' String length : ' + str(len(substr_scan)))

	if len(substr_scan) == 0 :
		print('Device Validation Failed, \nExit! ')

	elif device.find(substr_scan) >= 0:
		print('Yureka S ('+device+')')

		if _platform == 'linux' or _platform == 'linux2':
			flash_script_module = os.path.join(flash_script_path, 'flash.sh')
			subprocess.call(['source '+flash_script_module+' '+flash_script_path], shell=True)
		
		elif _platform == 'darwin':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')
		
		elif _platform == 'win32':
			print('Found '+_platform+'\n'+'')
			flash_script_module = os.path.join(flash_script_path, 'flash_all.bat')
			subprocess.Popen(flash_script_module+' '+flash_script_path+'\/', stderr=subprocess.STDOUT).communicate()

		else :
			print('Unable to recognise this OS')

	else :
		print('Device Not '+device+', \nExit!')


def fastboot_function(usb_attrs, recoveries_path):

	cmd1 = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'castor_recovery.img')
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)
	time.sleep(10)


if __name__ == '__main__':

	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0], sys.argv[5])
