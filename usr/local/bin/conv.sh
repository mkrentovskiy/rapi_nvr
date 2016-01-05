#!/bin/bash
ffmpeg -i $1 -c copy /srv/$2.mp4
rm $1
