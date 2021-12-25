nebra-miner-fw

# Guide for fixing your Nebra FW

**UPDATE 211225** The miners have not been running succesfully, both beacoing, witnessing and recieving data packets for a full week. 

The SD-cards that were used are Sandisk Endurance 32GB cards, and the Nebra miners are NEBHNT1, first batch, RPi3 CM and eMMC-key.

- Open an account at balena.cloud.com
- Start a fleet
- Create a device with `Raspberry Pi 3 (using 64bit OS)`
- Define a global variable for all services in the fleet. `VARIANT = NEBHNT-IN1`.
- Change the `Define DT overlays` parameter in the fleet configuration to `"vc4-fkms-v3d","enc28j60","spi1-3cs","uart0,txd0_pin=32,rxd0_pin=33,pin_func=7"`
- Flash your SD-card with the Balena image.
- Download the `docker-compose.yml` from https://github.com/NebraLtd/helium-miner-software and put that in an empty project folder.

Push the project to your fleet using the balenaCLI.

```
balena login
balena push {organisation}/{fleet}
```


1. [Helium miner software](https://github.com/NebraLtd/helium-miner-software)
2. [Helpfile for Nebra software](https://githubhelp.com/Xykon/helium-miner-software)
