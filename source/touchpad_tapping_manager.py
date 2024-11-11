import subprocess
import re


class TouchpadTappingManager:
  def __init__(self, device_id, prop_name):
    self.device_id = device_id
    self.prop_name = prop_name
  
  def enable(self):
    # Enable tap-to-click using xinput
    subprocess.run(['xinput', 'set-prop', self.device_id, self.prop_name, '1'])

  def disable(self):
    # Disable tap-to-click using xinput
    subprocess.run(['xinput', 'set-prop', self.device_id, self.prop_name, '0'])
