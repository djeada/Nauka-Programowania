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
            "constraints": "...",
            "notes": "..."
        }
    ]
}
"""

import re
import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Any


def parse_difficulty(difficulty_str: str) -> int:
    """Convert star difficulty to numeric value."""
    stars = difficulty_str.count('★')
    return stars if stars > 0 else 1


def clean_text(text: str) -> str:
    """Clean and normalize text content."""
    # Remove excessive whitespace while preserving intentional line breaks
    text = re.sub(r'\n\s*\n\s*\n+', '\n\n', text)
    return text.strip()


def extract_code_block(lines: List[str], start_idx: int) -> tuple[str, int]:
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


def parse_exercise(lines: List[str], start_idx: int) -> tuple[Optional[Dict[str, Any]], int]:
    """Parse a single exercise starting from start_idx."""
    exercise = {
        "id": "",
        "title": "",
        "difficulty": 1,
        "difficulty_display": "★☆☆",
        "tags": [],
        "description": "",
        "input": "",
        "output": "",
        "examples": [],
        "constraints": "",
        "notes": ""
    }
    
    i = start_idx
    current_section = None
    section_content = []
    current_example = {"input": "", "output": ""}
    example_state = None  # None, 'input', or 'output'
    
    # Parse exercise header (## ZAD-XX — Title)
    if i < len(lines):
        header_match = re.match(r'^##\s+(ZAD-\d+[A-Z]?)\s+[—-]\s+(.+)$', lines[i])
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
        difficulty_match = re.search(r'[★☆]+', difficulty_line)
        if difficulty_match:
            exercise["difficulty_display"] = difficulty_match.group(0)
            exercise["difficulty"] = parse_difficulty(difficulty_match.group(0))
        i += 1
    
    if i < len(lines) and lines[i].strip().startswith('**Tagi:**'):
        tags_line = lines[i]
        # Extract tags from backticks
        tags = re.findall(r'`([^`]+)`', tags_line)
        exercise["tags"] = tags
        i += 1
    
    # Parse remaining sections
    while i < len(lines):
        line = lines[i]
        
        # Check if we've reached the next exercise or end
        if line and (re.match(r'^##\s+ZAD-\d+[A-Z]?', line) or re.match(r'^#\s+[^#]', line)):
            break
        
        # Check for section headers
        if line and line.strip().startswith('### '):
            # Save previous section content
            if current_section and section_content:
                content = clean_text('\n'.join(section_content))
                if current_section == "Treść":
                    exercise["description"] = content
                elif current_section == "Wejście":
                    exercise["input"] = content
                elif current_section == "Wyjście":
                    exercise["output"] = content
                elif current_section in ["Ograniczenia / gwarancje", "Ograniczenia/gwarancje", "Gwarancje"]:
                    exercise["constraints"] = content
                elif current_section in ["Uwagi o formatowaniu", "Uwagi"]:
                    exercise["notes"] = content
            
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
            if line and re.match(r'\*\*Wejście:\*\*|\*\*Dane wejściowe:\*\*', line.strip()):
                example_state = 'input'
                i += 1
                continue
            
            # Look for **Wyjście:** or **Oczekiwane wyjście:** or **Dane wyjściowe:**
            if line and re.match(r'\*\*Wyjście:\*\*|\*\*Oczekiwane wyjście:\*\*|\*\*Dane wyjściowe:\*\*', line.strip()):
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
                    # Example complete, add it
                    if current_example["input"] or current_example["output"]:
                        exercise["examples"].append(current_example.copy())
                    current_example = {"input": "", "output": ""}
                    example_state = None
                i = new_i
                continue
        else:
            # Regular content line
            section_content.append(line)
        
        i += 1
    
    # Save last section content
    if current_section and section_content:
        content = clean_text('\n'.join(section_content))
        if current_section == "Treść":
            exercise["description"] = content
        elif current_section == "Wejście":
            exercise["input"] = content
        elif current_section == "Wyjście":
            exercise["output"] = content
        elif current_section in ["Ograniczenia / gwarancje", "Ograniczenia/gwarancje", "Gwarancje"]:
            exercise["constraints"] = content
        elif current_section in ["Uwagi o formatowaniu", "Uwagi"]:
            exercise["notes"] = content
    
    return exercise, i


def parse_markdown_file(file_path: Path) -> Dict[str, Any]:
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
        if re.match(r'^##\s+ZAD-\d+[A-Z]?', line):
            exercise, new_i = parse_exercise(lines, i)
            if exercise:
                result["exercises"].append(exercise)
            i = new_i
        else:
            i += 1
    
    return result


def main():
    """Main function to process all markdown files."""
    # Get the script directory and repository root
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    zbior_zadan_dir = repo_root / "zbior_zadan"
    output_dir = repo_root / "zbior_zadan_json"
    
    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)
    
    # Process all markdown files except szablon.md
    md_files = sorted(zbior_zadan_dir.glob("*.md"))
    all_exercises = []
    
    for md_file in md_files:
        if md_file.name == "szablon.md":
            continue
        
        print(f"Processing {md_file.name}...")
        
        try:
            result = parse_markdown_file(md_file)
            
            # Save individual file JSON
            output_file = output_dir / f"{md_file.stem}.json"
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            
            print(f"  ✓ Created {output_file.name} with {len(result['exercises'])} exercises")
            
            # Add to combined list
            all_exercises.append(result)
        
        except Exception as e:
            print(f"  ✗ Error processing {md_file.name}: {e}")
    
    # Create combined JSON file with all exercises
    combined_file = output_dir / "all_exercises.json"
    with open(combined_file, 'w', encoding='utf-8') as f:
        json.dump(all_exercises, f, ensure_ascii=False, indent=2)
    
    print(f"\n✓ Created combined file: {combined_file.name}")
    print(f"✓ Total files processed: {len(all_exercises)}")
    
    # Create summary statistics
    total_exercises = sum(len(chapter["exercises"]) for chapter in all_exercises)
    print(f"✓ Total exercises: {total_exercises}")


if __name__ == "__main__":
    main()
