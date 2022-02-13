#!/bin/bash
dir=`pwd`
data=$dir/../data/ENCODE10
ref=$dir/../data/human/Homo_sapiens.GRCh38.104.gtf
scallop2=$dir/../programs/scallop2
stringtie2=$dir/../programs/stringtie2
scallop=$dir/../programs/scallop
class2=$dir/../programs/class2/run_class.pl
gffcompare=$dir/../programs/gffcompare
result=$dir/ENCODE10_results

# step 0: check to-be-used tools/data
if [ "A" == "A" ];then
	echo "================================================================="
	echo "Check if to-be-used tools/data are properly linked..."
	echo "================================================================="
	if [ -e $data ];then
		echo -e "Dataset ENCODE10 found successfully!"
	else
		echo -e "Dataset ENCODE10 not found in directory 'data'.\nPlease follow the instructions in 'Step 2.2: Download Datasets' section 'ENCODE10' to properly download ENCODE10 data to the directory 'data'."
		echo -e "\nNote: ENCODE10 data are not downloaded automatically. Users need to download through the ENCODE10 doi link provided in the instructions, and store them properly in 'data/ENCODE10' directory before running experiments.\n"
    		exit 1
	fi
	
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

	echo -e "To-be-used tools/data found successfully!"

fi

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
		script=$result/scallop2/$i.scallop2.sh
		echo "cd $result/scallop2" > $script
                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/hisat.sort.bam -o $i.hisat.scallop2.gtf > $i.hisat.scallop2.log ; } 2> $i.hisat.scallop2.time" >> $script
		echo "{ /usr/bin/time -v $scallop2 -i $data/$i/star.sort.bam -o $i.star.scallop2.gtf > $i.star.scallop2.log ; } 2> $i.star.scallop2.time" >> $script
                echo "$gffcompare -r $ref -o $i.hisat.scallop2 $i.hisat.scallop2.gtf" >> $script
		echo "$gffcompare -r $ref -o $i.star.scallop2 $i.star.scallop2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.hisat.scallop2.me $i.hisat.scallop2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.star.scallop2.me $i.star.scallop2.gtf" >> $script

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
		script=$result/stringtie2/$i.stringtie2.sh
		echo "cd $result/stringtie2" > $script
                echo "{ /usr/bin/time -v $stringtie2 $data/$i/hisat.sort.bam -o $i.hisat.stringtie2.gtf > $i.hisat.stringtie2.log ; } 2> $i.hisat.stringtie2.time" >> $script
		echo "{ /usr/bin/time -v $stringtie2 $data/$i/star.sort.bam -o $i.star.stringtie2.gtf > $i.star.stringtie2.log ; } 2> $i.star.stringtie2.time" >> $script
                echo "$gffcompare -r $ref -o $i.hisat.stringtie2 $i.hisat.stringtie2.gtf" >> $script
		echo "$gffcompare -r $ref -o $i.star.stringtie2 $i.star.stringtie2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.hisat.stringtie2.me $i.hisat.stringtie2.gtf" >> $script
                echo "$gffcompare -r $ref -M -N -o $i.star.stringtie2.me $i.star.stringtie2.gtf" >> $script

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
		script=$result/scallop/$i.scallop.sh
                echo "cd $result/scallop" > $script
		echo "{ /usr/bin/time -v $scallop -i $data/$i/hisat.sort.bam -o $i.hisat.scallop.gtf > $i.hisat.scallop.log ; } 2> $i.hisat.scallop.time" >> $script
		echo "{ /usr/bin/time -v $scallop -i $data/$i/star.sort.bam -o $i.star.scallop.gtf > $i.star.scallop.log ; } 2> $i.star.scallop.time" >> $script
                echo "$gffcompare -r $ref -o $i.hisat.scallop $i.hisat.scallop.gtf" >> $script
		echo "$gffcompare -r $ref -o $i.star.scallop $i.star.scallop.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $i.hisat.scallop.me $i.hisat.scallop.gtf" >> $script
                echo "$gffcompare -r $ref -M -N -o $i.star.scallop.me $i.star.scallop.gtf" >> $script

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
                echo "{ /usr/bin/time -v perl $class2 -a $data/$i/hisat.sort.bam -o $result/class2/$i/$i.hisat.class2.gtf > $result/class2/$i/$i.hisat.class2.log ; } 2> $result/class2/$i/$i.hisat.class2.time" >> $script
                echo "$gffcompare -r $ref -o $result/class2/$i/$i.hisat.class2 $result/class2/$i/$i.hisat.class2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $result/class2/$i/$i.hisat.class2.me $result/class2/$i/$i.hisat.class2.gtf" >> $script
		echo "{ /usr/bin/time -v perl $class2 -a $data/$i/star.sort.bam -o $result/class2/$i/$i.star.class2.gtf > $result/class2/$i/$i.star.class2.log ; } 2> $result/class2/$i/$i.star.class2.time" >> $script
                echo "$gffcompare -r $ref -o $result/class2/$i/$i.star.class2 $result/class2/$i/$i.star.class2.gtf" >> $script
		echo "$gffcompare -r $ref -M -N -o $result/class2/$i/$i.star.class2.me $result/class2/$i/$i.star.class2.gtf" >> $script

                chmod +x $script
                echo $script >> $result/class2/class2.jobs.list

        done

        cat $result/class2/class2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

#============================================
# experiments for varying parameters
# p1: minimum gap
# p2: minimum coverage
#=============================================
# scallop2
if [ "A" == "B" ];then
        echo "running Scallop2..."
        cd $result/scallop2
	rm -rf scallop2.jobs.list
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
                for p1 in 20 50 100 200;
                do
                        for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        do
                                prefix=$i-$p1-$p2
                                script=$result/scallop2/$prefix.scallop2.sh
                                echo "cd $result/scallop2" > $script
                                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/hisat.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.hisat.scallop2.gtf > $prefix.hisat.scallop2.log ; } 2> $prefix.hisat.scallop2.time" >> $script
                                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/star.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.star.scallop2.gtf > $prefix.star.scallop2.log ; } 2> $prefix.star.scallop2.time" >> $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.hisat.scallop2.me $prefix.hisat.scallop2.gtf" >> $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.star.scallop2.me $prefix.star.scallop2.gtf" >> $script
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
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
                for p1 in 20 50 100 200;
                do
                        for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        do
                                prefix=$i-$p1-$p2
                                script=$result/stringtie2/$prefix.stringtie2.sh
                                echo "cd $result/stringtie2" > $script
                                echo "{ /usr/bin/time -v $stringtie2 -i $data/$i/hisat.sort.bam -g $p1 -c $p2 -o $prefix.hisat.stringtie2.gtf > $prefix.hisat.stringtie2.log ; } 2> $prefix.hisat.stringtie2.time" >> $script
                                echo "{ /usr/bin/time -v $stringtie2 -i $data/$i/star.sort.bam -g $p1 -c $p2 -o $prefix.star.stringtie2.gtf > $prefix.star.stringtie2.log ; } 2> $prefix.star.stringtie2.time" >> $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.hisat.stringtie2.me $prefix.hisat.stringtie2.gtf" >> $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.star.stringtie2.me $prefix.star.stringtie2.gtf" >> $script
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
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
                for p1 in 20 50 100 200;
                do
                        for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        do
                                prefix=$i-$p1-$p2
                                script=$result/scallop/$prefix.scallop.sh
                                echo "cd $result/scallop" > $script
                                echo "{ /usr/bin/time -v $scallop -i $data/$i/hisat.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.hisat.scallop.gtf > $prefix.hisat.scallop.log ; } 2> $prefix.hisat.scallop.time" >> $script
                                echo "{ /usr/bin/time -v $scallop -i $data/$i/star.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.star.scallop.gtf > $prefix.star.scallop.log ; } 2> $prefix.star.scallop.time" >> $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.hisat.scallop.me $prefix.hisat.scallop.gtf" >> $script
                                echo "$gffcompare -r $ref -M -N -o $prefix.star.scallop.me $prefix.star.scallop.gtf" >> $script
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
# scallop2
if [ "A" == "B" ];then
        echo "running Scallop2..."
        cd $result/scallop2
	rm -rf scallop2.jobs.list
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
                p1=100
                p2=0.001
                prefix=$i-$p1-$p2
                script=$result/scallop2/$prefix.scallop2.sh
                echo "cd $result/scallop2" > $script
                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/hisat.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.hisat.scallop2.gtf > $prefix.hisat.scallop2.log ; } 2> $prefix.hisat.scallop2.time" >> $script
                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/star.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.star.scallop2.gtf > $prefix.star.scallop2.log ; } 2> $prefix.star.scallop2.time" >> $script
                echo "$gffcompare -r $ref -M -N -o $prefix.hisat.scallop2.me $prefix.hisat.scallop2.gtf" >> $script
                echo "$gffcompare -r $ref -M -N -o $prefix.star.scallop2.me $prefix.star.scallop2.gtf" >> $script
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
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
                p1=50
                p2=0.001
                prefix=$i-$p1-$p2
                script=$result/stringtie2/$prefix.stringtie2.sh
                echo "cd $result/stringtie2" > $script
                echo "{ /usr/bin/time -v $stringtie2 -i $data/$i/hisat.sort.bam -g $p1 -c $p2 -o $prefix.hisat.stringtie2.gtf > $prefix.hisat.stringtie2.log ; } 2> $prefix.hisat.stringtie2.time" >> $script
                echo "{ /usr/bin/time -v $stringtie2 -i $data/$i/star.sort.bam -g $p1 -c $p2 -o $prefix.star.stringtie2.gtf > $prefix.star.stringtie2.log ; } 2> $prefix.star.stringtie2.time" >> $script
                echo "$gffcompare -r $ref -M -N -o $prefix.hisat.stringtie2.me $prefix.hisat.stringtie2.gtf" >> $script
                echo "$gffcompare -r $ref -M -N -o $prefix.star.stringtie2.me $prefix.star.stringtie2.gtf" >> $script
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
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
                p1=50
                p2=0.001
                prefix=$i-$p1-$p2
                script=$result/scallop/$prefix.scallop.sh
                echo "cd $result/scallop" > $script
                echo "{ /usr/bin/time -v $scallop -i $data/$i/hisat.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.hisat.scallop.gtf > $prefix.hisat.scallop.log ; } 2> $prefix.hisat.scallop.time" >> $script
                echo "{ /usr/bin/time -v $scallop -i $data/$i/star.sort.bam --min_bundle_gap $p1 --min_transcript_coverage $p2 -o $prefix.star.scallop.gtf > $prefix.star.scallop.log ; } 2> $prefix.star.scallop.time" >> $script
                echo "$gffcompare -r $ref -M -N -o $prefix.hisat.scallop.me $prefix.hisat.scallop.gtf" >> $script
                echo "$gffcompare -r $ref -M -N -o $prefix.star.scallop.me $prefix.star.scallop.gtf" >> $script
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
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
        do
                prefix=$i
                script=$result/scallop2/$prefix.scallop2.sh
                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/hisat.sort.bam -f $prefix.hisat.non-full.scallop2.gtf -o $prefix.hisat.scallop2.gtf > $prefix.hisat.scallop2.log ; } 2> $prefix.hisat.scallop2.time" >> $script
                echo "{ /usr/bin/time -v $scallop2 -i $data/$i/star.sort.bam -f $prefix.star.non-full.scallop2.gtf -o $prefix.star.scallop2.gtf > $prefix.star.scallop2.log ; } 2> $prefix.star.scallop2.time" >> $script
                echo "gffcompare -r $ref -M -N -o $prefix.hisat.scallop2.me $prefix.hisat.scallop2.gtf" >> $script
                echo "gffcompare -r $ref -M -N -o $prefix.star.scallop2.me $prefix.star.scallop2.gtf" >> $script
		echo "gffcompare -r $ref -M -N -o $prefix.hisat.non-full.scallop2.me $prefix.hisat.non-full.scallop2.gtf" >> $script
                echo "gffcompare -r $ref -M -N -o $prefix.star.non-full.scallop2.me $prefix.star.non-full.scallop2.gtf" >> $script
                chmod +x $script
                echo $script >> scallop2.jobs.list
        done
        cat scallop2.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi


