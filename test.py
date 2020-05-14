
from dronekit import connect, VehicleMode, LocationGlobalRelative, LocationGlobal, Command, CommandSequence
from pymavlink import mavutil
import time
import argparse

parser = argparse.ArgumentParser(description='Demonstrates basic mission operations.')
parser.add_argument('--connect', 
                   help="vehicle connection target string. If not specified, SITL automatically started and used.")
args = parser.parse_args()

connection_string = args.connect
sitl = None


#Start SITL if no connection string specified
if not connection_string:
    import dronekit_sitl
    sitl = dronekit_sitl.start_default()
    connection_string = sitl.connection_string()


# Connect to the Vehicle
print('Connecting to vehicle on: %s' % connection_string)

#TODO make SITL connection string dynamic again instead of hard coded UDP port
vehicle = connect('tcp:127.0.0.1:5760', wait_ready=True)
cmds = vehicle.commands
vehicle.initialize(4,heartbeat_timeout=120)

# let initialization and pre-arming checks happen
while not vehicle.is_armable:
    print('initializing vehicle')
    time.sleep(1)

#ensure that the vehicle is in the proper autopilot mode for guidance
vehicle.mode = VehicleMode('GUIDED')
vehicle.armed = True

# give time to arm no idea why same variable used for check
#TODO figure out why were checking same variable that we just set
while not vehicle.armed:
    print('Arming vehicle')
    time.sleep(1)

#takeoff, hover for 10 seconds and then land

vehicle.simple_takeoff(15)
time.sleep(1)
vehicle.mode = VehicleMode('LAND')

