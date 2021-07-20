#!/bin/bash

dir=`pwd`

# step 1: download
if [ "A" == "A" ];then
        cd $dir

	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.R1.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.R2.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.I1.fastq.gz
	wget ftp://ftp.ebi.ac.uk/pub/databases/microarray/data/experiment/MTAB/E-MTAB-8735/Smartseq3.Fibroblasts.GelCut.I2.fastq.gz
fi

# step 2: preprocess
if [ "A" == "A" ];then
        cd $dir
        /path/to/zUMIs/zUMIs.sh -c -y Mouse-Fibroblast.yaml
fi

