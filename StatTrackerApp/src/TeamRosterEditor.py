import tkinter as tk
from tkinter import simpledialog, messagebox

from config import team_roster, event_codes


#=================================FUNCTIONS=================================
def quit_application():
    if messagebox.askyesno("Quit", "Are you sure you want to quit?"):
        root.destroy()

def populate_roster_listbox():
    for number, names in team_roster.items():
        roster_listbox.insert(tk.END, f"{number}: {names[0]} {names[1]}")

def populate_event_code_listbox():
    for code, description in event_codes.items():
        event_code_listbox.insert(tk.END, f"{code}: {description}")

def save_changes():
    with open("config.py", "w") as file:
        file.write("team_roster = " + str(team_roster) + "\n")
        file.write("event_codes = " + str(event_codes) + "\n")
    messagebox.showinfo("Save", "Changes saved successfully.")

def add_player():
    number = simpledialog.askstring("Add Player", "Enter player's number:")
    if number:
        first_name = simpledialog.askstring("Add Player", "Enter player's first name:")
        last_name = simpledialog.askstring("Add Player", "Enter player's last name:")
        team_roster[int(number)] = (first_name, last_name)
        update_roster_view()

def remove_player():
    number = simpledialog.askstring("Remove Player", "Enter player's number to remove:")
    if number and int(number) in team_roster:
        del team_roster[int(number)]
        update_roster_view()

def add_event_code():
    code = simpledialog.askstring("Add Event Code", "Enter new event code:")
    if code:
        description = simpledialog.askstring("Add Event Code", "Enter event code description:")
        event_codes[code] = description
        update_event_code_view()

def remove_event_code():
    code = simpledialog.askstring("Remove Event Code", "Enter event code to remove:")
    if code and code in event_codes:
        del event_codes[code]
        update_event_code_view()

def update_roster_view():
    roster_listbox.delete(0, tk.END)
    for number, names in team_roster.items():
        roster_listbox.insert(tk.END, f"{number}: {names[0]} {names[1]}")

def update_event_code_view():
    event_code_listbox.delete(0, tk.END)
    for code, description in event_codes.items():
        event_code_listbox.insert(tk.END, f"{code}: {description}")
        
def edit_player():
    selected = roster_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "No player selected")
        return

    player_number = list(team_roster.keys())[selected[0]]
    player_data = team_roster[player_number]

    new_first_name = simpledialog.askstring("Edit Player", "Enter player's new first name:", initialvalue=player_data[0])
    new_last_name = simpledialog.askstring("Edit Player", "Enter player's new last name:", initialvalue=player_data[1])

    if new_first_name and new_last_name:
        team_roster[player_number] = (new_first_name, new_last_name)
        update_roster_view()

def edit_event_code():
    selected = event_code_listbox.curselection()
    if not selected:
        messagebox.showerror("Error", "No event code selected")
        return

    event_code = list(event_codes.keys())[selected[0]]
    new_description = simpledialog.askstring("Edit Event Code", "Enter new event code description:", initialvalue=event_codes[event_code])

    if new_description:
        event_codes[event_code] = new_description
        update_event_code_view()

#========================CREATE MAIN WINDOW AND LAYOUT==========================        
root = tk.Tk()
root.title("Team Roster and Event Code Editor")

# Team Roster Frame
roster_frame = tk.LabelFrame(root, text="Team Roster")
roster_listbox = tk.Listbox(roster_frame)
add_player_button = tk.Button(roster_frame, text="Add Player", command=add_player)
remove_player_button = tk.Button(roster_frame, text="Remove Player", command=remove_player)
roster_listbox.pack()
add_player_button.pack()
remove_player_button.pack()
roster_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Event Code Frame
event_code_frame = tk.LabelFrame(root, text="Event Codes")
event_code_listbox = tk.Listbox(event_code_frame)
add_event_code_button = tk.Button(event_code_frame, text="Add Event Code", command=add_event_code)
remove_event_code_button = tk.Button(event_code_frame, text="Remove Event Code", command=remove_event_code)
event_code_listbox.pack()
add_event_code_button.pack()
remove_event_code_button.pack()
event_code_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Save Button
save_button = tk.Button(root, text="Save", command=save_changes)
save_button.pack()

# Edit Buttons
edit_roster_button = tk.Button(roster_frame, text="Edit Player Name", command=edit_player)
edit_event_code_button = tk.Button(event_code_frame, text="Edit Event Description", command=edit_event_code)
edit_roster_button.pack()
edit_event_code_button.pack()

# Quit Button
quit_button = tk.Button(root, text="Quit", command=quit_application)
quit_button.pack()

# Populate the listboxes
populate_roster_listbox()
populate_event_code_listbox()

# Run the application
root.mainloop()
