#!/usr/bin/python3
import argparse
import random
print("""
  ____ _ _     _               _     _       __  __       _             
 / ___(_) |__ | |__   ___ _ __(_)___| |__   |  \/  | __ _| | _____ _ __ 
| |  _| | '_ \| '_ \ / _ \ '__| / __| '_ \  | |\/| |/ _` | |/ / _ \ '__|
| |_| | | |_) | |_) |  __/ |  | \__ \ | | | | |  | | (_| |   <  __/ |   
 \____|_|_.__/|_.__/ \___|_|  |_|___/_| |_| |_|  |_|\__,_|_|\_\___|_|   
			By Rentix Productions                                                                       

""")

example_text = '''
python3 GibberishMaker.py -m 10 -l 100 -c abcdef12345ABCDE -o generated.txt
python3 GibberishMaker.py --max 5 --length 20 --outfile my2ndGib.txt
'''

parser = argparse.ArgumentParser(epilog=example_text)

parser.add_argument('--max', '-m', help='Set the maximumoccupancy120 characters.')
parser.add_argument('--length', '-l', help='Set the amount of gibberished words.')
parser.add_argument('--chars', '-c', help='Set chars')
parser.add_argument('--outfile', '-o', help='Set an output file')

args = parser.parse_args()

if args.max and args.length and args.chars and args.outfile:
	try:
		chars = str(args.chars)
		final = ''
		lis = []
		for i in range(0, int(args.length), 1):
			for i in range(0, int(args.max)):
				final += random.choice(chars)
			lis.append(final)
			final = ''

		file = open(str(args.outfile), 'w')
		for line in lis:
			file.write(line)
			file.write('\n')
		file.close()
		print ('Your file is ready! -> %s' % args.outfile)
	except:
		print("I am so sorry but I don't speak Uketerianburg...\nCheck your syntax.\nMake sure that you insert numbers where you should and letters where you need.")
else:
	print('Something is missing... Check your syntax or use -h for examples.')
