import time

from source.setup_utils import perform_setup
from source.touchpad_tapping_manager import TouchpadTappingManager
from source.config_manager import ConfigManager, DeviceConfig
from source.xinput_utils import XinputUtils

def main():
  configs = ConfigManager.read_env_file()
  if configs is None:
    # The `configs` variable` is None so this means we should perform setup:
    perform_setup()
    return

  touchpad_tapping_manager = TouchpadTappingManager(configs.touchpad_xinput_id, configs.touchpad_tapping_enabled_prop)

  while True:
    is_usb_mouse_connected = len([x for x in XinputUtils.extract_xinput_devices() if x.name == configs.usb_mouse_xinput_name]) > 0
    if is_usb_mouse_connected:
      print("USB mouse connected, disabling touchpad clicking.")
      touchpad_tapping_manager.disable()
    else:
      print("USB mouse not connected, enabling touchpad clicking.")
      touchpad_tapping_manager.enable()

    time.sleep(1)  # Check every second

if __name__ == "__main__":
  main()
