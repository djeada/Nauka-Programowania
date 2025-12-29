# Scripts

This directory contains utility scripts for the Nauka Programowania project.

## md_to_json.py

This script converts all markdown files from the `zbior_zadan` directory to JSON format suitable for consumption by external APIs and LeetCode-like websites.

### Features

- **Parses 25 markdown files** containing 270+ programming exercises
- **Extracts structured data**:
  - Chapter title and description
  - Exercise ID, title, and difficulty level
  - Tags for categorization
  - Problem description
  - Input/output specifications
  - Example test cases
  - Constraints and notes
- **Generates JSON files**:
  - Individual JSON file for each chapter (e.g., `01_interakcja_z_konsola.json`)
  - Combined `all_exercises.json` with all exercises
- **API-ready format**: JSON structure designed for easy integration with coding platforms

### Requirements

- Python 3.6 or higher (no external dependencies required)

### Usage

Run the script from the repository root:

```bash
python3 scripts/md_to_json.py
```

This will create a `zbior_zadan_json` directory containing:
- 25 individual JSON files (one per chapter)
- 1 combined `all_exercises.json` file with all exercises

#### Command-line Options

```bash
python3 scripts/md_to_json.py --help
```

Available options:
- `--input-dir DIR`: Input directory containing markdown files (default: `zbior_zadan`)
- `--output-dir DIR`: Output directory for JSON files (default: `zbior_zadan_json`)
- `--exclude FILE [FILE ...]`: Files to exclude from processing (default: `szablon.md`)

Example with custom directories:
```bash
python3 scripts/md_to_json.py --input-dir custom_exercises --output-dir output/json
```

### JSON Schema

Each generated JSON file follows this structure:

```json
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
```

### Difficulty Levels

- `1` (★☆☆): Easy
- `2` (★★☆): Medium
- `3` (★★★): Hard

### Output

The script generates approximately 500KB of JSON data total, containing:
- **25 chapters**
- **270+ exercises**
- Complete problem descriptions, examples, and constraints

## generate_pdf.py

This script generates a professional PDF document from all markdown files in the `zbior_zadan` directory.

### Features

- **Professional Layout**: Clean, modern design with gradient title page
- **Table of Contents**: Auto-generated with all chapters listed
- **Proper Formatting**: 
  - Syntax-highlighted code blocks
  - Well-formatted tables
  - Mathematical formulas support
  - Proper page breaks and margins
- **Page Numbers**: Automatic page numbering with headers
- **A4 Format**: Standard A4 page size with appropriate margins

### Requirements

Install the required Python packages:

```bash
pip install weasyprint markdown2 pygments
```

### Usage

Run the script from the repository root:

```bash
python3 scripts/generate_pdf.py
```

This will generate `Nauka_Programowania_Zbior_Zadan.pdf` in the repository root directory.

### Output

The generated PDF includes:
1. **Title Page**: Professional cover with project name and year
2. **Table of Contents**: List of all 25 chapters
3. **All Exercises**: Complete zbior_zadan content in order (01-25)

The PDF is approximately 0.6-0.7 MB in size and contains all exercise content in a clean, readable format suitable for printing or digital distribution.

## update_descriptions.py

This script updates exercise descriptions in source code files based on markdown content from zbior_zadan.
