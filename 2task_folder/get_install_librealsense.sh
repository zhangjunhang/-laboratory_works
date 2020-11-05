#!/bin/bash

sudo apt-get install libxinerama-dev
sudo apt-get install libxcursor-dev
sudo apt-get install git libssl-dev libusb-1.0-0-dev pkg-config libgtk-3-dev
sudo apt-get install libglfw3-dev libgl1-mesa-dev libglu1-mesa-dev

git clone https://github.com/IntelRealSense/librealsense.git
cd librealsense

sudo cp config/99-realsense-libusb.rules /etc/udev/rules.d/
./scripts/patch-realsense-ubuntu-lts.sh

mkdir build && cd build

echo "You succesfully installed librealsense"

case "$1" in
	-make_with_demo)
		cmake .. -DBUILD_EXAMPLES=true -DBUILD_WITH_OPENMP=false -DHWM_OVER_XU=false
		make -j4
		sudo make install

		echo "You successfully built demo"
		;;
	*) echo "no such option" ;;
esac


