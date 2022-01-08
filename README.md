nebra-miner-fw

# Guide for fixing your Nebra FW

**UPDATE 220108** The miners have not been running succesfully, both beacoing, witnessing and recieving data packets for several weeks. They do seem unstable though, and still needs to be restarted from time to time. This seems to be a hardware related problem.

The SD-cards that were used are Sandisk Endurance 32GB cards, and the Nebra miners are NEBHNT1, first batch, RPi3 CM and eMMC-key.

- Open an account at balena.cloud.com
- Start a fleet
- Create a device with `Raspberry Pi 3 (using 64bit OS)`
- Define a global variable for all services in the fleet. `VARIANT = NEBHNT-IN1`.
- Change the `Define DT overlays` parameter in the fleet configuration to `"vc4-fkms-v3d","enc28j60","spi1-3cs","uart0,txd0_pin=32,rxd0_pin=33,pin_func=7"`
- Flash your SD-card with the Balena image.
- Download the `docker-compose.yml` from https://github.com/NebraLtd/helium-miner-software and put that in an empty project folder.

- Note: In the `docker-compose.yml` there is a simple watchdog application. Set your enviroment variable in Balena Cloud `REQ_URL=https://{your_endpoint_URL}` and it will automatically send a hearbeat every minute. 


Push the project to your fleet using the balenaCLI.

```
balena login
balena push {organisation}/{fleet}
```

1. [Helium miner software](https://github.com/NebraLtd/helium-miner-software)
2. [Helpfile for Nebra software](https://githubhelp.com/Xykon/helium-miner-software)
