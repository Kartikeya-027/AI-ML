
import csv


def load_data(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data


def train(data):
    disease_count = {}     
    symptom_count = {}     
    symptoms_list = []

    for key in data[0].keys():
        if key != "disease":
            symptoms_list.append(key)

    for row in data:
        disease = row["disease"]

        if disease not in disease_count:
            disease_count[disease] = 0
            symptom_count[disease] = {}
            for s in symptoms_list:
                symptom_count[disease][s] = 0

        disease_count[disease] += 1

        for s in symptoms_list:
            if row[s] == "1":
                symptom_count[disease][s] += 1

    return disease_count, symptom_count, symptoms_list



def predict(user_symptoms, disease_count, symptom_count, symptoms_list):
    scores = {}

    total_records = sum(disease_count.values())

    for disease in disease_count:
        score = disease_count[disease] / total_records

        count = disease_count[disease]

        for symptom in symptoms_list:
            prob = (symptom_count[disease][symptom] + 1) / (count + 2)  

            if user_symptoms[symptom] == 1:
                score = score * prob
            else:
                score = score * (1 - prob)

        scores[disease] = score

    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_scores

def get_user_symptoms(symptoms_list):
    print("\n--- Enter your symptoms ---")
    print("Type 'y' for yes and 'n' for no\n")

    user_symptoms = {}

    for symptom in symptoms_list:
        readable = symptom.replace("_", " ").capitalize()

        answer = ""
        while answer not in ["y", "n"]:
            answer = input(f"Do you have {readable}? (y/n): ").strip().lower()

        if answer == "y":
            user_symptoms[symptom] = 1
        else:
            user_symptoms[symptom] = 0

    return user_symptoms


def show_results(sorted_scores):
    print("\n--- Prediction Results ---\n")

    top3 = sorted_scores[:3]

    total = sum(score for _, score in top3)

    for i, (disease, score) in enumerate(top3):
        if total > 0:
            percent = (score / total) * 100
        else:
            percent = 0

        rank = i + 1
        print(f"#{rank} {disease}  ->  {percent:.1f}% match")

    print("\nNOTE: This is not a medical diagnosis. Please consult a doctor.")


def main():
    print("=================================")
    print("   Disease Prediction System     ")
    print("=================================")

    filename = "disease_dataset.csv"
    data = load_data(filename)
    print(f"\nDataset loaded: {len(data)} records found")

    disease_count, symptom_count, symptoms_list = train(data)
    print(f"Diseases in dataset: {list(disease_count.keys())}")

    while True:
        user_symptoms = get_user_symptoms(symptoms_list)

        results = predict(user_symptoms, disease_count, symptom_count, symptoms_list)

        show_results(results)

        
        again = input("\nDo you want to check again? (Y/N): ").strip().lower()
        if again != "Y":
            print("\nGoodbye! Stay healthy.")
            break

main()
