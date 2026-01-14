import pymupdf4llm
import sys

path = "Reports/Final Design of Drainage System Report.pdf"
md = pymupdf4llm.to_markdown(path)
print(md[:2000])
