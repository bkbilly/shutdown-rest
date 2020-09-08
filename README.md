# shutdown-rest
Remotely shutdown PC from Restful commands and runs on the system tray.

## Features
  - Uses system notifications for informing the user that the computer is scheduled for shutdown after 60 seconds.
  - Gives the option of canceling the shutdown sequence with the system tray options.
  - Has the option of custom icons by adding at the same directory an image with a name `shutdown.png`.
  - Works both on Windows and Linux but some linux distributions might not show the systemtray.

## Usage
Install requirements:
```bash
pip install -r requirements.txt
```
On Windows you can make it executable like so: `pyinstaller --onefile -w shutdown_rest.py`.
The exe output can be copied to the folder `C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp` in order to start on windows boots.

## REST Commands
To call the service these services are exposed to the network:
  - http://\<ip>:5000/shutdown
  - http://\<ip>:5000/cancel_shutdown
