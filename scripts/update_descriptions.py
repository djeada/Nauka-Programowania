#!/usr/bin/env python3
"""
Update file descriptions/comments from task markdown files.

This script reads task descriptions from markdown files and updates
the corresponding source code files with appropriate comments.

Supported file types:
- Python (.py) - uses triple-quoted strings or # comments
- C++ (.cpp) - uses /* */ or // comments
- Java (.java) - uses /* */ or // comments
- JavaScript (.js) - uses /* */ or // comments
- Rust (.rs) - uses /* */ or // comments
- Shell (.sh) - uses # comments
"""
from enum import Enum
from typing import Optional, Tuple
from dataclasses import dataclass
from pathlib import Path
import sys
import argparse


class CommentStyle(Enum):
    DELIMITED = 1
    LINE_BY_LINE = 2


@dataclass
class CommentInfo:
    delimited: Optional[Tuple[str, str]] = None
    line_by_line: Optional[str] = None


def localize_delimited_comment(content, start_delimiter, end_delimiter):
    """
    Locate and remove a delimited comment block from the content.
    
    Args:
        content: List of lines from the file
        start_delimiter: Starting delimiter (e.g., '/*')
        end_delimiter: Ending delimiter (e.g., '*/')
    
    Returns:
        Modified content with the comment removed, or None if not found
    """
    start_index = None
    end_index = None
    for i, line in enumerate(content):
        if start_index is not None and end_index is not None:
            break
        elif start_index is None and line.strip().startswith(start_delimiter):
            start_index = i
            if len(line.strip()) > len(start_delimiter) and line.strip()[
                len(start_delimiter) :
            ].endswith(end_delimiter):
                end_index = i
        elif start_index is not None and line.strip().endswith(end_delimiter):
            end_index = i

    if start_index is None or end_index is None:
        print(
            "Couldn't find the start and/or end delimiter. Please check the delimiters provided."
        )
        return None

    comment_content = content[start_index + 1 : end_index]
    del content[start_index : end_index + 1]
    return content


def localize_line_by_line_comment(content, delimiter):
    """
    Locate and remove line-by-line comments from the content.
    
    Args:
        content: List of lines from the file
        delimiter: Comment delimiter (e.g., '#', '//')
    
    Returns:
        Modified content with comments removed, or None if no changes
    """
    modified_content = []
    removing_comments = False
    for line in content:
        if not removing_comments and line.strip().startswith(delimiter):
            removing_comments = True
        elif removing_comments and not line.strip().startswith(delimiter):
            removing_comments = False

        if not removing_comments:
            modified_content.append(line)

    if len(modified_content) == len(content):
        return None
    else:
        return modified_content


def localize_top_comment(file_path, comment_style, start_delimiter, end_delimiter=None):
    """
    Locate and remove the top comment from a file.
    
    Args:
        file_path: Path to the file
        comment_style: CommentStyle enum (DELIMITED or LINE_BY_LINE)
        start_delimiter: Starting delimiter
        end_delimiter: Ending delimiter (for DELIMITED style)
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
    except UnicodeDecodeError:
        # Try with a different encoding if UTF-8 fails
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.readlines()

    if comment_style == CommentStyle.DELIMITED:
        modified_content = localize_delimited_comment(
            content, start_delimiter, end_delimiter
        )
    elif comment_style == CommentStyle.LINE_BY_LINE:
        modified_content = localize_line_by_line_comment(content, start_delimiter)

    if modified_content is not None:
        with open(file_path, "w", encoding="utf-8") as file:
            file.writelines(modified_content)
    else:
        print(f"  No top comment found in {file_path}")


def insert_delimited_comment(content, start_delimiter, end_delimiter, comment_content):
    """
    Insert a delimited comment at the beginning of the content.
    
    Args:
        content: List of lines from the file
        start_delimiter: Starting delimiter (e.g., '/*')
        end_delimiter: Ending delimiter (e.g., '*/')
        comment_content: The comment text to insert
    
    Returns:
        Modified content with the comment inserted
    """
    comment_lines = (
        [start_delimiter + "\n"]
        + [line + "\n" for line in comment_content.split("\n")]
        + [end_delimiter + "\n"]
    )
    return comment_lines + content


def insert_line_by_line_comment(content, delimiter, comment_content):
    """
    Insert line-by-line comments at the beginning of the content.
    
    Args:
        content: List of lines from the file
        delimiter: Comment delimiter (e.g., '#', '//')
        comment_content: The comment text to insert
    
    Returns:
        Modified content with comments inserted
    """
    comment_lines = [f"{delimiter} {line}\n" for line in comment_content.split("\n")]
    return comment_lines + content


def insert_top_comment(
    file_path, comment_style, start_delimiter, end_delimiter, comment_content
):
    """
    Insert a comment at the top of a file.
    
    Args:
        file_path: Path to the file
        comment_style: CommentStyle enum (DELIMITED or LINE_BY_LINE)
        start_delimiter: Starting delimiter
        end_delimiter: Ending delimiter (for DELIMITED style)
        comment_content: The comment text to insert
    """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.readlines()
    except UnicodeDecodeError:
        # Try with a different encoding if UTF-8 fails
        with open(file_path, "r", encoding="latin-1") as file:
            content = file.readlines()

    if comment_style == CommentStyle.DELIMITED:
        modified_content = insert_delimited_comment(
            content, start_delimiter, end_delimiter, comment_content + "\n"
        )
    elif comment_style == CommentStyle.LINE_BY_LINE:
        modified_content = insert_line_by_line_comment(
            content, start_delimiter, comment_content
        )

    with open(file_path, "w", encoding="utf-8") as file:
        file.writelines(modified_content)


def parse_tasks(input_str):
    """
    Parse tasks from a markdown file content.
    
    Args:
        input_str: Content of the markdown file
    
    Returns:
        Dictionary mapping task IDs to task content
    """
    # split the input string into lines
    lines = input_str.split("\n")

    # initialize a dictionary to hold the tasks
    tasks = {}

    # initialize variables to keep track of the current task
    task_num = 1
    task_lines = []
    in_task = False

    # loop over the lines and extract task information
    for line in lines:
        line_stripped = line.strip()

        # Check if this is a task header (e.g., "## Zadanie 1" or "## Zad1")
        if line_stripped.startswith("## Zad"):
            # add the current task to the dictionary
            if task_lines:
                task_id = "zad" + str(task_num)
                task_content = "\n".join(task_lines)
                tasks[task_id] = task_content
                task_num += 1
                task_lines = []
            
            in_task = True
            # Skip the task header itself, start collecting from next line
            continue

        # Collect lines that are part of a task
        if in_task and line_stripped:
            # Stop at the horizontal rule or next major section
            if line_stripped == "---" or line_stripped.startswith("# "):
                continue
            task_lines.append(line_stripped)

    # Don't forget the last task
    if task_lines:
        task_id = "zad" + str(task_num)
        task_content = "\n".join(task_lines)
        tasks[task_id] = task_content

    # return the dictionary of tasks
    return tasks


def main():
    parser = argparse.ArgumentParser(
        description="Update file descriptions/comments from task markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python update_descriptions.py zbior_zadan/ src/python/ py
  python update_descriptions.py zbior_zadan/ src/cpp/ cpp
  python update_descriptions.py zbior_zadan/ src/java/ java
        """
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help="Directory containing markdown files with task descriptions"
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help="Directory containing source code files to update"
    )
    parser.add_argument(
        "file_extension",
        type=str,
        help="File extension (e.g., py, cpp, java, js, rs, sh)"
    )

    args = parser.parse_args()

    # Validate input directory
    input_path = Path(args.input_dir)
    if not input_path.exists():
        print(f"Error: Input directory '{args.input_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)
    if not input_path.is_dir():
        print(f"Error: Input path '{args.input_dir}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    # Validate output directory
    output_path = Path(args.output_dir)
    if not output_path.exists():
        print(f"Error: Output directory '{args.output_dir}' does not exist.", file=sys.stderr)
        sys.exit(1)
    if not output_path.is_dir():
        print(f"Error: Output path '{args.output_dir}' is not a directory.", file=sys.stderr)
        sys.exit(1)

    file_extension = args.file_extension

    file_extension_comment_map = {
        "cpp": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "java": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "js": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "py": CommentInfo(delimited=('"""', '"""'), line_by_line="#"),
        "rs": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "sh": CommentInfo(line_by_line="#"),
    }

    # Validate file extension
    if file_extension not in file_extension_comment_map:
        print(f"Error: Unsupported file extension '{file_extension}'.", file=sys.stderr)
        print(f"Supported extensions: {', '.join(file_extension_comment_map.keys())}", file=sys.stderr)
        sys.exit(1)

    input_files = sorted(Path(args.input_dir).iterdir(), key=lambda p: str(p))
    output_dirs = sorted(Path(args.output_dir).iterdir(), key=lambda p: str(p))

    for input_file, output_dir in zip(input_files, output_dirs):
        # Skip non-markdown files
        if not input_file.is_file() or input_file.suffix != ".md":
            continue
        
        # Skip if output_dir is not a directory
        if not output_dir.is_dir():
            continue

        print(f"Processing: {input_file.name} -> {output_dir.name}")

        try:
            file_content = Path(input_file).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            # Try with a different encoding if UTF-8 fails
            try:
                file_content = Path(input_file).read_text(encoding="latin-1")
            except Exception as e:
                print(f"Error reading {input_file}: {e}", file=sys.stderr)
                continue
        except Exception as e:
            print(f"Error reading {input_file}: {e}", file=sys.stderr)
            continue

        tasks = parse_tasks(file_content)

        files = [
            file
            for file in Path(output_dir).iterdir()
            if file.is_file() and file.suffix == f".{file_extension}"
        ]

        if file_extension == "java":
            files = [
                file / "Main.java"
                for file in Path(output_dir).iterdir()
                if file.is_dir()
            ]
        files = sorted(files, key=lambda p: str(p))

        # Check if we have matching number of files and tasks
        if len(files) != len(tasks):
            print(f"Warning: Number of files ({len(files)}) does not match number of tasks ({len(tasks)}) in {input_file.name}", file=sys.stderr)

        for file, task in zip(files, tasks.values()):
            if not file.exists():
                print(f"Warning: File {file} does not exist, skipping.", file=sys.stderr)
                continue

            comment_info = file_extension_comment_map.get(file_extension)

            if comment_info is None:
                print(
                    f"No comment information found for file extension '{file_extension}'.",
                    file=sys.stderr
                )
                return

            if comment_info.delimited is not None:
                comment_style = CommentStyle.DELIMITED
                start_delimiter, end_delimiter = comment_info.delimited
            elif comment_info.line_by_line is not None:
                comment_style = CommentStyle.LINE_BY_LINE
                start_delimiter, end_delimiter = comment_info.line_by_line, None
            else:
                print("Invalid comment information.", file=sys.stderr)
                return

            try:
                # Localize the top comment and remove it from the file
                localize_top_comment(file, comment_style, start_delimiter, end_delimiter)

                # Insert a top comment at the beginning of the file
                insert_top_comment(file, comment_style, start_delimiter, end_delimiter, task)
                print(f"  Updated: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}", file=sys.stderr)
                continue


if __name__ == "__main__":
    main()
