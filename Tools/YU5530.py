#!/usr/bin/python -tt
import sys
import subprocess
import time
import os



def fastboot_function(device, usb_attrs, flash_script_path):

	cmd1 = 'fastboot'+usb_attrs+'getvar product'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)
	time.sleep(2)

	if len(scan1) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif scan1.find('WT6755_66_SZ_') >= 0:
		print('Yunicorn ('+device+')')
		
		if _platform == 'linux' or _platform == 'linux2':
			flash_script_module = os.path.join(flash_script_path, 'flash.sh')
			subprocess.call(['source '+flash_script_module+' '+flash_script_path], shell=True)
			wait_for_user_input = raw_input('Device Flashed Successfully !!! .......')

		elif _platform == 'darwin':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')
		
		elif _platform == 'win32':
			print('Found '+_platform+'\n'+'')
			flash_script_module = os.path.join(flash_script_path, 'flash_all.bat')
			subprocess.Popen(flash_script_module+' '+flash_script_path+'\/', stderr=subprocess.STDOUT).communicate()
			wait_for_user_input = raw_input('Device Flashed Successfully !!! .......')
			
		else :
			print('Unable to recognise this OS')



	else :
		print('Device Not '+device+', \nExit!')


if __name__ == '__main__':

	fastboot_function(sys.argv[0], sys.argv[1], sys.argv[5])
