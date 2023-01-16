#07_06_yes_no.py

from guizero import App, Text
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))

from sphero_sdk import SpheroRvrObserver
from sphero_sdk import BatteryVoltageStatesEnum as VoltageStates

app = App(title = "Battery State")
rvr = SpheroRvrObserver()
voltage_state = ''
voltage_states = ''
battery_percentage_out = ''

def battery_percentage_handler(battery_percentage):
    global battery_percentage_out
    battery_percentage_out = battery_percentage
    
    
    
def battery_voltage_handler(battery_voltage_state):
    global voltage_state
    voltage_state = battey_voltage_state
    global state_info
    state_info = '[{}, {}, {}]'.format(
        '{}: {}'.format(VoltageStates.unkown.name,
VoltageStates.unkown.value),
        '{}: {}'.format(VoltageStates.ok.name,
VoltageStates.ok.value),
        '{}: {}'.format(VoltageStates.low.name,
Voltage)
        )
    global voltage_states
    voltage_states = 'voltage states: ' + state_info
                        
Text(app, text="Battery Percentage " +
str(battery_percentage_out['percentage']))
        Text(app, text="Voltage State " +
str(voltage_state['state']))
                        Text(app, text=voltage_states)
                        app.display()

def ask():
    if yesno("Question", "Yes or No?"):
        info("Result", "You clicked Yes")
    else:
        warn("Result", "You clicked No")

app = App()
button = PushButton(app, text="Click Me", command=ask)
app.display()