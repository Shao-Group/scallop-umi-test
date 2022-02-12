#!/bin/bash
dir=`pwd`

# collect results
if [ "A" == "A" ];then
	echo "collecting HEK293T..."
	$dir/collect_HEK293T.sh
	echo "collecting Mouse-Fibroblast..."
	$dir/collect_Mouse-Fibroblast.sh
fi

# plot figures for running all four methods at default
if [ "A" == "A" ];then
	mkdir -p $dir/HEK293T/figure
	mkdir -p $dir/Mouse-Fibroblast/figure

	echo "plotting HEK293T..."
	python $dir/plots_HEK293T.py
	echo "plotting Mouse-Fibroblast..."
	python $dir/plots_Mouse_Fibroblast.py
fi

# plot figures for multi-exon transcirpts only results
if [ "A" == "B" ];then
        echo "plotting multi-exon transcirpts only results on HEK293T..."
        python $dir/plots_multi_HEK293T.py
        echo "plotting multi-exon transcirpts only results on Mouse-Fibroblast..."
        python $dir/plots_multi_Mouse_Fibroblast.py
fi

# plot figures for quant experiments
if [ "A" == "B" ];then
	echo "plotting quant results..."
	python $dir/plots_smartseq3_quant.py
fi

# plot figures for class experiments
if [ "A" == "B" ];then
	echo "plotting class results..."
	python $dir/plots_smartseq3_class.py
fi

# plot figures for varying parameters experiments
if [ "A" == "B" ];then
	echo "plotting varying parameters results..."
	python $dir/plots_HEK293T_parameter.py
	python $dir/plots_Mouse_Fibroblast_parameter.py
fi

# plot figures for full-length and non-full-length distribution
if [ "A" == "B" ];then
	echo "plotting full-length and non-full-length distribution..."
	python $dir/plots_HEK293T_fragments.py
	python $dir/plots_Mouse_Fibroblast_fragments.py
fi
