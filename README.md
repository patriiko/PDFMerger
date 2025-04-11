# 📄 PDF Merger

A simple Python project to merge multiple PDF files into one.

## 🚀 Features

- Merge multiple PDF files into a single file
- Optionally insert a PDF into a specific position within another
- Ideal for organizing and combining documents

## 🛠 Setup Instructions

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

Modify the logic in `merge.py` according to how you want to merge or insert PDFs.

## 📂 Project Structure

```
pdf-merger/
├── venv/               # Virtual environment (ignored by Git)
├── pdfs/               # Folder with input PDF files
├── merge.py            # Your main Python script
├── requirements.txt    # Python package requirements
├── .gitignore          # Files and folders Git should ignore
└── README.md           # Project documentation
```

## 🧩 Dependencies

- PyPDF2

## ⚠️ Notes

- Make sure to activate your virtual environment every time you start working.
- `venv/` is excluded from version control using `.gitignore`.

## 📬 License

MIT License
