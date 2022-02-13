# Overview

This repository tests and compares the performance of transcript assembler
[**Scallop2**](https://github.com/Shao-Group/scallop2) with other three leading transcript assemblers,
[StringTie2](https://github.com/gpertea/stringtie),
[Scallop](https://github.com/Kingsford-Group/scallop) and
[CLASS2](http://ccb.jhu.edu/people/florea/research/CLASS2).
Here we provide instructions to download and link all necessary tools, we also provide scripts to download datasets, run the four methods, evaluated the
predicted transcripts, and reproduce the results and figures in the Scallop2 paper.

The pipeline involves in the following four steps:
1. Download and/or compile necessary tools (`programs` directory).
2. Download necessary datasets (`data` directory).
3. Run the methods to produce results (`results` directory).
4. Summarize results and produce figures (`plots` directory).

**Important Notice**: Tools are not downloaded automatically.
Users need to separately download and link all necessary tools to the folder `programs` before running scripts. 
Please follow the instructions in Step 1 Download Tools to download and link all necessary tools.

# Step 1 : Download and Link Tools

Our experiments involve the following ten tools.
Tools are not downloaded automatically.
Users need to separately download all neccessary tools and link them to the folder `programs` before running experiments.

Tool | Version | Description
------------ | ------------ | ------------
[Scallop2](https://github.com/Shao-Group/Scallop2) | v1.1.2 | Transcript assembler
[StringTie2](https://github.com/gpertea/stringtie) | v2.1.7 | Transcript assembler
[Scallop](https://github.com/Kingsford-Group/scallop) | v0.10.5 | Transcript assembler
[CLASS2](http://ccb.jhu.edu/people/florea/research/CLASS2) | v2.1.7 | Transcript assembler
[zUMIs](https://github.com/sdparekh/zUMIs) | v2.9.4 | Process RNA-seq data with barcodes
[STAR](https://github.com/alexdobin/STAR) | v2.7.3a | RNA-seq aligner
[gffcompare](http://ccb.jhu.edu/software/stringtie/gff.shtml) | v0.9.9c | Evaluate assembled transcripts
[Salmon](https://salmon.readthedocs.io/en/latest/salmon.html) | v1.6.0 | Transcript quantification
[bedtools](https://bedtools.readthedocs.io/en/latest/content/overview.html) | v2.29.1 | Toolset for genome arithmetic
[gtfcuff](https://github.com/Kingsford-Group/rnaseqtools) |  | RNA-seq tool

Instructions on Download and Link Tools:

**Step 1.1**: Click above tools and those hyperlinks will navigate users to the homepage of tools. Then please follow the instructions provided in tools' homepages to download and/or compile above ten tools.

**Step 1.2**: Please link or copy the executable files to `programs` directory if they are avaliable (scallop2, stringtie2, scallop, STAR, gffcompare, salmon, bedtools, and gtfcuff). Otherwise please link the directory here (zUMIs and class2).

Please make sure tools can be called by the following paths:
```
your/path/to/programs/scallop2
your/path/to/programs/stringtie2
your/path/to/programs/scallop
your/path/to/programs/class2/run_class.pl
your/path/to/programs/zUMIs/zUMIs.sh
your/path/to/programs/STAR
your/path/to/programs/gffcomapre
your/path/to/programs/salmon
your/path/to/programs/bedtools
your/path/to/programs/gtfcuff
```
You may need to rename some executable files (e.g. rename 'stringtie' to 'stringtie2') or folders (e.g. rename 'CLASS-2.1.7' to 'class2') to make sure that all tools can be called successfully by above paths. 

## **Example of how to download and copy/link tool to `programs`**
Here we provide an example how to download and copy/link tool to the `programs` directory. We use tool [STAR](https://github.com/alexdobin/STAR) as an example. 

a) Following the step 1.1, click the [STAR](https://github.com/alexdobin/STAR) in the above table and we will be navigated to its GitHub page.

b) Then click the **Releases** in the middel-right of that page and find the release version 'STAR 2.7.3a ______ 2019/10/08'.

c) Click the **Assets**, we will see 'Source code (zip)' and 'Source code (tar.gz)'. Suppose we choose 'Source code (tar.gz)' and download it.

d) Enter the directory that contains the downloaded 'Source code (tar.gz)', and run command to uncompress it:
```
tar -zxvf STAR-2.7.3a.tar.gz
```  
A folder named 'STAR-2.7.3a' will appear.

e) Enter directory 'STAR-2.7.3a' and we can find pre-compiled executables for Linux and Mac OS X under 'bin'. Choose the one fits your operating system.
Suppose we are going to use the one for Linux_x86_64, we will enter the directory 'Linux_x86_64' under 'bin'. 

f) Following the step 1.2, we need to copy/link the executable file 'STAR' to directory `programs`. If you would like to copy the executable file 'STAR' to directory `programs`, you can use the command (please make sure you replace the 'your/path/to/programs' with your true path to directory `programs`):
```
cp STAR your/path/to/programs/
```
or if you would like to do link, you will need to enter the directory `programs`firstly using the command (please make sure you replace the 'your/path/to/programs' with your true path to directory `programs`): 
```
cd your/path/to/programs/
```
and then link the executable file 'STAR' using command (please make sure you replace the 'your/path/to/STAR' with your true path to executable file 'STAR'):
```
ln -sf your/path/to/STAR ./
```

Please make sure all necessary tools have been separately downloaded and linked to the folder `programs` before running experiments.

# Step 2: Download Datasets and Preprocess
Once all necessary tools are all available, we can start to download and preprocess data.

We compare the four methods on three datasets, namely **HEK293T**, **Mouse-Fibroblast**, and **ENCODE10**. 
Besides, we also need the annotation files for evaluation purposes.
In directory `data`, we provide metadata for these datasets.

For dataset **ENCODE10**, we provide its doi link and users need to download ENCODE10 data using the doi link.
For datasets **HEK293T** and **Mouse-Fibroblast**, we provide scripts to download and preprocess them.
For annotations, we provide script to download and index them.

## Step 2.1 Download Annotations and Create Index
For **HEK293T** and **ENCODE10** datasets, we use human annotation database as reference;
for **Mouse-Fibroblast** dataset, we use mouse annotation database as reference.
Use the following script in `data` to download annotations and generate indexes:
```
./download_index.annotation.sh
```
The files will appear under `data/human` and `data/mouse`.

## Step 2.2 Download Datasets
## **HEK293T**
The first dataset, namely **HEK293T**,
contains 192 human cells downloaded from [Smart-seq3 project (2020)](https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-8735).
All these cells are sequenced with strand-specific and multiple-end protocol using barcoding technology.
For the raw sequencing data, we demultiplex and preprocess using [zUMIs](https://github.com/sdparekh/zUMIs) tool, in which [STAR](https://github.com/alexdobin/STAR) will be called to generate reads alignments.
This dataset can be downloaded and preprocessed by the script in `data` directory.
```
./download_preprocess.HEK293T.sh
```
The downloaded files will appear under `data`.

## **Mouse-Fibroblast**
The second dataset, namely **Mouse-Fibroblast**,
contains 369 mouse cells downloaded from [Smart-seq3 project (2020)](https://www.ebi.ac.uk/arrayexpress/experiments/E-MTAB-8735).
All these cells are sequenced with strand-specific and multiple-end protocol using barcoding technology.
For the raw sequencing data, we demultiplex and preprocess using [zUMIs](https://github.com/sdparekh/zUMIs) tool, in which [STAR](https://github.com/alexdobin/STAR) will be called to generate reads alignments.
This dataset can be downloaded and preprocessed by the script in `data` directory.
```
./download_preprocess.Mouse-Fibroblast.sh
```
The downloaded files will appear under `data`.

## **ENCODE10**
The third dataset, namely **ENCODE10**,
contains 10 human RNA-seq samples downloaded from [ENCODE project (2003--2012)](https://genome.ucsc.edu/ENCODE/).

All these samples are sequenced with strand-specific and paired-end protocols.
For each of these 10 samples, we align it with three RNA-seq aligners,
[STAR](https://github.com/alexdobin/STAR), and
[HISAT2](https://ccb.jhu.edu/software/hisat2/index.shtml).
Among them the STAR and HISAT2 alignments are
available at [doi:10.26208/8c06-w247](https://doi.org/10.26208/8c06-w247) (same data used in another research work).

**Important Notice**: 
Please download **ENCODE10** dataset using the doi link [doi:10.26208/8c06-w247](https://doi.org/10.26208/8c06-w247). Please create a folder named `ENCODE10` in `data` directory, and make sure all downloaded data of **ENCODE10** dataset are stored in the `data/ENCODE10` directory.

Please make sure `data/ENCODE10` directory contains 10 folders (folder names are Accession IDs) and each folder contains one `hisat.sort.bam` and one `star.sort.bam`.


# Step 3: Run the Methods

Once the datasets and programs are all available, use the following scripts in `results`
to run the assemblers on the datasets:
```
./run.HEK293T.sh
./run.Mouse-Fibroblast.sh
./run.ENCODE10.sh
```

**Note**: CLASS2 runs more than 11 days on sample SRR387661 of **ENCODE10** dataset during our experiments. Therefore, you may also need to terminate the `run.HEK293T.sh` manually.

In each of these three scripts, you can modify it to run different
methods (Scallop2, StringTie2, Scallop, and CLASS2). You can also modify the scripts to specify
how many CPU cores you want to use to run the jobs in parallel. 


# Step 4: Analysis Results and Reproduce Figures

Once all the results of four methods on three datasets have been generated, one can use the following scripts in `plots` to reproduce the figures:
```
./build.Smartseq3.figures.sh
./build.ENCODE10.figures.sh
```
Here `build.Smartseq3.figures.sh` will generate figures for **HEK293T**, **Mouse-Fibroblast**. `build.ENCODE10.figures.sh` will generate figures for **ENCODE10**.

**Important Notice**: You need to install Python3 packages `numpy` and `matplotlib` to process data and generate figures.

The figures will appear under `plots/HEK293T/figure`, `plots/Mouse-Fibroblast/figure` and `plots/ENCODE10/figure`. 

Default setting will generate figures for comparing all four assemblers running at default parameters on three datasets. You can modify the scripts in `results` and `plots` to run assemblers at different parameters.
