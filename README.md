# Disease Prediction System

This project is a Python-based diagnostic tool that uses a **Naive Bayes** approach to predict potential illnesses based on user-reported symptoms. It processes a historical dataset to calculate the probability of specific diseases.

---

## 📂 Project Structure

* **`disease_predictor.py`**: The main Python script containing the logic for data loading, model training (probability calculation), and the interactive user interface.
* [cite_start]**`disease_dataset.csv`**: A dataset containing 50 records of various diseases (COVID-19, Influenza, Asthma, etc.) and their associated symptoms marked as binary values (1 for yes, 0 for no). [cite: 1]

---

## 🚀 How It Works

The system follows a simple four-step pipeline:

1.  **Data Loading**: Reads the CSV file and identifies the list of unique symptoms and diseases.
2.  **Training**: Calculates the frequency of each disease and the frequency of symptoms occurring within those diseases.
3.  **User Input**: An interactive loop asks the user to confirm or deny the presence of specific symptoms (e.g., fever, cough, fatigue).
4.  **Prediction**: Using the Naive Bayes formula with **Laplace Smoothing**, it calculates a probability score for each disease and displays the **Top 3 matches**.

---

## 🛠️ Installation & Usage

### Prerequisites
* Python 3.x installed on your system.

### Running the Program
1.  Ensure `disease_predictor.py` and `disease_dataset.csv` are in the same folder.
2.  Open your terminal or command prompt.
3.  Run the script:
    ```bash
    python disease_predictor.py
    ```
4.  Follow the on-screen prompts by typing `y` (yes) or `n` (no) for each symptom.

---

## 📊 Dataset Coverage
[cite_start]The system can currently predict the following conditions based on the provided data[cite: 1]:
* Common Cold
* Influenza
* COVID-19
* Malaria
* Dengue
* Typhoid
* Pneumonia
* Gastroenteritis
* Asthma
* Chickenpox

---

## ⚠️ Disclaimer
**This tool is for educational purposes only.** The predictions are based on a small, static dataset and do not constitute a professional medical diagnosis. Always consult a healthcare professional for medical advice.
