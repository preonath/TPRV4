home="/home/tanmoy/Genotyping_Ref/"

mkdir $home\/Genotype
for file in $home\/vcf/*.vcf
do
  name=`basename $file | cut -f 1 -d '.'`
  echo $name
  python $home\/Find_parv4_genotype.py --vcf $file --geno $home\/genotype_definition.txt --output $home\/Genotype/$name\.genotype
done
