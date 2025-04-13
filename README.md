# PDF Merger

A simple Python project to merge multiple PDF files into one.

## Features

- Automatically scans the `pdfs/` folder for PDF files
- Merges multiple PDF files into a single file
- Outputs the result to the `merged/` folder as `result.pdf`
- Skips merge and exits quietly if no PDFs are found

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/pdf-merger.git
cd pdf-merger
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate         # On Windows
source venv/bin/activate        # On macOS/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add your PDF files

Place all the PDF files you want to work with inside the `pdfs/` folder.

### 5. Run the script

```bash
python merge.py
```

If there are PDF files in the folder, a `merged/result.pdf` will be created.

## Project Structure

```
pdf-merger/
├── venv/               # Virtual environment (ignored by Git)
├── pdfs/               # Folder with input PDF files
│   └── .gitkeep        # Placeholder to track folder in Git
├── merged/             # Output folder (created if PDFs are found)
├── merge.py            # Python script that performs the merge
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore rules
└── README.md           # Project documentation
```

## Dependencies

- PyPDF2

## Notes

- Make sure to activate your virtual environment every time you start working.
- The script will not create any output unless valid PDF files are found.
- The `merged/` folder is created only when needed.
- `venv/` is excluded from version control using `.gitignore`.

## License

MIT License
