#!/bin/bash

./collect_ENCODE10.sh
./collect_HEK293T.sh
./collect_Mouse-Fibroblast.sh

mkdir -p ./ENCODE10/figure
mkdir -p ./HEK293T/figure
mkdir -p ./Mouse-Fibroblast/figure

python plot_ENCODE10.py
python plot_HEK293T.py
python plot_Fibroblast.py
