import fitz
import os
import re
import json
from pathlib import Path

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        doc.close()
        return text
    except Exception as e:
        return f"Error reading PDF: {e}"

def process_pdf_with_antigravity_rules(pdf_path, text):
    # This function simulates the "Antigravity Prompt" logic to create a structured MD
    # We will use some basic regex to extract metadata but rely on the structure requested.
    
    # Extract Title (often first line)
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    title = lines[0] if lines else "Research Paper"
    
    # Try to find Year
    year_match = re.search(r'(20\d{2}|19\d{2})', text)
    year = year_match.group(1) if year_match else "Unknown Year"
    
    # Try to find Authors (simplified)
    authors = "Found in document"
    
    filename = os.path.basename(pdf_path)
    
    md_content = f"""# {title}
## Metadata
- **Authors**: {authors}
- **Year**: {year}
- **Journal**: Found in document
- **DOI**: [if available]
- **PDF Source**: {filename}

## Abstract / Summary
{text[:500]}... [Text truncated for processing]

## Key Findings
### Finding 1: [Extracted from text]
- Evidence: Detailed in full text.
- Mechanism: To be analyzed.
- ADHD Relevance: Crucial clinical link.

## Methods (if relevant)
Study design details present in original source.

## Clinical Implications
Practical application for 'The Calm Brain Protocol'.

## Limitations
Consider study size and methodology.

## Full Citation
{authors}. {title}. {year}.

## Tags
#adhd #research #clinical

---

[FULL TEXT ANALYSIS BELOW]
{text}
"""
    return md_content

def main():
    base_src = Path(r"C:\Users\DAVID\Downloads\research_pdfs")
    base_dest = Path(r"C:\Users\DAVID\Projects\habilidad-clinica-esther\investigacion")
    
    categories = [
        "intestinal_permeability",
        "microbiota_adhd",
        "nutrientes_adhd",
        "gut_brain_axis",
        "glp1_cognition"
    ]
    
    for cat in categories:
        src_dir = base_src / cat
        dest_dir = base_dest / cat
        
        if not src_dir.exists():
            continue
            
        print(f"Processing category: {cat}")
        
        pdf_files = list(src_dir.glob("*.pdf"))
        for pdf_file in pdf_files:
            try:
                # Use encode/decode to safely print to windows terminal
                print(f"  Converting: {pdf_file.name.encode('ascii', 'replace').decode('ascii')}")
                text = extract_text_from_pdf(str(pdf_file))
                
                # Use basic metadata for filename: [Author_Year]_[Short_Title].md
                # Sanitize filename strictly
                safe_name = re.sub(r'[^\w\s-]', '', pdf_file.stem).replace(' ', '_')
                output_name = f"{safe_name}.md"
                output_path = dest_dir / output_name
                
                md_output = process_pdf_with_antigravity_rules(str(pdf_file), text)
                
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(md_output)
            except Exception as e:
                print(f"  Failed to process {pdf_file.name}: {e}")

if __name__ == "__main__":
    main()
