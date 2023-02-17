# NetworkMonitoring

Python Code that allows Network Engineers to apply use-cases exploring Network Observability, Assurance and Automation to enhance Network Monitoring

## Overview

Python Code that allows Network Engineers to run through their existing infrastructure running IOS Software using discovery commands to establish a baseline of the infrastructure state with saved CSV files to show physical connectivity, mac-addresses, etc. 

## Use Case Description

This use case is particularly helpful in validating network documentation as well as for Engineers who have joined new networks without any basline documentation as a reference. PYATS's modular methods with parsing makes it incredibly easy to target specific datasets and document within CSV format. 

**Python**

The script is written in python using PYATS to interact with the active devices, a definite set of commands based on experience as well as CSV files to store the outcomes.

**Output**: The results of the commands are stored in individual CSV files. You can also find the raw configuration outputs as well as the exception errors stored in individual text files that would be created after each run.

## Contacts
*Oluyemi Oshunkoya (yemi_o@outlook.com)

## Solution Components
*Python
*Genie
*PYATS

## Prerequisites 

Python3.6 and above

## Toolbox
The toolbox includes multiple librairies to clarify the code.

IOS_Master_Function.py: includes all functions relating to parsing the configuration excerpts and providing relevant data.
Leveraging Genie Parsers to extract a specific output, and saving it to the database.

IOS_Master.py: includes the final script run which contains relevant commands, and stores returned values into a CSV file.

## Step 1 - Downloading - Option A Using a Docker Image

1. Download and setup docker suitable for your Operating System 
https://docs.docker.com/get-docker/

2. Download the latest version of the PYATS from docker hub

$ docker pull ciscotestautomation/pyats:latest

3. Run the docker image 

$ docker run -it ciscotestautomation/pyats:latest /bin/bash

## Step 1 - Downloading - Option B Using GIT

1. Clone the repository

git clone https://github.com/yzmar4real/networkmonitoring.git

2. CD into the directory 

cd networkmonitoring

3. (Optional) Use the directory as a virtual environment for the project

python3 -m venv . 

4. (Optional) Start the virtual environment and install the requirements for the project

source bin/activate

## Step 2 - Defining the Testbed for devices to be audited

1. Edit genie.yml file to include parameters for your devices. It is usually advisable to start from the Core device outbound. 

Note that you can update the list of devices based on your cdp discovery and rerun the script for maximum reach.

## Step 3 - Executing the Script 

1. Execute the main script from console

python3 Main.py
