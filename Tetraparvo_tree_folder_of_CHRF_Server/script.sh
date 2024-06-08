home="/home/chrf/Tetraparvo_tree/"
path="/home/chrf/Tetraparvo_tree/Assembly/"
bwa index -p $home\/ref $home\/ref.fa
bwa_index=/home/chrf/Tetraparvo_tree/ref.fa

mkdir -p $home\/SAM $home\/BCF $home\/consensus $home\/Renamed

for file in $path\/*
do
	name=$(basename ${file} |cut -d . -f 1,2)
	echo $name
	#minimap2 -ax asm5 $home\/ref.fa $home\/Assembly/${name}.fasta> $home\/SAM/${name}.sam
	cat $file | seqkit replace -p .+ -r "contig_{nr}" > $home\/Renamed/$name
	bwa mem $home\/ref $home\/Renamed/$name > $home\/SAM/${name}.sam
	samtools view -ubS --threads 12 $home\/SAM/${name}.sam > $home\/SAM/$name\.bam
	samtools sort --threads 12 $home\/SAM/$name\.bam -o $home\/SAM/$name\.sorted.bam
	samtools index -@ 12 $home\/SAM/$name\.sorted.bam
	samtools mpileup -d 1000 -t DP -t SP -ugBf $home\/ref.fa $home\/SAM/$name\.sorted.bam | bcftools call -cv --threads 12 | bcftools view -v snps --threads 12 > $home\/BCF/$name\.raw.vcf
	grep -c -v "#" $home\/BCF/$name\.raw.vcf

	echo '# Generate consensus sequence.'
	cp $home\/BCF/$name\.raw.vcf $home\/BCF/$name\.raw_1.vcf
	bgzip --threads 12 $home\/BCF/$name\.raw_1.vcf
	bcftools index --threads 12 $home\/BCF/$name\.raw_1.vcf.gz
	bcftools consensus -f $home\/ref.fa $home\/BCF/$name\.raw_1.vcf.gz > $home\/consensus/${name}.fasta
	sed -i -e "s/>.*/>${name}/" $home\/consensus/${name}.fasta
done

mkdir $home\/SNPsites $home\/Phylogeny
cat $home\/consensus/*.fasta > $home\/SNPsites/All_Hprv4_consensus.fasta
grep -c ">" $home\/SNPsites/All_Hprv4_consensus.fasta
snp-sites -pc -o $home\/Phylogeny/All_Hprv4_consensus.phylip $home\/SNPsites/All_Hprv4_consensus.fasta
head -1 $home\/Phylogeny/All_Hprv4_consensus.phylip

cd $home\/Phylogeny/
mkdir $home\/Phylogeny/raxml

#iqtree -s All_Hprv4_consensus.phylip -st DNA -o MH215556.1 -m MF

# raxml-ng for tree building (best tree and bootstrap at the same time)
raxml-ng --seed 1206 --all --msa All_Hprv4_consensus.phylip --model TPM3+F+G4 --bs-trees 1000 --brlen scaled --prefix All_Hprv4 --extra thread-pin --outgroup MH215556.1 --threads 90 --force --redo

raxml-ng --support --tree All_Hprv4.raxml.bestTree --bs-trees All_Hprv4.raxml.bootstraps
xsx
















# Compute the best topology ("RAxML_bestTree" file):
time(raxmlHPC-PTHREADS-AVX -p 1206 -s All_Hprv4_consensus.phylip -m GTRGAMMA -o MH215556.1 -T 12 -n All_Hprv4.bestTree)
# Compute 100 bootstraps to assess tree structure ( "RAxML_bootstrap" file):
time(raxmlHPC-PTHREADS-AVX -p 1206 -x 4221 -s All_Hprv4_consensus.phylip -N 1000 -m GTRGAMMA -T 92 -o MH215556.1 -n All_Hprv4.bsSupport)
# Compute final tree: (with RAxML_bestTree & RAxML_bootstrap)
time(raxmlHPC-PTHREADS-AVX -p 1206 -m GTRGAMMA -f b -t RAxML_bestTree.All_Hprv4.bestTree -z RAxML_bootstrap.All_Hprv4.bsSupport -o MH215556.1 -n All_Hprv4.bestTree.bsSupport)





