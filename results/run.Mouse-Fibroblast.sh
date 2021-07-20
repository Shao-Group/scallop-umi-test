#!/bin/bash

dir=`pwd`
data=$dir/../data/Mouse-Fibroblast/zUMIs_output/demultiplexed
index=$dir/Mouse-Fibroblast_index
ref=$dir/../data/mouse/Mus_musculus.GRCm39.104.gtf
scallop2=$dir/../programs/scallop2
stringtie2=$dir/../programs/stringtie2
scallop=$dir/../programs/scallop
class2=$dir/../programs/class2/run_class.pl
gffcomapre=$dir/../programs/gffcompare
result=$dir/Mouse-Fibroblast_results

#============================================
# create index for cells
#=============================================
if [ "A" == "A" ];then
        mkdir -p $index
        cd $index

        i=1
        for k in `ls $data/*.demx.bam`
        do
                if [ "$i" -lt "500"  ]; then
                        ln -sf $data/$k .
                        echo "cell #$i: $k" >> index.list
                        mv $k $i.bam
                        let i++
                fi
        done
fi

#============================================
# assembly and evaluate
#=============================================
# Scallop2
if [ "A" == "A" ];then
        echo "running Scallop2..."
        mkdir -p $result/scallop2
        cd $result/scallop2

	# generate job list
	rm -rf scallop2.jobs.list

        for((i=1;i<=369;i++));
        do
		script=$i.scallop2.sh
                echo "{ /usr/bin/time -v $scallop2 -i $index/$i.bam -o $i.scallop2.gtf > $i.scallop2.log ; } 2> $i.scallop2.time" > $script
                echo "$gffcompare -r $ref -o $i.scallop2 $i.scallop2.gtf" >> $script

		chmod +x $script
		echo $script >> scallop2.jobs.list

        done

	cat scallop2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi


# StringTie2
if [ "A" == "A" ];then
        echo "running StringTie2..."
        mkdir -p $result/stringtie2
        cd $result/stringtie2

	# generate job list
	rm -rf stringtie2.jobs.list

        for((i=1;i<=369;i++));
        do
		script=$i.stringtie2.sh
                echo "{ /usr/bin/time -v $stringtie2 $index/$i.bam -o $i.stringtie2.gtf > $i.stringtie2.log ; } 2> $i.stringtie2.time" > $script
                echo "$gffcompare -r $ref -o $i.stringtie2 $i.stringtie2.gtf" >> $script

		chmod +x $script
		echo $script >> stringtie2.jobs.list

        done

	cat stringtie2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

# Scallop
if [ "A" == "A" ];then
        echo "running Scallop..."
        mkdir -p $result/scallop
        cd $result/scallop

	# generate job list
	rm -rf scallop.jobs.list

        for((i=1;i<=369;i++));
        do
		script=$result/$i.scallop.sh
                echo "{ /usr/bin/time -v $scallop -i $index/$i.bam -o $i.scallop.gtf > $i.scallop.log ; } 2> $i.scallop.time" > $script
                echo "$gffcompare -r $ref -o $i.scallop $i.scallop.gtf" >> $script

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

        for((i=1;i<=369;i++));
        do
                script=$result/$i.class2.sh
                echo "{ /usr/bin/time -v perl $class2 -a $index/$i.bam -o $i.class2.gtf > $i.class2.log ; } 2> $i.class2.time" > $script
                echo "$gffcompare -r $ref -o $i.class2 $i.class2.gtf" >> $script

                chmod +x $script
                echo $script >> class2.jobs.list
        done

        cat class2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi
