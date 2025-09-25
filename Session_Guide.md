# 🍃 Brightway Course: Session Guide

Welcome to the introductory session on Brightway! This document will serve as our guide for the next two hours. We'll follow the steps together, and you can use this as a reference after the course is complete.

**Course Goal:** By the end of this session, you will be able to perform fundamental Life Cycle Assessment (LCA) operations in Brightway using both Python code and the Activity Browser graphical interface.

**Prerequisites:** It is expected that you have completed all the pre-work instructions in the `README.md` file.

---

### Part 1: Launching Our Environment & Finding Data

**Goal:** In this section, we'll start our coding environment and learn how to connect to the Ecoinvent database to find specific processes.

1.  **Launch the Environment:**
    * First, open the **Anaconda Prompt** from your Start Menu.
    * In the black terminal window, navigate to our course folder by typing `cd Desktop\brightway_course` and pressing Enter.
    * Next, activate our software environment by typing `conda activate bw-course` and pressing Enter.
    * Finally, start the Jupyter Lab interface by typing `jupyter lab` and pressing Enter. This will open a new tab in your web browser.

2.  **Open the Notebook:**
    * In the Jupyter Lab browser tab, find and open the `Brightway_Session.ipynb` file.

    > **What are Jupyter Notebooks?**  
    > Jupyter Notebooks are like interactive lab notebooks for code. They let us write and run code in small blocks, called cells, and see the output immediately. We can also write notes and text, making them perfect for learning and experimenting.

3.  **Find an Activity:**
    * In the notebook, we will run the first few code cells to import the Brightway library and connect to the `ecoinvent-3.9.1-cutoff` database that you installed.
    * We will then learn how to use the `.search()` method to look for a specific process: the Spanish process for operating an electric water pump. We will see how to loop through the search results to select the exact activity we want.

---

### Part 2: Calculating Environmental Impact with Code

**Goal:** Now we'll use Python to perform a complete, simple Life Cycle Assessment and explore the results.

1.  **Run a Simple LCA:**
    * To perform an LCA, we need a **functional unit** (our water pump activity) and an **impact method**.
    * We will search for the "IPCC 2021" method for Global Warming Potential (GWP).
    * Using our functional unit and method, we'll perform the LCA calculation using the `lca.lci()` and `lca.lcia()` functions and interpret the final score.

2.  **Explore the Technosphere:**
    * What makes up that final impact score? We will look inside the process to see its direct inputs, also called the **technosphere**.
    * We will run the code that iterates through the `.technosphere()` exchanges to see the underlying processes, paying close attention to the electricity input.

---

### Part 3: Visual Exploration with the Activity Browser

**Goal:** While code is powerful, a graphical interface is often better for exploration. Here, we'll learn to use the Activity Browser.

1.  **Launch Activity Browser:**
    * Go back to your Anaconda Prompt window (or open a new one and activate the `bw-course` environment).
    * Type `activity-browser` and press Enter.
    * When prompted, select the `ecoinvent-3.9.1-cutoff` database.

2.  **Perform an LCA in the GUI:**
    * We will find the same `'water pump operation, electric'` process using the search bar.
    * We will then walk through the steps to select a functional unit, choose an LCIA method, and run the calculation to see the results and Sankey diagrams.

3.  **Import Data from Excel:**
    * A common task is to import your own inventory data. We will see how the Activity Browser makes this easy by using the `Database` -> `Import from Excel` menu option.

---

### Part 4: Bonus - Comparative LCA

**Goal:** To finish, we'll see a powerful feature of using code: creating a new process to compare scenarios.

1.  **Create a New Process from Code:**
    * Returning to our Jupyter Notebook, we will see how the pump's carbon footprint changes if we run it with French electricity instead of Spanish.
    * We will run cells that programmatically:
        1.  **Copy** the original Spanish water pump activity.
        2.  **Find** the French low-voltage electricity market.
        3.  **Swap** the electricity input in our new copied activity.
        4.  **Save** the new activity.

2.  **Compare the Results:**
    * Finally, we'll run the LCA on our new, modified activity and compare the GWP score to the original Spanish one.

---

### Session Recap & Next Steps

Congratulations! You have now learned how to:
* Connect to an Ecoinvent database in Brightway.
* Find activities and perform an LCA using Python.
* Explore the inputs of a unit process.
* Use the Activity Browser for visual analysis and data import.
* Create a new process from an existing one to run a comparative LCA.

For further learning, we recommend exploring the [official Brightway documentation](https://docs.brightway.dev/) and community forums like [Stack Overflow](https://stackoverflow.com/questions/tagged/brightway).
