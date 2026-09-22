import tkinter as tk
from tkinter import ttk

from database import connect_database


# =========================================================
# PROFESSIONAL DASHBOARD
# =========================================================

class Dashboard:

    def __init__(self, parent, app):

        self.parent = parent
        self.app = app

        # -------------------------------------------------
        # COLORS
        # -------------------------------------------------

        self.bg = "#0a0f1c"
        self.header = "#101827"

        self.card = "#121b2b"
        self.card_hover = "#18243a"

        self.table_bg = "#0d1626"
        self.table_row = "#111c2e"
        self.table_alt = "#0e192a"
        self.table_header = "#18253a"

        self.border = "#24334b"

        self.text = "#f8fafc"
        self.text_secondary = "#cbd5e1"
        self.text_muted = "#718096"

        self.blue = "#3b82f6"
        self.blue_light = "#60a5fa"

        self.green = "#22c55e"
        self.green_light = "#4ade80"

        self.red = "#ef4444"
        self.red_light = "#f87171"

        self.purple = "#8b5cf6"
        self.orange = "#f59e0b"

        # -------------------------------------------------
        # DATA
        # -------------------------------------------------

        self.total_students = 0
        self.passed_students = 0
        self.failed_students = 0
        self.average_marks = 0

        self.create_styles()
        self.load_dashboard_data()
        self.create_page()

    # =====================================================
    # TREEVIEW STYLE
    # =====================================================

    def create_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        # -------------------------------------------------
        # TABLE
        # -------------------------------------------------

        style.configure(
            "Professional.Treeview",
            background=self.table_bg,
            foreground=self.text_secondary,
            fieldbackground=self.table_bg,
            borderwidth=0,
            relief="flat",
            rowheight=48,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Professional.Treeview.Heading",
            background=self.table_header,
            foreground="#e2e8f0",
            relief="flat",
            borderwidth=0,
            font=("Segoe UI", 9, "bold"),
            padding=(12, 12)
        )

        style.map(
            "Professional.Treeview",
            background=[
                ("selected", "#1d4ed8")
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        style.map(
            "Professional.Treeview.Heading",
            background=[
                ("active", "#20304a")
            ]
        )

        # -------------------------------------------------
        # SCROLLBAR
        # -------------------------------------------------

        style.configure(
            "Professional.Vertical.TScrollbar",
            background="#17243a",
            troughcolor=self.table_bg,
            bordercolor=self.table_bg,
            arrowcolor="#64748b",
            width=10
        )

    # =====================================================
    # LOAD DATABASE DATA
    # =====================================================

    def load_dashboard_data(self):

        try:

            conn = connect_database()

            if conn is None:
                return

            cursor = conn.cursor()

            # -------------------------------------------------
            # TOTAL
            # -------------------------------------------------

            cursor.execute(
                "SELECT COUNT(*) FROM Students"
            )

            result = cursor.fetchone()

            if result:
                self.total_students = result[0]

            # -------------------------------------------------
            # PASS
            # -------------------------------------------------

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM Students
                WHERE Status = 'PASS'
                """
            )

            result = cursor.fetchone()

            if result:
                self.passed_students = result[0]

            # -------------------------------------------------
            # FAIL
            # -------------------------------------------------

            cursor.execute(
                """
                SELECT COUNT(*)
                FROM Students
                WHERE Status = 'FAIL'
                """
            )

            result = cursor.fetchone()

            if result:
                self.failed_students = result[0]

            # -------------------------------------------------
            # AVERAGE
            # -------------------------------------------------

            cursor.execute(
                """
                SELECT ISNULL(
                    AVG(CAST(Marks AS FLOAT)),
                    0
                )
                FROM Students
                """
            )

            result = cursor.fetchone()

            if result:
                self.average_marks = result[0]

            conn.close()

        except Exception as e:

            print(
                "Dashboard Data Error:",
                e
            )

    # =====================================================
    # MAIN PAGE
    # =====================================================

    def create_page(self):

        # -------------------------------------------------
        # HEADER
        # -------------------------------------------------

        header = tk.Frame(
            self.parent,
            bg=self.header,
            height=92
        )

        header.pack(
            fill=tk.X
        )

        header.pack_propagate(False)

        # Left header

        title_frame = tk.Frame(
            header,
            bg=self.header
        )

        title_frame.pack(
            side=tk.LEFT,
            padx=30
        )

        tk.Label(
            title_frame,
            text="Dashboard",
            bg=self.header,
            fg=self.text,
            font=("Segoe UI", 23, "bold")
        ).pack(
            anchor="w",
            pady=(14, 0)
        )

        tk.Label(
            title_frame,
            text="Student Result Management System",
            bg=self.header,
            fg=self.text_muted,
            font=("Segoe UI", 9)
        ).pack(
            anchor="w"
        )

        # Right header

        status_frame = tk.Frame(
            header,
            bg=self.header
        )

        status_frame.pack(
            side=tk.RIGHT,
            padx=30
        )

        connection_ok = self.check_connection()

        if connection_ok:

            status_text = "●  DATABASE CONNECTED"
            status_color = self.green

        else:

            status_text = "●  DATABASE OFFLINE"
            status_color = self.red

        tk.Label(
            status_frame,
            text=status_text,
            bg=self.header,
            fg=status_color,
            font=("Segoe UI", 9, "bold")
        ).pack(
            pady=(18, 0)
        )

        tk.Label(
            status_frame,
            text="Microsoft SQL Server",
            bg=self.header,
            fg=self.text_muted,
            font=("Segoe UI", 8)
        ).pack()

        # -------------------------------------------------
        # CONTENT
        # -------------------------------------------------

        content = tk.Frame(
            self.parent,
            bg=self.bg
        )

        content.pack(
            fill=tk.BOTH,
            expand=True,
            padx=25,
            pady=22
        )

        # -------------------------------------------------
        # KPI SECTION
        # -------------------------------------------------

        kpi_frame = tk.Frame(
            content,
            bg=self.bg
        )

        kpi_frame.pack(
            fill=tk.X
        )

        for i in range(4):

            kpi_frame.grid_columnconfigure(
                i,
                weight=1
            )

        self.create_kpi(
            kpi_frame,
            0,
            "TOTAL STUDENTS",
            str(self.total_students),
            "Registered students",
            self.blue,
            "◉"
        )

        self.create_kpi(
            kpi_frame,
            1,
            "PASSED STUDENTS",
            str(self.passed_students),
            "Students above 40%",
            self.green,
            "✓"
        )

        self.create_kpi(
            kpi_frame,
            2,
            "FAILED STUDENTS",
            str(self.failed_students),
            "Needs improvement",
            self.red,
            "!"
        )

        self.create_kpi(
            kpi_frame,
            3,
            "AVERAGE MARKS",
            f"{self.average_marks:.1f}%",
            "Overall performance",
            self.purple,
            "★"
        )

        # -------------------------------------------------
        # MIDDLE SECTION
        # -------------------------------------------------

        middle = tk.Frame(
            content,
            bg=self.bg
        )

        middle.pack(
            fill=tk.X,
            pady=(20, 20)
        )

        middle.grid_columnconfigure(
            0,
            weight=3
        )

        middle.grid_columnconfigure(
            1,
            weight=1
        )

        # Performance card

        performance_card = tk.Frame(
            middle,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        performance_card.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(0, 8)
        )

        tk.Label(
            performance_card,
            text="Academic Performance",
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 14, "bold")
        ).pack(
            anchor="w",
            padx=22,
            pady=(18, 2)
        )

        tk.Label(
            performance_card,
            text="Overall student performance distribution",
            bg=self.card,
            fg=self.text_muted,
            font=("Segoe UI", 8)
        ).pack(
            anchor="w",
            padx=22,
            pady=(0, 18)
        )

        performance_inner = tk.Frame(
            performance_card,
            bg=self.card
        )

        performance_inner.pack(
            fill=tk.X,
            padx=22,
            pady=(0, 20)
        )

        total = self.total_students

        pass_percentage = 0
        fail_percentage = 0

        if total > 0:

            pass_percentage = (
                self.passed_students / total
            ) * 100

            fail_percentage = (
                self.failed_students / total
            ) * 100

        self.performance_row(
            performance_inner,
            "PASS",
            pass_percentage,
            self.green
        )

        self.performance_row(
            performance_inner,
            "FAIL",
            fail_percentage,
            self.red
        )

        # System card

        system_card = tk.Frame(
            middle,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        system_card.grid(
            row=0,
            column=1,
            sticky="nsew",
            padx=(8, 0)
        )

        tk.Label(
            system_card,
            text="System Status",
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 14, "bold")
        ).pack(
            anchor="w",
            padx=20,
            pady=(18, 15)
        )

        self.system_info(
            system_card,
            "DATABASE",
            "ONLINE",
            self.green
        )

        self.system_info(
            system_card,
            "SERVER",
            "SQL SERVER",
            self.blue
        )

        self.system_info(
            system_card,
            "APPLICATION",
            "RUNNING",
            self.green
        )

        self.system_info(
            system_card,
            "VERSION",
            "2.0",
            self.purple
        )

        # -------------------------------------------------
        # STUDENT TABLE
        # -------------------------------------------------

        table_card = tk.Frame(
            content,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        table_card.pack(
            fill=tk.BOTH,
            expand=True
        )

        table_header = tk.Frame(
            table_card,
            bg=self.card,
            height=65
        )

        table_header.pack(
            fill=tk.X
        )

        table_header.pack_propagate(False)

        title_box = tk.Frame(
            table_header,
            bg=self.card
        )

        title_box.pack(
            side=tk.LEFT,
            padx=22
        )

        tk.Label(
            title_box,
            text="Recent Student Records",
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 14, "bold")
        ).pack(
            anchor="w",
            pady=(10, 0)
        )

        tk.Label(
            title_box,
            text="Latest student records from MS SQL Server",
            bg=self.card,
            fg=self.text_muted,
            font=("Segoe UI", 8)
        ).pack(
            anchor="w"
        )

        tk.Button(
            table_header,
            text="VIEW ALL STUDENTS  →",
            command=self.app.show_students,
            bg=self.card,
            fg=self.blue_light,
            activebackground=self.card_hover,
            activeforeground="white",
            relief=tk.FLAT,
            borderwidth=0,
            font=("Segoe UI", 8, "bold"),
            cursor="hand2"
        ).pack(
            side=tk.RIGHT,
            padx=22
        )

        # -------------------------------------------------
        # TABLE
        # -------------------------------------------------

        table_container = tk.Frame(
            table_card,
            bg=self.table_bg
        )

        table_container.pack(
            fill=tk.BOTH,
            expand=True,
            padx=18,
            pady=(0, 18)
        )

        columns = (
            "id",
            "name",
            "course",
            "marks",
            "status"
        )

        table = ttk.Treeview(
            table_container,
            columns=columns,
            show="headings",
            style="Professional.Treeview"
        )

        table.heading(
            "id",
            text="ID"
        )

        table.heading(
            "name",
            text="STUDENT NAME"
        )

        table.heading(
            "course",
            text="COURSE"
        )

        table.heading(
            "marks",
            text="MARKS"
        )

        table.heading(
            "status",
            text="STATUS"
        )

        table.column(
            "id",
            width=70,
            anchor="center"
        )

        table.column(
            "name",
            width=280,
            anchor="w"
        )

        table.column(
            "course",
            width=200,
            anchor="w"
        )

        table.column(
            "marks",
            width=130,
            anchor="center"
        )

        table.column(
            "status",
            width=130,
            anchor="center"
        )

        # -------------------------------------------------
        # ROW COLORS
        # -------------------------------------------------

        table.tag_configure(
            "even",
            background=self.table_row,
            foreground=self.text_secondary
        )

        table.tag_configure(
            "odd",
            background=self.table_alt,
            foreground=self.text_secondary
        )

        table.tag_configure(
            "pass",
            foreground=self.green_light
        )

        table.tag_configure(
            "fail",
            foreground=self.red_light
        )

        # -------------------------------------------------
        # SCROLLBAR
        # -------------------------------------------------

        scrollbar = ttk.Scrollbar(
            table_container,
            orient="vertical",
            command=table.yview,
            style="Professional.Vertical.TScrollbar"
        )

        table.configure(
            yscrollcommand=scrollbar.set
        )

        table.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        scrollbar.pack(
            side=tk.RIGHT,
            fill=tk.Y
        )

        # -------------------------------------------------
        # LOAD STUDENTS
        # -------------------------------------------------

        self.load_recent_students(
            table
        )

    # =====================================================
    # KPI CARD
    # =====================================================

    def create_kpi(
        self,
        parent,
        column,
        title,
        value,
        subtitle,
        color,
        icon
    ):

        card = tk.Frame(
            parent,
            bg=self.card,
            height=125,
            highlightbackground=self.border,
            highlightthickness=1
        )

        card.grid(
            row=0,
            column=column,
            sticky="nsew",
            padx=6
        )

        card.grid_propagate(False)

        # Top accent

        tk.Frame(
            card,
            bg=color,
            height=4
        ).pack(
            fill=tk.X
        )

        body = tk.Frame(
            card,
            bg=self.card
        )

        body.pack(
            fill=tk.BOTH,
            expand=True,
            padx=16,
            pady=10
        )

        icon_label = tk.Label(
            body,
            text=icon,
            bg=color,
            fg="white",
            font=("Segoe UI", 11, "bold"),
            width=3,
            height=1
        )

        icon_label.pack(
            side=tk.LEFT,
            anchor="n",
            padx=(0, 12)
        )

        info = tk.Frame(
            body,
            bg=self.card
        )

        info.pack(
            side=tk.LEFT,
            fill=tk.BOTH,
            expand=True
        )

        tk.Label(
            info,
            text=title,
            bg=self.card,
            fg=self.text_muted,
            font=("Segoe UI", 8, "bold")
        ).pack(
            anchor="w"
        )

        tk.Label(
            info,
            text=value,
            bg=self.card,
            fg=self.text,
            font=("Segoe UI", 21, "bold")
        ).pack(
            anchor="w",
            pady=(2, 0)
        )

        tk.Label(
            info,
            text=subtitle,
            bg=self.card,
            fg=self.text_muted,
            font=("Segoe UI", 8)
        ).pack(
            anchor="w"
        )

    # =====================================================
    # PERFORMANCE ROW
    # =====================================================

    def performance_row(
        self,
        parent,
        title,
        percentage,
        color
    ):

        row = tk.Frame(
            parent,
            bg=self.card
        )

        row.pack(
            fill=tk.X,
            pady=7
        )

        tk.Label(
            row,
            text=title,
            bg=self.card,
            fg=self.text_secondary,
            font=("Segoe UI", 9, "bold"),
            width=8,
            anchor="w"
        ).pack(
            side=tk.LEFT
        )

        bar_background = tk.Frame(
            row,
            bg="#0b1322",
            height=10
        )

        bar_background.pack(
            side=tk.LEFT,
            fill=tk.X,
            expand=True,
            padx=10
        )

        fill_width = max(
            int(percentage * 2.5),
            2
        )

        if percentage == 0:
            fill_width = 0

        tk.Frame(
            bar_background,
            bg=color,
            height=10,
            width=fill_width
        ).place(
            x=0,
            y=0
        )

        tk.Label(
            row,
            text=f"{percentage:.1f}%",
            bg=self.card,
            fg=color,
            font=("Segoe UI", 9, "bold"),
            width=8,
            anchor="e"
        ).pack(
            side=tk.RIGHT
        )

    # =====================================================
    # SYSTEM INFO
    # =====================================================

    def system_info(
        self,
        parent,
        title,
        value,
        color
    ):

        frame = tk.Frame(
            parent,
            bg=self.card
        )

        frame.pack(
            fill=tk.X,
            padx=20,
            pady=5
        )

        tk.Label(
            frame,
            text=title,
            bg=self.card,
            fg=self.text_muted,
            font=("Segoe UI", 8, "bold")
        ).pack(
            side=tk.LEFT
        )

        tk.Label(
            frame,
            text="● " + value,
            bg=self.card,
            fg=color,
            font=("Segoe UI", 8, "bold")
        ).pack(
            side=tk.RIGHT
        )

    # =====================================================
    # DATABASE CHECK
    # =====================================================

    def check_connection(self):

        try:

            conn = connect_database()

            if conn:

                conn.close()

                return True

            return False

        except:

            return False

    # =====================================================
    # LOAD RECENT STUDENTS
    # =====================================================

    def load_recent_students(
        self,
        table
    ):

        try:

            conn = connect_database()

            if conn is None:
                return

            cursor = conn.cursor()

            cursor.execute(
                """
                SELECT TOP 10
                    StudentID,
                    StudentName,
                    Course,
                    Marks,
                    Status
                FROM Students
                ORDER BY StudentID DESC
                """
            )

            rows = cursor.fetchall()

            for index, row in enumerate(rows):

                if index % 2 == 0:

                    row_tag = "even"

                else:

                    row_tag = "odd"

                table.insert(
                    "",
                    tk.END,
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        f"{row[3]}%",
                        row[4]
                    ),
                    tags=(row_tag,)
                )

            conn.close()

        except Exception as e:

            print(
                "Student Table Error:",
                e
            )