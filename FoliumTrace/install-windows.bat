del Pipfile.lock

python -m pip install pip --upgrade
pip install pipenv --upgrade

pipenv install

pipenv run pip install "./pip/win32/GDAL-2.3.2-cp36-cp36m-win32.whl"
pipenv run pip install "./pip/win32/Shapely-1.6.4.post1-cp36-cp36m-win32.whl"
pipenv run pip install "./pip/win32/Fiona-1.8.2-cp36-cp36m-win32.whl"
pipenv run pip install "./pip/win32/pyproj-1.9.5.1-cp36-cp36m-win32.whl"

pipenv run pip install "./pip/win64/GDAL-2.3.2-cp36-cp36m-win_amd64.whl"
pipenv run pip install "./pip/win64/Shapely-1.6.4.post1-cp36-cp36m-win_amd64.whl"
pipenv run pip install "./pip/win64/Fiona-1.8.2-cp36-cp36m-win_amd64.whl"
pipenv run pip install "./pip/win64/pyproj-1.9.5.1-cp36-cp36m-win_amd64.whl"

pipenv run pip install geopandas

pause