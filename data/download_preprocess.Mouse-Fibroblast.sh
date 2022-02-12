#!/bin/bash
dir=`pwd`
zumis=$dir/../programs/zUMIs/zUMIs.sh

# step 0: check all to-be-used tools/data
if [ "A" == "A" ];then
        echo "================================================================="
        echo "start to check if to-be-used tools/data are properly installed..."
        echo "================================================================="
        if [ -e $zumis ];then
                echo -e "Find tool zUMIs successfully!"
        else
                echo -e "Tool zUMIs has not been linked to the directory 'programs' yet.\nPlease follow the instructions in 'Step 1: Download and Link Tools' to install and link all necessary tools to the directory 'programs'."
                echo -e "\nNote: Tools are not downloaded automatically. Users need to download and/or compile all required tools, and then link them to 'programs' directory before running experiments.\n"
                exit 1
        fi
        echo -e "Find all to-be-used tools/data successfully!"
fi


# step 1: download
if [ "A" == "A" ];then
        cd $dir

	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.R1.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.R2.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.I1.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.I2.fastq.gz
fi

# step 2: preprocess by tool zUMIs
if [ "A" == "A" ];then
        cd $dir
	sed -i "s! curDir! $dir! g" Mouse-Fibroblast.yaml
        $zumis -c -y Mouse-Fibroblast.yaml
fi

