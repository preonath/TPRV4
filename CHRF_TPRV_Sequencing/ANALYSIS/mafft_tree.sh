home="/media/chrf/Home03/TPRV/TPRV_all/TPRV4/"
script="/home/chrf/WGS_Scripts/"

# Run mafft
cat $home\/Assembly_Cons/* > $home\/MAFFT/TPRV_57_merged.fa
grep -c ">" $home\/MAFFT/TPRV_57_merged.fa
sed -i -e 's/_TP4/ TP4/g' $home\/MAFFT/TPRV_57_merged.fa
sed -i -e 's/_L1_/ L1_/g' $home\/MAFFT/TPRV_57_merged.fa
cut -f 1 -d ' ' $home\/MAFFT/TPRV_57_merged.fa > $home\/MAFFT/tmp && mv $home\/MAFFT/tmp $home\/MAFFT/TPRV_57_merged.fa

mafft --maxiterate 1000 --localpair --thread 92 $home\/MAFFT/TPRV_57_merged.fa > $home\/MAFFT/TPRV_57_mafft.fa

echo "Convert to phylip"
python $script\/fasta2phylip.py -i  $home\/MAFFT/TPRV_57_mafft.fa -o  $home\/MAFFT/TPRV_57_mafft.phylip

mkdir -p $home\/MAFFT/raxml
cd $home\/MAFFT/

# Compute the best topology ("RAxML_bestTree" file):
time(raxmlHPC-PTHREADS-AVX -p 1501 -s TPRV_57_mafft.phylip -m GTRGAMMA -T 92 -o HQ113143 -n TPRV_57_mafft.bestTree)
# Compute 100 bootstraps to assess tree structure ( "RAxML_bootstrap" file):
time(raxmlHPC-PTHREADS-AVX -p 1501 -x 2023 -s TPRV_57_mafft.phylip -N 100 -m GTRGAMMA -T 92 -o HQ113143 -n TPRV_57_mafft.bsSupport)
# Compute final tree: (with RAxML_bestTree & RAxML_bootstrap)
time(raxmlHPC-PTHREADS-AVX -p 151 -m GTRGAMMA -f b -t RAxML_bestTree.TPRV_57_mafft.bestTree -T 4 -z RAxML_bootstrap.TPRV_57_mafft.bsSupport -o HQ113143 -n TPRV_57_mafft.bestTree.bsSupport)
cd
mv $home\/MAFFT/*TPRV_57_mafft* $home\/MAFFT/raxml/
cp $home\/MAFFT/raxml/RAxML_bipartitionsBranchLabels.* $home\/MAFFT/
cp $home\/MAFFT/RAxML_bipartitionsBranchLabels.TPRV_57_mafft.bestTree.bsSupport $home\/MAFFT/TPRV_57_mafft.bestTree.bsSupport.corrected


#-----------------------------------------------#
#		FOR SEQUENCES WITH NCBI-30				#
#-----------------------------------------------#
nhome="/media/chrf/Home03/TPRV/TPRV_all/TPRV4/MAFFT/CHRF57_NCBI30/"

# clean NCBI seqs
cut -f 1 -d ' ' $nhome\/TPRV_ncbi30.fa > $nhome\/tmp && mv $nhome\/tmp $nhome\/TPRV_ncbi30.fa

# Run mafft
cat $home\/MAFFT/TPRV_57_merged.fa $nhome\/TPRV_ncbi30.fa > $nhome\/TPRV_CHRF57_NCBI30.fa
grep -c ">" $nhome\/TPRV_CHRF57_NCBI30.fa

mafft --maxiterate 1000 --localpair --thread 92 $nhome\/TPRV_CHRF57_NCBI30.fa > $nhome\/TPRV_CHRF57_NCBI30_mafft.fa

echo "Convert to phylip"
python $script\/fasta2phylip.py -i  $nhome\/TPRV_CHRF57_NCBI30_mafft.fa -o $nhome\/TPRV_CHRF57_NCBI30_mafft.phylip

mkdir -p $nhome\/raxml
cd $nhome\/

# Compute the best topology ("RAxML_bestTree" file):
time(raxmlHPC-PTHREADS-AVX -p 1501 -s TPRV_CHRF57_NCBI30_mafft.phylip -m GTRGAMMA -T 92 -o HQ113143 -n TPRV_CHRF57_NCBI30_mafft.bestTree)
# Compute 100 bootstraps to assess tree structure ( "RAxML_bootstrap" file):
time(raxmlHPC-PTHREADS-AVX -p 1501 -x 2023 -s TPRV_CHRF57_NCBI30_mafft.phylip -N 100 -m GTRGAMMA -T 92 -o HQ113143 -n TPRV_CHRF57_NCBI30_mafft.bsSupport)
# Compute final tree: (with RAxML_bestTree & RAxML_bootstrap)
time(raxmlHPC-PTHREADS-AVX -p 151 -m GTRGAMMA -f b -t RAxML_bestTree.TPRV_CHRF57_NCBI30_mafft.bestTree -T 4 -z RAxML_bootstrap.TPRV_CHRF57_NCBI30_mafft.bsSupport -o HQ113143 -n TPRV_CHRF57_NCBI30_mafft.bestTree.bsSupport)
cd
mv $nhome\/*TPRV_CHRF57_NCBI30_mafft* $nhome\/raxml/
cp $nhome\/raxml/RAxML_bipartitionsBranchLabels.* $nhome\/
cp $nhome\/RAxML_bipartitionsBranchLabels.TPRV_CHRF57_NCBI30_mafft.bestTree.bsSupport $nhome\/TPRV_CHRF57_NCBI30_mafft.bestTree.bsSupport.corrected

