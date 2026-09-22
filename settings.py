<<<<<<< HEAD
import tkinter as tk

from database import connect_database


# =========================================================
# SETTINGS
# =========================================================

class Settings:

    def __init__(self, parent, app):

        self.parent = parent
        self.app = app

        self.bg = app.bg
        self.card = app.card
        self.border = app.border

        self.text = app.text
        self.text_muted = app.text_muted

        self.blue = app.blue
        self.green = app.green
        self.red = app.red

        self.create_page()

    # =====================================================
    # PAGE
    # =====================================================

    def create_page(self):

        header = tk.Frame(
            self.parent,
            bg="#111827",
            height=85
        )

        header.pack(
            fill=tk.X
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Settings",
            bg="#111827",
            fg=self.text,
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(16, 0)
        )

        tk.Label(
            header,
            text="Application and database information",
            bg="#111827",
            fg=self.text_muted,
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            padx=30
        )

        container = tk.Frame(
            self.parent,
            bg=self.bg
        )

        container.pack(
            fill=tk.BOTH,
            expand=True,
            padx=25,
            pady=25
        )

        # =================================================
        # DATABASE
        # =================================================

        database_card = tk.Frame(
            container,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        database_card.pack(
            fill=tk.X,
            pady=(0, 20)
        )

        tk.Label(
            database_card,
            text="Database Connection",
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(20, 12)
        )

        conn = connect_database()

        if conn:

            status = "●  CONNECTED"
            status_color = self.green

            conn.close()

        else:

            status = "●  DISCONNECTED"
            status_color = self.red

        tk.Label(
            database_card,
            text=status,
            bg=self.card,
            fg=status_color,
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 18)
        )

        self.info_row(
            database_card,
            "SQL Server",
            r"LAPTOP-9T226DAT\OMKARSQLSERVER"
        )

        self.info_row(
            database_card,
            "Database",
            "RMS_DB"
        )

        self.info_row(
            database_card,
            "Authentication",
            "Windows Authentication"
        )

        # =================================================
        # APPLICATION
        # =================================================

        application_card = tk.Frame(
            container,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        application_card.pack(
            fill=tk.X
        )

        tk.Label(
            application_card,
            text="Application Information",
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(20, 15)
        )

        self.info_row(
            application_card,
            "Application",
            "Student Result Management System"
        )

        self.info_row(
            application_card,
            "Version",
            "2.0 Enterprise"
        )

        self.info_row(
            application_card,
            "Frontend",
            "Python Tkinter"
        )

        self.info_row(
            application_card,
            "Database",
            "Microsoft SQL Server"
        )

        self.info_row(
            application_card,
            "Driver",
            "ODBC Driver 17 for SQL Server"
        )

    # =====================================================
    # INFO ROW
    # =====================================================

    def info_row(
        self,
        parent,
        label,
        value
    ):

        frame = tk.Frame(
            parent,
            bg=self.card
        )

        frame.pack(
            fill=tk.X,
            padx=22,
            pady=6
        )

        tk.Label(
            frame,
            text=label,
            bg=self.card,
            fg=self.text_muted,
            font=("Segoe UI", 9)
        ).pack(
            side=tk.LEFT
        )

        tk.Label(
            frame,
            text=value,
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 9, "bold")
        ).pack(
            side=tk.RIGHT
=======
import tkinter as tk

from database import connect_database


# =========================================================
# SETTINGS
# =========================================================

class Settings:

    def __init__(self, parent, app):

        self.parent = parent
        self.app = app

        self.bg = app.bg
        self.card = app.card
        self.border = app.border

        self.text = app.text
        self.text_muted = app.text_muted

        self.blue = app.blue
        self.green = app.green
        self.red = app.red

        self.create_page()

    # =====================================================
    # PAGE
    # =====================================================

    def create_page(self):

        header = tk.Frame(
            self.parent,
            bg="#111827",
            height=85
        )

        header.pack(
            fill=tk.X
        )

        header.pack_propagate(False)

        tk.Label(
            header,
            text="Settings",
            bg="#111827",
            fg=self.text,
            font=("Segoe UI", 22, "bold")
        ).pack(
            anchor="w",
            padx=28,
            pady=(16, 0)
        )

        tk.Label(
            header,
            text="Application and database information",
            bg="#111827",
            fg=self.text_muted,
            font=("Segoe UI", 9)
        ).pack(
            anchor="w",
            padx=30
        )

        container = tk.Frame(
            self.parent,
            bg=self.bg
        )

        container.pack(
            fill=tk.BOTH,
            expand=True,
            padx=25,
            pady=25
        )

        # =================================================
        # DATABASE
        # =================================================

        database_card = tk.Frame(
            container,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        database_card.pack(
            fill=tk.X,
            pady=(0, 20)
        )

        tk.Label(
            database_card,
            text="Database Connection",
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(20, 12)
        )

        conn = connect_database()

        if conn:

            status = "●  CONNECTED"
            status_color = self.green

            conn.close()

        else:

            status = "●  DISCONNECTED"
            status_color = self.red

        tk.Label(
            database_card,
            text=status,
            bg=self.card,
            fg=status_color,
            font=("Segoe UI", 10, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 18)
        )

        self.info_row(
            database_card,
            "SQL Server",
            r"LAPTOP-9T226DAT\OMKARSQLSERVER"
        )

        self.info_row(
            database_card,
            "Database",
            "RMS_DB"
        )

        self.info_row(
            database_card,
            "Authentication",
            "Windows Authentication"
        )

        # =================================================
        # APPLICATION
        # =================================================

        application_card = tk.Frame(
            container,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        application_card.pack(
            fill=tk.X
        )

        tk.Label(
            application_card,
            text="Application Information",
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 15, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(20, 15)
        )

        self.info_row(
            application_card,
            "Application",
            "Student Result Management System"
        )

        self.info_row(
            application_card,
            "Version",
            "2.0 Enterprise"
        )

        self.info_row(
            application_card,
            "Frontend",
            "Python Tkinter"
        )

        self.info_row(
            application_card,
            "Database",
            "Microsoft SQL Server"
        )

        self.info_row(
            application_card,
            "Driver",
            "ODBC Driver 17 for SQL Server"
        )

    # =====================================================
    # INFO ROW
    # =====================================================

    def info_row(
        self,
        parent,
        label,
        value
    ):

        frame = tk.Frame(
            parent,
            bg=self.card
        )

        frame.pack(
            fill=tk.X,
            padx=22,
            pady=6
        )

        tk.Label(
            frame,
            text=label,
            bg=self.card,
            fg=self.text_muted,
            font=("Segoe UI", 9)
        ).pack(
            side=tk.LEFT
        )

        tk.Label(
            frame,
            text=value,
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 9, "bold")
        ).pack(
            side=tk.RIGHT
>>>>>>> master
        )