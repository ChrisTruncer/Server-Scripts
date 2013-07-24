#!/bin/bash
#############################################################################
# Backup Script
# Description:Script to backup system configs. Taken from @themightyshiv
#############################################################################


# Global Variables
var_host=`hostname`
var_date=`date +%m.%d.%Y`
var_bdir='<directories to backup delimited by a space without a trailing slash>'
var_sdir='<directory to backup to>'
var_pusr='<user to own the backup>'
var_pgrp='<group to own the backup>'
# Directory to exclude from backup
var_excl='--exclude=/backups/*'

# Remove Previous Backups (If Any)
rm -rf ${var_sdir}/${var_host}*.tar.gz

# Create New Backup
tar ${var_excl} -czf ${var_sdir}/${var_host}.tar.gz ${var_bdir} >> /dev/null 2>&1

# Set Backup Permissions
chown ${var_pusr}:${var_pgrp} ${var_sdir}/${var_host}.tar.gz
chmod 600 ${var_sdir}/${var_host}.tar.gz

# Dump All Databases
mysqldump -u root --password="<database password>" --all-databases > /backups/databasebackup.sql
