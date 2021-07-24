#!/bin/bash
dir=`pwd`

echo "collecting ENCODE10..."
$dir/collect_ENCODE10.sh
echo "collecting HEK293T..."
$dir/collect_HEK293T.sh
echo "collecting Mouse-Fibroblast..."
$dir/collect_Mouse-Fibroblast.sh

mkdir -p $dir/ENCODE10/figure
mkdir -p $dir/HEK293T/figure
mkdir -p $dir/Mouse-Fibroblast/figure

echo "plotting ENCODE10..."
python $dir/plots_ENCODE10.py
echo "plotting HEK293T..."
python $dir/plots_HEK293T.py
echo "plotting Mouse-Fibroblast..."
python $dir/plots_Mouse-Fibroblast.py
