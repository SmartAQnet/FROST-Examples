#!/bin/bash

rm -f Pipfile.lock

python -m pip install pip --upgrade
pip install pipenv --upgrade

pipenv install

pipenv run pip install shapely==1.6.4
pipenv run pip install fiona==1.8.2
pipenv run pip install pyproj==1.9.5.1
pipenv run pip install geopandas
