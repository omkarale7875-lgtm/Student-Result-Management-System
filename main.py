import tkinter as tk
from tkinter import messagebox

from dashboard import Dashboard
from students import Students
from results import Results
from courses import Courses
from settings import Settings
from exit_page import ExitPage


# =========================================================
# MAIN APPLICATION
# =========================================================

class RMS:

    def __init__(self, root):

        self.root = root

        self.root.title(
            "Student Result Management System"
        )

        self.root.geometry(
            "1400x780+20+20"
        )

        self.root.minsize(
            1150,
            650
        )

        # =================================================
        # COLORS
        # =================================================

        self.bg = "#0b1120"
        self.sidebar = "#080d19"
        self.header = "#111827"
        self.card = "#151f32"
        self.border = "#26344d"

        self.blue = "#3b82f6"
        self.blue_dark = "#2563eb"

        self.green = "#22c55e"
        self.red = "#ef4444"
        self.orange = "#f59e0b"
        self.purple = "#8b5cf6"

        self.text = "#f8fafc"
        self.text_secondary = "#cbd5e1"
        self.text_muted = "#64748b"

        # =================================================
        # MAIN AREA
        # =================================================

        self.sidebar_frame = tk.Frame(
            self.root,
            bg=self.sidebar,
            width=230
        )

        self.sidebar_frame.pack(
            side=tk.LEFT,
            fill=tk.Y
        )

        self.sidebar_frame.pack_propagate(False)

        self.content_frame = tk.Frame(
            self.root,
            bg=self.bg
        )

        self.content_frame.pack(
            side=tk.RIGHT,
            fill=tk.BOTH,
            expand=True
        )

        # =================================================
        # SIDEBAR
        # =================================================

        self.create_sidebar()

        # =================================================
        # DEFAULT PAGE
        # =================================================

        self.show_dashboard()

    # =====================================================
    # SIDEBAR
    # =====================================================

    def create_sidebar(self):

        logo_frame = tk.Frame(
            self.sidebar_frame,
            bg=self.sidebar
        )

        logo_frame.pack(
            fill=tk.X,
            pady=(25, 30)
        )

        tk.Label(
            logo_frame,
            text="RMS",
            bg=self.sidebar,
            fg=self.blue,
            font=("Segoe UI", 26, "bold")
        ).pack()

        tk.Label(
            logo_frame,
            text="ACADEMIC PORTAL",
            bg=self.sidebar,
            fg=self.text_muted,
            font=("Segoe UI", 8, "bold")
        ).pack(
            pady=(2, 0)
        )

        # =================================================
        # MENU
        # =================================================

        self.menu_button(
            "▣   Dashboard",
            self.show_dashboard
        )

        self.menu_button(
            "♙   Students",
            self.show_students
        )

        self.menu_button(
            "▤   Results",
            self.show_results
        )

        self.menu_button(
            "▦   Courses",
            self.show_courses
        )

        self.menu_button(
            "⚙   Settings",
            self.show_settings
        )

        # =================================================
        # EXIT
        # =================================================

        tk.Frame(
            self.sidebar_frame,
            bg=self.sidebar
        ).pack(
            expand=True,
            fill=tk.BOTH
        )

        self.menu_button(
            "✕   Exit",
            self.exit_application
        )

        tk.Label(
            self.sidebar_frame,
            text="RMS v2.0  •  Enterprise",
            bg=self.sidebar,
            fg=self.text_muted,
            font=("Segoe UI", 8)
        ).pack(
            pady=20
        )

    # =====================================================
    # MENU BUTTON
    # =====================================================

    def menu_button(self, text, command):

        button = tk.Button(
            self.sidebar_frame,
            text=text,
            command=command,
            bg=self.sidebar,
            fg=self.text_secondary,
            activebackground="#111827",
            activeforeground="white",
            relief=tk.FLAT,
            borderwidth=0,
            anchor="w",
            font=("Segoe UI", 10, "bold"),
            cursor="hand2"
        )

        button.pack(
            fill=tk.X,
            padx=12,
            pady=3,
            ipady=11
        )

    # =====================================================
    # CLEAR CONTENT
    # =====================================================

    def clear_content(self):

        for widget in self.content_frame.winfo_children():

            widget.destroy()

    # =====================================================
    # DASHBOARD
    # =====================================================

    def show_dashboard(self):

        self.clear_content()

        Dashboard(
            self.content_frame,
            self
        )

    # =====================================================
    # STUDENTS
    # =====================================================

    def show_students(self):

        self.clear_content()

        Students(
            self.content_frame,
            self
        )

    # =====================================================
    # RESULTS
    # =====================================================

    def show_results(self):

        self.clear_content()

        Results(
            self.content_frame,
            self
        )

    # =====================================================
    # COURSES
    # =====================================================

    def show_courses(self):

        self.clear_content()

        Courses(
            self.content_frame,
            self
        )

    # =====================================================
    # SETTINGS
    # =====================================================

    def show_settings(self):

        self.clear_content()

        Settings(
            self.content_frame,
            self
        )

    # =====================================================
    # EXIT
    # =====================================================

    def exit_application(self):

        ExitPage(
            self.root
        )


# =========================================================
# PROGRAM START
# =========================================================

if __name__ == "__main__":

    root = tk.Tk()

    app = RMS(root)

    root.mainloop()