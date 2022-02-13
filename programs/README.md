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
