#!/bin/bash

dir=`pwd`
result=$dir/../data/HEK293T_results
data=$dir/HEK293T

#=============================
# collect results
#=============================
if [ "A" == "A" ];then
	mkdir -p $data
        cd $result
        for t in scallop2 stringtie2 scallop class2;
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
