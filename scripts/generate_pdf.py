#!/usr/bin/env python3
"""
Script to generate a professional PDF from zbior_zadan markdown files.
This combines all exercise files into a single, well-formatted PDF document.
"""

import os
import re
from pathlib import Path
from datetime import datetime
import markdown2
from weasyprint import HTML, CSS


def get_markdown_files(zbior_dir):
    """Get all markdown files from zbior_zadan directory, sorted by number."""
    md_files = []
    for file in zbior_dir.glob("*.md"):
        # Skip the template file
        if file.name == "szablon.md":
            continue
        # Extract number from filename for sorting
        match = re.match(r"(\d+)_.*\.md", file.name)
        if match:
            number = int(match.group(1))
            md_files.append((number, file))
    
    # Sort by number
    md_files.sort(key=lambda x: x[0])
    return [f[1] for f in md_files]


def create_title_page():
    """Create HTML for the title page."""
    current_year = datetime.now().year
    return f"""
    <div class="title-page">
        <h1 class="main-title">Nauka Programowania</h1>
        <h2 class="subtitle">Zbiór Zadań</h2>
        <p class="description">Kompletny zbiór zadań programistycznych<br/>
        od podstaw do zaawansowanych technik</p>
        <p class="year">{current_year}</p>
    </div>
    <div class="page-break"></div>
    """


def create_table_of_contents(md_files):
    """Create HTML for table of contents."""
    toc_html = """
    <div class="toc">
        <h1 class="toc-title">Spis Treści</h1>
        <ul class="toc-list">
    """
    
    for file in md_files:
        # Extract title from filename
        name = file.stem
        match = re.match(r"(\d+)_(.*)", name)
        if match:
            number = match.group(1)
            title = match.group(2).replace("_", " ").title()
            toc_html += f'        <li class="toc-item"><span class="toc-number">{number}.</span> {title}</li>\n'
    
    toc_html += """
        </ul>
    </div>
    <div class="page-break"></div>
    """
    return toc_html


def process_markdown_content(content):
    """Process markdown content and convert to HTML."""
    # Convert markdown to HTML with extras for better formatting
    html = markdown2.markdown(
        content,
        extras=[
            "fenced-code-blocks",
            "tables",
            "break-on-newline",
            "code-friendly",
            "cuddled-lists",
            "header-ids"
        ]
    )
    return html


def create_css():
    """Create CSS for professional PDF styling."""
    return """
    @page {
        size: A4;
        margin: 2.5cm 2cm;
        
        @top-center {
            content: "Nauka Programowania - Zbiór Zadań";
            font-size: 9pt;
            color: #666;
            font-family: 'DejaVu Sans', Arial, sans-serif;
        }
        
        @bottom-center {
            content: "Strona " counter(page);
            font-size: 9pt;
            color: #666;
            font-family: 'DejaVu Sans', Arial, sans-serif;
        }
    }
    
    /* Title page doesn't need headers/footers */
    @page :first {
        @top-center { content: none; }
        @bottom-center { content: none; }
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        font-family: 'DejaVu Sans', Arial, sans-serif;
        font-size: 11pt;
        line-height: 1.6;
        color: #333;
    }
    
    /* Title Page */
    .title-page {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        margin: -2.5cm -2cm;
        padding: 2.5cm 2cm;
    }
    
    .main-title {
        font-size: 48pt;
        font-weight: bold;
        margin-bottom: 20pt;
        text-transform: uppercase;
        letter-spacing: 2pt;
    }
    
    .subtitle {
        font-size: 32pt;
        font-weight: 300;
        margin-bottom: 40pt;
    }
    
    .description {
        font-size: 14pt;
        margin-bottom: 60pt;
        font-weight: 300;
        line-height: 1.8;
    }
    
    .year {
        font-size: 18pt;
        font-weight: 300;
    }
    
    /* Table of Contents */
    .toc {
        page-break-after: always;
    }
    
    .toc-title {
        font-size: 28pt;
        font-weight: bold;
        color: #667eea;
        margin-bottom: 30pt;
        border-bottom: 3pt solid #667eea;
        padding-bottom: 10pt;
    }
    
    .toc-list {
        list-style: none;
        padding-left: 0;
    }
    
    .toc-item {
        font-size: 13pt;
        padding: 8pt 0;
        border-bottom: 1pt solid #eee;
    }
    
    .toc-number {
        display: inline-block;
        width: 40pt;
        font-weight: bold;
        color: #667eea;
    }
    
    /* Headings */
    h1 {
        font-size: 24pt;
        font-weight: bold;
        color: #667eea;
        margin-top: 30pt;
        margin-bottom: 20pt;
        page-break-before: always;
        border-bottom: 2pt solid #667eea;
        padding-bottom: 8pt;
    }
    
    h1:first-of-type {
        page-break-before: avoid;
    }
    
    h2 {
        font-size: 18pt;
        font-weight: bold;
        color: #444;
        margin-top: 25pt;
        margin-bottom: 15pt;
        page-break-after: avoid;
    }
    
    h3 {
        font-size: 14pt;
        font-weight: bold;
        color: #555;
        margin-top: 20pt;
        margin-bottom: 12pt;
        page-break-after: avoid;
    }
    
    h4, h5, h6 {
        font-size: 12pt;
        font-weight: bold;
        color: #666;
        margin-top: 15pt;
        margin-bottom: 10pt;
        page-break-after: avoid;
    }
    
    /* Paragraphs */
    p {
        margin-bottom: 12pt;
        text-align: justify;
        orphans: 3;
        widows: 3;
    }
    
    /* Lists */
    ul, ol {
        margin-bottom: 12pt;
        margin-left: 20pt;
        orphans: 3;
        widows: 3;
    }
    
    li {
        margin-bottom: 6pt;
    }
    
    /* Code blocks */
    pre {
        background-color: #f5f5f5;
        border: 1pt solid #ddd;
        border-left: 4pt solid #667eea;
        border-radius: 4pt;
        padding: 12pt;
        margin-bottom: 15pt;
        overflow-x: auto;
        font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
        font-size: 9pt;
        line-height: 1.4;
        page-break-inside: avoid;
    }
    
    code {
        font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
        font-size: 10pt;
        background-color: #f5f5f5;
        padding: 2pt 4pt;
        border-radius: 2pt;
    }
    
    pre code {
        background-color: transparent;
        padding: 0;
    }
    
    /* Tables */
    table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 15pt;
        page-break-inside: avoid;
    }
    
    th, td {
        border: 1pt solid #ddd;
        padding: 8pt;
        text-align: left;
    }
    
    th {
        background-color: #667eea;
        color: white;
        font-weight: bold;
    }
    
    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    
    /* Blockquotes */
    blockquote {
        border-left: 4pt solid #667eea;
        padding-left: 15pt;
        margin-left: 0;
        margin-bottom: 15pt;
        color: #555;
        font-style: italic;
    }
    
    /* Links */
    a {
        color: #667eea;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Strong and emphasis */
    strong {
        font-weight: bold;
        color: #222;
    }
    
    em {
        font-style: italic;
    }
    
    /* Page breaks */
    .page-break {
        page-break-after: always;
    }
    
    /* Avoid breaking inside these elements */
    h1, h2, h3, h4, h5, h6 {
        page-break-after: avoid;
    }
    
    pre, blockquote, table {
        page-break-inside: avoid;
    }
    
    /* Horizontal rules */
    hr {
        border: none;
        border-top: 1pt solid #ddd;
        margin: 20pt 0;
    }
    """


def generate_pdf(zbior_dir, output_file):
    """Generate a professional PDF from markdown files."""
    print("Starting PDF generation...")
    
    # Get all markdown files
    md_files = get_markdown_files(zbior_dir)
    print(f"Found {len(md_files)} markdown files")
    
    # Start building HTML content
    html_content = """
    <!DOCTYPE html>
    <html lang="pl">
    <head>
        <meta charset="UTF-8">
        <title>Nauka Programowania - Zbiór Zadań</title>
    </head>
    <body>
    """
    
    # Add title page
    html_content += create_title_page()
    print("Created title page")
    
    # Add table of contents
    html_content += create_table_of_contents(md_files)
    print("Created table of contents")
    
    # Process each markdown file
    for idx, md_file in enumerate(md_files, 1):
        print(f"Processing file {idx}/{len(md_files)}: {md_file.name}")
        content = md_file.read_text(encoding='utf-8')
        html = process_markdown_content(content)
        html_content += f'<div class="chapter">\n{html}\n</div>\n'
    
    # Close HTML
    html_content += """
    </body>
    </html>
    """
    
    # Create CSS
    css = create_css()
    
    # Generate PDF
    print(f"Generating PDF: {output_file}")
    HTML(string=html_content).write_pdf(
        output_file,
        stylesheets=[CSS(string=css)]
    )
    
    print(f"PDF generated successfully: {output_file}")
    
    # Get file size
    size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"PDF size: {size_mb:.2f} MB")


def main():
    """Main function."""
    # Get paths
    script_dir = Path(__file__).parent
    repo_dir = script_dir.parent
    zbior_dir = repo_dir / "zbior_zadan"
    output_file = repo_dir / "Nauka_Programowania_Zbior_Zadan.pdf"
    
    # Validate directory exists
    if not zbior_dir.exists():
        print(f"Error: Directory {zbior_dir} does not exist!")
        return 1
    
    try:
        generate_pdf(zbior_dir, output_file)
        return 0
    except Exception as e:
        print(f"Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    exit(main())
