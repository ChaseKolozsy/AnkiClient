#!/usr/bin/env python3
import sys
import re
import os

def extract_chapter_number(line):
    """
    Extracts the chapter number from a line containing a 'Chapter_X' tag.
    Assumes the tags are in the last tab-separated field.
    """
    try:
        fields = line.strip().split('\\t')
        if not fields:
            return None # Skip empty lines

        tags_field = fields[-1]
        # Look for 'Chapter_' followed by digits
        match = re.search(r'Chapter_(\d+)', tags_field)
        if match:
            return int(match.group(1))
    except Exception as e:
        print(f"Warning: Could not process line: {line.strip()}. Error: {e}", file=sys.stderr)
    return None # Return None if no Chapter tag is found or if error occurs

def sort_file_by_chapter(filepath):
    """
    Sorts the lines of a file based on the 'Chapter_X' tag numerically.
    Overwrites the original file with the sorted content.
    Preserves lines starting with '#'.
    """
    if not os.path.exists(filepath):
        print(f"Error: File not found: {filepath}", file=sys.stderr)
        sys.exit(1)

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading file {filepath}: {e}", file=sys.stderr)
        sys.exit(1)

    header_lines = [line for line in lines if line.startswith('#')]
    data_lines = [line for line in lines if not line.startswith('#') and line.strip()] # Exclude comments and empty lines

    # Store lines with their chapter numbers
    line_chapter_pairs = []
    for line in data_lines:
        chapter_num = extract_chapter_number(line)
        if chapter_num is not None:
            line_chapter_pairs.append((chapter_num, line))
        else:
            # Keep lines without a chapter tag, maybe append them at the end or beginning?
            # For now, let's append them at the end, unsorted relative to each other
            line_chapter_pairs.append((float('inf'), line)) # Assign infinity to sort them last

    # Sort based on chapter number
    line_chapter_pairs.sort(key=lambda x: x[0])

    # Prepare sorted lines for writing
    sorted_lines = header_lines + [line for chapter_num, line in line_chapter_pairs]

    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(sorted_lines)
        print(f"Successfully sorted {filepath} by chapter tag.")
    except Exception as e:
        print(f"Error writing sorted file {filepath}: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python sort_by_chapter_tag.py <filepath>")
        sys.exit(1)

    file_to_sort = sys.argv[1]
    sort_file_by_chapter(file_to_sort)