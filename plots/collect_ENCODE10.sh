#!/bin/bash

dir=`pwd`
result=$dir/../data/ENCODE10_results
data=$dir/ENCODE10
gtfcuff=$dir/../programs/gtfcuff

#=============================
# collect results
#=============================
if [ "A" == "A" ];then
	mkdir -p $data
        cd $result
        for t in scallop2 stringtie2 scallop;
        do
		cd $result/$t
		rm *.results
                for c in hisat star;
                do
                        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
                        do
                                less $i.$c.$t | awk '{print $5}' | sed -n '6p' >> $c.$t.numTranscripts.results
                                less $i.$c.$t | awk '{print $3}' | sed -n '19p' >> $c.$t.numMatchTranscripts.results
                                grep "Maximum resident set size" $i.$c.$t.time | awk '{print $6}' >> $c.$t.memory.results
                                grep "User time" $i.$c.$t.time | awk '{print $4}' >> $c.$t.usrtime.results
                                grep "System time" $i.$c.$t.time | awk '{print $4}' >> $c.$t.systime.results

			done
                done
		mkdir -p $data/$t
		mv *.results $data/$t
        done
fi

if [ "A" == "A" ];then
        mkdir -p $data
        for t in class2;
        do
		mkdir -p $data/$t
		cd $data/$t
		rm *.results
                for c in hisat star;
                do
                        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
                        do
                                less $result/$i/$i.$c.$t | awk '{print $5}' | sed -n '6p' >> $c.$t.numTranscripts.results
                                less $result/$i/$i.$c.$t | awk '{print $3}' | sed -n '19p' >> $c.$t.numMatchTranscripts.results
                                grep "Maximum resident set size" $result/$i/$i.$c.$t.time | awk '{print $6}' >> $c.$t.memory.results
                                grep "User time" $result/$i/$i.$c.$t.time | awk '{print $4}' >> $c.$t.usrtime.results
                                grep "System time" $result/$i/$i.$c.$t.time | awk '{print $4}' >> $c.$t.systime.results

                        done
                done
        done
fi

if [ "A" == "A" ];then

	for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
	do
        	for t in hisat star;
        	do
			$gtfcuff roc $result/scallop2/$i.$t.scallop2.$i.$t.scallop2.gtf.tmap 235227 cov > $data/scallop2/$i.$t.roc
                	cd $data/scallop2

			less $i.$t.roc | awk '{print $10}' > $i.$t.roc-cor
                	less $i.$t.roc | awk '{print $16}' > $i.$t.roc-pre
		done
	done
fi
