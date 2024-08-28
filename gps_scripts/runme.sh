#!/bin/bash

set -x

if [ ! $# -eq 2 ];
then
  echo 'Example: bash runme.sh <gpx_dir>'
  exit
fi

gpx_dir=$1
final_png=$2

echo 'use gpx_dir $gpx_dir'

perl logdraw.pl -SRCDIR $gpx_dir -TRACK_COLOR "#FFFFFF00" -IMAGE_SIZE 1000
perl logdraw.pl -SRCDIR $gpx_dir -TRACK_COLOR "#FFFFFF00" -TRACK_THICKNESS 10 -OUTPUT thick.png -IMAGE_SIZE 1000

matrix=""
matrix="${matrix} 0.0 0.0 0.0 0.0 0.0"
matrix="${matrix} 0.0 0.3 0.0 0.0 0.0"
matrix="${matrix} 0.0 0.0 0.6 0.0 0.0"
matrix="${matrix} 0.0 0.0 0.0 0.0 0.0"
matrix="${matrix} 0.0 0.0 0.0 0.0 0.0"

magick thick.png -gaussian-blur 30x10 -color-matrix "${matrix}" halo.png
magick halo.png output.png output.png -composite $final_png

rm -f thick.png
rm -f halo.png
rm -f output.png

