import os
from typing import Optional

class DeviceConfig:
  def __init__(
    self,
    touchpad_tapping_enabled_prop: str,
    usb_mouse_xinput_name: str,
    usb_mouse_xinput_id: str,
    touchpad_xinput_name: str,
    touchpad_xinput_id: str,
  ):
    self.touchpad_tapping_enabled_prop: str = touchpad_tapping_enabled_prop
    self.usb_mouse_xinput_name: str = usb_mouse_xinput_name
    self.usb_mouse_xinput_id: str = usb_mouse_xinput_id
    self.touchpad_xinput_name: str = touchpad_xinput_name
    self.touchpad_xinput_id: str = touchpad_xinput_id

  def __repr__(self):
    return (
      f"DeviceConfig("
      f"touchpad_tapping_enabled_prop={self.touchpad_tapping_enabled_prop}, "
      f"usb_mouse_xinput_name={self.usb_mouse_xinput_name}, "
      f"usb_mouse_xinput_id={self.usb_mouse_xinput_id}, "
      f"touchpad_xinput_name={self.touchpad_xinput_name}, "
      f"touchpad_xinput_id={self.touchpad_xinput_id})"
    )

class ConfigManager:
  CONFIG_DOT_ENV_PATH = ".env"

  @staticmethod
  def read_env_file() -> Optional[DeviceConfig]:
    """
    Reads a .env file and returns a DeviceConfig object with the properties set.
    """
    file_path = ConfigManager.CONFIG_DOT_ENV_PATH

    if not os.path.exists(file_path):
      print(f"Error: {file_path} does not exist.")
      return None

    config_data = {}
    with open(file_path, 'r') as file:
      for line in file:
        # Ignore comments and empty lines
        line = line.strip()
        if not line or line.startswith('#'):
          continue

        key, value = line.split('=', 1)
        config_data[key.strip()] = value.strip()

    # Parse values and create DeviceConfig object
    try:
      return DeviceConfig(**config_data)
    except KeyError as e:
      print(f"Error: Missing required configuration key {e}")
      return None
    except ValueError as e:
      print(f"Error: Invalid value in .env file - {e}")
      return None

  @staticmethod
  def update_env_file(config: DeviceConfig) -> bool:
    """
    Updates or creates a .env file with the values from the DeviceConfig object.
    """
    file_path = ConfigManager.CONFIG_DOT_ENV_PATH
    config_names = [name for name in dir(config) if not name.startswith("_")]

    try:
      with open(file_path, 'w') as file:
        for name in config_names:
          file.write(f"{name}={getattr(config, name)}\n")
      return True
    except Exception as e:
      print(f"Error: Could not update .env file - {e}")
      return False
