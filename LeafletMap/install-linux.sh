#!/bin/bash

rm -f Pipfile.lock

python -m pip install pip --upgrade
pip install pipenv --upgrade

pipenv install
