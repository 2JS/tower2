# Implementation

Tower Dashboard is simply a web service controling multiple devices via USB interface. It's developed for Raspberry Pi specifically. 

## Web Service

##### Flask & Frontend

We chose Flask as backend because it's python, lightweight, simple.

It's frontend is written in HTML with jinja, decorated with bootstrap.

##### RESTful API

Data transfer is done by RESTful API for devices. `GET` and `POST` is implemented.

## Docker & Reverse Proxy

We introduced Docker for local development and stable portability. There are two containers defined. `app`, which runs flask on python, and `proxy`, which runs Traefik reverse proxy.

##### app

`app` container is enclaving dependencies and this web server. `consistent` volume is for consistent data storage such as user credentials. It directly maps connection to `ttyACM0`, `ttyACM1`, and `ttyUSB0`.

##### proxy

The reason of using Traefik reverse proxy is for automatic HTTPS certificate renewal. Traefik provides it and integrates very well with Docker.

* Let's Encrypt auto-renewal with given `EMAIL` and `HOST` variable defined in `.env` file.
* Traefik dashboard(do not confuse with Tower Dashboard) is accessible within localhost.
* Takes both HTTP(80) and HTTPS(443) requests, HTTP is redirected to HTTPS.

## USB I/O

USB connection is accomplished by hardcoded mapping to corresponding devices, which is fragile with USB replugging.