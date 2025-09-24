# 🍃 Brightway Course: Session Guide

[cite_start]Welcome to the introductory session on Brightway! [cite: 69] [cite_start]This document will serve as our guide for the next two hours[cite: 70].

[cite_start]**Course Goal:** By the end of this session, you will be able to perform fundamental Life Cycle Assessment (LCA) operations in Brightway using both Python code and the Activity Browser graphical interface[cite: 72].

[cite_start]**Prerequisites:** It is expected that you have completed all the pre-work instructions in the `README.md` file[cite: 73].

---

### Part 1: Launching Our Environment & Finding Data

[cite_start]**Goal:** In this section, we'll start our coding environment and learn how to connect to the Ecoinvent database to find specific processes[cite: 74].

1.  **Launch the Environment:**
    * [cite_start]First, open the **Anaconda Prompt** from your Start Menu[cite: 75].
    * [cite_start]In the terminal window, navigate to our course folder by typing `cd Desktop\brightway_course` and pressing Enter[cite: 76].
    * [cite_start]Next, activate our software environment by typing `conda activate bw-course` and pressing Enter[cite: 77].
    * [cite_start]Finally, start the Jupyter Lab interface by typing `jupyter lab` and pressing Enter[cite: 78]. [cite_start]This will open a new tab in your web browser[cite: 79].

2.  **Open the Notebook:**
    * [cite_start]In the Jupyter Lab browser tab, find and double-click the `Brightway_Session.ipynb` file to open it[cite: 80].
    > **What are Jupyter Notebooks?** They are interactive lab notebooks for code, letting us write and run code in small blocks (cells) and see the output immediately[cite: 81, 82].

3.  **Find an Activity:**
    * [cite_start]In the notebook, we will run the first few code cells to import the Brightway library and connect to the `ecoinvent-3.11-cutoff` database[cite: 84].
    * [cite_start]We will then use the `.search()` method to look for the Spanish process for operating an electric water pump[cite: 85].

---

### Part 2: Calculating Environmental Impact with Code

[cite_start]**Goal:** Now we'll use Python to perform a complete, simple Life Cycle Assessment and explore the results[cite: 87].

1.  **Run a Simple LCA:**
    * [cite_start]To perform an LCA, we need a **functional unit** and an **impact method**[cite: 88].
    * [cite_start]We will search for the "IPCC 2021" method for Global Warming Potential (GWP)[cite: 89].
    * [cite_start]We'll perform the LCA calculation using the `.lci()` and `.lcia()` functions and interpret the final score[cite: 90].

2.  **Explore the Technosphere:**
    * [cite_start]We will look inside the process to see its direct inputs, also called the **technosphere**[cite: 92].
    * [cite_start]We will run code that iterates through the `.technosphere()` exchanges to see the underlying processes[cite: 93].

---

### Part 3: Visual Exploration with the Activity Browser

[cite_start]**Goal:** A graphical interface is often better for exploration[cite: 94]. [cite_start]Here, we'll learn to use the Activity Browser[cite: 95].

1.  **Launch Activity Browser:**
    * [cite_start]Go back to your Anaconda Prompt window (or open a new one and activate the `bw-course` environment)[cite: 95].
    * [cite_start]Type `activity-browser` and press Enter[cite: 96].
    * [cite_start]When prompted, select the `ecoinvent-3.11-cutoff` database[cite: 96].

2.  **Perform an LCA in the GUI:**
    * [cite_start]We will find the same `'water pump operation, electric'` process using the search bar[cite: 97].
    * [cite_start]We will then walk through the steps to select a functional unit, choose an LCIA method, and run the calculation[cite: 98].

3.  **Import Data from Excel (Brief Overview):**
    * [cite_start]We will see how the Activity Browser can import inventory data using the `Database` -> `Import from Excel` menu option[cite: 100].

---

### Part 4: Bonus - Comparative LCA

[cite_start]**Goal:** To finish, we'll see a powerful feature of using code: creating a new process to compare scenarios[cite: 101].

1.  **Create a New Process from Code:**
    * [cite_start]Returning to our Jupyter Notebook, we will see how the pump's carbon footprint changes if we run it with French electricity instead of Spanish[cite: 102].
    * [cite_start]We will run cells that programmatically: **Copy** the original activity, **Find** the French electricity market, **Swap** the electricity input, and **Save** the new activity[cite: 103, 104, 105].

2.  **Compare the Results:**
    * [cite_start]Finally, we'll run the LCA on our new, modified activity and compare the GWP score to the original one[cite: 105].

### Session Recap & Next Steps

Congratulations! [cite_start]You have now learned how to connect to a database, find activities, perform an LCA with Python, explore inputs, use the Activity Browser, and run a comparative LCA[cite: 106, 107, 108, 109].