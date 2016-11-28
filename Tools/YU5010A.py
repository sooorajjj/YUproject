#!/usr/bin/python -tt
import sys
import os
import subprocess
import time



def validation(device):

	cmd1 = 'adb devices'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)

	time.sleep(8)

	cmd2 = 'adb shell mount /system && adb shell grep -m 1  "^ro.build.display.wtid=" /system/build.prop'
	scan2 = str(subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan = scan2[22:] #len(scan)-2
	print(substr_scan +' String length : ' + str(len(substr_scan)))

	time.sleep(3)
	cmd3 = 'adb shell grep -m 1  "^ro.product.model=" /system/build.prop'
	scan3 = str(subprocess.check_output(cmd3, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan3 = scan3[17:] #len(scan)-2

	if len(substr_scan3) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif device.find(substr_scan3) >= 0:

		if substr_scan.find('125') >= 0:
			print('Unsigned Device')

		elif substr_scan.find('126') >= 0:
			print('Signed Device')

		else :
			print('Unknown Model of Yuphoria')

	else :
		print('Device Not '+device+', \nExit!')


def fastboot_function(usb_attrs, recoveries_path):

	cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'twrp-yuphoria.img')
	print(cmd)
	scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan)
	time.sleep(20)


if __name__ == '__main__':
	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0])
