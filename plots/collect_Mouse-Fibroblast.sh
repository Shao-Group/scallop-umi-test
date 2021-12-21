#!/bin/bash

dir=`pwd`
result=$dir/../results/Mouse-Fibroblast_results
data=$dir/Mouse-Fibroblast
gtfcuff=$dir/../programs/gtfcuff

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
			less $i.$t.me | awk '{print $9}' | sed -n '6p'| sed 's/(//' >> $t.numMultiTranscripts.results
                        less $i.$t.me | awk '{print $4}' | sed -n '18p' >> $t.numMatchIntronChain.results
                        grep "Maximum resident set size" $i.$t.time | awk '{print $6}' >> $t.memory.results
                        grep "User time" $i.$t.time | awk '{print $4}' >> $t.usrtime.results
                        grep "System time" $i.$t.time | awk '{print $4}' >> $t.systime.results

                done
		mkdir -p $data/$t
		mv *.results $data/$t
        done
fi

if [ "A" == "A" ];then
        for((i=1;i<=369;i++));
        do
                for t in scallop2 stringtie2 scallop class2;
                do
                                $gtfcuff roc $result/$t/$i.$t.$i.$t.gtf.tmap 141532 cov > $data/$t/$i.$t.roc
                                $gtfcuff roc $result/$t/$i.$t.me.$i.$t.gtf.tmap 114718 cov > $data/$t/$i.$t.me.roc

                                cd $data/$t

                                less $i.$t.roc | awk '{print $10}' > $i.$t.roc-cor
                                less $i.$t.roc | awk '{print $16}' > $i.$t.roc-pre
                                less $i.$t.me.roc | awk '{print $10}' > $i.$t.me.roc-cor
                                less $i.$t.me.roc | awk '{print $16}' > $i.$t.me.roc-pre
                done
        done
fi

#=======================================
# collect results for varying parameters
#=======================================
if [ "A" == "A" ];then
        mkdir -p $data
        for t in scallop2 stringtie2 scallop;
        do
                mkdir -p $data/$t
                for p1 in 20 50 100 200;
                do
                        for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        do
                                prefix=$p1-$p2
                                for((i=1;i<=369;i++));
                                do
                                        cd $result/$t
                                        less $i-$prefix.$t.me | awk '{print $9}' | sed -n '6p'| sed 's/(//' >> $prefix.$t.numMultiTranscripts.results
                                        less $i-$prefix.$t.me | awk '{print $4}' | sed -n '18p' >> $prefix.$t.numMatchIntronChain.results
                                        $gtfcuff roc $result/$t/$i-$prefix.$t.me.$i-$prefix.$t.gtf.tmap 210237 cov > $data/$t/$i.$prefix.$t.me.roc
                                        cd $data/$t
                                        less $i.$prefix.$t.me.roc | awk '{print $10}' > $i.$prefix.$t.me.roc-cor
                                        less $i.$prefix.$t.me.roc | awk '{print $16}' > $i.$prefix.$t.me.roc-pre
                                done
                                mv $result/$t/*.results $data/$t
                        done
                done
	done
fi
