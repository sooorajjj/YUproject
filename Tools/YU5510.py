#!/usr/bin/python -tt
import sys
from sys import platform as _platform
import subprocess
import time
import os


def validation(device, flash_script_path):
	cmd1 = 'adb devices'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)

	cmd2 = 'adb shell mount /system && adb shell grep -m 1  "^ro.product.name=" /system/build.prop'
	scan2 = str(subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan = scan2[16:] #len(scan)-2
	print(substr_scan +' String length : ' + str(len(substr_scan)))

	cmd3 = 'adb shell grep panel.xres= /proc/cmdline'
	scan3 = str(subprocess.check_output(cmd3, shell=True, stderr=subprocess.STDOUT).strip())
	# substr_scan = scan2[17:] #len(scan)-2

	cmd4 = 'adb shell grep -m 1  "^ro.product.model=" /system/build.prop'
	scan4 = str(subprocess.check_output(cmd4, shell=True, stderr=subprocess.STDOUT).strip())

	if len(substr_scan) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif ('YUREKA').find(substr_scan) >= 0:
		print('True')

		if scan3.find('panel.xres=1080') >= 0:
			print('Yureka Plus ')

			if len(scan4) == 0:
				flash_script_module = os.path.join(flash_script_path, 'flash.sh')
				# execfile(flash_script_module)#it will be available in execfile[Target] __main__
				subprocess.call(['source '+flash_script_module+' '+flash_script_path], shell=True)

			else :
				print(' Device is probably Yureka plus YU5510A( A version )')

		else :
			print('Unknown Model of'+device)
			
	else :
		print('Device Not '+device+', \nExit!')

def fastboot_function(usb_attrs, recoveries_path):
	cmd = 'fastboot'+usb_attrs+'getvar version'
	scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
	# version: REFRESH_emmccid_secureboot
	# version: 0.5_emmccid_secureboot

	# print scan +' String length : ' + str(len(scan))
	# print scan +'String length : ' + str(len(scan))

	if scan.find('0.5_emmccid_secureboot') >= 0 :

		print("Unsigned Device Detected")

		if _platform == 'linux' or _platform == 'linux2':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')
		elif _platform == 'darwin':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')
		elif _platform == 'win32':
			print('Found '+_platform+'\n'+'')

			
		else :
			print('Unable to recognise this OS')


		exit()

		
	elif scan.find('REFRESH_emmccid_secureboot') >= 0 :

		print("Signed Device Detected")

		cmd0 = 'fastboot'+usb_attrs+'oem device-info'
		scan0 = str(subprocess.check_output(cmd0, shell=True, stderr=subprocess.STDOUT).strip())
		print(scan0)

		if scan0.find('Device unlocked: false') >= 0 :
			print('Locked Bootloader \n Proceed with unlocking bootloader')

			cmd1 = 'fastboot'+usb_attrs+'oem unlock'
			scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
			print(scan1)

			cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'TWRP_v2.8.7.0_Yureka_Plus.img')
			scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
			print(scan)
			time.sleep(10)


		elif scan0.find('Device unlocked: true') >= 0 :
			print('unlocked bootloader')
			cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'TWRP_v2.8.7.0_Yureka_Plus.img')
			scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
			print(scan)
			time.sleep(10)

		else : 
			print('Wrong choice of device')

	else :
		print('Device Not Found in Database')


if __name__ == '__main__':

	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0], sys.argv[5])
