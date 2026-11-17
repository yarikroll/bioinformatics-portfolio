# Educational Bioinformatics Parsers (From Scratch)

A minimal, dependency-free Python implementation of FASTA and FASTQ parsers, written for educational purposes. 

## Motivation

Most beginners are taught to use `Biopython` to handle sequence files. While it is the correct tool for production, it acts as a black box. When a FASTQ file is truncated or contains a mismatched quality string, beginners often struggle to diagnose the error because they have never interacted with the raw structure of the file.

This repository is not a replacement for `Biopython`. It is a learning resource. The goal is to demystify the mechanics of biological file formats by implementing them from scratch, focusing on memory efficiency and error handling.

## What You Can Learn

*   **FASTA parsing:** How to handle sequences that are wrapped across multiple lines and how to avoid creating "ghost" records from empty lines.
*   **FASTQ validation:** How to read files line-by-line to avoid memory exhaustion (`readline()` vs `readlines()`), and how to detect truncated files where the end-of-file occurs in the middle of a record.
*   **Data integrity:** Why the sequence length must always equal the quality string length, and how to compute Phred quality scores (Q-scores) from ASCII characters using the Phred+33 offset.

## Repository Structure

```text
├── fasta_parser.py      # Parses FASTA files and returns a dictionary of {id: length}
├── fastq_validator.py   # Validates FASTQ structure and checks for truncation
└── README.md
```
## Requirements
*  Python 3.6 or higher.

*  No external dependencies (no pip install required).
## Usage
* **FASTA Parser**
```
from fasta_parser import parse_fasta

records = parse_fasta("example.fasta")
print(records)
# Expected output: {'geneA': 8, 'geneB': 6}
```
* **FASTQ Validator**
```
from fastq_validator import validate_fastq

try:
    validate_fastq("example.fastq")
    print("File is valid.")
except ValueError as e:
    print(f"Validation failed: {e}")
```
## Limitations
This is an educational implementation, not production software. It does not handle every edge case defined in the official specifications (e.g., multi-line FASTQ records, which are rare but technically allowed). For real-world analyses, use Biopython or needletail.
## Author
Yarikroll - Undergraduate BME student.
This project is part of a self-directed curriculum to build foundational skills for a PhD in Bioinformatics.
