# ev3-vuforia
A repository that connects EV3 to Vuforia Spatial Toolbox

Import the server.py and ports.py files to the EV3. Connect your EV3 to your computer by scanning for bluetooth devices on the EV3. Use the command system_profiler SPBluetoothDataType to find the Bluetooth MAC Address of the EV3. In line 10 of client.py change to the Bluetooth MAC Address of your EV3.

Place client.py, config.html, and index.js in their own folder (I named mine EV3) under vuforia-spatial-robotic-addon/interfaces/.

zeroTest.js is used as a testing script that does not loop in the Vuforia Spatial Toolbox. This can be useful for debugging the connection between your computer and the EV3 as the code is simpler, and does not need to wait for the Vuforia server to begin running.

To establish a connection:
* Run server.py on the EV3 and run server.js from the vuforia-spatial-edge-server folder
* Wait for server.py to print "up and running" (10-15 seconds)
* Make your objects according to https://spatialtoolbox.vuforia.com/docs/use/connect-to-the-physical-world/create-object with the ObjectName: "moveButton" and tool name "motor"
* In the Vuforia app, just add a switch (or something else that will give a value of true) to the button attached to the object. 
