import json
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

FILENAME = "expenses.json"

# -------------------------
# Load expenses from file
# -------------------------
def load_expenses():
    try:
        with open(FILENAME, "r") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return []


# -------------------------
# Save expenses to file
# -------------------------
def save_expenses():
    with open(FILENAME, "w") as f:
        json.dump(expenses, f, indent=4)


# -------------------------
# Refresh table UI
# -------------------------
def refresh_table():
    table.delete(*table.get_children())
    for i, exp in enumerate(expenses, start=1):
        table.insert("", "end", values=(i, exp["category"], exp["amount"], exp["date"]))


# -------------------------
# Add expense
# -------------------------
def add_expense():
    category = entry_category.get().strip()
    amount = entry_amount.get().strip()

    if not category or not amount:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        amount = int(amount)
        if amount <= 0:
            raise ValueError
    except:
        messagebox.showerror("Error", "Amount must be a positive number.")
        return

    expenses.append({
        "category": category,
        "amount": amount,
        "date": date.today().isoformat()
    })

    save_expenses()
    refresh_table()

    entry_category.delete(0, tk.END)
    entry_amount.delete(0, tk.END)


# -------------------------
# Delete selected expense
# -------------------------
def delete_expense():
    selection = table.selection()

    if not selection:
        messagebox.showwarning("Warning", "Select a row to delete.")
        return

    item = table.item(selection)
    index = item["values"][0] - 1  # index in list

    del expenses[index]
    save_expenses()
    refresh_table()


# -------------------------
# Update expense
# -------------------------
def update_expense():
    selection = table.selection()
    if not selection:
        messagebox.showwarning("Warning", "Select a row to update.")
        return

    item = table.item(selection)
    index = item["values"][0] - 1
    exp = expenses[index]

    def apply_update():
        new_cat = update_category.get().strip()
        new_amt = update_amount.get().strip()
        new_date = update_date.get().strip()

        if not new_cat or not new_amt or not new_date:
            messagebox.showerror("Error", "All fields required!")
            return

        try:
            int(new_amt)
        except:
            messagebox.showerror("Error", "Amount must be a number.")
            return

        # Validate date
        try:
            date.fromisoformat(new_date)
        except:
            messagebox.showerror("Error", "Enter date as YYYY-MM-DD.")
            return

        # Update dictionary
        exp["category"] = new_cat
        exp["amount"] = int(new_amt)
        exp["date"] = new_date

        save_expenses()
        refresh_table()
        update_window.destroy()

    # Create update window
    update_window = tk.Toplevel(root)
    update_window.title("Update Expense")
    update_window.geometry("300x200")

    tk.Label(update_window, text="Category:").pack()
    update_category = tk.Entry(update_window)
    update_category.pack()
    update_category.insert(0, exp["category"])

    tk.Label(update_window, text="Amount:").pack()
    update_amount = tk.Entry(update_window)
    update_amount.pack()
    update_amount.insert(0, exp["amount"])

    tk.Label(update_window, text="Date (YYYY-MM-DD):").pack()
    update_date = tk.Entry(update_window)
    update_date.pack()
    update_date.insert(0, exp["date"])

    tk.Button(update_window, text="Apply", command=apply_update).pack(pady=10)


# -------------------------
# Search by category
# -------------------------
def search_category():
    query = entry_search.get().strip()
    if not query:
        messagebox.showwarning("Error", "Enter a category to search.")
        return

    table.delete(*table.get_children())

    for i, exp in enumerate(expenses, start=1):
        if exp["category"].lower() == query.lower():
            table.insert("", "end", values=(i, exp["category"], exp["amount"], exp["date"]))


# -------------------------
# Search by date
# -------------------------
def search_date():
    d = entry_search.get().strip()

    try:
        date.fromisoformat(d)
    except:
        messagebox.showerror("Error", "Enter date as YYYY-MM-DD.")
        return

    table.delete(*table.get_children())

    for i, exp in enumerate(expenses, start=1):
        if exp["date"] == d:
            table.insert("", "end", values=(i, exp["category"], exp["amount"], exp["date"]))


# -------------------------
# Reset table after search
# -------------------------
def reset_table():
    refresh_table()


# ------------------------------------
# GUI Setup
# ------------------------------------
root = tk.Tk()
root.title("Expense Tracker")
root.geometry("650x500")

# Input Fields
tk.Label(root, text="Category:").place(x=20, y=20)
entry_category = tk.Entry(root)
entry_category.place(x=100, y=20)

tk.Label(root, text="Amount:").place(x=20, y=60)
entry_amount = tk.Entry(root)
entry_amount.place(x=100, y=60)

tk.Button(root, text="Add Expense", command=add_expense).place(x=250, y=40)

# Search Field
tk.Label(root, text="Search:").place(x=20, y=110)
entry_search = tk.Entry(root)
entry_search.place(x=100, y=110)

tk.Button(root, text="By Category", command=search_category).place(x=250, y=100)
tk.Button(root, text="By Date", command=search_date).place(x=340, y=100)
tk.Button(root, text="Reset", command=reset_table).place(x=410, y=100)

# Table
columns = ("No", "Category", "Amount", "Date")
table = ttk.Treeview(root, columns=columns, show="headings", height=15)

for col in columns:
    table.heading(col, text=col)
    table.column(col, width=100)

table.place(x=20, y=150)

# Buttons
tk.Button(root, text="Delete", command=delete_expense).place(x=500, y=150)
tk.Button(root, text="Update", command=update_expense).place(x=500, y=190)

# Load data
expenses = load_expenses()
refresh_table()

root.mainloop()
