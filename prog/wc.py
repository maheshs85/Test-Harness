import argparse
import sys
def wc(text):
    character_count = len(text)
    word_count = len(text.split())
    line_count = len(text.splitlines())
    return (line_count, word_count, character_count)

def print_counts(file, char_count, word_count, line_count, args):
    print_text = ''
    if args.lines:
        print_text += f"       {line_count}"
    if args.words:
        print_text += f"       {word_count}"
    if args.characters:
        print_text += f"       {character_count}"
    print_text += f" {file}"
    print(print_text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Count characters, words, and lines in a text file.")
    parser.add_argument("files", nargs="*", help="List of text files to analyze (optional)")
    parser.add_argument("-l", "--lines", action="store_true", help="Count only lines")
    parser.add_argument("-w", "--words", action="store_true", help="Count only words")
    parser.add_argument("-c", "--characters", action="store_true", help="Count only characters")
    args = parser.parse_args()

    if args.files:
        total_characters = 0
        total_words = 0
        total_lines = 0
        for file in args.files:
            try:
                with open(file, 'r') as f:
                    text = f.read()
                    line_count, word_count, character_count = wc(text)

                    if not any([args.lines, args.words, args.characters]):
                        print(f"       {line_count}       {word_count}       {character_count} {file}")
                    else:
                        print_counts(file, character_count, word_count, line_count, args)

                    total_lines += line_count
                    total_words += word_count
                    total_characters += character_count
                    
            except FileNotFoundError:
                print(f"File '{file}' not found.")
                sys.exit(1)
            except Exception as e:
                print(f"An error occurred: {e}")
                sys.exit(1)

        if len(args.files) > 1:
            print(f"       {total_lines}       {total_words}      {total_characters} total")            
        sys.exit(0)
    else:
        text = sys.stdin.read()
        line_count, word_count, character_count = wc(text)
        print(f"      {line_count}      {word_count}     {character_count}")
        sys.exit(0)
