# statusboard
A status board written in Python for the Raspberry Pi.

## Requires
* Python 3+ (apt-get install python3)
* python-tk (apt-get install python3-tk)
* X11 (apt-get install xorg openbox)

## Development Environment

This repository ships with a development environment built in Vagrant, which requires [VirtualBox](https://www.virtualbox.org/) and [Vagrant](https://www.vagrantup.com/) to be installed on the host machine.

To use the Vagrant development box, `cd` to the root directory of this project and run `vagrant up`. This will take some time the first time the command is run, as it needs to download the base box and configure it for first use.

Once the box loads, run `vagrant rsync-auto` to keep the contents of the project folder in sync with the Vagrant box so you can make changes and preview them.

Once the box is running, open VirtualBox, right click on `statusboard-dev`, and click `show`. Log in with the username `vagrant` and the password `vagrant`.

To start the dashboard, from the window session:

* `startx`
* Right click on the desktop and click `Terminal Emulator`
* `python3 /vagrant/main.py`

To quit a development session:

* In terminal emulator, `exit`
* Right click on the desktop environment in X11 and select `Exit`
* In the VirtualBox window, type `exit`
* Click the close box on the VirtualBox window and select `Continue running in the background`
* In the main terminal window used to start Vagrant, run `vagrant halt`
