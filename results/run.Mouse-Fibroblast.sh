#!/bin/bash
dir=`pwd`
data=$dir/../data/Mouse-Fibroblast/zUMIs_output/demultiplexed
index=$dir/Mouse-Fibroblast_index
ref=$dir/../data/mouse/Mus_musculus.GRCm39.104.gtf
scallop2=$dir/../programs/scallop2
stringtie2=$dir/../programs/stringtie2
scallop=$dir/../programs/scallop
class2=$dir/../programs/class2/run_class.pl
gffcompare=$dir/../programs/gffcompare
result=$dir/Mouse-Fibroblast_results

# step 0: check to-be-used tools
if [ "A" == "A" ];then
	echo "================================================================="
	echo "Check if to-be-used tools are properly linked..."
	echo "================================================================="
	if [ -e $scallop2 ];then
		echo -e "Tool Scallop2 found successfully!"
	else
		echo -e "Tool Scallop2 not found in directory 'programs'.\nPlease follow the instructions in 'Step 1: Download and Link Tools' to properly download and link all necessary tools to the directory 'programs'."
		echo -e "\nNote: Tools are not downloaded automatically. Users need to download and/or compile all required tools, and then link them to 'programs' directory before running experiments.\n"
    		exit 1
	fi

	if [ -e $stringtie2 ];then
                echo -e "Tool StringTie2 found successfully!"
        else
                echo -e "Tool StringTie2 not found in directory 'programs'.\nPlease follow the instructions in 'Step 1: Download and Link Tools' to properly download and link all necessary tools to the directory 'programs'."
                echo -e "\nNote: Tools are not downloaded automatically. Users need to download and/or compile all required tools, and then link them to 'programs' directory before running experiments.\n"
                exit 1
        fi

        if [ -e $scallop ];then
                echo -e "Tool Scallop found successfully!"
        else
                echo -e "Tool Scallop not found in directory 'programs'.\nPlease follow the instructions in 'Step 1: Download and Link Tools' to properly download and link all necessary tools to the directory 'programs'."
                echo -e "\nNote: Tools are not downloaded automatically. Users need to download and/or compile all required tools, and then link them to 'programs' directory before running experiments.\n"
                exit 1
        fi
        
	if [ -e $class2 ];then
                echo -e "Tool CLASS2 found successfully!"
        else
                echo -e "Tool CLASS2 not found in directory 'programs'.\nPlease follow the instructions in 'Step 1: Download and Link Tools' to properly download and link all necessary tools to the directory 'programs'."
                echo -e "\nNote: Tools are not downloaded automatically. Users need to download and/or compile all required tools, and then link them to 'programs' directory before running experiments.\n"
                exit 1
        fi
        
	if [ -e $gffcompare ];then
                echo -e "Tool gffcompare found successfully!"
        else
                echo -e "Tool gffcompare not found in directory 'programs'.\nPlease follow the instructions in 'Step 1: Download and Link Tools' to properly download and link all necessary tools to the directory 'programs'."
                echo -e "\nNote: Tools are not downloaded automatically. Users need to download and/or compile all required tools, and then link them to 'programs' directory before running experiments.\n"
                exit 1
        fi

	echo -e "To-be-used tools found successfully!"

fi

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
		script=$result/scallop2/$i.scallop2.sh
                echo "{ /usr/bin/time -v $scallop2 -i $index/$i.bam -o $i.scallop2.gtf > $i.scallop2.log ; } 2> $i.scallop2.time" > $script
                echo "$gffcompare -r $ref -o $i.scallop2 $i.scallop2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.scallop2.me $i.scallop2.gtf" >> $script

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
		script=$result/stringtie2/$i.stringtie2.sh
                echo "{ /usr/bin/time -v $stringtie2 $index/$i.bam -o $i.stringtie2.gtf > $i.stringtie2.log ; } 2> $i.stringtie2.time" > $script
                echo "$gffcompare -r $ref -o $i.stringtie2 $i.stringtie2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.stringtie2.me $i.stringtie2.gtf" >> $script

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
		script=$result/scallop/$i.scallop.sh
                echo "{ /usr/bin/time -v $scallop -i $index/$i.bam --min_num_hits_in_bundle 5 -o $i.scallop.gtf > $i.scallop.log ; } 2> $i.scallop.time" > $script
                echo "$gffcompare -r $ref -o $i.scallop $i.scallop.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.scallop.me $i.scallop.gtf" >> $script

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
                script=$result/class2/$i.class2.sh
                echo "{ /usr/bin/time -v perl $class2 -a $index/$i.bam -o $i.class2.gtf > $i.class2.log ; } 2> $i.class2.time" > $script
                echo "$gffcompare -r $ref -o $i.class2 $i.class2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.class2.me $i.class2.gtf" >> $script

                chmod +x $script
                echo $script >> class2.jobs.list
        done

        cat class2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

#============================================
# experiments for varying parameters
# p1: minimum gap
# p2: minimum coverage
#=============================================
# Scallop2
if [ "A" == "B" ];then
        echo "running Scallop2..."
        cd $result/scallop2
	rm -rf scallop2.jobs.list
        for((i=1;i<=369;i++));
        do
                for p1 in 20 50 100 200;
                do
                        for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        do
                                prefix=$i-$p1-$p2
                                script=$result/scallop2/$prefix.scallop2.sh
                                echo "{ /usr/bin/time -v $scallop2 -i $index/$i.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.scallop2.gtf > $prefix.scallop2.log ; } 2> $prefix.scallop2.time" > $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.scallop2.me $prefix.scallop2.gtf" >> $script
                                chmod +x $script
                                echo $script >> scallop2.jobs.list
                        done
                done
        done
	cat scallop2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

# stringtie2
if [ "A" == "B" ];then
        echo "running stringtie2..."
        cd $result/stringtie2
        rm -rf stringtie2.jobs.list
        for((i=1;i<=369;i++));
        do
                for p1 in 20 50 100 200;
                do
                        for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        do
                                prefix=$i-$p1-$p2
                                script=$result/stringtie2/$prefix.stringtie2.sh
                                echo "{ /usr/bin/time -v $stringtie2 -i $index/$i.bam -g $p1 -c $p2 -o $prefix.stringtie2.gtf > $prefix.stringtie2.log ; } 2> $prefix.stringtie2.time" > $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.stringtie2.me $prefix.stringtie2.gtf" >> $script
                                chmod +x $script
                                echo $script >> stringtie2.jobs.list
                        done
                done
        done
        cat stringtie2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

# scallop
if [ "A" == "B" ];then
        echo "running scallop..."
        cd $result/scallop
        rm -rf scallop.jobs.list
        for((i=1;i<=369;i++));
        do
                for p1 in 20 50 100 200;
                do
                        for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        do
                                prefix=$i-$p1-$p2
                                script=$result/scallop/$prefix.scallop.sh
                                echo "{ /usr/bin/time -v $scallop -i $index/$i.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.scallop.gtf > $prefix.scallop.log ; } 2> $prefix.scallop.time" > $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.scallop.me $prefix.scallop.gtf" >> $script
                                chmod +x $script
                                echo $script >> scallop.jobs.list
                        done
                done
        done
        cat scallop.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

#============================================
# experiments for quant and class
# p1: minimum gap, using default value
# p2: minimum coverage, using 0.001
#=============================================
# Scallop2
if [ "A" == "B" ];then
        echo "running Scallop2..."
        cd $result/scallop2
        rm -rf scallop2.jobs.list
        for((i=1;i<369;i++));
        do
                p1=100
                p2=0.001
                prefix=$i-$p1-$p2
                script=$result/scallop2/$prefix.scallop2.sh
                echo "{ /usr/bin/time -v $scallop2 -i $index/$i.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.scallop2.gtf > $prefix.scallop2.log ; } 2> $prefix.scallop2.time" > $script
                echo "$gffcompare -r $ref -M -N -o $prefix.scallop2.me $prefix.scallop2.gtf" >> $script
                chmod +x $script
                echo $script >> scallop2.jobs.list
        done
        cat scallop2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

# stringtie2
if [ "A" == "B" ];then
        echo "running stringtie2..."
        cd $result/stringtie2
        rm -rf stringtie2.jobs.list
        for((i=1;i<=369;i++));
        do
                p1=50
                p2=0.001
                prefix=$i-$p1-$p2
                script=$result/stringtie2/$prefix.stringtie2.sh
                echo "{ /usr/bin/time -v $stringtie2 -i $index/$i.bam -g $p1 -c $p2 -o $prefix.stringtie2.gtf > $prefix.stringtie2.log ; } 2> $prefix.stringtie2.time" > $script
                echo "$gffcompare -r $ref -M -N -o $prefix.stringtie2.me $prefix.stringtie2.gtf" >> $script
                chmod +x $script
                echo $script >> stringtie2.jobs.list
        done
        cat stringtie2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

# scallop
if [ "A" == "B" ];then
        echo "running scallop..."
        cd $result/scallop
        rm -rf scallop.jobs.list
        for((i=1;i<369;i++));
        do
                p1=100
                p2=0.001
                prefix=$i-$p1-$p2
                script=$result/scallop/$prefix.scallop.sh
                echo "{ /usr/bin/time -v $scallop -i $index/$i.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.scallop.gtf > $prefix.scallop.log ; } 2> $prefix.scallop.time" > $script
                echo "$gffcompare -r $ref -M -N -o $prefix.scallop.me $prefix.scallop.gtf" >> $script
                chmod +x $script
                echo $script >> scallop.jobs.list
        done
        cat scallop.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

#============================================
# full-length and non-full-length
# transcripts assembled by Scallop2
#============================================
# Scallop2
if [ "A" == "B" ];then
        cd $result/scallop2
        rm -rf scallop2.jobs.list
        for((i=1;i<=369;i++));
        do
                script=$result/scallop2/$i.scallop2.sh
                echo "{ /usr/bin/time -v $scallop2 -i $index/$i.bam -f $i-non-full-scallop2.gtf -o $i-scallop2.gtf > scallop2.log ; } 2> scallop2.time" > $script
                echo "gffcompare -r $ref -M -N -o $i-non-full-scallop2.me $i-non-full-scallop2.gtf" >> $script
                echo "gffcompare -r $ref -M -N -o $i-scallop2.me $i-scallop2.gtf" >> $script
                chmod +x $script
                echo $script >> scallop2.jobs.list
        done
        cat scallop2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi
