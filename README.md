# Tower Dashboard

Tower is a custom apparatus designed and built by Junhee Won, an undergraduate scientist and engineer at KAIST. **Tower Dashboard** is supporting service of Tower, providing control of extruder/fiber motors and heater via web service.

Tower Dashboard is developed for Raspberry Pi with Docker.

The updated Software -specifically everything related to the server/User interface has been written by [2JS](https://github.com/2JS), an undergraduate software engineer and developer at KAIST. Full Acknowledgements to his contributions are due.

## Installation

1. Install Docker and Docker Compose.
2. Clone repository
3. Set up `.env` file.
4. `docker-compose up -d`

**Set up `.env` file**

Copy `.env.dist` to `.env`, and fill values.

| Variable            | Example        | Description                                        |
| ------------------- | -------------- | -------------------------------------------------- |
| EMAIL               | ex@amp.le      | Email address for Let's Encrypt HTTPS certificate. |
| HOST                | example.net    | Host server address.                               |
| TOWER_HEATER_PORT   | `/dev/ttyUSB0` | Heater USB port.                                   |
| TOWER_EXTRUDER_PORT | `/dev/ttyACM0` | Extruder USB port.                                 |
| TOWER_FIBER_PORT    | `/dev/ttyACM1` | Fiber USB port.                                    |

## Previous works

This project is created as a replacement of [tower-server](https://github.com/EOMMINHO/tower-server.git) worked by [EOMMINHO](https://github.com/EOMMINHO). The need of replacement is introduced to change the server from a PC to Raspberry Pi, since using a PC solely for this very light service is wasting too much hardware resource.

At first, we tried to port the original tower-server for Raspberry Pi (which is arm64 based), but some nodejs dependencies failed on Pi. So we rewriten entire server in python. (Of course, not exact translation)

We brought arduino-side code and communication protocol unchanged, which may differ in future.

## Future Works

#### USB identification

Currently, device mapping is not located automatically, and hardcoded in `.env` by hand. We'll resolve this by implementing identification step in communication protocol so that arduino tells which it is.

#### Soft limit

Master would be able to change the limit range of device value(speed or temperature) in future. Currently they're hardcoded.

## Known Issues

#### Arduino connection going unresponsive

Arduino connection goes randomly unresponsive only if their speed is 0. If they're not, it seems staying responsive. Resetting arduino temporarily resolves the issue.