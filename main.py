from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=500, height=600)
window.config(padx=30, pady=50)
font_ = ("Roboto Mono", 10, "bold")


def colculator():
    def resultWriter(bmi):
        result_sentence = ""
        if bmi < 16:
            result_sentence += "severe thinness"
        elif 16 < bmi <= 18.5:
            result_sentence += "mild thinness"
        elif 18.5 < bmi <= 25:
            result_sentence += "normal"
        elif 25 < bmi <= 30:
            result_sentence += "overweight"
        else:
            result_sentence += "obese"
        return result_sentence

    weight = weight_entry.get()
    height = height_entry.get()

    if weight == "" or height == "":
        result_label.config(text="These fields cannot be left blank.")
    else:
        try:
            bmi = float(weight) / (float(height) / 100) ** 2
            result = resultWriter(bmi)
            result_label.config(text=f"Your BMI: {round(bmi,2)}. You are {result}")
        except ValueError:
            result_label.config(text="please enter a numeric variable")


# GET WEIGHT
weight_label = Label(text="Please Enter Your Weight (kg)", font=font_)
weight_label.config(padx=10, pady=10)
weight_label.pack()
weight_entry = Entry(width=30, borderwidth=2)
weight_entry.pack()

# GET HEIGHT
height_label = Label(text="Please Enter Your Height (cm)", font=font_)
height_label.config(padx=10, pady=10)
height_label.pack()
height_entry = Entry(width=30, borderwidth=2)
height_entry.pack()

# Calculate Button
cal_button = Button(text="Calculate", command=colculator)
cal_button.pack()

# Result Label
result_label = Label(text="")
result_label.pack()


mainloop()
