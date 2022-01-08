# watchdog-nebra

Simple watchdog application that is installed together as a Docker application in the Nebra FW. The URL_REQ system variable needs to be set for your endpoint.

The watchdog URL is pointed at a Node-RED server which use the `trigger` node for sending a Discord notification if a miner is down. The Node-RED flow is found [here](node-red-flows.json)