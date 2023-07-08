import tkinter
import random
import UESNames as Nirn
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("400x400")
root.title("Elder Scrolls Name Generator")

gender_var = customtkinter.Variable()   # gender variable
race_var = customtkinter.Variable()   # race variable
checkbox_var = customtkinter.Variable()   # checkbox variable for redguard suffix


def generate_button():  # generate button function, return names based on user input
    name = "prisoner"
    gender = gender_var.get()
    race = race_var.get()
    checkbox = checkbox_var.get()
    if gender == "Male" and race == "Altmer":
        name = random.choice(Nirn.altmer_male_names)
    if gender == "Male" and race == "Argonian":
        name = random.choice(Nirn.argonian_male_names)
    if gender == "Male" and race == "Breton":
        name = random.choice(Nirn.breton_male_names)
    if gender == "Male" and race == "Bosmer":
        name = random.choice(Nirn.bosmer_male_names)
    if gender == "Male" and race == "Dunmer":
        name = random.choice(Nirn.dunmer_male_names)
    if gender == "Male" and race == "Khajiit":
        name = random.choice(Nirn.khajiit_male_names)
    if gender == "Male" and race == "Nord":
        name = random.choice(Nirn.nord_male_names)
    if gender == "Female" and race == "Altmer":
        name = random.choice(Nirn.altmer_female_names)
    if gender == "Female" and race == "Argonian":
        name = random.choice(Nirn.argonian_female_names)
    if gender == "Female" and race == "Breton":
        name = random.choice(Nirn.breton_female_names)
    if gender == "Female" and race == "Bosmer":
        name = random.choice(Nirn.bosmer_female_names)
    if gender == "Female" and race == "Dunmer":
        name = random.choice(Nirn.dunmer_female_names)
    if gender == "Female" and race == "Khajiit":
        name = random.choice(Nirn.khajiit_female_names)
    if gender == "Female" and race == "Nord":
        name = random.choice(Nirn.nord_female_names)
    if gender == "Male" and race == "Redguard":
        if checkbox == "1":
            name = (random.choice(Nirn.redmpre) + random.choice(Nirn.redmv) + random.choice(Nirn.redmc)
                    + random.choice(Nirn.redmsuf))
        else:
            name = (random.choice(Nirn.redmpre) + random.choice(Nirn.redmv) + random.choice(Nirn.redmc))
    if gender == "Female" and race == "Redguard":
        if checkbox == "1":
            name = (random.choice(Nirn.redfpre) + random.choice(Nirn.redfv) + random.choice(Nirn.redfc) +
                    random.choice(Nirn.redfsuf) + random.choice(Nirn.redfsuf2))
        else:
            name = (random.choice(Nirn.redfpre) + random.choice(Nirn.redfv) + random.choice(Nirn.redfc) +
                    random.choice(Nirn.redfsuf2))
    textbox.delete(1.0, tkinter.END)
    textbox.insert(text=name, index=tkinter.INSERT)  # Set the generated name in the textbox

# CTKWidgets


gender_label = customtkinter.CTkLabel(master=root, text="Select Gender:")
gender_label.pack()

male_checkbox = customtkinter.CTkRadioButton(master=root, text="Male", variable=gender_var, value="Male")
male_checkbox.pack()

female_checkbox = customtkinter.CTkRadioButton(master=root, text="Female", variable=gender_var, value="Female")
female_checkbox.pack()

race_label = customtkinter.CTkLabel(master=root, text="Select Race:")
race_label.pack()

altmer_checkbox = customtkinter.CTkRadioButton(master=root, text="Altmer", variable=race_var, value="Altmer")
altmer_checkbox.pack()

argonian_checkbox = customtkinter.CTkRadioButton(master=root, text="Argonian", variable=race_var, value="Argonian")
argonian_checkbox.pack()

breton_checkbox = customtkinter.CTkRadioButton(master=root, text="Breton", variable=race_var, value="Breton")
breton_checkbox.pack()

bosmer_checkbox = customtkinter.CTkRadioButton(master=root, text="Bosmer", variable=race_var, value="Bosmer")
bosmer_checkbox.pack()

dunmer_checkbox = customtkinter.CTkRadioButton(master=root, text="Dunmer", variable=race_var, value="Dunmer")
dunmer_checkbox.pack()

khajiit_checkbox = customtkinter.CTkRadioButton(master=root, text="Khajiit", variable=race_var, value="Khajiit")
khajiit_checkbox.pack()

nord_checkbox = customtkinter.CTkRadioButton(master=root, text="Nord", variable=race_var, value="Nord")
nord_checkbox.pack()

redguard_checkbox = customtkinter.CTkRadioButton(master=root, text="Redguard", variable=race_var, value="Redguard")
redguard_checkbox.pack()

checksuffix = customtkinter.CTkCheckBox(master=root, text="Suffix (Redguard Only (Recommended for male))",
                                        variable=checkbox_var, onvalue="1",
                                        offvalue="0")
checksuffix.pack()

button = customtkinter.CTkButton(master=root, text="Generate Name", command=generate_button)
button.pack()

textbox = customtkinter.CTkTextbox(master=root, width=120, height=20)
textbox.pack()

root.mainloop()
