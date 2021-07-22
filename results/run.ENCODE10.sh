#!/bin/bash

dir=`pwd`
data=$dir/../data/ENCODE10
ref=$dir/../data/human/Homo_sapiens.GRCh38.104.gtf
scallop2=$dir/../programs/scallop2
stringtie2=$dir/../programs/stringtie2
scallop=$dir/../programs/scallop
class2=$dir/../programs/class2/run_class.pl
gffcomapre=$dir/../programs/gffcompare
result=$dir/ENCODE10_results

#============================================
# assembly and evaluate
#=============================================
# scallop2
if [ "A" == "A" ];then
        echo "running Scallop2..."
        mkdir -p $result/scallop2
        cd $result/scallop2

	# generate job list
	rm -rf scallop2.jobs.list

        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
		script=$i.scallop2.sh
                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/hisat.sort.bam -o $i.hisat.scallop2.gtf > $i.hisat.scallop2.log ; } 2> $i.hisat.scallop2.time" > $script
		echo "{ /usr/bin/time -v $scallop2 -i $data/$i/star.sort.bam -o $i.star.scallop2.gtf > $i.star.scallop2.log ; } 2> $i.star.scallop2.time" >> $script
                echo "$gffcompare -r $ref -o $i.hisat.scallop2 $i.hisat.scallop2.gtf" >> $script
		echo "$gffcompare -r $ref -o $i.star.scallop2 $i.star.scallop2.gtf" >> $script

		chmod +x $script
		echo $script >> scallop2.jobs.list

        done

	cat scallop2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi


# stringtie2
if [ "A" == "A" ];then
        echo "running StringTie2..."
        mkdir -p $result/stringtie2
        cd $result/stringtie2

	# generate job list
	rm -rf stringtie2.jobs.list

        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
		script=$i.stringtie2.sh
                echo "{ /usr/bin/time -v $stringtie2 $data/$i/hisat.sort.bam -o $i.hisat.stringtie2.gtf > $i.hisat.stringtie2.log ; } 2> $i.hisat.stringtie2.time" > $script
		echo "{ /usr/bin/time -v $stringtie2 $data/$i/star.sort.bam -o $i.star.stringtie2.gtf > $i.star.stringtie2.log ; } 2> $i.star.stringtie2.time" >> $script
                echo "$gffcompare -r $ref -o $i.hisat.stringtie2 $i.hisat.stringtie2.gtf" >> $script
		echo "$gffcompare -r $ref -o $i.star.stringtie2 $i.star.stringtie2.gtf" >> $script

		chmod +x $script
		echo $script >> stringtie2.jobs.list

        done

	cat stringtie2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

# scallop
if [ "A" == "A" ];then
        echo "running Scallop..."
        mkdir -p $result/scallop
        cd $result/scallop

	# generate job list
	rm -rf scallop.jobs.list

        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
		script=$i.scallop.sh
                echo "{ /usr/bin/time -v $scallop -i $data/$i/hisat.sort.bam -o $i.hisat.scallop.gtf > $i.hisat.scallop.log ; } 2> $i.hisat.scallop.time" > $script
		echo "{ /usr/bin/time -v $scallop -i $data/$i/star.sort.bam -o $i.star.scallop.gtf > $i.star.scallop.log ; } 2> $i.star.scallop.time" >> $script
                echo "$gffcompare -r $ref -o $i.hisat.scallop $i.hisat.scallop.gtf" >> $script
		echo "$gffcompare -r $ref -o $i.star.scallop $i.star.scallop.gtf" >> $script

		chmod +x $script
		echo $script >> scallop.jobs.list

        done

	cat scallop.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi


# CLASS2
if [ "A" == "A" ];then
        echo "running CLASS2..."
        mkdir -p $result/class2
        cd $result/class2

        # generate job list
        rm -rf class2.jobs.list

	for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
		mkdir -p $result/class2/$i
		cd $result/class2/$i

                script=$result/class2/$i/$i.class2.sh
		echo "cd $result/class2/$i" > $script
                echo "{ /usr/bin/time -v perl $class2 -a $data/$i/hisat.sort.bam -o $i.hisat.class2.gtf > $i.hisat.class2.log ; } 2> $i.hisat.class2.time" >> $script
                echo "$gffcompare -r $ref -o $i.hisat.class2 $i.hisat.class2.gtf" >> $script
		echo "{ /usr/bin/time -v perl $class2 -a $data/$i/star.sort.bam -o $i.star.class2.gtf > $i.star.class2.log ; } 2> $i.star.class2.time" >> $script
                echo "$gffcompare -r $ref -o $i.star.class2 $i.star.class2.gtf" >> $script

                chmod +x $script
                echo $script >> $result/class2/class2.jobs.list

        done

        cat $result/class.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

