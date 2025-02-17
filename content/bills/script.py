import os

# Content template for the markdown files
md_content = """---
title: \"Portugese Irregular Verbs\" 
date: 1997-01-01
lastmod: 2024-05-08
tags:
    [
    \"Senate bill\",\"Imperial Senate\", \"Diplomatic Missive\", \"Imperial Decree\", \"Governmental Announcement\",
    \"In-effect\", \"Inconsequential\", \"Under consideration\", \"Successfully Enacted\", \"Amended\", \"Superceded\", \"Archived\", 
    \"Caerus\", \"Cathramis\", \"Halinn\", \"Iristoya\", \"Kejafros\", \"Rozakko'ra\", \"Talasi\", \"Tanragh\", \"Tiberia\",
    \"Soralae\", \"Hou Zhanaland\", \"Arushinim\", \"Verena\"
    ]

author: [\"Moritz-Maria von Igelfeld\"]
description: \"This book discusses Portugese irregular verbs in great details.\"
summary: \"This book discusses Portugese irregular verbs in great details.\"
cover:
    # image: \"book1.png\"
    alt: \"Portugese Irregular Verbs\"
    relative: false
editPost:
    URL: \"https://ljukkti.github.io/sorali-codex/tags/senate/\" 
    Text: \"Imperial Senate\"
showToc: false
disableAnchoredHeadings: false

---

#### Description
e wait

[^1]: The acknowledged aim of the book is to dwarf all other books in the field.
[^2]: As a result of such intensive research, the book's length is almost twelve hundred pages.

---

#### Praise

> There is nothing more to be said on this subject. Nothing - Anonymous reviewer

---

#### View

+ [Chapter 1: History of the Portuguese language](chapter1.pdf)
+ [Chapter 2: Review of regular verbs](chapter2.pdf)
+ [Chapter 3: Analysis of irregular verbs](chapter3.pdf)

---

#### Excerpt from Chapter 1

---

#### Citation
"""

# Generate 20 folders and markdown files
for i in range(1, 3):
    folder_name = f"bill{i}"
    file_name = f"{folder_name}.md"
    
    # Create the folder
    os.makedirs(folder_name, exist_ok=True)
    
    # Create and write the markdown file
    with open(os.path.join(folder_name, file_name), 'w', encoding='utf-8') as f:
        f.write(md_content)

print("20 markdown files have been successfully generated.")
