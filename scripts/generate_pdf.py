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
        <div class="title-page-inner">
            <p class="title-kicker">Kurs Programowania</p>
            <h1 class="main-title">Nauka Programowania</h1>
            <div class="title-rule"></div>
            <h2 class="subtitle">Zbiór Zadań</h2>
            <p class="description">Kompletny zbiór zadań programistycznych<br/>
            od podstaw do zaawansowanych technik</p>
            <div class="title-meta">
                <span class="title-tag">Wersja PDF</span>
                <span class="title-year">{current_year}</span>
            </div>
        </div>
    </div>
    <div class="page-break"></div>
    """


def create_table_of_contents(md_files):
    """Create HTML for table of contents."""
    toc_html = """
    <div class="toc">
        <h1 class="toc-title">Spis Treści</h1>
        <p class="toc-subtitle">Rozdziały uporządkowane rosnąco według numerów</p>
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
        margin: 2.4cm 2cm;
        
        @top-center {
            content: "Nauka Programowania - Zbiór Zadań";
            font-size: 9pt;
            color: #6b7280;
            font-family: 'DejaVu Sans', Arial, sans-serif;
            letter-spacing: 0.5pt;
        }
        
        @bottom-center {
            content: "Strona " counter(page);
            font-size: 9pt;
            color: #6b7280;
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
        line-height: 1.65;
        color: #1f2937;
    }
    
    /* Title Page */
    .title-page {
        height: 100vh;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        background:
            radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.2), transparent 45%),
            radial-gradient(circle at 80% 0%, rgba(255, 255, 255, 0.12), transparent 40%),
            linear-gradient(135deg, #16222a 0%, #3a6073 100%);
        color: white;
        margin: -2.4cm -2cm;
        padding: 2.4cm 2cm;
    }

    .title-page-inner {
        max-width: 80%;
    }

    .title-kicker {
        text-transform: uppercase;
        letter-spacing: 3pt;
        font-size: 9pt;
        color: rgba(255, 255, 255, 0.75);
        margin-bottom: 18pt;
    }
    
    .main-title {
        font-family: 'DejaVu Serif', 'Times New Roman', serif;
        font-size: 46pt;
        font-weight: 700;
        margin-bottom: 14pt;
        text-transform: uppercase;
        letter-spacing: 2.5pt;
    }

    .title-rule {
        width: 120pt;
        height: 4pt;
        margin: 0 auto 24pt auto;
        background: linear-gradient(90deg, #f2994a 0%, #ffd166 100%);
        border-radius: 2pt;
    }
    
    .subtitle {
        font-size: 28pt;
        font-weight: 300;
        margin-bottom: 24pt;
    }
    
    .description {
        font-size: 14pt;
        margin-bottom: 42pt;
        font-weight: 300;
        line-height: 1.8;
    }
    
    .title-meta {
        display: inline-flex;
        gap: 12pt;
        align-items: center;
        justify-content: center;
        font-size: 12pt;
        letter-spacing: 1pt;
    }

    .title-tag {
        text-transform: uppercase;
        padding: 6pt 12pt;
        border: 1pt solid rgba(255, 255, 255, 0.5);
        border-radius: 999pt;
        font-size: 9pt;
    }

    .title-year {
        font-size: 14pt;
        font-weight: 300;
    }
    
    /* Table of Contents */
    .toc {
        page-break-after: always;
    }
    
    .toc-title {
        font-family: 'DejaVu Serif', 'Times New Roman', serif;
        font-size: 26pt;
        font-weight: 700;
        color: #1f3a5f;
        margin-bottom: 10pt;
        border-bottom: 3pt solid #f2994a;
        padding-bottom: 10pt;
    }

    .toc-subtitle {
        font-size: 11pt;
        color: #6b7280;
        margin-bottom: 18pt;
    }
    
    .toc-list {
        list-style: none;
        padding-left: 0;
        column-count: 2;
        column-gap: 18pt;
    }
    
    .toc-item {
        font-size: 12pt;
        padding: 6pt 0;
        border-bottom: 1pt solid #eef2f7;
        break-inside: avoid;
    }
    
    .toc-number {
        display: inline-block;
        width: 40pt;
        font-weight: bold;
        color: #2d9cdb;
    }

    /* Headings */
    h1 {
        font-family: 'DejaVu Serif', 'Times New Roman', serif;
        font-size: 22pt;
        font-weight: 700;
        color: #1f3a5f;
        margin-top: 26pt;
        margin-bottom: 16pt;
        page-break-before: always;
        border-left: 6pt solid #2d9cdb;
        padding: 6pt 0 6pt 12pt;
        background: #f3f6fb;
    }
    
    h1:first-of-type {
        page-break-before: avoid;
    }
    
    h2 {
        font-size: 17pt;
        font-weight: 700;
        color: #2c3e50;
        margin-top: 22pt;
        margin-bottom: 12pt;
        page-break-after: avoid;
    }
    
    h3 {
        font-size: 13pt;
        font-weight: bold;
        color: #374151;
        margin-top: 18pt;
        margin-bottom: 10pt;
        page-break-after: avoid;
    }
    
    h4, h5, h6 {
        font-size: 12pt;
        font-weight: bold;
        color: #4b5563;
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
        margin-left: 22pt;
        orphans: 3;
        widows: 3;
    }
    
    li {
        margin-bottom: 6pt;
    }
    
    /* Code blocks */
    pre {
        background-color: #0f172a;
        border: 1pt solid #0b1220;
        border-left: 4pt solid #f2994a;
        border-radius: 6pt;
        padding: 12pt 14pt;
        margin-bottom: 15pt;
        overflow-x: auto;
        font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
        font-size: 9.5pt;
        line-height: 1.45;
        page-break-inside: avoid;
        color: #e5e7eb;
    }
    
    code {
        font-family: 'DejaVu Sans Mono', 'Courier New', monospace;
        font-size: 10pt;
        background-color: #f3f4f6;
        padding: 2pt 4pt;
        border-radius: 3pt;
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
        border-radius: 6pt;
        overflow: hidden;
    }
    
    th, td {
        border: 1pt solid #e5e7eb;
        padding: 8pt 10pt;
        text-align: left;
    }
    
    th {
        background-color: #1f3a5f;
        color: white;
        font-weight: bold;
    }
    
    tr:nth-child(even) {
        background-color: #f8fafc;
    }
    
    /* Blockquotes */
    blockquote {
        border-left: 4pt solid #2d9cdb;
        padding-left: 15pt;
        margin-left: 0;
        margin-bottom: 15pt;
        color: #4b5563;
        font-style: italic;
    }
    
    /* Links */
    a {
        color: #2d9cdb;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* Strong and emphasis */
    strong {
        font-weight: bold;
        color: #111827;
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
        border-top: 2pt solid #e5e7eb;
        margin: 22pt 0;
    }

    .chapter {
        padding-top: 6pt;
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
