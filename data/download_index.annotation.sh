#!/bin/bash

dir=`pwd`

# step 1: download reference
if [ "A" == "A" ];then
	cd $dir
	mkdir -p human
	cd human
	wget http://ftp.ensembl.org/pub/release-104/gtf/homo_sapiens/Homo_sapiens.GRCh38.104.gtf.gz
	wget http://ftp.ensembl.org/pub/release-104/fasta/homo_sapiens/dna/Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

	gzip -d Homo_sapiens.GRCh38.104.gtf.gz
	gzip -d Homo_sapiens.GRCh38.dna.primary_assembly.fa.gz

	cd $dir
	mkdir -p mouse
	cd mouse
	wget http://ftp.ensembl.org/pub/release-104/gtf/mus_musculus/Mus_musculus.GRCm39.104.gtf.gz
	wget http://ftp.ensembl.org/pub/release-104/fasta/mus_musculus/dna/Mus_musculus.GRCm39.dna.primary_assembly.fa.gz

	gzip -d Mus_musculus.GRCm39.104.gtf.gz
	gzip -d Mus_musculus.GRCm39.dna.primary_assembly.fa.gz
fi

# step 2: indexing
if [ "A" == "A" ];then
	cd $dir/human
	mkdir -p human_index
	/path/to/STAR --runMode genomeGenerate \
     		--runThreadN 30 \
     		--genomeDir ./human_index \
     		--genomeFastaFiles $dir/human/Homo_sapiens.GRCh38.dna.primary_assembly.fa \
     		--sjdbGTFfile $dir/human/Homo_sapiens.GRCh38.104.gtf \
     		--sjdbOverhang 149

	cd $dir/mouse
	mkdir -p mouse_index
	/path/to/STAR --runMode genomeGenerate \
     		--runThreadN 30 \
     		--genomeDir ./mouse_index \
     		--genomeFastaFiles $dir/mouse/Mus_musculus.GRCm39.dna.primary_assembly.fa \
     		--sjdbGTFfile $dir/mouse/Mus_musculus.GRCm39.104.gtf \
     		--sjdbOverhang 149
fi
