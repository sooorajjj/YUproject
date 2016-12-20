#!/usr/bin/python -tt
import sys
from sys import platform as _platform
import os
import subprocess
import time



def validation(device, flash_script_path, qfil_path, firmware_path):

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
			print('Device Verification Successful !')
			if _platform == 'linux' or _platform == 'linux2':
				device_firmware_path = os.path.join(firmware_path, 'YU4711+')
				flash_script_module = os.path.join(device_firmware_path, 'flash.sh')

				subprocess.call(['source '+flash_script_module+' '+device_firmware_path], shell=True)
				wait_for_user_input = raw_input('Device Flashed Successfully !!! .......')

			
			elif _platform == 'darwin':
				print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')

			elif _platform == 'win32':
				print('Found '+_platform+'\n'+'')

				device_firmware_path = os.path.join(firmware_path, 'YU4711+')
				flash_script_module = os.path.join(device_firmware_path, 'fastboot_flash.cmd')
				subprocess.Popen(flash_script_module+' '+device_firmware_path+'\/', stderr=subprocess.STDOUT).communicate()
				wait_for_user_input = raw_input('Device Flashed Successfully !!! .......')

				
				# print('------------[ Detach Your Device From Pc, Get it into Download Mode, And Reconnect it Now ]------------')
				# print('-----------[ Program is about to lunch QFIL tool with all the Firmwares loaded for YU4711+ ]-----------')
				# print('-------[ You Only need To Select the Port And Flat Build option in QFIL Tool and press Download]-------')
				
				# wait_for_user_input = raw_input('Press ENTER to Lunch QFIL tool:')

				# qfil_module = os.path.join(qfil_path, 'QFIL.exe')
				# device_firmware_path = os.path.join(firmware_path, 'YU4711+')

				# arg1 = ' -Mode=1 '
				# arg2 = '-COM=6 '
				# arg3 = '-SEARCHPATH="'+ device_firmware_path +'" '
				# arg4 = '-Sahara=true;"'+ device_firmware_path +'\prog_emmc_FireHose_8916.mbn" '
				# arg5 = '-RawProgram=rawprogram0.xml '
				# arg6 = '-patch=patch0.xml '
				# os.system(qfil_module + arg1 + arg2 + arg3 + arg4 + arg5 + arg6)
				

			else :
				print('Unable to recognise this OS')

	 
		elif int(substr_scan2) <= 1000000:#MemTotal:         916404 kB
			print('Yunique '+device)
	

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
			print('Unknown Model of Yunique')

	else :
		print('Device Not '+device+', \nExit!')


def fastboot_function(usb_attrs, recoveries_path):

	cmd0 = 'fastboot'+usb_attrs+'reboot-bootloader'
	scan0 = str(subprocess.check_output(cmd0, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan0)
	time.sleep(5)

	cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'TWRP-2.8.7.0_jalebi-v2.img')
	scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
	print(scan)
	time.sleep(20)


if __name__ == '__main__':
	fastboot_function(sys.argv[1], sys.argv[4])
	validation(sys.argv[0], sys.argv[5], sys.argv[6], sys.argv[9])
