#!/bin/bash
dir=`pwd`
result=$dir/../results/HEK293T_results
data=$dir/HEK293T
gtfcuff=$dir/../programs/gtfcuff
gffcompare=$dir/../programs/gffcompare
salmon=$dir/../programs/salmon
bedtools=$dir/../programs/bedtools

#=============================
# collect results
#=============================
if [ "A" == "A" ];then
	mkdir -p $data
        cd $result
        for t in scallop2 stringtie2 scallop class2;
        do
		cd $result/$t
		for((i=1;i<=192;i++));
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
        for((i=1;i<=192;i++));
	do
                for t in scallop2 stringtie2 scallop class2;
                do
                                $gtfcuff roc $result/$t/$i.$t.$i.$t.gtf.tmap 235227 cov > $data/$t/$i.$t.roc
                                $gtfcuff roc $result/$t/$i.$t.me.$i.$t.gtf.tmap 210237 cov > $data/$t/$i.$t.me.roc

                                cd $data/$t

                                less $i.$t.roc | awk '{print $10}' > $i.$t.roc-cor
                                less $i.$t.roc | awk '{print $16}' > $i.$t.roc-pre
                                less $i.$t.me.roc | awk '{print $10}' > $i.$t.me.roc-cor
                                less $i.$t.me.roc | awk '{print $16}' > $i.$t.me.roc-pre
                done
        done
fi

#=======================================
# collect results for quant and class
#=======================================
if [ "A" == "B" ];then
        qref=$dir/../data/human/quant/HEK293T
        cref=$dir/../data/human/class
        mkdir -p $qref

	index=$dir/../data/human/salmon.index
	fq=$dir/../data/HEK293T/fq
	bam=$dir/../results/HEK293T_index
	mkdir -p $fq
	cd $fq
	rm -rf bamtofq.jobs.list
	for((i=1;i<=192;i++));
        do
                script=$fq/$i.sh
                echo "$bedtools bamtofastq -i $bam/$i.bam -fq $fq/$i.end1.fq -fq2 $fq/$i.end2.fq" > $i.sh
                chmod +x $script
                echo $script >> bamtofq.jobs.list
        done
        cat bamtofq.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null

	quant=$qref/salmon_quant
        mkdir -p $quant
        cd $quant
        rm -rf quant.jobs.list
        for((i=1;i<=192;i++));
        do
                script=$quant/$i.sh
                echo "$salmon quant -i $index -l ISF -1 $fq/$i.end1.fq -2 $fq/$i.end2.fq --validateMappings -o $quant/$i.quant" > $i.sh
                chmod +x $script
                echo $script >> quant.jobs.list
        done
        cat quant.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null

	for((i=1;i<=192;i++));
        do
                cd $quant/$i.quant
                awk '{print $2,$3,$4,$5}' quant.sf > quant.sf.col25
                awk '{print $1}' quant.sf > quant.sf.col1
                sed -i -r 's/(.{15}).*/\1/' quant.sf.col1
                paste quant.sf.col1 quant.sf.col25 > quant.sf.mod
        done

	cd $qref
	tmap=$result/scallop2/1-100-0.001.scallop2.me.1-100-0.001.scallop2.gtf.tmap
        rm -rf subref.jobs.list
	for((i=1;i<=192;i++));
        do
                script=$qref/$i.sh
                echo "mkdir -p $i" > $script
                echo "cd $i" >> $script
                echo "$gtfcuff split-quant $tmap $quant/$i.quant/quant.sf.mod 0.1 $dir/../data/human/Homo_sapiens.GRCh38.104.gtf" >> $script
                chmod +x $script
                echo $script >> subref.jobs.list
        done
        cat subref.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null


        cd $result
        rm -rf qandc.jobs.list
	for((i=1;i<=192;i++));
        do
                for t in scallop2 stringtie2 scallop;
                do
                        num=50
                        if [ $t == "scallop2" ]; then
                                num=100
                        fi
                        script=$result/$t/$i.sh
                        echo "#!/bin/bash" > $script
			echo "cd $result/$t" >> $script
                        for n in low middle high;
                        do
                                echo "$gffcompare -r $qref/$i/$n.gtf -M -N -o $result/$t/$i.$n $result/$t/$i-$num-0.001.$t.gtf" >> $script
                        done
			echo "$gtfcuff split-class $i-$num-0.001.$t.me.$i-$num-0.001.$t.gtf.tmap $i-$num-0.001.$t.gtf $i" >> $script
                        for n in 2-3 4-6 7;
                        do
                                echo "$gffcompare -r $cref/$n.gtf -M -N -o $result/$t/$i.$n $result/$t/$i.$n.split.gtf" >> $script
                        done
                        chmod +x $script
                        echo $script >> qandc.jobs.list
                done
        done
        cat qandc.jobs.list | xargs -L 1 -I CMD -P 32 bash -c CMD 1> /dev/null 2> /dev/null
fi

if [ "A" == "B" ];then
        for t in scallop2 stringtie2 scallop;
        do
                for((i=1;i<=192;i++));
                do
                        cd $result/$t
                        num=50
                        if [ $t == "scallop2" ]; then
                                num=100
                        fi
                        for n in 2-3 4-6 7 low middle high;
                        do
                                less $i.$n | awk '{print $9}' | sed -n '6p'| sed 's/(//' >> $data/$t/$n.numMultiTranscripts.results
                                less $i.$n | awk '{print $4}' | sed -n '18p' >> $data/$t/$n.numMatchIntronChain.results
                                total=`less $i.$n | awk '{print $9}' | sed -n '8p' | sed 's/(//' `
                                $gtfcuff roc $result/$t/$i.$n.$i-$num-0.001.$t.gtf.tmap $total cov > $data/$t/$i.$n.roc
                                less $data/$t/$i.$n.roc | awk '{print $10}' > $data/$t/$i.$n.roc-cor
                                less $data/$t/$i.$n.roc | awk '{print $16}' > $data/$t/$i.$n.roc-pre
                        done
                done
        done
fi


#=======================================
# collect results for varying parameters
#=======================================
if [ "A" == "B" ];then
        mkdir -p $data
        for t in scallop2 stringtie2 scallop;
        do
                mkdir -p $data/$t
                for p1 in 20 50 100 200;
                do
			for p2 in 0.5 1 1.5 2 2.5 3 3.5 4 4.5 5 6 7 8 9 10;
			do
                                prefix=$p1-$p2
                                for((i=1;i<=192;i++));
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

#=======================================
# collect codes for full-length
# and non-full-length transcripts
#=======================================
if [ "A" == "B" ];then
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
