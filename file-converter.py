import markdown
import sys
import os
import argparse

def validate(path):
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"ファイルが見つかりません: {path}")
    return path

def change_mark(input_file, output_file):
    contents = ''

    with open(input_file) as i:
        contents = i.read()
    
    html_body = markdown.markdown(contents)

    with open(output_file, 'w') as o:
        o.write(html_body)

def main():
    args = sys.argv[1:]

    if len(args) < 2:
        print("引数の値が不正：python3 change_markdown.py [command] [input_text.md] [output_text.html]")
        sys.exit(1)
    
    validate(sys.argv[0])

    command = sys.argv[1]
    input_file = sys.argv[2]
    output_file = sys.argv[3]

    if command == 'markdown':
        change_mark(input_file, output_file)
    else:
        print("Invalid command or arguments.")
        sys.exit(1)


if __name__ == "__main__":
    main()