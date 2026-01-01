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
from typing import Optional, Tuple, Dict, List
from dataclasses import dataclass
from pathlib import Path
import sys
import argparse
import re


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
    first_non_empty = None

    for i, line in enumerate(content):
        if line.strip():
            first_non_empty = i
            break

    if first_non_empty is None:
        return None

    if not content[first_non_empty].strip().startswith(start_delimiter):
        return None

    start_index = first_non_empty
    if len(content[start_index].strip()) > len(start_delimiter) and content[
        start_index
    ].strip().endswith(end_delimiter):
        end_index = start_index
    else:
        for i in range(start_index + 1, len(content)):
            if content[i].strip().endswith(end_delimiter):
                end_index = i
                break

    if start_index is None or end_index is None:
        print(
            "Couldn't find the start and/or end delimiter. Please check the delimiters provided."
        )
        return None

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
    if not content:
        return None

    index = 0
    if delimiter == "#" and content[0].startswith("#!"):
        index = 1

    while index < len(content) and not content[index].strip():
        index += 1

    start_index = index
    if index < len(content) and content[index].lstrip().startswith(delimiter):
        index += 1
        while index < len(content):
            if content[index].lstrip().startswith(delimiter):
                index += 1
                continue
            if not content[index].strip():
                index += 1
                continue
            break

    if index == start_index:
        return None

    return content[:start_index] + content[index:]


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


def create_stub_file(file_path: Path, file_extension: str) -> None:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if file_extension == "py":
        content = 'if __name__ == "__main__":\n    pass\n'
    elif file_extension == "cpp":
        content = "#include <iostream>\n\nint main() {\n    return 0;\n}\n"
    elif file_extension == "java":
        content = "public class Main {\n    public static void main(String[] args) {\n    }\n}\n"
    elif file_extension == "js":
        content = "function main() {\n}\n\nmain();\n"
    elif file_extension == "rs":
        content = "fn main() {}\n"
    elif file_extension == "sh":
        content = "main() {\n}\n\nmain \"$@\"\n"
    elif file_extension == "hs":
        content = "main :: IO ()\nmain = pure ()\n"
    else:
        content = ""
    file_path.write_text(content, encoding="utf-8")


def parse_tasks(input_str) -> Dict[str, List[str]]:
    """
    Parse tasks from a markdown file content.
    
    Args:
        input_str: Content of the markdown file
    
    Returns:
        Dictionary mapping task IDs to task content
    """
    lines = input_str.split("\n")
    tasks: Dict[str, List[str]] = {}

    task_header_re = re.compile(r"^##\s+(ZAD-\d{2})([A-Z])?(?:\s+[—-]\s*(.*))?$")
    current_key = None
    current_header = None
    current_lines: List[str] = []

    def flush_task():
        nonlocal current_key, current_header, current_lines
        if current_key is None or current_header is None:
            return
        body = "\n".join(current_lines).rstrip()
        part_text = current_header if not body else f"{current_header}\n{body}"
        tasks.setdefault(current_key, []).append(part_text)
        current_key = None
        current_header = None
        current_lines = []

    for line in lines:
        stripped = line.rstrip("\n")
        header_match = task_header_re.match(stripped.strip())
        if header_match:
            flush_task()
            base_id = header_match.group(1)
            letter = header_match.group(2) or ""
            title = header_match.group(3) or ""
            header_text = base_id + letter
            if title:
                header_text += f" — {title}"
            current_key = base_id
            current_header = header_text
            continue

        if current_key is not None:
            if stripped.strip() == "---":
                continue
            if stripped.lstrip().startswith("# "):
                continue
            current_lines.append(stripped)

    flush_task()
    return tasks


def update_descriptions(input_dir: str, output_dir: str, file_extension: str) -> None:
    # Validate input directory or file
    input_path = Path(input_dir)
    if not input_path.exists():
        print(f"Error: Input path '{input_dir}' does not exist.", file=sys.stderr)
        return

    # Validate output directory
    output_path = Path(output_dir)
    if not output_path.exists():
        print(f"Error: Output directory '{output_dir}' does not exist.", file=sys.stderr)
        return
    if not output_path.is_dir():
        print(f"Error: Output path '{output_dir}' is not a directory.", file=sys.stderr)
        return

    file_extension_comment_map = {
        "cpp": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "java": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "js": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "py": CommentInfo(delimited=('"""', '"""'), line_by_line="#"),
        "rs": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "sh": CommentInfo(line_by_line="#"),
        "hs": CommentInfo(delimited=("{-", "-}"), line_by_line="--"),
    }

    if file_extension not in file_extension_comment_map:
        print(f"Error: Unsupported file extension '{file_extension}'.", file=sys.stderr)
        print(
            f"Supported extensions: {', '.join(file_extension_comment_map.keys())}",
            file=sys.stderr,
        )
        return

    if input_path.is_dir():
        input_files = sorted(
            [
                p
                for p in input_path.iterdir()
                if p.is_file() and p.suffix == ".md" and p.name != "szablon.md"
            ],
            key=lambda p: str(p),
        )
    else:
        if input_path.suffix != ".md":
            print(f"Error: Input file '{input_dir}' is not a markdown file.", file=sys.stderr)
            return
        input_files = [input_path]

    output_dirs = {p.name: p for p in output_path.iterdir() if p.is_dir()}

    for input_file in input_files:
        output_dir_path = output_dirs.get(input_file.stem)
        if output_dir_path is None:
            output_dir_path = output_path / input_file.stem
            output_dir_path.mkdir(parents=True, exist_ok=True)

        print(f"Processing: {input_file.name} -> {output_dir_path.name}")

        try:
            file_content = Path(input_file).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            try:
                file_content = Path(input_file).read_text(encoding="latin-1")
            except Exception as e:
                print(f"Error reading {input_file}: {e}", file=sys.stderr)
                continue
        except Exception as e:
            print(f"Error reading {input_file}: {e}", file=sys.stderr)
            continue

        tasks = parse_tasks(file_content)

        for task_key in sorted(tasks.keys()):
            match = re.search(r"(\d+)", task_key)
            if not match:
                print(f"Warning: Can't parse task id from {task_key}", file=sys.stderr)
                continue
            task_num = int(match.group(1))
            if file_extension == "java":
                dir_name = f"zad{task_num}"
                file = output_dir_path / dir_name / "Main.java"
            else:
                file = output_dir_path / f"zad{task_num:02d}.{file_extension}"

            if not file.exists():
                create_stub_file(file, file_extension)
                print(f"  Created: {file}")

            task_parts = tasks.get(task_key)
            if not task_parts:
                print(
                    f"Warning: No task content for {task_key} in {input_file.name}",
                    file=sys.stderr,
                )
                continue

            task = "\n\n".join(task_parts).rstrip()

            comment_info = file_extension_comment_map.get(file_extension)
            if comment_info is None:
                print(
                    f"No comment information found for file extension '{file_extension}'.",
                    file=sys.stderr,
                )
                return

            try:
                if comment_info.line_by_line is not None:
                    localize_top_comment(
                        file, CommentStyle.LINE_BY_LINE, comment_info.line_by_line
                    )
                if comment_info.delimited is not None:
                    start_delimiter, end_delimiter = comment_info.delimited
                    localize_top_comment(
                        file, CommentStyle.DELIMITED, start_delimiter, end_delimiter
                    )
                if comment_info.line_by_line is not None:
                    localize_top_comment(
                        file, CommentStyle.LINE_BY_LINE, comment_info.line_by_line
                    )

                if comment_info.delimited is not None:
                    start_delimiter, end_delimiter = comment_info.delimited
                    insert_top_comment(
                        file,
                        CommentStyle.DELIMITED,
                        start_delimiter,
                        end_delimiter,
                        task,
                    )
                elif comment_info.line_by_line is not None:
                    insert_top_comment(
                        file,
                        CommentStyle.LINE_BY_LINE,
                        comment_info.line_by_line,
                        None,
                        task,
                    )
                else:
                    print("Invalid comment information.", file=sys.stderr)
                    return

                print(f"  Updated: {file}")
            except Exception as e:
                print(f"Error processing {file}: {e}", file=sys.stderr)
                continue


def main():
    parser = argparse.ArgumentParser(
        description="Update file descriptions/comments from task markdown files.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Example usage:
  python update_descriptions.py zbior_zadan/ src/python/ py
  python update_descriptions.py zbior_zadan/ src/cpp/ cpp
  python update_descriptions.py zbior_zadan/ src/java/ java
        """,
    )
    parser.add_argument("input_dir", nargs="?", type=str)
    parser.add_argument("output_dir", nargs="?", type=str)
    parser.add_argument("file_extension", nargs="?", type=str)

    args = parser.parse_args()

    if args.input_dir and args.output_dir and args.file_extension:
        update_descriptions(args.input_dir, args.output_dir, args.file_extension)
        return

    if args.input_dir or args.output_dir or args.file_extension:
        parser.error("the following arguments are required: input_dir, output_dir, file_extension")

    defaults = [
        ("src/python", "py"),
        ("src/cpp", "cpp"),
        ("src/java", "java"),
        ("src/js", "js"),
        ("src/rust", "rs"),
        ("src/bash", "sh"),
        ("src/haskell", "hs"),
    ]

    for output_dir, ext in defaults:
        if not Path(output_dir).is_dir():
            continue
        update_descriptions("zbior_zadan", output_dir, ext)


if __name__ == "__main__":
    main()
