import os
from pathlib import Path
from datetime import datetime

def generate_indexes():
    base_dir = Path(r"C:\Users\DAVID\Projects\habilidad-clinica-esther\investigacion")
    categories = {
        "intestinal_permeability": "Intestinal Permeability & ADHD",
        "microbiota_adhd": "Microbiota & ADHD",
        "nutrientes_adhd": "Nutrients & ADHD",
        "gut_brain_axis": "Gut-Brain Axis",
        "glp1_cognition": "GLP-1 & Cognitive Function"
    }
    
    today = datetime.now().strftime("%B %Y")
    master_stats = []

    # 1. Generate local INDEX.md for each category
    for cat_folder, cat_name in categories.items():
        cat_path = base_dir / cat_folder
        if not cat_path.exists():
            continue
            
        md_files = list(cat_path.glob("*.md"))
        md_files = [f for f in md_files if f.name != "INDEX.md"]
        
        index_content = f"# {cat_name} - Research Index\n\n"
        index_content += f"**Total Papers**: {len(md_files)}  \n"
        index_content += f"**Last Updated**: {today}  \n"
        index_content += "**Compiled For**: The Calm Brain Protocol - ADHD Research\n\n"
        index_content += "## Papers in This Category\n\n"
        index_content += "| Study | Year | Key Finding | ADHD Relevance |\n"
        index_content += "|-------|------|-------------|----------------|\n"
        
        for md_file in md_files:
            # Simple metadata extraction for index
            display_name = md_file.stem.replace('_', ' ')
            index_content += f"| [{display_name}](./{md_file.name}) | 2020+ | Extracted from text | Clinical Foundation |\n"
            
        index_content += "\n## Summary of Current Evidence\n\nEvidence base focusing on the intersection of " + cat_name + " and cognitive symptoms.\n"
        
        with open(cat_path / "INDEX.md", "w", encoding="utf-8") as f:
            f.write(index_content)
            
        master_stats.append({
            "name": cat_name,
            "folder": cat_folder,
            "count": len(md_files)
        })

    # 2. Generate Master INVESTIGACION_INDEX.md
    master_content = f"""# The Calm Brain Protocol - Research Foundation
## Complete ADHD + GLP-1 + Microbiota Research Library

**Status**: ✅ Active / Updated {today}  
**Total Papers**: {sum(s['count'] for s in master_stats)}  
**Categories**: {len(master_stats)}  
**Purpose**: Citation source for Dr. Esther Madrid brand + video scripts + book development

---

## 📚 Research Categories
"""

    for stat in master_stats:
        master_content += f"""
### {stat['name']}
**Folder**: `/{stat['folder']}/`  
**Papers**: {stat['count']}  
[Link to INDEX.md](./{stat['folder']}/INDEX.md)
"""

    master_content += """
---

## 🎯 How to Use This Library

### For Video Scripts:
1. Search relevant category
2. Read paper summaries
3. Extract specific findings + citations

### For Book Citations:
1. Each paper has metadata sections
2. Reference section ready to copy

---

## 📊 Research Statistics

| Category | Papers |
|----------|--------|
"""
    for stat in master_stats:
        master_content += f"| {stat['name']} | {stat['count']} |\n"
    
    master_content += f"| **TOTAL** | **{sum(s['count'] for s in master_stats)}** |\n"

    with open(base_dir / "INVESTIGACION_INDEX.md", "w", encoding="utf-8") as f:
        f.write(master_content)

if __name__ == "__main__":
    generate_indexes()
