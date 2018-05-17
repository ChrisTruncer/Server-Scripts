#!/bin/bash

# Server Update Script
# This was basically taken from @TheMightyShiv
# Check out his stuff, great developer

# Get rid of everything on the console
clear

# Title Screen
echo '******************************************************'
echo "* Update.sh |     Update Script      | `hostname -f` *"
echo '******************************************************'

# Let's get the latest packages
apt-get update
apt-get upgrade -y

# And now install package updates & dependencies apt knows about
apt-get dist-upgrade -y

# Remove the junk I don't need
apt-get --purge autoremove -y

# Clean up installed packages
apt-get clean
apt-get autoclean

# And we're done!
echo "Finished!"
