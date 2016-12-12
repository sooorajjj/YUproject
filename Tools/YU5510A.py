#!/usr/bin/python -tt
import sys
from sys import platform as _platform
from xml.etree import ElementTree as ET
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
	substr_scan1 = scan4[17:] #len(scan)-2

	if len(substr_scan) == 0 :
		print("Device Validation Failed, \nExit! ")

	elif ('YUREKA').find(substr_scan) >= 0:
		print('True')

		if scan3.find('panel.xres=1080') :
			print('Yureka Plus ')

			if device.find(substr_scan1) >= 0:
				
				if _platform == 'linux' or _platform == 'linux2':
					flash_module = os.path.join(flash_script_path, 'Signed')
					flash_module_kk = os.path.join(flash_module, 'Kitkat')
					flash_script =os.path.join(flash_module_kk, 'flash.sh')
					subprocess.call(['source '+flash_script+' '+flash_module_kk], shell=True)
				
				elif _platform == 'darwin':
					print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')
				
				elif _platform == 'win32':
					print('Found '+_platform+'\n'+'')
					flash_module = os.path.join(flash_script_path, 'Signed')
					flash_module_kk = os.path.join(flash_module, 'Kitkat')
					flash_script =os.path.join(flash_module_kk, 'flash_all.bat')
					subprocess.Popen(flash_script+' '+flash_module_kk+'\/', stderr=subprocess.STDOUT).communicate()

				else :
					print('Unable to recognise this OS')


			else :
				print(' Device is probably YU5510( non A version)')

		else :
			print('Unknown Model of'+device)
			
	else :
		print('Device Not '+device+', \nExit!')

def fastboot_function(usb_attrs, recoveries_path, flash_script_path, ygdp_path):
	cmd = 'fastboot'+usb_attrs+'getvar version'
	scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
	# version: REFRESH_emmccid_secureboot
	# version: 0.5_emmccid_secureboot

	# print scan +' String length : ' + str(len(scan))
	# print scan +'String length : ' + str(len(scan))

	if scan.find('0.5_emmccid_secureboot') >= 0 :

		print("Signed LP Device Detected")

		if _platform == 'linux' or _platform == 'linux2':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')

		elif _platform == 'darwin':
			print('Found '+_platform+'\n'+'Sorry we only got Windows support for this device')

		elif _platform == 'win32':
			print('Found '+_platform+'\n'+'')

			flash_module = os.path.join(flash_script_path, 'Signed')
			flash_module_lp = os.path.join(flash_module, 'Lollipop')
			flash_package = os.path.join(flash_module_lp, '5.1.153.00.P0.160604.8675_I02.def.CPB')

			ygdp_exe = os.path.join(ygdp_path, 'YGDP_Assembly.exe')
			ygdp_config_module_path = os.path.join(ygdp_path, 'UserConfig')
			ygdp_config_module = os.path.join(ygdp_config_module_path, "UserConfig.xml")

			try:
			    ET.parse(ygdp_config_module)
			except ET.ParseError:
			    print('{} is corrupt'.format(ygdp_config_module))

			xml_tree = ET.ElementTree(file=ygdp_config_module) #path = path to .xml
			xml_file = xml_tree.getroot()
			# <CPB_PATH>C:\Users\ASUS\Desktop\yureka\4.4.013.00.P1.150928.8675_I02_Signed.CPB\4.4.013.00.P1.150928.8675_I02_Signed.CPB</CPB_PATH>

			print(ygdp_config_module+'\n'+flash_package)
			xml_tree.find('CPB_PATH').text = flash_package
			xml_tree.write(ygdp_config_module)
			os.system(ygdp_exe)


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

			wait_for_user_input = raw_input('Press VOLUME-UP on YU5510, Then Press ENTER in PC keyboard to continue to device verification: ')
			time.sleep(25)


			cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'TWRP_YU5510A_KK_recovery.img')
			scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
			print(scan)
			time.sleep(25)
			
			# There is no 64 bit 
			# cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'TWRP_v2.8.7.0_Yureka_Plus.img')
			# scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
			# print(scan)
			# time.sleep(10)


		elif scan0.find('Device unlocked: true') >= 0 :
			print('unlocked bootloader')
			cmd = 'fastboot'+usb_attrs+'boot '+os.path.join(recoveries_path, 'TWRP_YU5510A_KK_recovery.img')
			scan = str(subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT).strip())
			print(scan)
			time.sleep(25)

		else : 
			print('Wrong choice of device')

	else :
		print('Device Not Found in Database')


if __name__ == '__main__':

	fastboot_function(sys.argv[1], sys.argv[4], sys.argv[5], sys.argv[7])
	validation(sys.argv[0], sys.argv[5])
