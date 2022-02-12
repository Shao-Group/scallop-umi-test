# Step 1 : Download and Link Tools

Our experiments involve the following ten tools.
\*Note\*: Tools are not downloaded automatically.
Users need to separately download all neccessary tools and link them to the folder `programs` before running any scripts.

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

Make sure tools can be called by the following path:
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

Please make sure all necessary tools have been separately downloaded and linked to the folder `programs` before running experiments.

