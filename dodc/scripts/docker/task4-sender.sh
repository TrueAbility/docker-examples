#!/bin/bash

DATA=/var/lib/ta-data

scp -o StrictHostKeyChecking=no \
  -i ${DATA}/do_challenge \
  ${DATA}/piece4.png doftw@rcv:/data
