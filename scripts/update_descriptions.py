from enum import Enum
from typing import Optional, Tuple
from dataclasses import dataclass
from pathlib import Path
import sys


class CommentStyle(Enum):
    DELIMITED = 1
    LINE_BY_LINE = 2


@dataclass
class CommentInfo:
    delimited: Optional[Tuple[str, str]] = None
    line_by_line: Optional[str] = None


def localize_delimited_comment(content, start_delimiter, end_delimiter):
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
    modified_content = []
    removing_comments = False
    for line in content:
        if not removing_comments and line.strip().startswith(delimiter):
            removing_comments = True
        elif removing_comments and not line.strip().startswith(delimiter):
            removing_comments = False
            modified_content.append(line)

        if not removing_comments:
            modified_content.append(line)

    if len(modified_content) == len(content):
        return None
    else:
        return modified_content


def localize_top_comment(file_path, comment_style, start_delimiter, end_delimiter=None):
    with open(file_path, "r") as file:
        content = file.readlines()

    if comment_style == CommentStyle.DELIMITED:
        modified_content = localize_delimited_comment(
            content, start_delimiter, end_delimiter
        )
    elif comment_style == CommentStyle.LINE_BY_LINE:
        modified_content = localize_line_by_line_comment(content, start_delimiter)

    if modified_content is not None:
        with open(file_path, "w") as file:
            file.writelines(modified_content)
    else:
        print("No top comment found.")


def insert_delimited_comment(content, start_delimiter, end_delimiter, comment_content):
    comment_lines = (
        [start_delimiter + "\n"]
        + [line + "\n" for line in comment_content.split("\n")]
        + [end_delimiter + "\n"]
    )
    return comment_lines + content


def insert_line_by_line_comment(content, delimiter, comment_content):
    comment_lines = [f"{delimiter} {line}\n" for line in comment_content.split("\n")]
    return comment_lines + content


def insert_top_comment(
    file_path, comment_style, start_delimiter, end_delimiter, comment_content
):
    with open(file_path, "r") as file:
        content = file.readlines()

    if comment_style == CommentStyle.DELIMITED:
        modified_content = insert_delimited_comment(
            content, start_delimiter, end_delimiter, comment_content + "\n"
        )
    elif comment_style == CommentStyle.LINE_BY_LINE:
        modified_content = insert_line_by_line_comment(
            content, start_delimiter, comment_content
        )

    with open(file_path, "w") as file:
        file.writelines(modified_content)


def parse_tasks(input_str):
    # split the input string into lines
    lines = input_str.split("\n")
    lines = lines[1:]

    # initialize a dictionary to hold the tasks
    tasks = {}

    # initialize variables to keep track of the current task
    task_num = 1
    task_lines = []

    # loop over the lines and extract task information
    for line in lines:
        line = line.strip()

        if line.startswith("### Zad"):
            # add the current task to the dictionary
            if task_lines:
                task_id = "zad" + str(task_num)
                task_content = "\n".join(task_lines)
                tasks[task_id] = task_content
                task_num += 1
                task_lines = []

        elif line:
            # add the line to the current task content
            task_lines.append(line)

    if task_lines:
        task_id = "zad" + str(task_num)
        task_content = "\n".join(task_lines)
        tasks[task_id] = task_content
        task_num += 1
        task_lines = []

    # return the dictionary of tasks
    return tasks


def main():

    file_extension_comment_map = {
        "cpp": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "java": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "js": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "py": CommentInfo(delimited=('"""', '"""'), line_by_line="#"),
        "rs": CommentInfo(delimited=("/*", "*/"), line_by_line="//"),
        "sh": CommentInfo(line_by_line="#"),
    }

    input_files = sorted(Path(sys.argv[1]).iterdir(), key=lambda p: str(p))
    output_dirs = sorted(Path(sys.argv[2]).iterdir(), key=lambda p: str(p))
    file_extension = sys.argv[3]

    for input_file, output_dir in zip(input_files, output_dirs):
        print(input_file, output_dir)

        file_content = Path(input_file).read_text()
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
                    ]
        files = sorted(files, key=lambda p: str(p))

        for file, task in zip(files, tasks.values()):
            comment_info = file_extension_comment_map.get(file_extension)

            if comment_info is None:
                print(
                    f"No comment information found for file extension '{file_extension}'."
                )
                return

            if comment_info.delimited is not None:
                comment_style = CommentStyle.DELIMITED
                start_delimiter, end_delimiter = comment_info.delimited
            elif comment_info.line_by_line is not None:
                comment_style = CommentStyle.LINE_BY_LINE
                start_delimiter, end_delimiter = comment_info.line_by_line, None
            else:
                print("Invalid comment information.")
                return

            # Localize the top comment and remove it from the file
            localize_top_comment(file, comment_style, start_delimiter, end_delimiter)

            # Insert a top comment at the beginning of the file
            insert_top_comment(file, comment_style, start_delimiter, end_delimiter, task)


if __name__ == "__main__":
    main()
