import re
import tkinter as tk
from tkinter import messagebox

def assess_password_strength(password):
    """Assess the strength of a password based on given criteria."""
    criteria = {
        "length": len(password) >= 8,
        "uppercase": any(char.isupper() for char in password),
        "lowercase": any(char.islower() for char in password),
        "numbers": any(char.isdigit() for char in password),
        "special": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)),
    }

    # Evaluate overall strength
    score = sum(criteria.values())
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return criteria, strength

def generate_report(password, criteria, strength):
    """Generate a report based on password criteria and strength."""
    report = []
    report.append(f"Password: {'*' * len(password)}")
    report.append("\nPassword Criteria:")
    report.append(f"- At least 8 characters: {'Passed' if criteria['length'] else 'Failed'}")
    report.append(f"- Contains uppercase letters: {'Passed' if criteria['uppercase'] else 'Failed'}")
    report.append(f"- Contains lowercase letters: {'Passed' if criteria['lowercase'] else 'Failed'}")
    report.append(f"- Contains numbers: {'Passed' if criteria['numbers'] else 'Failed'}")
    report.append(f"- Contains special characters: {'Passed' if criteria['special'] else 'Failed'}")
    report.append(f"\nOverall Strength: {strength}")
    return "\n".join(report)

def check_password():
    password = entry_password.get()
    if not password:
        messagebox.showerror("Error", "Please enter a password.")
        return

    criteria, strength = assess_password_strength(password)
    report = generate_report(password, criteria, strength)

    text_report.delete("1.0", tk.END)
    text_report.insert(tk.END, report)

def toggle_password_visibility():
    if entry_password.cget("show") == "*":
        entry_password.config(show="")
        btn_toggle_password.config(text="Hide Password")
    else:
        entry_password.config(show="*")
        btn_toggle_password.config(text="Show Password")

def create_gui():
    root = tk.Tk()
    root.title("Password Strength Checker")

    # Configure grid weights for resizing
    root.columnconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    # Password Entry
    tk.Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=5, sticky="w")
    global entry_password
    entry_password = tk.Entry(root, width=30, show="*")
    entry_password.grid(row=0, column=1, padx=10, pady=5, sticky="ew")

    global btn_toggle_password
    btn_toggle_password = tk.Button(root, text="Show Password", command=toggle_password_visibility)
    btn_toggle_password.grid(row=0, column=2, padx=5, pady=5)

    # Check Button
    tk.Button(root, text="Check Strength", command=check_password).grid(row=1, column=0, columnspan=3, pady=10)

    # Report Text Area
    tk.Label(root, text="Password Strength Report:").grid(row=2, column=0, padx=10, pady=5, sticky="nw")
    global text_report
    text_report = tk.Text(root, width=50, height=10, state="normal")
    text_report.grid(row=2, column=1, padx=10, pady=5, sticky="nsew")

    # Add scrollbar
    scrollbar = tk.Scrollbar(root, command=text_report.yview)
    scrollbar.grid(row=2, column=2, sticky="ns")
    text_report.configure(yscrollcommand=scrollbar.set)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
