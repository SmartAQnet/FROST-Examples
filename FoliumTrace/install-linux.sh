#!/bin/bash

rm -f Pipfile.lock
sudo apt-get update
sudo apt-get install build-essential python-all-dev

python -m pip install pip --upgrade
pip install pipenv --upgrade

pipenv install

wget http://download.osgeo.org/gdal/2.3.2/gdal-2.3.2.tar.gz
tar xvfz gdal-2.3.2.tar.gz
cd gdal-2.3.2
./configure --with-python
make
sudo make install
cd ..

pipenv run pip install shapely==1.6.4
pipenv run pip install fiona==1.8.2
pipenv run pip install pyproj==1.9.5.1
pipenv run pip install geopandas
