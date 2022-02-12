#!/bin/bash

dir=`pwd`

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
	$dir/../programs/zUMIs/zUMIs.sh -c -y HEK293T.yaml
fi
