import tkinter as tk
from tkinter import *

def calculate_bmi():
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
        bmi = weight / (height * height)
        
        if bmi < 18.5:
            category = 'Underweight'
        elif 18.5 <= bmi <= 24.9:
            category = 'Healthy Weight'
        elif 25.0 <= bmi <= 29.9:
            category = 'Overweight'
        else:
            category = 'Obesity'
        
        result_label.config(text=f'Your Body Mass Index (BMI) is: {bmi:.2f}\nCategory: {category}')
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height")

# Creating the main window
window = tk.Tk()
window.title("BMI Calculator")

formula_label = tk.Label(window, text='Formula: BMI = weight (in kg) / height (in meters)²')
formula_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# weight label and entry
weight_label = tk.Label(window, text="Enter weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=10)

weight_entry = tk.Entry(window)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

# height label and entry
height_label = tk.Label(window, text="Enter height (m):")
height_label.grid(row=2, column=0, padx=10, pady=10)

height_entry = tk.Entry(window)
height_entry.grid(row=2, column=1, padx=10, pady=10)

# calculate button
calculate_button = tk.Button(window, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# the result label
result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()
