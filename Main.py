
import concurrent.futures
import json
import logging
from genie.testbed import load

logging.basicConfig(level=logging.DEBUG)

final = []
outcome = []

testbed = load('./genie.yml')

''' Create a Function that connects to the devices,
    Uses the api.get module from genie to parse the routing table,
    And a if logic to scan the outcomes for the default route
'''

def process_device(dev):
    dev.connect(learn_hostname=True,init_exec_commands=[],init_config_commands=[],log_stdout=True)
    try:
        routes = dev.api.get_routes()
        if '0.0.0.0/0' in routes:
            return {"Device_Name": dev.hostname, "Output": 'Default_Route_Present', "Code": '0'}
        else:
            return {"Device_Name": dev.hostname, "Output": 'Default_Route_Absent', "Code": 1}
    except Exception as e:
        logging.exception({"Device_Name": dev.hostname, "Output": 'Default_Route_Absent', "Code": 1})

''' Executes the function created using the devices within the testbed file,
    Saves the result in an list
    converts the list into a json object
'''
        
with concurrent.futures.ThreadPoolExecutor() as executor:
    future_to_device = {executor.submit(process_device, dev): dev for dev in testbed}
    for future in concurrent.futures.as_completed(future_to_device):
        dev = future_to_device[future]
        try:
            outcome.append(future.result())
        except Exception as exc:
            logging.exception(f'Device {dev.hostname} generated an exception: {exc}')

with open("./my_file.json", "w") as f:
    json.dump(outcome, f)
