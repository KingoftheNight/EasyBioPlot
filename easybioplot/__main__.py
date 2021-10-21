import sys
import os
import argparse
now_path = os.getcwd()
file_path = os.path.dirname(__file__)
sys.path.append(file_path)
try:
    from . import Weblogo as iweb
    from . import Reduce as ired
except:
    import Weblogo as iweb
    import Reduce as ired

def parse_weblogo(args):
	print('\nDrawing Weblogo...')
	if args.folder:
		if args.label:
			iweb.weblogo_multy(folder=args.folder[0], out=args.output[0], tp=args.type[0], label=args.label[0].split(','))
		else:
			iweb.weblogo_multy(folder=args.folder[0], out=args.output[0], tp=args.type[0])
	else:
		iweb.weblogo(file=args.document[0], out=args.output[0], tp=args.type[0])
	print('\nWeblogo has been saved at: ' + args.output[0])

def parse_reduce(args):
    print('\nDrawing ReduceSequence...')
    if args.sequence:
        ired.reduce(sq=args.sequence[0], out=args.output[0], raa=args.raacode[0])
    else:
        ired.reduce(file=args.document[0], out=args.output[0], raa=args.raacode[0])
    print('\nReduceSequence has been saved')

# main
def easybioplot():
    parser = argparse.ArgumentParser(description='A tool for drawing pictures of biology',
                                     fromfile_prefix_chars='@', conflict_handler='resolve')
    subparsers = parser.add_subparsers(help='EasyBioPlot help')
    # weblogo
    parser_wo = subparsers.add_parser('weblogo', add_help=False, help='weblogo')
    parser_wo.add_argument('-f', '--folder', nargs=1, help='Input a folder of FASTA files with sequences of equal length')
    parser_wo.add_argument('-d', '--document', nargs=1, help='Input a FASTA file with sequences of equal length')
    parser_wo.add_argument('-o', '--output', nargs=1, help='output file path')
    parser_wo.add_argument('-tp', '--type', nargs=1, help='file type')
    parser_wo.add_argument('-l', '--label', nargs=1, help='labels for mulity FASTA files')
    parser_wo.set_defaults(func=parse_weblogo)
    # reduce
    parser_re = subparsers.add_parser('reduce', add_help=False, help='reduce')
    parser_re.add_argument('-sq', '--sequence', nargs=1, help='Input a sequence')
    parser_re.add_argument('-d', '--document', nargs=1, help='Input a FASTA file with single sequence')
    parser_re.add_argument('-o', '--output', nargs=1, help='output file path')
    parser_re.add_argument('-r', '--raacode', nargs=1, help='reduce amino acid code')
    parser_re.set_defaults(func=parse_reduce)

    args = parser.parse_args()
    try:
        args.func(args)
    except AttributeError:
        pass

# main
if __name__ == '__main__':
    easybioplot()
