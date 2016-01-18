import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument("--input", type=str)
parser.add_argument("--flag", type = int)
	

args = parser.parse_args()
print(args.accumulate(args.integers))