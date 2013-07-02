#!/bin/bash

# Script for re-adding duplicate cracked cleartext passwords into a cracked
# hash list.

for hash in $(cat hashlist.txt)
do
    grep $hash cracked.txt >> multipasses.txt
done
