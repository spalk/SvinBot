# Raspberry Pi 3 setting up step by step
_Actual for January 2018_

## Burning Rasbian Image on SD card
1. Don't use NOOBS, use Raspian  directly. Download last image of **Raspbian Lite** (without Desktop) from [the official Raspberry site](https://www.raspberrypi.org/downloads/raspbian/).  
2. Burn it on SD card with [etcher](https://etcher.io/).

## Activating SSH 
1. **Befor inserting SD card in Raspberry!** To activate SSH - create empty file "SSH" on BOOT partition on SD card.
2. Insert SD card in Raspberry and load it. 
3. Find out IP address of Raspberry with **nmap** (`nmap -sn 192.168.1.0/24`) or on your router. 
4. Connect: `ssh pi@ip_address`. Default password is **raspberry**.

## Activating and setup WiFi
  * `/etc/dhcpcd.conf` - config where you cat set up static IP adress for your Raspberry. Add at the end for WiFi: 
```
interface wlan0
inform 192.168.1.32
static routers=192.168.1.1
static domain_name_servers=8.8.8.8 77.88.8.8
```
For Ethernet is the same with **eth0** 

  * `/etc/wpa_supplicant/wpa_supplicant.conf` - your WiFi network setup. Add to the end:
```
network={
    ssid="wifi_name"
    psk="wifi_password"
}
```

##  Configuration
* `raspi-config` 

## Change hostname
If you have more than one Raspberry Pi's it's good idea to change the hostname: 
  * `/etc/hostname`
  * `/etc/hosts` - also change for 127.0.1.1 

## Installing Software 

* `sudo apt-get update` - just in case :)

### Installing program list (`sudo apt-get install`):
* `nmap` 
* `git`
* `tree`
* `python3-pip`
* `python-pip`
* `screen`

### Installing from source: 
* `wiringPi`
  1. `git clone git://git.drogon.net/wiringPi` - clone source code
  2. `cd wiringPi` 
  2. `./build`
  3. `gpio readall` - test. You should see a status table of GPIO pins.

### Installing python3 packages (`sudo pip3 install`):
* `telepot` - for Telegram
* `gspread` - for Google Speadsheets
* `oauth2client` - OAuth
* `RPi.GPIO` - for GPIO
* `Adafruit_GPIO` - Adafruit libs use it
* `pygal` - graphs lib
  * `lxml`
  * `cairosvg`
  * `tinycss`
  * `cssselect`  
  sudo apt-get install python3-cairo

* `picamera` - Pi Camera

## Autorun script
To autorun script after loading Raspberry add command line to the end of file `/etc/rc.local` before line `exit 0`, for example:
```
python /home/pi/my-soft/my-script.py &
```
Be careful with this file. Mistake can make loading of Raspberry impossible. 

## Streaming video 

First you neen intall vlc

```
sudo apt-get update
sudo apt-get install vlc
```

Start streamnig:
`raspivid -o - -t 0 -hf -w 640 -h 360 -fps 25 | cvlc -vvv stream:///dev/stdin --sout '#rtp{sdp=rtsp://:8554}' :demux=h264`

Run VLC on remote device using link: 
`rtsp://rpi_with_camera_ip_address:8554/`




## Usefull commands 
* `sudo iwlist wlan0 scan` - list of all availiable networks
* `nmap -sn 192.168.1.0/24` - scan hosts in your network
* `gpio readall` - GPIO pins status 


## Usefull links
* [pinout.xyz](https://pinout.xyz/#)
