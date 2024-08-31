# Instructions on collecting data with the Raspberry Pi
If you ever can't find the absolute path, you can use the following command
```bash
echo "$(cd "$(dirname "$1")" && pwd -P)/$(basename "$1")"
```
## Setting up python environment
Update packages and install packages
```bash
sudo apt update
sudo apt upgrade
```
```bash
sudo apt install python3-full
sudo apt install git
```

Clone the repository and create virtual environment
```bash
git clone https://github.com/smartHiveProject/smartHive-vision.git
cd smartHive-vision/src
python -m venv env
```

Activate the virtual environment and install python packages
```bash
# Activate virtual environment
source env/bin/activate
# or:
. env/bin/activate

pip install -r requirements.txt
```
Whenever you want to run the scripts, you need to activate the virtual environment

## Setting up auto start on boot
Create a bash script to run the python script (Note: using the old script is recommended and the new one offers no benefit and only seems to crash once in a while)
```bash
touch start-raspi-cam.sh
nano start-raspi-cam.sh
```
```bash
!#/bin/bash

cd /home/user/path-to-repo/src
. smartenv/bin/activate
python raspi_cam_old.py
```
Set up a cron job to start this script each time the Raspberry Pi boots
```bash
sudo crontab -e
```
Add the following line to the file
```bash
@reboot sh /home/user/path-to-script/start-raspicam.sh
```
All recordings and logs will be in the `src` directory
