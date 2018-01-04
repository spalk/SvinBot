# Raspberry Pi 3 setting up step by step
_Actual for January 2018_

## Burning Rasbian Image on SD card
Download last image of [Raspbian](https://www.raspberrypi.org/downloads/raspbian/) from the official Raspberry site. Do not use NOOBS, take Raspian Lite (without Desktop) directly. Burn it on SD card with [etcher](https://etcher.io/).

##Activating SSH 
To activate SSH - create empty file "SSH" on BOOT partition on SD card before incerting it in Raspberry PI.
After loading Raspberry Pi find out IP of Raspberry and you can connect with SSH. 

##Activating and setup WiFi
  * *sudo iwlist wlan0 scan* - list of all availiable networks

  * */etc/dhcpcd.conf* - config where you cat set up static IP adress for your Raspberry. Add at the end for WiFi: 
```
interface wlan0
inform 192.168.1.32
static routers=192.168.1.1
static domain_name_servers=8.8.8.8 77.88.8.8
```
For Ethernet is the same with *eth0*

  * */etc/wpa_supplicant/wpa_supplicant.conf* - your WiFi network setup. Add to the end:
```
network={
    ssid="wifi_name"
    psk="wifi_password"
}
```

##Change hostname
If you have more than one Raspberry Pi's it's good idea to change the hostname: 
  * */etc/hostname*
  * */etc/hosts* - also change for 127.0.1.1 

##Installing Software 

* *sudo apt-get update* - just in case :)

Installing program list (*sudo apt-get install*):
* *nmap* 
* *git*
* *tree*
* *python3-pip*
* *python-pip*


Installing python3 packages (*sudo pip3 install*):
* *telepot* - for Telegram
* *gspread* - for Google Speadsheets
* *oauth2client* - OAuth
* *RPi.GPIO* - for Raspberry Pi
* *Adafruit_GPIO* 
* *pygal* - graphs
  * *lxml*
  * *cairosvg*
  * *tinycss*
  * *cssselect*  
* *picamera* - Pi Camera


## Autorun script
To autorun script after loading Raspberry add command line to the end of file */etc/rc.local* before line *exit 0*, for example:
```
python /home/pi/my-soft/my-script.py &
```
Be careful with this file. Mistake can make loading of Raspberry impossible. 
