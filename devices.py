 #!/usr/bin/python -tt
import sys
import string
import os
import subprocess

list = ['  0. YU5010', '  1. YU5010A', '  2. YU5510', '  3. YU5510A', '  4. AO5510', '  5. YU4711', '  6. YU5200', '  7. YU5530', '  8. YU5050']
device_list=['YU5010', 'YU5010A', 'YU5510', 'YU5510A', 'AO5510', 'YU4711', 'YU5200', 'YU5530', 'YU5050']

usb_attrs_list=[' -i 0x2a96 ', ' ', ' -i 0x2a96 ', ' -i 0x1ebf ', ' -i 0x1ebf ', ' -i 0x18d1 ', ' -i 0x18d1 ', ' -i 0x2a96 ', ' -i 0x2a96 ']

# print(' \n'.join(list))# or try commented way
# index_device_list=['0','1','2']
# selected_device_index = int(raw_input('Select a device model to continue :'))
# device = device_list[selected_device_index]
# print(device)
# print(usb_attrs)