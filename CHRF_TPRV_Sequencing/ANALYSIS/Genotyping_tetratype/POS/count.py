from argparse import (ArgumentParser, FileType)

def parse_args():
	"Parse the input arguments, use '-h' for help"
	commands = ArgumentParser(description='Find Parv4 genotype from mapped VCF.')
	commands.add_argument('--uniq', type=str, required=True, help='Unique positions (Required).')
	commands.add_argument('--all', type=str, required=True, help='All positions (Required).')
	commands.add_argument('--target', type=int, required=True, help='target count number (Required).')
	commands.add_argument('--res', type=str, required=False, default='Count_results.txt', help='Location and name for output file.')
	return commands.parse_args()
args = parse_args()

#
unique, positions = [], []

for pos in open(args.all, 'r'):
	positions.append(pos.rstrip().strip('\n'))

for pos in open(args.uniq, 'r'):
	pos1 = pos.rstrip().strip('\n')
	count = positions.count(pos1)
	if count >= args.target:
		print(str(pos1) + '\t' + str(count))

