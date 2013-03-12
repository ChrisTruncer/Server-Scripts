#!/bin/bash

# Server Update Script
# Author: Christopher Truncer @christruncer
# Date: 3/11/2013

# Get rid of everything on the console
clear

# Title Screen
echo '******************************************************'
echo "* Update.sh | Christophertruncer.com | `hostname -f` *"
echo '******************************************************'

# Let's get the latest packages
apt-get update

# And now install package updates & dependencies apt knows about
apt-get dist-upgrade

# Remove the junk I don't need
apt-get --purge autoremove

# Clean up installed packages
apt-get clean
apt-get autoclean

# And we're done!
echo "Finished!"
