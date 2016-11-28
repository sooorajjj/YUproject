#!/usr/bin/python -tt
import sys
import os
import subprocess
import time



def validation(device):

	cmd1 = 'adb devices'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)

	time.sleep(5)

	cmd2 = 'adb shell mount /system && adb shell grep -m 1  "^ro.product.model=" /system/build.prop'
	scan2 = str(subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan = scan2[17:] #len(scan)-2

	cmd3 = 'adb shell grep -m 1  "^MemTotal:" /proc/meminfo'
	scan3 = str(subprocess.check_output(cmd3, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan2 = scan3[17:len(scan3)-3] #len(scan)-2 #MemTotal:        1953696 kB #MemTotal:         916404 kB
	print(substr_scan +' String length : ' + str(len(substr_scan)))

	if len(substr_scan) == 0 :#MemTotal:        1953696 kB
		print("Device Validation Failed, \nExit! ")

	elif device.find(substr_scan) >= 0:

		if int(substr_scan2) >= 1553696:#MemTotal:        1953696 kB
			print('Yunique Plus '+device+'+')
	 
		elif int(substr_scan2) <= 1000000:#MemTotal:         916404 kB
			print('Yunique '+device)

		else :
			print('Unknown Model of Yunique')

	else :
		print('Device Not '+device+', \nExit!')


def fastboot_function(usb_attrs, recoveries_path):

	cmd0 = 'fastboot'+usb_attrs+'reboot-bootloader'
	scan0 = str(subprocess.check_output(cmd0, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan0)
	time.sleep(5)

	cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'TWRP-2.8.7.0_jalebi-v2.img')
	print(cmd)
	scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan)
	time.sleep(13)


if __name__ == '__main__':
	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0])
