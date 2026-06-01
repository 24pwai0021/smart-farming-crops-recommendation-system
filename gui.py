import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import pandas as pd
import joblib
import fertilizer

# Load model
model = joblib.load("crop_model.pkl")

# ---------------- PREDICT FUNCTION ----------------
def predict():
    try:
        sample = pd.DataFrame({
            "N": [float(n.get())],
            "P": [float(p.get())],
            "K": [float(k.get())],
            "temperature": [float(temp.get())],
            "humidity": [float(humidity.get())],
            "ph": [float(ph.get())],
            "rainfall": [float(rain.get())]
        })

        crop = model.predict(sample)[0]
        fert = fertilizer.get_fertilizer(crop)

        result_label.config(
            text=f"Recommended Crop: {crop}\n\nRecommended Fertilizer: {fert}"
        )

    except Exception:
        messagebox.showerror("Error", "Please enter valid values")

# ---------------- WINDOW ----------------
root = tk.Tk()
root.title("Smart Agriculture AI System")
root.geometry("700x600")
root.resizable(False, False)

# ---------------- BACKGROUND IMAGE ----------------
bg_image = Image.open("farm.jpg")
bg_image = bg_image.resize((700, 600))
bg_photo = ImageTk.PhotoImage(bg_image)

bg_label = tk.Label(root, image=bg_photo)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ---------------- TITLE ----------------
title = tk.Label(
    root,
    text="Crop Recommendation System",
    font=("Arial", 22, "bold"),
    bg="#411706",
    fg="#FFD0AD",
    padx=10,
    pady=12,
)
title.pack(pady=20)

# ---------------- MAIN FRAME ----------------
frame = tk.Frame(root, bg="#996512")
frame.place(relx=0.5, rely=0.55, anchor="center")

# Labels and Entries
fields = [
    ("Nitrogen (N)", "n"),
    ("Phosphorus (P)", "p"),
    ("Potassium (K)", "k"),
    ("Temperature (°C)", "temp"),
    ("Humidity (%)", "humidity"),
    ("pH Value", "ph"),
    ("Rainfall (mm)", "rain")
]

entries = {}

for i, (label_text, var_name) in enumerate(fields):
    tk.Label(
        frame,
        text=label_text,
        font=("Arial", 11, "bold"),
        bg="#996512"
    ).grid(row=i, column=0, padx=10, pady=8, sticky="w")

    entry = tk.Entry(frame, font=("Arial", 11), width=20)
    entry.grid(row=i, column=1, padx=10, pady=8)

    entries[var_name] = entry

n = entries["n"]
p = entries["p"]
k = entries["k"]
temp = entries["temp"]
humidity = entries["humidity"]
ph = entries["ph"]
rain = entries["rain"]

# ---------------- BUTTON ----------------
predict_btn = tk.Button(
    frame,
    text="PREDICT",
    command=predict,
    font=("Arial", 12, "bold"),
    bg="green",
    fg="white",
    width=15
)
predict_btn.grid(row=7, column=0, columnspan=2, pady=15)

# ---------------- RESULT ----------------
result_label = tk.Label(
    root,
    text="Enter values and click Predict",
    font=("Arial", 13, "bold"),
    bg="#996512",
    fg="black",
    wraplength=500,
    justify="center"
)

result_label.place(relx=0.5, rely=.9, anchor="center")

root.mainloop()