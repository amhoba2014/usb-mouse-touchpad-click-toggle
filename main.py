import os
import time
import psutil
import subprocess

def is_usb_mouse_connected():
  # Get list of all USB devices and check if a mouse is connected
  for device in psutil.disk_partitions():
    if "usb" in device.device.lower():
      # Check for mouse device in the output of xinput
      result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
      if "pointer" in result.stdout.lower():
        return True
  return False

def enable_touchpad_clicking():
  # Enable touchpad clicking using xinput
  subprocess.run(['xinput', 'set-prop', 'touchpad_device_id', 'libinput Click Method Enabled', '1', '0'])

def disable_touchpad_clicking():
  # Disable touchpad clicking using xinput
  subprocess.run(['xinput', 'set-prop', 'touchpad_device_id', 'libinput Click Method Enabled', '0', '0'])

def get_touchpad_device_id():
  # Get the device id of the touchpad
  result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
  for line in result.stdout.splitlines():
    if 'touchpad' in line.lower():
      # Extract device id from the output
      device_id = line.split()[3].split('=')[-1]
      return device_id
  return None

def main():
  # Identify the touchpad device id
  touchpad_device_id = get_touchpad_device_id()
  if not touchpad_device_id:
    print("Touchpad not found!")
    return

  print(f"Touchpad device ID: {touchpad_device_id}")

  while True:
    if is_usb_mouse_connected():
      print("USB mouse connected, disabling touchpad clicking.")
      disable_touchpad_clicking()
    else:
      print("USB mouse not connected, enabling touchpad clicking.")
      enable_touchpad_clicking()
    
    time.sleep(1)  # Check every second

if __name__ == "__main__":
  main()
