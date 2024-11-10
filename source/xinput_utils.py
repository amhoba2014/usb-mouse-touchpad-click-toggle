import re
import subprocess


class XInputDevice:
  def __init__(self, name: str, device_id: str, device_type: str):
    self.name = name
    self.device_id = device_id
    self.device_type = device_type

  def __repr__(self):
    return f"XInputDevice(name={self.name}, device_id={self.device_id}, device_type={self.device_type})"


class XInputProperty:
  def __init__(self, name: str, property_id: str, value: str):
    self.name = name
    self.property_id = property_id
    self.value = value

  def __repr__(self):
    return f"XInputProperty(name={self.name}, property_id={self.property_id}, value={self.value})"


class XinputUtils:

  @staticmethod
  def extract_xinput_devices() -> list[XInputDevice]:
    result = subprocess.run(['xinput', 'list'], capture_output=True, text=True)
    parsed_devices = []
    for line in result.stdout.splitlines():
      # Use regular expression to extract the necessary information
      match = re.search(r'↳\s+(.*?)\s+id=(\d+)\s+\[.*(pointer|keyboard).*\]', line)
      if match:
        name = match.group(1).strip()
        device_id= match.group(2).strip()
        device_type = match.group(3).strip()
        parsed_devices.append(XInputDevice(name, device_id, device_type))
    return parsed_devices

  @staticmethod
  def get_device_properties(device_id) -> list[XInputProperty]:
    # Run the xinput list-props command to get the properties of the device
    result = subprocess.run(['xinput', 'list-props', str(device_id)], capture_output=True, text=True)
    
    # Initialize a list to store the extracted properties
    properties = []
    
    # Regex to match the property names and their values
    pattern = re.compile(r'^(.*?)\s\((\d+)\):\s*(.*?)$')
    
    # Split the result into lines and process each line
    for line in result.stdout.splitlines():
      match = pattern.match(line.strip())
      if match:
        property_name = match.group(1).strip()
        property_id = match.group(2).strip()
        property_value = match.group(3).strip()
        properties.append(XInputProperty(property_name, property_id, property_value))
    
    return properties