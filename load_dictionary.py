import sys


def load(file):
    try:
        with open(file) as in_file:
            loaded_text = in_file.read().strip().split('\n')
            loaded_text = [text.lower() for text in loaded_text]
            return loaded_text
    except:
        print("{}\nERROR opening {}. Terminating program.".format(
            e, file), file=sys.stderr)
        sys.exit(1)
