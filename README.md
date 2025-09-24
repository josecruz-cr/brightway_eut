# 🍃 Brightway Course: Pre-Work Instructions

> This is an introductory course performed by the Sustainable Impact team at Eurecat, with the purpose of becoming familiar with Brightway and the Activity Browser interface.

Welcome to the course repository! To ensure our 2-hour session is a success, please complete these setup steps on your computer **before** the course begins. The final steps involve a large download and may take some time, so please plan accordingly.

This guide is for **MS Windows** users and assumes no prior programming experience.

---

## Step 1: Install Miniconda

Miniconda is a free program that manages our Python software. This is the only program you need to install from the web.

1.  Go to the [Miniconda download page for Windows](https://docs.anaconda.com/free/miniconda/miniconda-install/#windows-installers).
2.  Download the latest **Windows 64-bit installer**.
3.  Run the installer file you downloaded. Accept the default settings for all installation steps.

---

## Step 2: Download and Prepare Course Materials

All the files you need for the course are stored in this repository.

1.  Click the green **`< > Code`** button on the GitHub page for this repository.
2.  In the dropdown menu, click **`Download ZIP`**.
3.  A file named `brightway_eut-main.zip` (or similar) will be saved to your `Downloads` folder.
4.  Find the downloaded ZIP file. Right-click it and select **`Extract All...`**.
5.  After extraction, you will have a folder named `brightway_eut-main`. **Rename this folder** to exactly `brightway_course`.
6.  Finally, **move the `brightway_course` folder** to your **Desktop**.

---

## Step 3: Install the Software Environment

This step uses the command line to automatically install all our course software.

1.  **Open the Anaconda Prompt.** Click your Windows Start Menu, type `Anaconda Prompt`, and click on the result. A black terminal window will open.
2.  **Navigate to your course folder.** Type the following command exactly and press Enter:
    ```
    cd Desktop\brightway_course
    ```
3.  **Create the software environment.** This command reads the `environment.yaml` file and installs all required software. This will take 5-10 minutes.
    ```
    conda env create -f environment.yaml
    ```
    > If you are asked to agree to terms, type `y` and press Enter.

---

## Step 4: Download the Ecoinvent Database

Now you need to download the raw data file.

1.  Click the following link to download the required file: [Download Ecoinvent 3.11 ecoSpold02](https://eurecatcloud.sharepoint.com/:u:/s/WEEIUnit-LiniaImpacteAmbiental/EWTDKOQCCmVOrS1IA_YFRZ4BT91T2UDVE3I5gGJA9H_ycQ?e=1xlXv8).
2.  The file is named `ecoinvent 3.11_cutoff_ecoSpold02.7z`.
3.  **Crucially, move this downloaded `.7z` file** into the `brightway_course` folder on your Desktop. The folder should now contain this file alongside the other course materials.

---

## Step 5: Import the Ecoinvent Database into Brightway

This is the final step. We will run a script that sets up the database for you.

1.  If you closed it, open the **Anaconda Prompt** again and navigate to the course folder:
    ```
    cd Desktop\brightway_course
    ```
2.  **Activate the environment.** You must do this every time you want to use the course software.
    ```
    conda activate bw-course
    ```
    > You'll know it worked if the text at the start of the prompt changes from `(base)` to `(bw-course)`.
3.  **Run the import script.** This will take 10-20 minutes. Type the following command and press Enter:
    ```
    python import_ecoinvent.py
    ```
    You will see a lot of text as it imports and processes the database.

---

## ✅ Readiness Checklist

You are ready for the course if:

* The final command (`python import_ecoinvent.py`) finishes with a "SUCCESS" message.
* You did not see any major red "ERROR" messages during the process.

### 🆘 Getting Help

If you encounter any issues, please contact your instructor **before** the session begins. Looking forward to seeing you in the course!