import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from PIL import Image, ImageTk
import pandas as pd

# Read the car data from a CSV file
dataframe = pd.read_csv('car details v4.csv', header=0, encoding='utf-8')

# Convert the prices to Euros
dataframe['Price'] = dataframe['Price'] * 0.011

# Function to search for cars based on selected criteria
def search_cars():
    # Get the selected values from the comboboxes
    make = make_combobox.get().replace("'", "").lower()  # Remove quotation marks and convert to lowercase
    price = price_combobox.get()
    mileage = mileage_combobox.get()
    transmission = transmission_combobox.get()
    fuel_type = fuel_combobox.get()

    # Enable editing of the results text widget
    results_text.configure(state=tk.NORMAL)
    # Clear previous search results
    results_text.delete('1.0', tk.END)

    found_cars = False

    # Iterate over each row in the dataframe
    for _, row in dataframe.iterrows():
        # Check if the car matches the selected criteria
        if (not make or make in row['Make'].lower()) and \
           (not price or (price and float(row['Price']) <= float(price.split('-')[1]) and float(row['Price']) >= float(price.split('-')[0]))) and \
           (not mileage or (mileage and float(row['Kilometer']) <= float(mileage.split('-')[1]) and float(row['Kilometer']) >= float(mileage.split('-')[0]))) and \
           (not transmission or (transmission and row['Transmission'].lower() == transmission.lower())) and \
           (not fuel_type or (fuel_type and row['Fuel Type'].lower() == fuel_type.lower())):
            # Insert car details into the results text widget
            results_text.insert(tk.END, f"Brand: {row['Make']}\n")
            results_text.insert(tk.END, f"Model: {row['Model']}\n")
            results_text.insert(tk.END, f"Year: {row['Year']}\n")
            results_text.insert(tk.END, f"Price: {round(row['Price'])} €\n")
            results_text.insert(tk.END, f"Fuel: {row['Fuel Type']}\n")
            results_text.insert(tk.END, f"Transmission: {row['Transmission']}\n")
            results_text.insert(tk.END, f"Location: {row['Location']}\n")
            results_text.insert(tk.END, f"Color: {row['Color']}\n")
            results_text.insert(tk.END, f"Owner: {row['Owner']}\n")
            results_text.insert(tk.END, f"Seller type: {row['Seller Type']}\n")
            results_text.insert(tk.END, f"Engine: {row['Engine']}\n")
            results_text.insert(tk.END, f"Max Power: {row['Max Power']}\n")
            results_text.insert(tk.END, f"Max Torque: {row['Max Torque']}\n")
            results_text.insert(tk.END, f"Drivetrain: {row['Drivetrain']}\n")
            results_text.insert(tk.END, f"Length: {row['Length']}\n")
            results_text.insert(tk.END, f"Width: {row['Width']}\n")
            results_text.insert(tk.END, f"Height: {row['Height']}\n")
            results_text.insert(tk.END, f"Seating Capacity: {row['Seating Capacity']}\n")
            results_text.insert(tk.END, f"Fuel Tank Capacity: {row['Fuel Tank Capacity']}\n")
            results_text.insert(tk.END, f"Engine: {row['Engine']}\n")
            results_text.insert(tk.END, f"Mileage: {row['Kilometer']} km\n")
            results_text.insert(tk.END, '____________\n\n')
            found_cars = True

    # If no cars are found, display a message
    if not found_cars:
        results_text.insert(tk.END, "No cars found matching the criteria.\n")

    # Disable editing of the results text widget
    results_text.configure(state=tk.DISABLED)

# Function to clear the search results
def clear_results():
    # Enable editing of the results text widget
    results_text.configure(state=tk.NORMAL)
    # Clear the results
    results_text.delete('1.0', tk.END)
    # Disable editing of the results text widget
    results_text.configure(state=tk.DISABLED)
    # Reset combobox selections
    fuel_combobox.current(0)
    make_combobox.current(0)
    mileage_combobox.current(0)
    price_combobox.current(0)
    transmission_combobox.current(0)

# Create the main window
window = tk.Tk()
window.title("Car Search")
window.geometry("507x1000")

# Load and display the logo image
image = Image.open("Black and Green Modern Automotive Logo.png")
image = image.resize((500, 200))
photo = ImageTk.PhotoImage(image)
image_label = tk.Label(window, image=photo)
image_label.grid(row=0, column=1, columnspan=2)

# Create labels and comboboxes for the search criteria
make_label = ttk.Label(window, text="Brand:")
make_label.grid(row=1, column=1, padx=10, pady=5)
make_combobox = ttk.Combobox(window, values=[''] + sorted(dataframe['Make'].unique().tolist()), state='readonly')
make_combobox.grid(row=1, column=2, padx=10, pady=5)

price_label = ttk.Label(window, text="Price:")
price_label.grid(row=2, column=1, padx=10, pady=5)
price_combobox = ttk.Combobox(window, values=[''] + ["0-5000", "5000-10000", "10000-20000", "20000-30000", "30000-50000", "50000-100000", "100000-150000", "150000-200000", f"200000-{int(max(dataframe['Price']))}"], state='readonly')
price_combobox.grid(row=2, column=2, padx=10, pady=5)

mileage_label = ttk.Label(window, text="Mileage:")
mileage_label.grid(row=3, column=1, padx=10, pady=5)
mileage_combobox = ttk.Combobox(window, values=[''] + ["0-50000", "50000-100000", "100000-150000", "150000-300000", "300000-500000", f"500000-{max(dataframe['Kilometer'])}"], state='readonly')
mileage_combobox.grid(row=3, column=2, padx=10, pady=5)

transmission_label = ttk.Label(window, text="Transmission:")
transmission_label.grid(row=4, column=1, padx=10, pady=5)
transmission_combobox = ttk.Combobox(window, values=[''] + sorted(dataframe['Transmission'].unique().tolist()), state='readonly')
transmission_combobox.grid(row=4, column=2, padx=10, pady=5)

fuel_label = ttk.Label(window, text="Fuel Type:")
fuel_label.grid(row=5, column=1, padx=10, pady=5)
fuel_combobox = ttk.Combobox(window, values=[''] + sorted(dataframe['Fuel Type'].unique().tolist()), state='readonly')
fuel_combobox.grid(row=5, column=2, padx=10, pady=5)

# Create buttons for searching and clearing results
search_button = ttk.Button(window, text="Search", command=search_cars)
search_button.grid(row=6, column=2, padx=10, pady=10)
clear_button = ttk.Button(window, text="Clear", command=clear_results)
clear_button.grid(row=6, column=1, padx=10, pady=10)

# Create a scrolled text widget to display the search results
results_text = scrolledtext.ScrolledText(window, height=30, width=60, state=tk.DISABLED)
results_text.grid(row=7, column=1, columnspan=2, padx=10, pady=10)

# Run the main window loop
window.mainloop()
