import tkinter as tk
from tkinter import messagebox


# =========================================================
# EXIT PAGE
# =========================================================

class ExitPage:

    def __init__(self, root):

        self.root = root

        self.confirm_exit()

    # =====================================================
    # CONFIRM EXIT
    # =====================================================

    def confirm_exit(self):

        answer = messagebox.askyesno(
            "Exit RMS",
            "Are you sure you want to exit\n"
            "Student Result Management System?"
        )

        if answer:

            self.root.destroy()