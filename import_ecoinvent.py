import sys
import os
import shutil
import py7zr
import appdirs

# --- Configuration ---
# Name for the Brightway project
PROJECT_NAME = "bw-course-project"
# Name for the database once imported
DB_NAME = "ecoinvent-3.11-cutoff"
# Filename of the downloaded Ecoinvent data
ECOINVENT_FILE = "ecoinvent 3.11_cutoff_ecoSpold02.7z"
# Temporary directory for extracted files
EXTRACT_DIR = "extracted_ecoinvent_data"
# ---------------------

# --- Main import logic ---
# It's better to import brightway after the reset logic to avoid
# any potential file-locking issues, although it's rare.
print("--- Brightway Database Importer for Eurecat Course ---")

# --- Step 1: Clean Slate Reset ---
# This "hard reset" is the most robust way to ensure every student
# starts from the same clean state[cite: 37].
print(f"\n[Step 1/4] Checking for and removing any old '{PROJECT_NAME}' project data...")
bw2_projects_dir = appdirs.user_data_dir("pylca", "Brightway2") [cite: 39]
project_dir = os.path.join(bw2_projects_dir, PROJECT_NAME)
if os.path.exists(project_dir):
    shutil.rmtree(project_dir, ignore_errors=True)
print("Reset complete.")

# Now, with a clean directory, we import the Brightway2 libraries
import brightway2 as bw
import bw2io

# --- Step 2: Brightway Setup ---
# Set up the project and download standard data (biosphere, methods).
# This requires an internet connection on the first run[cite: 41].
print(f"\n[Step 2/4] Setting up new Brightway project: '{PROJECT_NAME}'...")
bw.projects.set_current(PROJECT_NAME)
print("Downloading and installing standard data (biosphere, LCIA methods)...")
bw2io.bw2setup() [cite: 42]

# --- Step 3: Find and Extract Ecoinvent Data ---
current_path = os.getcwd()
file_path = os.path.join(current_path, ECOINVENT_FILE)
extract_path = os.path.join(current_path, EXTRACT_DIR)

if DB_NAME in bw.databases:
    print(f"\nDatabase '{DB_NAME}' already exists. Nothing to do.")
    print("\n✅ SUCCESS: You are all set for the course!")
    sys.exit(0)

if not os.path.exists(file_path):
    print(f"\n❌ ERROR: Ecoinvent file not found!", file=sys.stderr)
    print(f"Please make sure the file '{ECOINVENT_FILE}' is in this folder:", file=sys.stderr) [cite: 43]
    print(f"--> {current_path}", file=sys.stderr)
    sys.exit(1)

print(f"\n[Step 3/4] Found Ecoinvent data file. Extracting...")
try:
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)
    with py7zr.SevenZipFile(file_path, mode='r') as z: [cite: 44]
        z.extractall(path=extract_path) [cite: 44]
    print("Extraction complete.")
except Exception as e:
    print("\n❌ ERROR: Could not extract the .7z file.", file=sys.stderr)
    print(f"It might be corrupted. Try downloading '{ECOINVENT_FILE}' again.", file=sys.stderr)
    print(f"Detailed error: {e}", file=sys.stderr)
    sys.exit(1)

# --- Step 4: Import Database ---
# The actual data is usually in a 'datasets' subfolder
import_path = os.path.join(extract_path, 'datasets')
if not os.path.exists(import_path):
    subfolders = [f.path for f in os.scandir(extract_path) if f.is_dir()]
    import_path = subfolders[0] if subfolders else extract_path [cite: 45]

print(f"Data for import found at: {import_path}")
print(f"\n[Step 4/4] Starting database import into Brightway...") [cite: 46]
print("This is the longest step (10-20 minutes) and uses a lot of memory.") [cite: 46]

try:
    importer = bw2io.SingleOutputEcospold2Importer(import_path, DB_NAME)
    importer.apply_strategies()
    importer.statistics()
    importer.write_database()
    print(f"\n✅ SUCCESS: Database '{DB_NAME}' has been imported!")
except Exception as e: [cite: 47]
    print("\n❌ ERROR: An unexpected error occurred during import.", file=sys.stderr) [cite: 47]
    print("Please check if you have enough free RAM and disk space.", file=sys.stderr) [cite: 47]
    print(f"Detailed error: {e}", file=sys.stderr)
    sys.exit(1)