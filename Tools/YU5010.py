#!/usr/bin/python -tt
import sys
import subprocess
import time
import os


def validation(device, flash_script_path):

	cmd1 = 'adb devices'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)
	time.sleep(8)

	cmd2 = 'adb shell mount /system && adb shell grep -m 1  "^ro.product.model=" /system/build.prop'
	scan2 = str(subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan = scan2[17:] #len(scan)-2
	print(substr_scan +' String length : ' + str(len(substr_scan)))

	if len(substr_scan) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif device.find(substr_scan) >= 0:
		print('True')
		flash_script_module = os.path.join(flash_script_path, 'flash.sh')
		# execfile(flash_script_module)#it will be available in execfile[Target] __main__
		subprocess.call(['source '+flash_script_module+' '+flash_script_path], shell=True)

	else :
		print('Device Not '+device+', \nExit!')


def fastboot_function(usb_attrs, recoveries_path):

	cmd0 = 'fastboot'+usb_attrs+'reboot-bootloader'
	scan0 = str(subprocess.check_output(cmd0, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan0)
	time.sleep(5)

	cmd1 = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'twrp-yuphoria.img')
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)
	time.sleep(20)



if __name__ == '__main__':

	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0], sys.argv[5])
