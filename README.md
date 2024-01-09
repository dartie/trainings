# Trainings

## Setup 

```bash
# Create dedicated virtual environment 
# (it avoids to encounter issues with markdown conversion)
virtualenv venv-trainings

# Enable virtual environment
source venv-trainings/bin/activate

# Install requirements
pip install -r requirements.txt
```

## Usage

```bash
# syntax
python create-preso.py "<file.md>" - t "<theme-name>"

# syntax
python create-preso.py Go-Nalug.md -t nalug
```