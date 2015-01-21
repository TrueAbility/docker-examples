Welcome to the latest TrueAbility Challenge sponsored by our friends at [DigitalOcean](http://digitalocean.com).  First off, **don't rush**!  The leader board is ordered by accuracy first, and then timing.  Make sure you read all of the instructions thoroughly, and double check your work!

We hope that you brushed up on your [Docker](http://docker.com) skills, 'cause you'll need it if you have any hope at ranking at the top of the leader board.  Below you will find a series of four tasks related to Linux and Docker Administration.  Complete a task, and you will unlock a piece of the puzzle... but don't forget to copy the pieces into place in order to solve the puzzle, and get full credit.

**Grading**

Each task has a script associated with it that is located in the `/root/files` directory.  Prior to grading, all puzzle pieces will be cleared from the `/var/ta/answerX` directories and we will re-run the scripts from `/root/files`.  Your solution must deliver the correct puzzle piece to the associated `/var/ta/answerX` directory after its `/root/files` script is executed.

In addition, once you have unlocked a puzzle piece, copy it to `/root/puzzle/pieces` with one of the following file names to put it into the correct position: `topleft.png`, `topright.png`, `bottomleft.png`, or `bottomright.png`.  For example: 

```
# cp /var/ta/taskX/pieceX.png /root/puzzle/pieces/topleft.png
```

You can view the puzzle at `http://$SERVER_IP.xip.io` (replacing `$SERVER_IP` with the primary IP address of the server).  The pieces must be in the right location on this web page in order to get full credit.  

**Note the following**

 * The Docker instances will always be started from their associated scripts for grading, i.e. `/root/files/taskX.sh`.
  * You can modify the scripts to perform any actions necessary to solve a task
   * The scripts can run any Docker image, as long as that image solves the requirements of the task (meaning, you can build and run your own images based on the originals).
    * You will need to ensure that your script performs any housekeeping necessary for the Docker image to run successfully.
     * You do **not** need to solve the tasks in order... feel free to jump around if you can't figure something out.
      * All puzzle pieces in `/var/ta/answerX` directories will be removed prior grading.
       * Nothing in the directories `/root/files` or `/root/puzzle`  will be modified during grading... your changes here will be persistent.


## Task 1

The Docker image `ta:task1` is loaded on the system, and is run by the script `/root/files/task1.sh`.  It's purpose is simple: When run, it copies the first puzzle piece to the location `/data/piece1.png` **inside the docker instance**, and then exits.  Modify the script `/root/files/task1.sh` in order to capture the file that is being copied, and store it as `/var/ta/task1/piece1.png` **on the host server**.  

*Note: The file `/var/ta/task1/piece1.png` will be removed before `task1.sh` is executed during grading.*


## Task 2

The second puzzle piece is located inside of the `ta:task2` Docker image and is run from the script `/root/files/task2.sh`.  This image runs a script `/usr/bin/mover.sh`  **inside the docker instance** that is intended to copy the second puzzle piece to the location `/data/piece2.png` **iniside the docker instance**, but the relevant lines have been commented out.  Your task is to remove the comments from `/usr/bin/mover.sh` **inside the docker instance** and modify the `/root/files/task2.sh` script **on the server** to make capture the file that is being copied to `/var/ta/task2/piece2.png` **on the host server**.

## Task 3

The following Docker images have been loaded on the system and pre-configured:

 * `ta:task3_web` runs a simple HTTP server on port `80` that loads data from a CouchDB request from a server running at host `db` on port *5984*
  * `ta:task3_db` runs a CouchDB server on port `5984` that contains the third puzzle piece   

  Both images are configured to run as daemons via the script `/root/files/task3.sh`.  Modify the script to accomplish the following:

   1. The `ta:task3_web` container's web server is accessible on the **host** server's `localhost` interface on port `8000`
    1. The `ta:task3_web` container can communicate with the `ta:task3_db` container via the hostname `db`

    If successful, the following command run on the **host server** will unlock the third puzzle piece:

    ```
# wget http://localhost:8000/piece3.png -O /var/ta/task3/piece3.png
    ```

    *Note: We will re-run the above `wget` command in order to test your solution.  Additionally, ensure that your solution to the `task3.sh` script is idempotent and can be rerun consecutively without errors.*


## Task 4

The fourth puzzle piece is located inside of the `ta:task4-snd` Docker image loaded on the server.  It executes `scp piece4.png doftw@rcv:/data` and exits.  To unlock the fourth piece, you will need to create another Docker instance that will be the recipient of the `scp` command.  

To unlock the fourth puzzle piece, you will need to create your own Docker image/container that will receive the SCP'd file from `ta:task4-snd`.  It will need to meet the following requirements:

 1. Have a user account for `doftw`
  1. The user's SSH `authorized_keys` file must contain the provided public key found at `/root/files/do_challenge.pub` **on the host server**
   1. Run SSH Server on the standard port `22`

   Additionally, you will need to modify the `/root/files/task4.sh` script so that:

    1. Your new image is run continuously in a detached state
     1. The `ta:task4-snd` container must be able to communicate with the new container via the hostname `rcv`
      1. The file SCP'd from `ta:task4-snd` to `/data/piece4.png` **on the new container** is stored as `/var/ta/task4/piece4.png` **on the host server**

      You may use any base image you wish, however **debian:stable** has already been pre-loaded on the system for you. 

      *Note: Ensure that your solution to the `task4.sh` script is idempotent and can be rerun consecutively without errors.*
