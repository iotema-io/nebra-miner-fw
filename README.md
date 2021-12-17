nebra-miner-fw

# Guide for fixing your Nebra FW

**NOTE 211217: This has not been verified during a longer time period and only on three units** So far it seems to be working for the last 24h, will update this README with more information if it works over a longer time period.

The SD-cards that were used are Sandisk Endurance 32GB cards, and the Nebra miners are NEBHNT1, first batch, RPi3 CM and eMMC-key.

- Open an account at balena.cloud.com
- Start a fleet
- Create a device with `Raspberry Pi 3 (using 64bit OS)`
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
