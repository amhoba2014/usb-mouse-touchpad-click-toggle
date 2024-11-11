from source.config_manager import ConfigManager, DeviceConfig
from source.xinput_utils import XinputUtils


def perform_setup():
  print("Let's perform a setup.")
  xinput_devices = XinputUtils.extract_xinput_devices()
  xinput_pointer_devices = [device for device in xinput_devices if device.device_type == "pointer"]
  # Choose USB mouse device:
  print()
  print("Please choose the USB mouse device from the list below (example: 'PixArt USB Optical Mouse'):")
  for i, x in enumerate(xinput_pointer_devices):
    print(i, x.name)
  index = int(input("Enter the numeric index: "))
  if index < 0 or index >= len(xinput_pointer_devices):
    print("Please choose from the list!")
    return
  chosen_usb_mouse_device = xinput_pointer_devices[index]
  print("The chosen device is:", chosen_usb_mouse_device.name)
  # Choose touchpad device:
  print()
  print("Please choose the Touchpad device from the list below (example: 'SynPS/2 Synaptics TouchPad'):")
  for i, x in enumerate(xinput_pointer_devices):
    print(i, x.name)
  index = int(input("Enter the numeric index: "))
  if index < 0 or index >= len(xinput_pointer_devices):
    print("Please choose from the list!")
    return
  chosen_touchpad_device = xinput_pointer_devices[index]
  print("The chosen device is:", chosen_touchpad_device.name)
  # Choose the suitable prop:
  print()
  print("Now please carefully choose the prop of your touchpad that determines if tapping is enabled or not (example: 'libinput Tapping Enabled'):")
  touchpad_device_properties = XinputUtils.get_device_properties(chosen_touchpad_device.device_id)
  for i, x in enumerate(touchpad_device_properties):
    print(i, x.name)
  index = int(input("Enter the numeric index: "))
  if index < 0 or index >= len(touchpad_device_properties):
    print("Please choose from the list!")
    return
  chosen_touchpad_device_property = touchpad_device_properties[index]
  print("The chosen device property is:", chosen_touchpad_device_property.name)
  # Save the .env file:
  ConfigManager.update_env_file(
    DeviceConfig(
      chosen_touchpad_device_property.name,
      chosen_usb_mouse_device.name,
      chosen_usb_mouse_device.device_id,
      chosen_touchpad_device.name,
      chosen_touchpad_device.device_id
    )
  )
  # Setup finished:
  print()
  print("Perfect! We are setup! Please restart the script to continue!")
  print()
