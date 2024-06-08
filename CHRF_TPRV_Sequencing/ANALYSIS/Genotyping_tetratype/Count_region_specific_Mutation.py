#!/bin/env python2.7

# Written by - Arif Mohammad Tanmoy
# This script was used to analyze the O2-antigen synthesis region of Salmonella Paratyphi A in DOI: (TO-DO).

import os
from optparse import OptionParser
from more_itertools import locate

def main():
	usage = "usage: %prog [options]"
	parser = OptionParser(usage=usage)
	parser.add_option("-r", "--reg", action="store", dest="region", help="Region, colon-separated.", default=True)
	parser.add_option("-d", "--dir", action="store", dest="directory", help="Folder with VCF files.", default=True)
	parser.add_option("-e", "--ext", action="store", dest="file_extension", help="Extension of the VCF files.", default=True)
	parser.add_option("-o", "--output", action="store", dest="output", help="output file", default="Mutation_Frequency.list")
	return parser.parse_args()
(options, args) = main()

## Open files and folders
start,end = str(options.region).split(':')
folder = str(options.directory)
extension = str(options.file_extension)
output = open(options.output, 'w')

# Generate a list of VCF filenames
alist = os.listdir(folder)
vcffiles = []
for i in range(0, len(alist)):
	if str(alist[i]).endswith(extension):
		 vcffiles.append(folder+str(alist[i]))

# Gather all SNP details in all isolates in the target region
pos, snp = [], []
for i in range(0, len(vcffiles)):
	for line in open(str(vcffiles[i]), 'r'):
		if not line.startswith('#'):
			rec = line.split('\t')
			if int(end) >= int(rec[1]) >= int(start): 
				pos.append(rec[1])
				snp.append(rec[3]+'-'+rec[4])
# Check if both the lists have the same length! (They have to)
if len(pos) == len(snp):
	list_OK = 1
else:
	list_OK = 0

# Make a unique list of all SNP positions
uniq_pos = list(set(pos))

# Now, Let's count the Mutations
for i in range(0, len(uniq_pos)):
	pos_num = pos.count(uniq_pos[i])	# Count the position

	if list_OK == 1:	# Check if snp and pos list lengths are the same

		if pos_num == 1:	# if SNP count is 1
			pos_loc = pos.index(uniq_pos[i])
			mut = snp[pos_loc]
			print str(uniq_pos[i])+'\t'+mut+'\t'+str(pos_num)
			output.write(str(uniq_pos[i])+'\t'+mut+'\t'+str(pos_num)+'\n')

		else:	# if SNP count is more than 1
			pos_loc = list(locate(pos, lambda x: x == uniq_pos[i]))
			pos_snps = []

			for k in range(0, len(pos_loc)):
				pos_snps.append(snp[pos_loc[k]])	
			pos_snps_num = len(pos_snps)
			pos_snps_uniq = list(set(pos_snps))

			if len(pos_snps_uniq) == 1:	# if each SNP count is 1
				print str(uniq_pos[i])+'\t'+str(pos_snps_uniq[0])+'\t'+str(pos_snps_num)
				output.write(str(uniq_pos[i])+'\t'+str(pos_snps_uniq[0])+'\t'+str(pos_snps_num)+'\n')

			else:	# if each SNP count is more than 1
				for m in range(0, len(pos_snps_uniq)):
					pos_snps_uniq_num = pos_snps.count(pos_snps_uniq[m])
					print str(uniq_pos[i])+'\t'+str(pos_snps_uniq[m])+'\t'+str(pos_snps_uniq_num)
					output.write(str(uniq_pos[i])+'\t'+str(pos_snps_uniq[m])+'\t'+str(pos_snps_uniq_num)+'\n')
output.close()
