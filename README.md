# 🍃 Brightway Course: Pre-Work Instructions

> [cite_start]This is an introductory course with the purpose of becoming familiar with Brightway and the Activity Browser interface[cite: 1].

Welcome to the course repository! [cite_start]To ensure our 2-hour session is a success, please complete these setup steps on your computer **before** the course begins. [cite_start]The final steps involve a large download and may take some time, so please plan accordingly[cite: 3].

[cite_start]This guide is for **MS Windows** users and assumes no prior programming experience[cite: 4].

---

## Step 1: Install Miniconda

[cite_start]Miniconda is a free program that manages our Python software[cite: 5]. [cite_start]This is the only program you need to install from the web[cite: 6].

1.  Go to the [Miniconda download page for Windows](https://docs.anaconda.com/free/miniconda/miniconda-install/#windows-installers).
2.  [cite_start]Download the latest **Windows 64-bit installer**[cite: 7].
3.  Run the installer file you downloaded. [cite_start]Accept the default settings for all installation steps[cite: 8].

---

## Step 2: Download and Prepare Course Materials

[cite_start]All the files you need for the course are stored in this repository[cite: 9].

1.  [cite_start]On the GitHub page, click the green **`< > Code`** button[cite: 10].
2.  [cite_start]In the dropdown menu, click **`Download ZIP`**[cite: 11].
3.  [cite_start]A file named `brightway_eut-main.zip` (or similar) will be saved, likely to your `Downloads` folder[cite: 11, 13].
4.  Find the downloaded ZIP file. [cite_start]Right-click it and select **`Extract All...`**[cite: 14].
5.  After extraction, you will have a folder named `brightway_eut-main`. **Rename this folder** to exactly `brightway_course`[cite: 15].
6.  [cite_start]Finally, **move the `brightway_course` folder** to your **Desktop**[cite: 16].

---

## Step 3: Install the Software Environment

[cite_start]This step uses the command line to automatically install all our course software[cite: 17].

1.  [cite_start]**Open the Anaconda Prompt.** Click your Windows Start Menu, type `Anaconda Prompt`, and click on the result[cite: 18]. [cite_start]A black terminal window will open[cite: 19].
2.  [cite_start]**Navigate to your course folder.** Type the following command exactly and press Enter[cite: 19]:
    ```
    cd Desktop\brightway_course
    ```
3.  [cite_start]**Create the software environment.** This command reads the `environment.yaml` file and installs everything[cite: 19]. [cite_start]This will take 5-10 minutes and requires an internet connection[cite: 20].
    ```
    conda env create -f environment.yaml
    ```
    > [cite_start]If you are asked to agree to terms, type `y` and press Enter[cite: 21].

---

## Step 4: Download the Ecoinvent Database

[cite_start]Now you need to download the raw data file[cite: 22].

1.  [cite_start]Click the following link to download the required file: [Download Ecoinvent 3.11 ecoSpold02](https://eurecatcloud.sharepoint.com/:u:/s/WEEIUnit-LiniaImpacteAmbiental/EWTDKOQCCmVOrS1IA_YFRZ4BT91T2UDVE3I5gGJA9H_ycQ?e=1xlXv8)[cite: 23].
2.  [cite_start]The file is named `ecoinvent 3.11_cutoff_ecoSpold02.7z`[cite: 23, 24].
3.  [cite_start]**Crucially, move this downloaded `.7z` file** into the `brightway_course` folder on your Desktop[cite: 24]. [cite_start]The folder should now contain this file alongside the other course materials[cite: 25].

---

## Step 5: Import the Ecoinvent Database into Brightway

[cite_start]This is the final setup step[cite: 26]. [cite_start]We will run a script that sets up the database for you[cite: 27].

1.  [cite_start]If you closed it, open the **Anaconda Prompt** and navigate to the course folder again[cite: 28]:
    ```
    cd Desktop\brightway_course
    ```
2.  [cite_start]**Activate the environment.** You must do this every time you want to use the course software[cite: 28].
    ```
    conda activate bw-course
    ```
    > [cite_start]You'll know it worked if the prompt changes from `(base)` to `(bw-course)`[cite: 29].
3.  [cite_start]**Run the import script.** This will take 10-20 minutes[cite: 30]. [cite_start]Type the following command and press Enter[cite: 30]:
    ```
    python import_ecoinvent.py
    ```
    [cite_start]You will see a lot of text as the script works[cite: 31].

---

## ✅ Readiness Checklist

[cite_start]You are ready for the course if[cite: 32]:
* The final command (`python import_ecoinvent.py`) finishes with a "SUCCESS" message[cite: 32].
* [cite_start]You did not see any major red "ERROR" messages during the process[cite: 33].

### 🆘 Getting Help

[cite_start]If you encounter any issues, please contact your instructor **before** the session begins[cite: 34]. [cite_start]Looking forward to seeing you in the course! [cite: 35]