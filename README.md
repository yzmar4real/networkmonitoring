# NetworkMonitoring

Python Code that allows Network Engineers to apply use-cases exploring Network Observability, Assurance and Automation to enhance Network Monitoring

## Overview

Python Code that allows Network Engineers to enhance monitoring capability by targeting specific triggers within the network infrastructure. 

## Use Case Description

This use case is particularly helpful in validating network observability & assurance by utilizing defined triggers. PYATS's modular methods with parsing makes it incredibly easy to extract the specific information required. (In this case route presence within the table).

**Python**

The script is written in python using PYATS to interact with the active devices, a GENIE model API to extract the state of a route within the routing table, and store the results in a json file.

**Output**: The results of the state is stored in a json file. This can also be enhanced to execute follow up actions such as shutdown an interface, etc. 

## Contacts
*Oluyemi Oshunkoya (yemi_o@outlook.com)

## Solution Components
*Python
*Genie
*PYATS

## Prerequisites 

Python3.6 and above

## Toolbox

Main.py: includes the main script run which contains relevant code to connect to the devices highlighted in the testbed file and returns the outcome as a json file.

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

1. Edit genie.yml file to include parameters for your devices. It is usually advisable to target the device with the most outbound interface.

## Step 3 - Executing the Script 

1. Execute the main script from console

python3 Main.py
