#!/usr/bin/env python3
"""
Brightway2 Ecoinvent Import Script (for course use)

Assumptions:
 - You are using Brightway2 (classic stack, not brightway25).
 - Activity Browser is installed in the same conda env.
 - Ecoinvent 3.9.1 (cutoff, ecoSpold02 format) has already been unzipped manually.
 - The extracted folder is named exactly: "ecoinvent 3.9.1_cutoff_ecoSpold02".
 - Inside that folder there is a subfolder called "datasets" with the .spold files.

Behavior:
 - Ensures a clean Brightway2 project environment.
 - Installs biosphere3 + LCIA methods if missing.
 - Imports Ecoinvent into Brightway2.
"""

import os
import sys
import traceback

# --- Configuration ---
PROJECT_NAME = "bw-course-project"
DB_NAME = "ecoinvent-3.9.1-cutoff"
ECOINVENT_DIR = "ecoinvent 3.9.1_cutoff_ecoSpold02"  # Folder name after manual extraction
# ----------------------

print("--- Brightway2 Ecoinvent Importer ---\n")

# Step 1: Import Brightway2 packages
print("[1/4] Importing Brightway packages...")
try:
    import brightway2 as bw
    import bw2io
except Exception as e:
    print("ERROR: Could not import Brightway2 packages.")
    print("Did you activate the 'bw-course' conda environment?")
    print("Detailed error:", e)
    sys.exit(1)
print("Packages imported.\n")

# Step 2: Set up project and biosphere
print("[2/4] Setting up Brightway2 project...")
bw.projects.set_current(PROJECT_NAME)

if "biosphere3" not in bw.databases:
    print(" - Installing standard biosphere and LCIA methods...")
    bw2io.bw2setup()
else:
    print(" - Biosphere already present.")
print()

# Step 3: Locate ecoinvent datasets folder
print("[3/4] Checking ecoinvent folder...")
spold_dir = os.path.join(ECOINVENT_DIR, "datasets")

if not os.path.isdir(spold_dir):
    print(f"ERROR: Could not find datasets folder at: {spold_dir}")
    print("Make sure you unzipped ecoinvent and kept the folder structure intact.")
    sys.exit(1)

print(f" - Found .spold folder at: {spold_dir}\n")

# Step 4: Import ecoinvent
print("[4/4] Importing ecoinvent...")
try:
    if DB_NAME in bw.databases:
        print(f" - Database '{DB_NAME}' already exists. Skipping import.")
    else:
        importer = bw2io.SingleOutputEcospold2Importer(spold_dir, DB_NAME)
        importer.apply_strategies()
        importer.statistics()
        importer.write_database()
        print(f" - Successfully imported '{DB_NAME}' with {len(bw.Database(DB_NAME))} activities.")
except Exception as e:
    print("ERROR: Import failed.")
    print(traceback.format_exc())
    sys.exit(1)

print("\nAll done. You can now open Activity Browser and explore the database.")
