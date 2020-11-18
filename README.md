# cs107-FinalProject 
[![Build Status](https://travis-ci.com/DeriveMeCrazy-AutoDiff/cs107-FinalProject.svg?token=tjHxgXnrZQTw99nTC12g&branch=m1b)](https://travis-ci.com/DeriveMeCrazy-AutoDiff/cs107-FinalProject)
[![codecov](https://codecov.io/gh/DeriveMeCrazy-AutoDiff/cs107-FinalProject/branch/master/graph/badge.svg?token=G7FvPYxS2N)](https://codecov.io/gh/DeriveMeCrazy-AutoDiff/cs107-FinalProject)

### Group #21
John Alling \
Moriya Dechtiar \
Al-Muataz Khalil \
Tianen Liu

## Installing the Dependencies
If installing within a conda environment:
```
conda install --file requirements.txt
```
Otherwise:
```
pip install -r requirements.txt
```
## Usage
First, add the package to your python path (will not be necessary in future project iterations)
```
import os
os.path.insert(0,'/path/to/cs107-FinalProject/auto_diff_pkg/')
```
The package can then be imported and utilized.
```
import AutoDiff as AD
```
Please see `docs/demo.ipynb` for demonstrations of the AutoDiff class.
