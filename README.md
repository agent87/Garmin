# Garmin watch data parsing & analytics
This goes to all my atheltic peeps who posses a garmin smart watch but can't access their synchronise their stats on the \
garmin connect because they run unsupported O.S such as LINUX plus also posses some data science skills awaiting in the  \
shelf.

## Installation
clone the git repository\
`git clone https://github.com/agent87/garmin.git`

change to the garmin directory\
`cd garmin-data-analytics`

create a conda env and install packages/libraries using the environment image\
`conda env create environment.yml`

or install requried packages/libraries using PIP\
`pip install -r requirements.txt`

## configuration
Present in The Garmin Folder is Configuration File which can modified to suit your needs

Credential section\
`ID_FS_LABEL = GARMIN`\
`uname= default_uname`\
`passwd = my_secret_password`\
`user = root`\


Auto Sync Function\
`rasp_sync = False`   #Sync files from remote raspberry pi\
`cloud_sync = False`  #automatic upload to Garmin connect platform\
`local_sync = True`  #auto-back up on local machine\

Automatic device mount Detection\
`auto_detect = False`

## Data Parsing

## Database
