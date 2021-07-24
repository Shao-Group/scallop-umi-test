#!/bin/bash

dir=`pwd`
result=$dir/../results/Mouse-Fibroblast_results
data=$dir/Mouse-Fibroblast

#=============================
# collect results
#=============================
if [ "A" == "A" ];then
	mkdir -p $data
        cd $result
        for t in scallop2 stringtie2 scallop class2;
        do
		cd $result/$t
		for((i=1;i<=369;i++));
                do
			less $i.$t | awk '{print $5}' | sed -n '6p' >> $t.numTranscripts.results
                        less $i.$t | awk '{print $3}' | sed -n '19p' >> $t.numMatchTranscripts.results
                        grep "Maximum resident set size" $i.$t.time | awk '{print $6}' >> $t.memory.results
                        grep "User time" $i.$t.time | awk '{print $4}' >> $t.usrtime.results
                        grep "System time" $i.$t.time | awk '{print $4}' >> $t.systime.results

                done
		mkdir -p $data/$t
		mv *.results $data/$t
        done
fi
