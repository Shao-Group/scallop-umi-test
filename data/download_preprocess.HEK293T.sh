#!/bin/bash
dir=`pwd`
zumis=$dir/../programs/zUMIs/zUMIs.sh

# step 0: check all to-be-used tools/data
if [ "A" == "A" ];then
        echo "================================================================="
        echo "Check if to-be-used tools/data are properly linked..."
        echo "================================================================="
        if [ -e $STAR ];then
                echo -e "Tool zUMIs found successfully!"
        else
                echo -e "Tool zUMIs not found in directory 'programs'.\nPlease follow the instructions in 'Step 1: Download and Link Tools' to properly download and link all necessary tools to the directory 'programs'."
                echo -e "\nNote: Tools are not downloaded automatically. Users need to download and/or compile all required tools, and then link them to 'programs' directory before running experiments.\n"
                exit 1
        fi
        echo -e "To-be-used tools/data found successfully!"
fi

# step 1: download
if [ "A" == "A" ];then
        cd $dir
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.diySpike.R1.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.diySpike.R2.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.diySpike.I1.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.diySpike.I2.fastq.gz
fi

# step 2: preprocessi by tool zUMIs
if [ "A" == "A" ];then
        cd $dir
	sed -i "s! curDir! $dir! g" HEK293T.yaml
	$zumis -c -y HEK293T.yaml
fi
