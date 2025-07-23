# 🐿️ Squirrel Fur Color Count (Pandas Project)

This Python script analyzes real-world data from the 2018 Central Park Squirrel Census to count the number of squirrels by primary fur color using the `pandas` library.

---

## 📁 Project Structure

```

squirrel\_fur\_color/
├── squirrel\_count.py              # Main analysis script
├── 2018\_Central\_Park\_Squirrel\_Census\_\*.csv  # Input dataset
├── squirrel\_count.csv             # Output summary CSV
└── README.md                      # Project documentation

---

## 📊 What the Script Does

- Reads the 2018 Central Park Squirrel Census data from a `.csv` file.
- Extracts and counts occurrences of each squirrel fur color:
  - Gray
  - Cinnamon
  - Black
- Organizes the results into a new dataframe.
- Saves the summary as a new CSV file: `squirrel_count.csv`.

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system.
2. Install `pandas` if not already available:

```bash
pip install pandas
````

3. Place the dataset (`2018_Central_Park_Squirrel_Census_...csv`) in the same directory as the script.
4. Run the script:

```bash
python squirrel_count.py
```

5. The result will be saved as `squirrel_count.csv`.

---

## 🧠 Key Concepts Used

* Reading CSVs with `pandas.read_csv`
* Filtering rows by column values
* Counting row matches using `len()`
* Creating new DataFrames from dictionaries
* Exporting data to CSV

---

## ✅ Requirements

* Python 3.x
* pandas

---

A simple yet effective example of real-world data analysis using pandas.


