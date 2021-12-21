#=======================================
# collect codes for full-length
# and non-full-length transcripts
#=======================================
if [ "A" == "A" ];then
        mkdir -p $data/scallop2/scallop2-full
        cd $data/scallop2/scallop2-full
        rm -rf *.codes
        for((i=1;i<=192;i++));
        do
                ln -sf $result/scallop2/$i-scallop2.me.$i-scallop2.gtf.tmap .
                file=$i-scallop2.me.$i-scallop2.gtf.tmap
                sed -i '1d' $file
                less $file | awk '{print $3}' >> $i.codes
        done

        mkdir -p $data/scallop2/scallop2-non-full
        cd $data/scallop2/scallop2-non-full
        rm -rf *.codes
        for((i=1;i<=192;i++));
        do
                ln -sf $result/scallop2/$i-non-full-scallop2.me.$i-non-full-scallop2.gtf.tmap .
                file=$i-non-full-scallop2.me.$i-non-full-scallop2.gtf.tmap
                sed -i '1d' $file
                less $file | awk '{print $3}' >> $i.codes
        done
fi
#=======================================
# collect codes for full-length
# and non-full-length transcripts
#=======================================
if [ "A" == "A" ];then
        mkdir -p $data/scallop2/scallop2-full
        cd $data/scallop2/scallop2-full
        rm -rf *.codes
        for((i=1;i<=192;i++));
        do
                ln -sf $result/scallop2/$i-scallop2.me.$i-scallop2.gtf.tmap .
                file=$i-scallop2.me.$i-scallop2.gtf.tmap
                sed -i '1d' $file
                less $file | awk '{print $3}' >> $i.codes
        done

        mkdir -p $data/scallop2/scallop2-non-full
        cd $data/scallop2/scallop2-non-full
        rm -rf *.codes
        for((i=1;i<=192;i++));
        do
                ln -sf $result/scallop2/$i-non-full-scallop2.me.$i-non-full-scallop2.gtf.tmap .
                file=$i-non-full-scallop2.me.$i-non-full-scallop2.gtf.tmap
                sed -i '1d' $file
                less $file | awk '{print $3}' >> $i.codes
        done
fi
#!/bin/bash
dir=`pwd`
result=$dir/../results/ENCODE10_results
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
                for c in hisat star;
                do
                        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
                        do
                                less $i.$c.$t | awk '{print $5}' | sed -n '6p' >> $c.$t.numTranscripts.results
                                less $i.$c.$t | awk '{print $3}' | sed -n '19p' >> $c.$t.numMatchTranscripts.results
				less $i.$c.$t.me | awk '{print $9}' | sed -n '6p'| sed 's/(//' >> $c.$t.numMultiTranscripts.results
                        	less $i.$c.$t.me | awk '{print $4}' | sed -n '18p' >> $c.$t.numMatchIntronChain.results
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
				less $result/$i/$i.$c.$t.me | awk '{print $9}' | sed -n '6p'| sed 's/(//' >> $c.$t.numMultiTranscripts.results
                                less $result/$i/$i.$c.$t.me | awk '{print $4}' | sed -n '18p' >> $c.$t.numMatchIntronChain.results
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
			for c in scallop2 stringtie2 scallop class2;
			do
				$gtfcuff roc $result/$c/$i.$t.$c.$i.$t.$c.gtf.tmap 235227 cov > $data/$c/$i.$t.roc
                                $gtfcuff roc $result/$c/$i.$t.$c.me.$i.$t.$c.gtf.tmap 210237 cov > $data/$c/$i.$t.me.roc

				cd $data/$c

				less $i.$t.roc | awk '{print $10}' > $i.$t.roc-cor
                		less $i.$t.roc | awk '{print $16}' > $i.$t.roc-pre
				less $i.$t.me.roc | awk '{print $10}' > $i.$t.me.roc-cor
                                less $i.$t.me.roc | awk '{print $16}' > $i.$t.me.roc-pre
			done
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
		for c in hisat star;
		do
                	for p1 in 20 50 100 200;
                	do
                        	for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
                        	do
                                	prefix=$p1-$p2
                                	for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
					do
                                        	cd $result/$t
						less $i-$prefix.$c.$t.me | awk '{print $9}' | sed -n '6p'| sed 's/(//' >> $prefix.$c.$t.numMultiTranscripts.results
                                                less $i-$prefix.$c.$t.me | awk '{print $4}' | sed -n '18p' >> $prefix.$c.$t.numMatchIntronChain.results
						$gtfcuff roc $result/$t/$i-$prefix.$c.$t.me.$i-$prefix.$c.$t.gtf.tmap 210237 cov > $data/$t/$i.$prefix.$c.$t.me.roc
						cd $data/$t
						less $i.$prefix.$c.$t.me.roc | awk '{print $10}' > $i.$prefix.$c.$t.me.roc-cor
                                                less $i.$prefix.$c.$t.me.roc | awk '{print $16}' > $i.$prefix.$c.$t.me.roc-pre
					done
                                done
                        done
                done
		mv $result/$t/*.results $data/$t
	done
fi

#=======================================
# collect codes for full-length
# and non-full-length transcripts
#=======================================
if [ "A" == "A" ];then
        mkdir -p $data/scallop2/scallop2-full
        cd $data/scallop2/scallop2-full
        rm -rf *.codes
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
	do
		for a in hisat star;
        	do
                	ln -sf $result/scallop2/$i.$a.scallop2.me.$i.$a.scallop2.gtf.tmap .
                	file=$i.$a.scallop2.me.$i.$a.scallop2.gtf.tmap
                	sed -i '1d' $file
                	less $file | awk '{print $3}' >> $i.codes
		done
        done

        mkdir -p $data/scallop2/scallop2-non-full
        cd $data/scallop2/scallop2-non-full
        rm -rf *.codes
        for i in SRR307903 SRR315323 SRR387661 SRR534307 SRR545695 SRR307911 SRR315334 SRR534291 SRR534319 SRR545723;
	do
		for a in hisat star;
		do
                	ln -sf $result/scallop2/$i.$a.non-full.scallop2.me.$i.$a.non-full.scallop2.gtf.tmap .
                	file=$i.$a.non-full.scallop2.me.$i.$a.non-full.scallop2.gtf.tmap
                	sed -i '1d' $file
                	less $file | awk '{print $3}' >> $i.codes
		done
        done
fi

