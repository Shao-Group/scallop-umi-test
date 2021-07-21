# Overview

This repository tests and compares the performance of transcript assembler
[**Scallop2**](https://github.com/Kingsford-Group/scallop2) with other three leading transcript assemblers,
[StringTie2](https://github.com/gpertea/stringtie),
[Scallop](https://github.com/Kingsford-Group/scallop) and
[CLASS2](http://ccb.jhu.edu/people/florea/research/CLASS2).
Here we provide scripts to download datasets, run the three methods, evaluated the
predicted transcripts, and reproduce the results and figures in the manuscript (under review).

The pipeline involves in the followint four steps:

1. Download necessary datasets (`data` directory).
2. Download and/or compile necessary programs (`programs` directory).
3. Run the methods to produce results (`results` directory).
4. Summarize results and produce figures (`plots` directory).

# Datasets
We compare the four methods on three datasets, namely **HEK293T**, **Mouse-Fibroblast**, and **ENCODE10**. 
Besides, we also need the annotation files for evaluation purposes.
In directory `data`, we provide metadata for these datasets, and also provide scripts to download them.

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

## Annotations
For **HEK293T** and **ENCODE10** datasets, we use human annotation database as reference;
for **Mouse-Fibroblast** dataset, we use the mouse annotation database as reference.
Use the following script in `data` to download annotations and c:
```
./download_index.annotation.sh
```
The downloaded files will appear under `data/human` and 'data/mouse'.


# Programs

Our experiments involve the following four programs:

Program | Version | Description
------------ | ------------ | ------------ 
[Scallop2](https://github.com/Shao-Group/Scallop2) | v1.1.1 | Transcript assembler
[StringTie2](https://ccb.jhu.edu/software/stringtie/) | v2.1.7 | Transcript assembler
[Scallop](https://github.com/Kingsford-Group/scallop) | v0.10.5 | Transcript assembler
[CLASS2](http://ccb.jhu.edu/people/florea/research/CLASS2) | v.2.1.7 | Transcript assembler
[gffcompare](http://ccb.jhu.edu/software/stringtie/gff.shtml) | v0.9.9c | Evaluate assembled transcripts
[gtfcuff](https://github.com/Kingsford-Group/rnaseqtools) |  | RNA-seq tool

You need to download and/or complile them,
and then link them to `programs` directory.
Make sure that the program names are in lower cases (i.e., `scallop2`, `stringtie2`, `scallop`, and `gffcompare`)
in `programs` directory.


# Run the Methods

Once the datasets and programs are all available, use the following scripts in `results`
to run the methods assemblers on the datasets:
```
./run.HEK293T.sh
./run.Mouse-Fibroblast.sh
./run.ENCODE10.sh
```
In each of these three scripts, you can modify it to run different
methods (Scallop2, StringTie2, Scallop, and CLASS2), and to run
with different minimum coverage threshold. You can also modify the scripts to specify
how many CPU cores you want to use to run the jobs in parallel.


# Analysis Results and Reproduce Figures

Once the results have been generated, one can use the following scripts in `plots` to reproduce the figures:
```
./build.figures.sh
```
You may need to install Python packages `matplotlib` and `numpy`.
The figrues will appear under `plots/HEK293T/figure`, `plots/Mouse-Fibroblast/figure` and `plots/ENCODE10/figure`.
