# Docker Challenge

This git repository contains all the files needed to recreate the docker images used for the Docker Challenge that was hosted by trueability.com in November, 2014.  The grading system has not been included. 

Pre-built docker images are available in the trueability/dodc repository, and
the rest of the file describes the setup and solution for the Docker Challenge.

A copy of the instructions for the challenge can be found in *scenario_instructions.md*

## System Setup

  1. You will need to make sure that `docker` and your choice of web servers is installed on the system.
  1. Setup the web server for the puzzle:
    * `ln -s /path/to/webserver/htdocs /root/puzzle`
    * cp `host_index.html /root/puzzle/index.html`
    * `mkdir -p /root/puzzle/{pieces,task{1,2,3,4}}`
  1. Setup directories for the pieces to be dropped into:
    * `mkdir -p /var/ta/task{1,2,3,4}`
  1. Setup the files directory
    * `mkdir -p /root/files`
    * `cp scripts/*-prep /root/files`
    * `cp ssh/do_challenge.pub /root/files`
  1. Pull down starting images:
    * `docker pull debian/stable:latest`
    * `docker pull trueability/dodc:task1`
    * `docker pull trueability/dodc:task2`
    * `docker pull trueability/dodc:task3_web`
    * `docker pull trueability/dodc:task3_db`
    * `docker pull trueability/dodc:task4-snd`

## Solutions

  1. `cp scripts/*-resolve /root/files`
  1. Pull down solution images:
    * `docker pull trueability/dodc:task2_answer`
    * `docker pull trueability/dodc:task4-rcv`

## Building the Images

The `build_images.sh` script was to generate all the docker images used in this challenge.

The script provides a **build_image** function that:
  * creates a symlink to the file in *dockerfiles/* that corresponds with the tag you want to build
  * calls `docker build -t` to create the image

All dockerfiles assume a context of being run from the root directory.  Any additional scripts that need to be added to the images are kept in *scripts/docker/*.  If you modify or add any scripts, be sure to update the corresponding *dockerfiles/Dockerfile.{tag}* as well.

If you wish to build your own images and make them available publically, please
change the **REPO** variable.

The ssh keypair for Task #4 is stored in the *ssh/* directory and was created for this contest only (ie, don't try to use it to get into muh github account, you jackals).  To generate a new set of keys use `ssh-keygen -f ssh/do_challenge -t dsa`

## Getting Help/Sending Feedback

Please post to https://community.trueability.com/ if you have any feedback or questions.

Good luck!
