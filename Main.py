import tkinter as tk
import process as pc

def send_message(btn):
    sub = subject_txt.get().strip()
    path = file_path.get().strip()
    link = link_txt.get().strip()
    date = date_txt.get().strip()
    time = time_txt.get().strip()
    pc.Loader(btn,path,sub,link,date,time)



# Create the main window
root = tk.Tk()
root.title("Enhanced GUI")
root.geometry("800x600")
root.configure(bg="#eaf7fc")  # Set background color

# Center align the grid
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(9, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(2, weight=1)

# Add a stylish title label
title_label = tk.Label(root, text="Welcome to the Enhanced GUI", font=("Helvetica", 16, "bold"), fg="#003366", bg="#eaf7fc")
title_label.grid(row=0, column=0, columnspan=3, pady=10)

# Add Text areas and their labels
subject = tk.Label(root, text="Enter Subject:", font=("Arial", 12, "bold"), bg="#eaf7fc", fg="#00509e")
subject.grid(row=1, column=0, pady=5)
subject_txt = tk.Entry(root, font=("Arial", 12), bg="#f0faff", highlightbackground="#b3d9ff", highlightthickness=1, width=40)
subject_txt.grid(row=1, column=1, padx=10, pady=10)

text_label_2 = tk.Label(root, text="Enter File path:", font=("Arial", 12, "bold"), bg="#eaf7fc", fg="#00509e")
text_label_2.grid(row=2, column=0, pady=5)
file_path = tk.Entry(root, font=("Arial", 12), bg="#f0faff", highlightbackground="#b3d9ff", highlightthickness=1, width=40)
file_path.grid(row=2, column=1, padx=10, pady=10)

link_lbl = tk.Label(root, text="Enter Link:", font=("Arial", 12, "bold"), bg="#eaf7fc", fg="#00509e")
link_lbl.grid(row=3, column=0, pady=5)
link_txt = tk.Entry(root, font=("Arial", 12), bg="#f0faff", highlightbackground="#b3d9ff", highlightthickness=1, width=40)
link_txt.grid(row=3, column=1, padx=10, pady=10)

date_lbl = tk.Label(root, text="Enter Date:", font=("Arial", 12, "bold"), bg="#eaf7fc", fg="#00509e")
date_lbl.grid(row=4, column=0, pady=5)
date_txt = tk.Entry(root, font=("Arial", 12), bg="#f0faff", highlightbackground="#b3d9ff", highlightthickness=1, width=40)
date_txt.grid(row=4, column=1, padx=10, pady=10)

time_lbl = tk.Label(root, text="Enter Time:", font=("Arial", 12, "bold"), bg="#eaf7fc", fg="#00509e")
time_lbl.grid(row=5, column=0, pady=5)
time_txt = tk.Entry(root, font=("Arial", 12), bg="#f0faff", highlightbackground="#b3d9ff", highlightthickness=1, width=40)
time_txt.grid(row=5, column=1, padx=10, pady=10)

# Add buttons
aptitude_btn = tk.Button(root, text="Apptitude mail", font=("Arial", 12, "bold"), bg="yellow", activebackground="#3399ff", fg="#000000", command=lambda: send_message(1), relief="raised", bd=3)
aptitude_btn.grid(row=7, column=0, padx=10, pady=15)

GD_1_btn = tk.Button(root, text="GD-1 mail", font=("Arial", 12, "bold"), bg="yellow", activebackground="#3399ff", fg="#000000", command=lambda: send_message(2), relief="raised", bd=3)
GD_1_btn.grid(row=7, column=1, padx=10, pady=15)

GD_2_btn = tk.Button(root, text="GD-2 mail", font=("Arial", 12, "bold"), bg="yellow", activebackground="#3399ff", fg="#000000", command=lambda: send_message(3), relief="raised", bd=3)
GD_2_btn.grid(row=7, column=2, padx=10, pady=15)

# Add a label for displaying messages
greeting_label = tk.Label(root, text="", font=("Arial", 12, "italic"), fg="#003366", bg="#eaf7fc")
greeting_label.grid(row=8, column=0, columnspan=3, pady=20)

# Run the main event loop
root.mainloop()
