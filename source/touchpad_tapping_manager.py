import subprocess


class TouchpadTappingManager:
  def __init__(self, device_id, prop_name):
    self.device_id = device_id
    self.prop_name = prop_name
  
  def enable(self):
    self._set('1')

  def disable(self):
    self._set('0')

  def _set(self, value: str):
    subprocess.run(['xinput', 'set-prop', self.device_id, self.prop_name, value])
