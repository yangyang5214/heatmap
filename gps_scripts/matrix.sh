#!/bin/bash

set -x

if [ ! $# -eq 1 ];
then
  echo 'Example: bash runme.sh <gpx_dir>'
  exit
fi

gpx_dir=$1

echo 'use gpx_dir $gpx_dir'

matrix="${matrix} 0.0 0.0 0.0 0.0 0.0"
matrix="${matrix} 0.0 0.3 0.0 0.0 0.0"
matrix="${matrix} 0.0 0.0 0.6 0.0 0.0"
matrix="${matrix} 0.0 0.0 0.0 0.0 0.0"
matrix="${matrix} 0.0 0.0 0.0 0.0 0.0"

magick thick.png -gaussian-blur 30x10 -color-matrix "${matrix}" halo.png

