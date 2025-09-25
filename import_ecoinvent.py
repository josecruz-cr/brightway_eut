import sys
import os
import shutil
import py7zr
import appdirs
import traceback

# --- Configuration ---
PROJECT_NAME = "bw-course-project"       # Brightway project name
DB_NAME = "ecoinvent-3.11-cutoff"        # Name for imported database
ECOINVENT_FILE = "ecoinvent 3.11_cutoff_ecoSpold02.7z"  # Ecoinvent .7z file
EXTRACT_DIR = "extracted_ecoinvent_data"  # Temporary extraction folder
# ---------------------

print("--- Brightway Database Importer for Eurecat Course ---")

# --- Step 1: Clean Slate Reset ---
print(f"\n[Step 1/4] Removing any old project data for '{PROJECT_NAME}'...")
bw2_projects_dir = appdirs.user_data_dir("pylca", "Brightway2")
project_dir = os.path.join(bw2_projects_dir, PROJECT_NAME)
if os.path.exists(project_dir):
    shutil.rmtree(project_dir, ignore_errors=True)
print("Reset complete.")

# --- Step 2: Brightway Setup ---
import brightway2 as bw
import bw2io

print(f"\n[Step 2/4] Creating new Brightway project: '{PROJECT_NAME}'...")
bw.projects.set_current(PROJECT_NAME)

if 'biosphere3' not in bw.databases:
    print("Downloading and installing standard data (biosphere, LCIA methods)...")
    bw2io.bw2setup()
else:
    print("Standard data already installed. Skipping download.")

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
    print(f"Please make sure '{ECOINVENT_FILE}' is in this folder: {current_path}", file=sys.stderr)
    sys.exit(1)

print(f"\n[Step 3/4] Extracting Ecoinvent data from '{ECOINVENT_FILE}'...")
try:
    if os.path.exists(extract_path):
        shutil.rmtree(extract_path)
    with py7zr.SevenZipFile(file_path, mode='r') as z:
        z.extractall(path=extract_path)
    print("Extraction complete.")
except Exception as e:
    print("\n❌ ERROR: Could not extract the .7z file.", file=sys.stderr)
    print(f"It might be corrupted. Try downloading '{ECOINVENT_FILE}' again.", file=sys.stderr)
    print(f"Detailed error: {e}", file=sys.stderr)
    sys.exit(1)

# --- Step 4: Import Database ---
# Recursively find folder containing .spold files
import_path = None
for root, dirs, files in os.walk(extract_path):
    if any(f.endswith('.spold') for f in files):
        import_path = root
        break

if import_path is None:
    print("\n❌ ERROR: No .spold files found in extracted data.", file=sys.stderr)
    sys.exit(1)

print(f"Data for import found at: {import_path}")
print(f"\n[Step 4/4] Starting database import into Brightway...")
print("⚠️ This step may take 10-20 minutes and use a lot of RAM.")

try:
    if DB_NAME in bw.databases:
        print(f"Database '{DB_NAME}' exists. Removing for clean import...")
        del bw.databases[DB_NAME]

    importer = bw2io.SingleOutputEcospold2Importer(import_path, DB_NAME)
    importer.apply_strategies()
    importer.statistics()
    importer.write_database()
    print(f"\n✅ SUCCESS: Database '{DB_NAME}' has been imported!")
except Exception as e:
    print("\n❌ ERROR: An unexpected error occurred during import.", file=sys.stderr)
    print("Please check if you have enough free RAM and disk space.", file=sys.stderr)
    print(f"Detailed error: {e}", file=sys.stderr)
    print(traceback.format_exc())
    sys.exit(1)
