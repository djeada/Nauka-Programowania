#!/usr/bin/env python3
"""
Script to convert zbior_zadan markdown files to JSON format.

This script parses all .md files in the zbior_zadan directory and converts them
to JSON format suitable for consumption by external APIs and LeetCode-like websites.

JSON Schema:
{
    "file": "01_interakcja_z_konsola.md",
    "chapter_title": "Rozdział 1: Interakcja z konsolą (stdin/stdout)",
    "chapter_description": "...",
    "exercises": [
        {
            "id": "ZAD-01",
            "slug": "01_interakcja_z_konsola/ZAD-01",
            "title": "Wypisywanie tekstu na ekran",
            "difficulty": 1,
            "difficulty_display": "★☆☆",
            "tags": ["I/O", "print", "string"],
            "description": "...",
            "input": "...",
            "output": "...",
            "examples": [
                {
                    "input": "...",
                    "output": "..."
                }
            ],
            "testcases": [
                {
                    "input": "...",
                    "output": "..."
                }
            ],
            "constraints": "...",
            "notes": "..."
        }
    ]
}
"""

import re
import json
import os
import traceback
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple


# Compile regex patterns at module level for performance
EXERCISE_HEADER_PATTERN = re.compile(r'^##\s+(ZAD-\d+[A-Z]?)\s+[—-]\s+(.+)$')
CHAPTER_HEADER_PATTERN = re.compile(r'^#\s+[^#]')
DIFFICULTY_PATTERN = re.compile(r'[★☆]+')
TAG_PATTERN = re.compile(r'`([^`]+)`')
INPUT_MARKER_PATTERN = re.compile(r'\*\*Wejście:\*\*|\*\*Dane wejściowe:\*\*')
OUTPUT_MARKER_PATTERN = re.compile(r'\*\*Wyjście:\*\*|\*\*Oczekiwane wyjście:\*\*|\*\*Dane wyjściowe:\*\*')

# Section name mappings for consistent handling
SECTION_NAMES = {
    'description': ['Treść'],
    'input': ['Wejście'],
    'output': ['Wyjście'],
    'constraints': ['Ograniczenia / gwarancje', 'Ograniczenia/gwarancje', 'Gwarancje'],
    'notes': ['Uwagi o formatowaniu', 'Uwagi']
}


def parse_difficulty(difficulty_str: str) -> int:
    """Convert star difficulty to numeric value."""
    stars = difficulty_str.count('★')
    return stars if stars > 0 else 1


def clean_text(text: str) -> str:
    """Clean and normalize text content."""
    # Remove excessive whitespace while preserving intentional line breaks
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()


def extract_code_block(lines: List[str], start_idx: int) -> Tuple[str, int]:
    """Extract a code block starting from start_idx."""
    code_lines = []
    i = start_idx
    
    # Skip the opening ```
    if i < len(lines) and lines[i].strip().startswith('```'):
        i += 1
    
    # Collect code lines until closing ```
    while i < len(lines):
        if lines[i].strip().startswith('```'):
            i += 1
            break
        code_lines.append(lines[i].rstrip())
        i += 1
    
    return '\n'.join(code_lines), i


def map_section_to_field(section_name: str) -> Optional[str]:
    """Map a section name to its corresponding field in the exercise dict."""
    for field, names in SECTION_NAMES.items():
        if section_name in names:
            return field
    return None


def save_section_content(exercise: Dict[str, Any], section_name: str, content: str) -> None:
    """Save content to the appropriate field based on section name."""
    field = map_section_to_field(section_name)
    if field:
        exercise[field] = content


def parse_exercise(lines: List[str], start_idx: int) -> Tuple[Optional[Dict[str, Any]], int]:
    """Parse a single exercise starting from start_idx."""
    exercise = {
        "id": "",
        "slug": "",
        "title": "",
        "difficulty": 1,
        "difficulty_display": "★☆☆",
        "tags": [],
        "description": "",
        "input": "",
        "output": "",
        "examples": [],
        "testcases": [],
        "constraints": "",
        "notes": ""
    }
    
    i = start_idx
    current_section = None
    section_content = []
    current_example = {"input": "", "output": ""}
    example_state = None  # None, 'input', or 'output'
    
    # Parse exercise header (## ZAD-XX — Title)
    # Note: The pattern matches both em dash (—) and hyphen (-) for flexibility
    if i < len(lines):
        header_match = EXERCISE_HEADER_PATTERN.match(lines[i])
        if not header_match:
            return None, i
        
        exercise["id"] = header_match.group(1)
        exercise["title"] = header_match.group(2).strip()
        i += 1
    else:
        return None, i
    
    # Skip empty lines
    while i < len(lines) and not lines[i].strip():
        i += 1
    
    # Parse difficulty and tags
    if i < len(lines) and lines[i].strip().startswith('**Poziom:**'):
        difficulty_line = lines[i]
        difficulty_match = DIFFICULTY_PATTERN.search(difficulty_line)
        if difficulty_match:
            exercise["difficulty_display"] = difficulty_match.group(0)
            exercise["difficulty"] = parse_difficulty(difficulty_match.group(0))
        i += 1
    
    if i < len(lines) and lines[i].strip().startswith('**Tagi:**'):
        tags_line = lines[i]
        # Extract tags from backticks
        tags = TAG_PATTERN.findall(tags_line)
        exercise["tags"] = tags
        i += 1
    
    # Parse remaining sections
    while i < len(lines):
        line = lines[i]
        
        # Check if we've reached the next exercise or end
        if line and (EXERCISE_HEADER_PATTERN.match(line) or CHAPTER_HEADER_PATTERN.match(line)):
            break
        
        # Check for section headers
        if line and line.strip().startswith('### '):
            # Save previous section content
            if current_section and section_content:
                content = clean_text('\n'.join(section_content))
                save_section_content(exercise, current_section, content)
            
            section_content = []
            current_section = line.strip().replace('### ', '').strip()
            i += 1
            
            # Special handling for Przykład section
            if current_section.startswith("Przykład"):
                example_state = None
                current_example = {"input": "", "output": ""}
            
            continue
        
        # Handle content based on current section
        if current_section and (current_section == "Przykład" or current_section.startswith("Przykład")):
            # Look for **Wejście:** or **Dane wejściowe:**
            if line and INPUT_MARKER_PATTERN.match(line.strip()):
                example_state = 'input'
                i += 1
                continue
            
            # Look for **Wyjście:** or **Oczekiwane wyjście:** or **Dane wyjściowe:**
            if line and OUTPUT_MARKER_PATTERN.match(line.strip()):
                example_state = 'output'
                i += 1
                continue
            
            # Handle code blocks
            if line and line.strip().startswith('```'):
                code, new_i = extract_code_block(lines, i)
                if example_state == 'input':
                    current_example["input"] = code
                elif example_state == 'output':
                    current_example["output"] = code
                    # Example complete, add it only if both input and output are present
                    if current_example["input"] and current_example["output"]:
                        exercise["examples"].append(current_example.copy())
                    current_example = {"input": "", "output": ""}
                    example_state = None
                else:
                    # Output-only example block
                    current_example["output"] = code
                    exercise["examples"].append(current_example.copy())
                    current_example = {"input": "", "output": ""}
                i = new_i
                continue
        else:
            # Regular content line
            if line.strip() != '---':
                section_content.append(line)
        
        i += 1
    
    # Save last section content
    if current_section and section_content:
        content = clean_text('\n'.join(section_content))
        save_section_content(exercise, current_section, content)
    
    return exercise, i


def parse_markdown_file(file_path: Path, tests_map: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Parse a single markdown file and extract all exercises."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    lines = content.split('\n')
    
    result = {
        "file": file_path.name,
        "chapter_title": "",
        "chapter_description": "",
        "exercises": []
    }
    
    i = 0
    
    # Parse chapter title (# Chapter Title)
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('# ') and not line.strip().startswith('##'):
            result["chapter_title"] = line.strip().replace('# ', '')
            i += 1
            
            # Collect chapter description until first exercise
            desc_lines = []
            while i < len(lines):
                if lines[i].strip().startswith('## ZAD-'):
                    break
                if lines[i].strip() and not lines[i].strip().startswith('---'):
                    desc_lines.append(lines[i])
                i += 1
            
            result["chapter_description"] = clean_text('\n'.join(desc_lines))
            break
        i += 1
    
    # Parse all exercises
    while i < len(lines):
        line = lines[i]
        
        # Look for exercise headers
        if EXERCISE_HEADER_PATTERN.match(line):
            exercise, new_i = parse_exercise(lines, i)
            if exercise:
                exercise["slug"] = f"{file_path.stem}/{exercise['id']}"
                if tests_map:
                    testcase_key = exercise["id"]
                    slug_key = exercise["slug"]
                    if testcase_key in tests_map:
                        exercise["testcases"] = tests_map.get(testcase_key, [])
                    elif slug_key in tests_map:
                        exercise["testcases"] = tests_map.get(slug_key, [])
                result["exercises"].append(exercise)
            i = new_i
        else:
            i += 1
    
    return result


def main():
    """Main function to process all markdown files."""
    import argparse
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description='Convert zbior_zadan markdown files to JSON format'
    )
    parser.add_argument(
        '--input-dir',
        default='zbior_zadan',
        help='Input directory containing markdown files (default: zbior_zadan)'
    )
    parser.add_argument(
        '--output-dir',
        default='zbior_zadan_json',
        help='Output directory for JSON files (default: zbior_zadan_json)'
    )
    parser.add_argument(
        '--exclude',
        nargs='*',
        default=['szablon.md'],
        help='Files to exclude from processing (default: szablon.md)'
    )
    parser.add_argument(
        '--tests-dir',
        default='zbior_zadan_tests',
        help='Directory containing per-chapter JSON testcase maps (default: zbior_zadan_tests)'
    )
    
    args = parser.parse_args()
    
    # Get the script directory and repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    zbior_zadan_dir = repo_root / args.input_dir
    output_dir = repo_root / args.output_dir
    tests_dir = repo_root / args.tests_dir
    
    # Check if input directory exists
    if not zbior_zadan_dir.exists():
        print(f"Error: Input directory '{args.input_dir}' not found")
        return 1
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Process all markdown files except excluded ones
    md_files = sorted(zbior_zadan_dir.glob("*.md"))
    total_files = 0
    total_exercises = 0
    
    for md_file in md_files:
        if md_file.name in args.exclude:
            continue
        
        print(f"Processing {md_file.name}...")
        
        try:
            tests_map = None
            tests_file = tests_dir / f"{md_file.stem}.json"
            if tests_file.exists():
                with open(tests_file, 'r', encoding='utf-8') as f:
                    tests_map = json.load(f)
            result = parse_markdown_file(md_file, tests_map)
            
            # Save individual file JSON
            output_file = output_dir / f"{md_file.stem}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            print(f"  ✓ Created {output_file.name} with {len(result['exercises'])} exercises")
            
            total_files += 1
            total_exercises += len(result["exercises"])
        
        except (IOError, OSError) as e:
            print(f"  ✗ File error processing {md_file.name}: {e}")
        except UnicodeDecodeError as e:
            print(f"  ✗ Encoding error processing {md_file.name}: {e}")
        except Exception as e:
            print(f"  ✗ Unexpected error processing {md_file.name}: {e}")
            traceback.print_exc()
    
    print(f"\n✓ Total files processed: {total_files}")
    print(f"✓ Total exercises: {total_exercises}")
    
    return 0


if __name__ == "__main__":
    import sys
    sys.exit(main())
