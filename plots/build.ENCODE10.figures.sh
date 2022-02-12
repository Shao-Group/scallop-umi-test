#!/bin/bash
dir=`pwd`

# collect results
if [ "A" == "A" ];then
	echo "collecting ENCODE10..."
	$dir/collect_ENCODE10.sh
fi

# plot figures for running all four methods at default
if [ "A" == "A" ];then
	mkdir -p $dir/ENCODE10/figure

	echo "plotting ENCODE10..."
	python $dir/plots_ENCODE10.py
fi

# plot figures for running all four methods at default
if [ "A" == "B" ];then
        echo "plotting multi-exon transcirpts only results on ENCODE10..."
        python $dir/plots_multi_ENCODE10.py
fi

# plot figures for quant experiments
if [ "A" == "B" ];then
	echo "plotting quant results..."
	python $dir/plots_ENCODE10_quant.py
fi

# plot figures for class experiments
if [ "A" == "B" ];then
	echo "plotting class results..."
	python $dir/plots_ENCODE10_class.py
fi

# plot figures for varying parameters experiments
if [ "A" == "B" ];then
	echo "plotting varying parameters results..."
	python $dir/plots_ENCODE10_parameter.py
fi

# plot figures for full-length and non-full-length distribution
if [ "A" == "B" ];then
	echo "plotting full-length and non-full-length distribution..."
	python $dir/plots_ENCODE10_fragments.py
fi
