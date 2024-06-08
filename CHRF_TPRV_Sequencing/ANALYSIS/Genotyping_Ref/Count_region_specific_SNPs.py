#!/bin/env python2.7

# Written by - Arif Mohammad Tanmoy
# This script was used to analyze the O2-antigen synthesis region of Salmonella Paratyphi A in DOI: (TO-DO).

import os
from optparse import OptionParser

def main():
	usage = "usage: %prog [options]"
	parser = OptionParser(usage=usage)
	parser.add_option("-s", "--snp", action="store", dest="snpall", help="All_SNP position file.", default=True)
	parser.add_option("-r", "--reg", action="store", dest="region", help="Region, colon-separated.", default=True)
	parser.add_option("-d", "--dir", action="store", dest="directory", help="Folder with SNP position files.", default=True)
	parser.add_option("-e", "--ext", action="store", dest="file_extension", help="Extension of the position files.", default=True)
	parser.add_option("-o", "--output", action="store", dest="output", help="output file", default="Genotype_specific_SNPs.list")
	return parser.parse_args()
(options, args) = main()

## Open files
all_pos = open(options.snpall, 'r')
start,end = str(options.region).split(':')
folder = str(options.directory)
extension = str(options.file_extension)
output = open(options.output, 'w')

# Take all SNPs in the target region in a list
reg_loc = []
for line in open(options.snpall, 'r'):
	loc = line.rstrip()
	if int(loc) >= int(start) and int(loc) <= int(end):
		reg_loc.append(loc)
#print reg_loc

# Generate a list of position filenames
alist = os.listdir(folder)
posfiles = []
for i in range(0, len(alist)):
	if str(alist[i]).endswith(extension):
		 posfiles.append(folder+str(alist[i]))
#print len(posfiles)

# Now Let's count the positions
for i in range(int(start),int(end)):
	n=0
	for j in range(0, len(posfiles)):
		for line in open(str(posfiles[j]), 'r'):
			rec = line.rstrip()
			if str(i) == rec:
				n=n+1
			else:
				n=n+0
	print str(i)+'\t'+str(n)
	output.write(str(i)+'\t'+str(n)+'\n')
output.close()

