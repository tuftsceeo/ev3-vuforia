# ev3-vuforia
A repository that connects EV3 to Vuforia Spatial Toolbox

Requires Python 3.7 (not 3.8)!!

Requires zerorpc to be npm installed (npm install zerorpc) within the vuforia-spatial-edge-server folder, and also pip installed (pip install zerorpc) on your computer.

Import the server.py and ports.py files to the EV3 (scp /Users/.../server.py robot@IPAddress:)
Connect your EV3 to your computer by scanning for bluetooth devices on the EV3. Use the command system_profiler SPBluetoothDataType to find the Bluetooth MAC Address of the EV3. In line 10 of client.py change to the Bluetooth MAC Address of your EV3.

Place client.py, config.html, and index.js in their own folder (I named mine EV3) under vuforia-spatial-robotic-addon/interfaces/.

zeroTest.js is used as a testing script that does not loop in the Vuforia Spatial Toolbox. This can be useful for debugging the connection between your computer and the EV3 as the code is simpler, and does not need to wait for the Vuforia server to begin running.

To establish a connection:
* ssh into your EV3 (ssh robot@IPAddress)
* Run node server.js from the vuforia-spatial-edge-server folder
* Run server.py on the EV3
* Wait for server.py to print "up and running" (10-15 seconds)
* Run client.py in a separate terminal screen (cd vuforia-spatial-edge-server/addons/.../interfaces/EV3)
* Go to http://localhost:8080 to configure and create your new EV3 interface
* Under "Manage Hardware Interfaces" turn on EV3 and refresh the server. Go back to this tab and click on the settings icon next to EV3.
* Give the object a name within hardware interfaces, (ex. test_ev3), and add an object with the same name under "Object Configuration"
* Add a target to the object using the Vuforia Developer Portal (follow https://spatialtoolbox.vuforia.com/docs/use/connect-to-the-physical-world/create-object)
* When the page is refreshed/server is run again a tool should appear under your object by the name IO
* In the Vuforia app, nodes will appear for each motor/sensor and tools (ex. slider/button) can be connected to those nodes for your object
