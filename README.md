# statusboard
A status board written in Python for the Raspberry Pi.

## Requires
* Python 3+ (apt-get install python3)
* python-tk (apt-get install python3-tk)
* X11 (apt-get install xorg openbox)

## Development Environment

This repository ships with a development environment built in Vagrant, which requires [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/) to be installed on the host machine.

To use the Vagrant development box, `cd` to the `vagrant` directory and run `vagrant up`. This will take some time the first time the command is run, as it needs to download the base box and configure it for first use.
