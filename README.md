Ok, let's turn your Raspberry Pi 2 into simple NVR with simple steps:

0. Use Raspbian.

1. first of all, we need some software on board:

 sudo apt-get install tmux gcc g++ librtmp-dev libssl-dev zlib1g-dev libpcre3-dev

2. next, we must build and install ffmpeg and nginx-rtmp:

 wget http://ffmpeg.org/releases/ffmpeg-snapshot-git.tar.bz2
 tar xf ffmpeg-snapshot-git.tar.bz2
 cd ffmpeg
 ./configure --enable-nonfree --enable-librtmp
 make
 sudo make install

 wget http://nginx.org/download/nginx-1.8.0.tar.gz
 tar xf nginx-1.8.0.tar.gz
 git clone https://github.com/arut/nginx-rtmp-module.git
 cd nginx-1.8.0
 ./configure --add-module=`pwd`/../nginx-rtmp-module
 make
 sudo make install

3. now you can copy files from this repo up to root of your device with replacing.

4. next,configure cams. 

You're know, that there are two type of IP-cams - with RTSP bug or without. 
Firts of it need two step capture - special RTSP client for stream capture and ffpmeg for pipe processing.
Last needs only ffmpeg. Take a look at /usr/local/video. There are two examples for each - cam0 for valid RTSP (Xiaomi Ant, etc) and with bug 
(most of others chinees IP-cams). Note: if you need more then two cams, you can copy this scripts and configure by yourself, but don't forget about 
/etc/rc.local with it's start point and /usr/local/nginx/html/index.html for interface.

5. now up your browser and get http://rapi_ip for online view or http://rapi_ip/srv for archive (must work on Apple devices too). Pretty simple.
