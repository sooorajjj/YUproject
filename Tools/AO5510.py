#!/usr/bin/python -tt
import sys
import subprocess
import time
import os

def validation(device, flash_script_path):

	cmd1 = 'adb devices'
	scan1 = str(subprocess.check_output(cmd1, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan1)

	time.sleep(4)
	cmd2 = 'adb shell mount /system && adb shell grep -m 1  "^ro.product.name=" /system/build.prop'
	scan2 = str(subprocess.check_output(cmd2, shell=True, stderr=subprocess.STDOUT).strip())
	substr_scan = scan2[16:] #len(scan)-2
	print(substr_scan +' String length : ' + str(len(substr_scan)))

	cmd3 = 'adb shell grep panel.xres= /proc/cmdline'
	scan3 = str(subprocess.check_output(cmd3, shell=True, stderr=subprocess.STDOUT).strip())
	# substr_scan = scan2[17:] #len(scan)-2

	if len(substr_scan) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif substr_scan.find('YUREKA') >= 0:
		print('True')
		
		if scan3.find('panel.xres=720') :
			print('Yureka')

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
			print('Unknown Model of'+device)

	else :
		print('Device Not '+device+', \nExit!')


def fastboot_function(usb_attrs, recoveries_path):

	# cmd = 'fastboot'+usb_attrs+'getvar version'
	# scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())

	cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'twrp-3.0.2-0-tomato.img')
	scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan)
	time.sleep(20)

if __name__ == '__main__':

	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0], sys.argv[5])
