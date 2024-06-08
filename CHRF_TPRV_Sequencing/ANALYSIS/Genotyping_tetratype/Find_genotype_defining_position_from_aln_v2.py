#!/usr/bin/env python
'''
Author: Arif Mohammad Tanmoy (arif.tanmoy@chrfbd.org)

'''
import numpy as np
from Bio import SeqIO
from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='VCF to Gene mutations.')
	commands.add_argument('--allele', type=str, required=True, help='Allele file in fasta format (Required).')
	commands.add_argument('--geno', type=str, required=True, help='Gentoype data (Required).')
	commands.add_argument('--pos', type=str, required=True, help='Complete allele position data (Required).')
	commands.add_argument('--ref', type=str, required=True, help='Reference in genbank format (Required).')
	commands.add_argument('--output', type=str, required=False, default='Genotype_Specific_Alleles.txt', help='Location and name for output file.')
	return commands.parse_args()
args = parse_args()

genodata = open(args.geno, 'r')
pos_file = open(args.pos, 'r')
ref_genbank = SeqIO.parse(open(args.ref,"r"), 'genbank')
result = open(args.output, 'w')
result.write('Clade\tNo_Uniq_Allele\tUniq_allele_POS\tUniq_allele\tNo_Uniq_CDS_allele\tUniq_CDS_allele_POS\tUniq_CDS_allele\tUniq_CDS_allele_locus\n')

clades = ["1", "2", "3"]

## MLST loci
mlst_loci = ['thrA', 'aroC', 'hisD', 'sucA', 'purE', 'dnaN', 'hemD']
mlst_start = [376, 552321, 887875, 2081181, 2270911, 3820149, 3918200]
mlst_end = [2838, 553406, 889179, 2083982, 2271420, 3821249, 3918895]


# Convert string to list
def Convert_string_to_list(string): 
	list1 = []
	list1[:0] = string
	return list1


# Extact sequence
def seq_extractor_by_query(fastafile, query):
	idd, seq, outseq = [], [], []
	for rec in SeqIO.parse(open(fastafile,"r"), 'fasta'):
		idd.append(str(rec.id))
		seq.append(str(rec.seq))
	for i in range(0, len(query)):
		if (query[i]) in idd:
			j = idd.index(str(query[i]))
			seq_list = Convert_string_to_list(str(seq[j]))
			outseq.append(seq_list)
		else:
			print "Cannot find the following query:\n"+str(query[i])
	return outseq


# Substract
def subtract(list1, list2): 
	list3 = [x for x in list1 if x not in list2]
	return list3


# Check if POS are in CDS or a MLST loci
def check_if_POS_in_a_loci(pos_list, pos_allele, start, end, tag):
	in_loci, in_locus, allele = [], [], []
	for i in range(0, len(pos_list)):
		for j in range(0, len(start)):
			if (start[j] <= int(pos_list[i]) <= end[j]):
				in_loci.append(pos_list[i])
				allele.append(pos_allele[i])
				in_locus.append(tag[j])
	return in_loci, in_locus, allele


# Take position data in a list
position = []
for line in pos_file:
	position.append(line.rstrip())
pos_num = len(position)


## Open and parse genbank file
cds_start, cds_end, cds_loci = [], [], []
for rec in ref_genbank:
	for x in range(0, len(rec.features)):
		if rec.features[x].type == 'CDS':	# Sorting out only CDS sequences
			# Discard any CDS with join-ed sequence
			if str(rec.features[x].location).find('join') == -1:	# This script is not equipped to find mutations in join-ed CDS 
				locat = str(rec.features[x].location).replace('<','').replace('>','').split(']')[0].replace('[','')	# However, we will consider mutations in pseudo/truncated/frame-shifted genes. 
				cds_start.append(int(locat.split(':')[0]))
				cds_end.append((int(locat.split(':')[1])))
				cds_loci.append(''.join(rec.features[x].qualifiers['locus_tag']))
			else:
				not_print = '\n# This script cannot parse join-ed CDS. Such loci in your Genbank file are:\n#Locus_tags\t#Location\n'+str(rec.features[x].qualifiers['locus_tag'])+'\t'+str(rec.features[x].location)+'\n'


print 'Clade\tNo_Uniq_Allele\tNo_Uniq_allele_CDS'

## Start by genotype data
idd, geno= [], []
# generate all id list
for line in genodata:
	idd.append(line.split('\t')[0])
	geno.append(line.split('\t')[1])
	# generate clade-wise id list
for i in range(0, len(clades)):
	geno_idd, geno_uniq = [], []
	for j in range(0, len(geno)):
		if geno[j].startswith(str(clades[i])):
			geno_idd.append(idd[j])
	# generate clade-wise other id list
	other_idd = subtract(idd, geno_idd)	
	
	# generate clade-wise geno_id and other_id fasta file
	geno_fasta = np.array(seq_extractor_by_query(args.allele, geno_idd))
	other_fasta = np.array(seq_extractor_by_query(args.allele, other_idd))

	# find the common conserved pos for geno_idd
	geno_uniq_allele, geno_uniq_pos= [], []
	for k in range(0, len(position)):
		col = geno_fasta[:, k]
		col_uniq = list(set(col))
		if len(col_uniq) == 1:
			other_col_uniq = list(set(other_fasta[:, k]))
			if str(col_uniq[0]) not in other_col_uniq:
				geno_uniq.append(k)
				geno_uniq_allele.append(str(col_uniq[0]))
				geno_uniq_pos.append(position[k])
	
	## check if any specific POS is from the MLST loci
	geno_specific_POS_mlst_tags = check_if_POS_in_a_loci(geno_uniq_pos, geno_uniq_allele, mlst_start, mlst_end, mlst_loci)
	geno_specific_POS_mlst = geno_specific_POS_mlst_tags[0]
	geno_specific_POS_mlst_loci = geno_specific_POS_mlst_tags[1]
	geno_specific_POS_mlst_allele = geno_specific_POS_mlst_tags[2]
	
	## check if any specific POS is from CDS
	geno_specific_POS_cds_tags = check_if_POS_in_a_loci(geno_uniq_pos, geno_uniq_allele, cds_start, cds_end, cds_loci)
	geno_specific_POS_cds = geno_specific_POS_cds_tags[0]
	geno_specific_POS_cds_loci = geno_specific_POS_cds_tags[1]
	geno_specific_POS_cds_allele = geno_specific_POS_cds_tags[2]
	
	result.write("%s\t%i\t%s\t%s\t%i\t%s\t%s\t%s\n" % (str(clades[i]), len(geno_uniq), (','.join(geno_uniq_pos)), (','.join(geno_uniq_allele)), len(geno_specific_POS_cds), (','.join(geno_specific_POS_cds)), (','.join(geno_specific_POS_cds_allele)), (','.join(geno_specific_POS_cds_loci))))
	
	print "%s\t%i\t%i" % (str(clades[i]), len(geno_uniq), len(geno_specific_POS_cds))


