import time

from source.input_device_manager import InputDeviceManager
from source.config_manager import ConfigManager
from source.xinput_utils import XinputUtils

def main():
  configs = ConfigManager.read_env_file()
  if configs is None:
    # configs is None so this means we should perform setup.
    xinput_devices = XinputUtils.extract_xinput_devices()
    xinput_pointer_devices = [device for device in xinput_devices if device.device_type == "pointer"]
    print(xinput_pointer_devices)
    return

  while True:
    # Identify the touchpad device id
    touchpad_device_id = InputDeviceManager.get_touchpad_device_id()

    if not touchpad_device_id:
      print("Touchpad not found!")
    else:
      print(f"Touchpad found and the device ID is {touchpad_device_id}")
      if InputDeviceManager.is_usb_mouse_connected():
        print("USB mouse connected, disabling touchpad clicking.")
        InputDeviceManager.disable_touchpad_clicking(touchpad_device_id)
      else:
        print("USB mouse not connected, enabling touchpad clicking.")
        InputDeviceManager.enable_touchpad_clicking(touchpad_device_id)

    time.sleep(1)  # Check every second

if __name__ == "__main__":
  main()
