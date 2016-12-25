#!/usr/bin/env bash

###########
# GENERAL #
###########

# Update apt cache
apt-get update

##########
# PYTHON #
##########

apt-get install python3 python3-tk -y

########
# XORG #
########

apt-get install xorg openbox -y
