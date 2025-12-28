# Scripts

This directory contains utility scripts for the Nauka Programowania project.

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
