#!/usr/bin/env python3
import sys
import os

if len(sys.argv) < 3:
    sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

if not os.path.exists(input_file):
    sys.stderr.write(f"Missing {input_file}\n")
    sys.exit(1)
try:
    with open(input_file, 'r') as markdown_file:
        content = markdown_file.read()

    with open(output_file, 'w') as html_file:
        html_file.write(content)

    sys.exit(0)

except Exception as e:
    sys.stderr.write(f"Error: {e}\n")
    sys.exit(1)
