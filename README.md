# USB Mouse Touchpad Click Toggle

This project provides a Python script that automatically enables or disables the touchpad's tap-to-click functionality based on whether a USB mouse is connected. When a USB mouse is connected, tap-to-click on the touchpad is disabled to avoid accidental clicks. When the mouse is disconnected, tap-to-click is re-enabled for ease of use.

The script runs in the background, checking every second for the status of the USB mouse and adjusting the touchpad's click behavior accordingly.

## Features

- Detects when a USB mouse is connected or disconnected.
- Disables tap-to-click functionality on the touchpad when a USB mouse is connected.
- Re-enables tap-to-click functionality when the USB mouse is disconnected.
- Runs continuously, checking the mouse connection status every second.

## Requirements

- **Linux** operating system (tested on Ubuntu/Debian-based systems).
- **Python 3** (tested with Python 3.10.12).
- **xinput**: A utility to configure and manage input devices (used for managing touchpad and pointer device settings).
- **poetry**: A dependency manager and tool for packaging Python projects (used for managing project dependencies and environment).

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/amhoba2014/usb-mouse-touchpad-click-toggle ;
   cd usb-mouse-touchpad-click-toggle ;
   ```

2. Install the required dependencies:

   ```bash
   poetry install ;
   ````

3. Run the script:

   ```bash
   poetry run python toggle_touchpad_click.py
   ```

## Usage

Once the script is running, it will monitor the connection of the USB mouse and automatically toggle the touchpad click functionality every second.

- If the USB mouse is connected, tap-to-click on the touchpad is **disabled**.
- If the USB mouse is disconnected, tap-to-click is **enabled**.

You can stop the script by pressing `CTRL + C` in the terminal.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! Feel free to fork the repository, make your changes, and submit a pull request.
