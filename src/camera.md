# Collecting data with the Raspberry Pi
> [!NOTE]
> If you ever can't find the absolute path, you can use the following command to get it:
```bash
echo "$(cd "$(dirname "$1")" && pwd -P)/$(basename "$1")"
```

## Setting up a python virtual environment on the Raspberry Pi
After you SSH into the Raspberry Pi, you can follow these steps:  

Update packages and install required packages
```bash
sudo apt update
sudo apt upgrade
```
```bash
sudo apt install python3-full
sudo apt install git
```

Clone the repository where you want it to be located and create a python virtual environment
```bash
git clone https://github.com/smartHiveProject/smartHive-vision.git
cd smartHive-vision/src
python -m venv env
```

Activate the venv and install python packages
```bash
# Activate virtual environment
source env/bin/activate
# or:
. env/bin/activate

# Update pip and install packages
pip install --upgrade pip
pip install -r requirements.txt
```
> [!NOTE]
> Whenever you want to run the scripts manually, you will need to activate the virtual environment first

## Setting the script to start up on boot
Create a bash script which will run the python script in the virtual environment
```bash
touch start-raspi-cam.sh
nano start-raspi-cam.sh
```
```bash
!#/bin/bash

cd /home/user/path-to-repo/src
. smartenv/bin/activate
python raspi_cam.py
```
To start this bash file on startup, create a cron job to start this script each time the Raspberry Pi boots
```bash
sudo crontab -e
```
and add the following line to the file
```bash
@reboot sh /home/user/path-to-script/start-raspicam.sh
```
All recordings and logs will be in the `src` directory
