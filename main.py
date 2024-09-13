import tkinter as tk
from tkinter import messagebox

class Account:
    """A class representing a bank account."""
    
    def __init__(self, account_number, name, initial_balance=0.0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            return f"Deposited {amount} successfully."
        else:
            return "Invalid deposit amount."

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"Withdrawn {amount} successfully."
        else:
            return "Invalid or insufficient funds for withdrawal."

    def display_balance(self):
        """Display the current balance."""
        return f"Current balance: {self.balance}"

    def display_account_details(self):
        """Display account details."""
        return f"Account Number: {self.account_number}\nAccount Holder: {self.name}\nBalance: {self.balance}"


class BankingSystem:
    """A class representing the banking system with GUI."""
    
    def __init__(self):
        self.accounts = {}
        self.root = tk.Tk()
        self.root.title("Banking System")
        self.create_main_menu()

    def create_main_menu(self):
        """Create the main menu of the banking system."""
        self.clear_frame()
        tk.Label(self.root, text="Banking System", font=("Arial", 20)).pack(pady=10)
        tk.Button(self.root, text="Create Account", command=self.create_account).pack(pady=5)
        tk.Button(self.root, text="Access Account", command=self.access_account).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.quit).pack(pady=5)

    def create_account(self):
        """Create a new bank account with GUI input."""
        self.clear_frame()
        tk.Label(self.root, text="Create Account", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Account Number:").pack()
        account_number_entry = tk.Entry(self.root)
        account_number_entry.pack()
        tk.Label(self.root, text="Account Holder Name:").pack()
        name_entry = tk.Entry(self.root)
        name_entry.pack()
        tk.Label(self.root, text="Initial Deposit Amount:").pack()
        initial_balance_entry = tk.Entry(self.root)
        initial_balance_entry.pack()
        
        def submit():
            account_number = account_number_entry.get()
            name = name_entry.get()
            try:
                initial_balance = float(initial_balance_entry.get())
                if account_number in self.accounts:
                    messagebox.showerror("Error", "Account number already exists!")
                else:
                    self.accounts[account_number] = Account(account_number, name, initial_balance)
                    messagebox.showinfo("Success", "Account created successfully!")
                    self.create_main_menu()
            except ValueError:
                messagebox.showerror("Error", "Invalid deposit amount!")

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=5)

    def access_account(self):
        """Access an existing account with GUI input."""
        self.clear_frame()
        tk.Label(self.root, text="Access Account", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter Account Number:").pack()
        account_number_entry = tk.Entry(self.root)
        account_number_entry.pack()

        def submit():
            account_number = account_number_entry.get()
            account = self.accounts.get(account_number)
            if account:
                self.account_menu(account)
            else:
                messagebox.showerror("Error", "Account not found!")

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=5)

    def account_menu(self, account):
        """Display the account menu for specific operations."""
        self.clear_frame()
        tk.Label(self.root, text="Account Menu", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.root, text="Deposit", command=lambda: self.deposit(account)).pack(pady=5)
        tk.Button(self.root, text="Withdraw", command=lambda: self.withdraw(account)).pack(pady=5)
        tk.Button(self.root, text="Check Balance", command=lambda: self.show_message(account.display_balance())).pack(pady=5)
        tk.Button(self.root, text="Account Details", command=lambda: self.show_message(account.display_account_details())).pack(pady=5)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack(pady=5)

    def deposit(self, account):
        """GUI for depositing money."""
        self.clear_frame()
        tk.Label(self.root, text="Deposit Money", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter Amount:").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def submit():
            try:
                amount = float(amount_entry.get())
                message = account.deposit(amount)
                messagebox.showinfo("Deposit", message)
                self.account_menu(account)
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered.")

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=lambda: self.account_menu(account)).pack(pady=5)

    def withdraw(self, account):
        """GUI for withdrawing money."""
        self.clear_frame()
        tk.Label(self.root, text="Withdraw Money", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Enter Amount:").pack()
        amount_entry = tk.Entry(self.root)
        amount_entry.pack()

        def submit():
            try:
                amount = float(amount_entry.get())
                message = account.withdraw(amount)
                messagebox.showinfo("Withdraw", message)
                self.account_menu(account)
            except ValueError:
                messagebox.showerror("Error", "Invalid amount entered.")

        tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
        tk.Button(self.root, text="Back", command=lambda: self.account_menu(account)).pack(pady=5)

    def show_message(self, message):
        """Display a message in a popup."""
        messagebox.showinfo("Information", message)

    def clear_frame(self):
        """Clear the current frame for new content."""
        for widget in self.root.winfo_children():
            widget.destroy()

    def run(self):
        """Run the GUI application."""
        self.root.mainloop()


# Main execution
if __name__ == "__main__":
    system = BankingSystem()
    system.run()
