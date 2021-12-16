nebra-miner-fw

# Guide for fixing your Nebra FW

- Open an account at balena.cloud.com
- Start a fleet
- Create a device with `Raspberry Pi 3 (using 64bit OS)`
- Change the `Define DT overlays` parameter in the fleet configuration to `"vc4-fkms-v3d","enc28j60","spi1-3cs","uart0,txd0_pin=32,rxd0_pin=33,pin_func=7"`
- Flash your SD-card with the Balena image.
- Download the `docker-compose.yml` from https://github.com/NebraLtd/helium-miner-software and put that in an empty folder.

Push the project to your fleet using the balenaCLI.

```
balena login
balena push {organisation}/{fleet}
```
