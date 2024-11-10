import subprocess
import re

class InputDeviceManager:
  
  @staticmethod
  def is_usb_mouse_connected():
    # Run xinput to list all input devices
    result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
    
    # Check if a USB mouse is connected (detect pointer devices)
    for line in result.stdout.splitlines():
      if 'pointer' in line.lower() and 'usb' in line.lower():
        return True
    return False

  @staticmethod
  def enable_touchpad_clicking(device_id):
    # Enable tap-to-click using xinput
    subprocess.run(['xinput', 'set-prop', device_id, 'libinput Tapping Enabled', '1'])

  @staticmethod
  def disable_touchpad_clicking(device_id):
    # Disable tap-to-click using xinput
    subprocess.run(['xinput', 'set-prop', device_id, 'libinput Tapping Enabled', '0'])

  @staticmethod
  def get_touchpad_device_id():
    # Get the device id of the touchpad
    result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
    
    # Regex pattern to match 'id={integer}' in the line
    id_pattern = re.compile(r'id=(\d+)')
    
    for line in result.stdout.splitlines():
      if 'touchpad' in line.lower():
        # Try to match the pattern in the line
        match = id_pattern.search(line)
        if match:
          # Extract the device id from the regex match
          device_id = match.group(1)
          return device_id
    
    return None
