home="/media/asus/275dd380-2319-4638-bcdd-5f65b2b1d4b5/CHRF_Project_Data/CHRF_TPRV_Sequencing/ANALYSIS/Genotyping_Ref"

mkdir $home\/Genotype
for file in $home\/vcf/*.vcf
do
  name=`basename $file | cut -f 1 -d '.'`
  echo $name
  python $home\/Find_parv4_genotype.py --vcf $file --geno $home\/genotype_definition.txt --output $home\/Genotype/$name\.genotype
done
