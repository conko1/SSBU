from PIL import Image
import pandas as pd

def ul_11():
    img = Image.open("data/microscope.jpg")
    img = img.rotate(90)
    img.save("data/microscope.jpg")


def ul_15():
    with open("data/example.csv", "r") as file:
        df = pd.read_csv("data/example.csv")  # Načítanie CSV súboru do DataFrame
        print(df)  # Zobrazenie celého DataFrame
        print("\nŠtatistiky dát:\n", df.describe())


def ul_2_3():
    df = pd.read_csv("data/patients.csv")
    df.columns = ["name", "diagnosis"]
    df["ID"] = range(19)
    diagnosis_counts = df["diagnosis"].value_counts()
    print(df)
    print("\nPočet diagnóz:\n", diagnosis_counts)


def ul_2_4():
    img = Image.open("data/microscope.jpg")
    cropped_img = img.crop((300, 550, 1000, 1250))
    cropped_img.show()


def ul_2_5():
    class PatientData:
        def __init__(self, file_path):
            self.df = pd.read_csv(file_path, header=None)
            self.df.columns = ["name", "diagnosis"]

        def count_diagnoses(self):
            return self.df["diagnosis"].value_counts()

        def get_most_common_diagnosis(self, n):
            return self.df["diagnosis"].value_counts().head(n)

        def display_summary(self):
            print(self.df.describe())

    patient_data = PatientData("data/patients.csv")

    print("Počet pacientov s jednotlivými diagnózami:")
    print(patient_data.count_diagnoses())

    print("\n3 najčastejšie diagnózy:")
    print(patient_data.get_most_common_diagnosis(3))

    print("\nZákladné štatistiky:")
    patient_data.display_summary()


ul_2_4()
