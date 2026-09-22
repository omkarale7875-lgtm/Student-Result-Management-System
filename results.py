<<<<<<< HEAD
import tkinter as tk
from tkinter import ttk, messagebox

from database import connect_database


class Results:

    def __init__(self, parent, app):

        self.parent = parent
        self.app = app

        # =====================================================
        # COLORS
        # =====================================================

        self.bg = "#0a0f1c"
        self.card = "#121b2b"
        self.card2 = "#0f1929"

        self.table_bg = "#0d1626"
        self.table_row = "#111c2e"
        self.table_alt = "#0e192a"
        self.table_header = "#18253a"

        self.border = "#24334b"

        self.blue = "#3b82f6"
        self.green = "#22c55e"
        self.red = "#ef4444"
        self.orange = "#f59e0b"
        self.purple = "#8b5cf6"

        self.text = "#f8fafc"
        self.text_secondary = "#cbd5e1"
        self.text_muted = "#718096"

        self.create_styles()
        self.create_page()
        self.load_results()

    # =====================================================
    # STYLES
    # =====================================================

    def create_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Result.Treeview",
            background=self.table_bg,
            foreground=self.text_secondary,
            fieldbackground=self.table_bg,
            rowheight=46,
            borderwidth=0,
            relief="flat",
            font=("Segoe UI", 10)
        )

        style.map(
            "Result.Treeview",
            background=[
                ("selected", self.blue)
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        style.configure(
            "Result.Treeview.Heading",
            background=self.table_header,
            foreground=self.text,
            font=("Segoe UI Semibold", 10),
            borderwidth=0,
            relief="flat",
            padding=(10, 13)
        )

        style.map(
            "Result.Treeview.Heading",
            background=[
                ("active", "#223552")
            ]
        )

        style.configure(
            "Result.Vertical.TScrollbar",
            background="#18253a",
            troughcolor=self.bg,
            bordercolor=self.bg,
            arrowcolor=self.text_secondary
        )

    # =====================================================
    # MAIN PAGE
    # =====================================================

    def create_page(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        main = tk.Frame(
            self.parent,
            bg=self.bg
        )

        main.pack(
            fill="both",
            expand=True
        )

        # =================================================
        # HEADER
        # =================================================

        header = tk.Frame(
            main,
            bg=self.bg
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 18)
        )

        title_area = tk.Frame(
            header,
            bg=self.bg
        )

        title_area.pack(
            side="left"
        )

        tk.Label(
            title_area,
            text="Results & Analytics",
            font=("Segoe UI Semibold", 24),
            bg=self.bg,
            fg=self.text
        ).pack(
            anchor="w"
        )

        tk.Label(
            title_area,
            text="Monitor academic performance, grades and overall results",
            font=("Segoe UI", 10),
            bg=self.bg,
            fg=self.text_muted
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # Database status

        status_box = tk.Frame(
            header,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        status_box.pack(
            side="right"
        )

        tk.Label(
            status_box,
            text="●",
            font=("Segoe UI", 12),
            bg=self.card,
            fg=self.green
        ).pack(
            side="left",
            padx=(12, 5),
            pady=9
        )

        tk.Label(
            status_box,
            text="Live Results",
            font=("Segoe UI Semibold", 9),
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="left",
            padx=(0, 12)
        )

        # =================================================
        # KPI SECTION
        # =================================================

        kpi_frame = tk.Frame(
            main,
            bg=self.bg
        )

        kpi_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 18)
        )

        self.total_card = self.create_kpi(
            kpi_frame,
            "TOTAL STUDENTS",
            "0",
            self.blue
        )

        self.pass_card = self.create_kpi(
            kpi_frame,
            "PASSED",
            "0",
            self.green
        )

        self.fail_card = self.create_kpi(
            kpi_frame,
            "FAILED",
            "0",
            self.red
        )

        self.avg_card = self.create_kpi(
            kpi_frame,
            "AVERAGE MARKS",
            "0.00",
            self.purple
        )

        self.rate_card = self.create_kpi(
            kpi_frame,
            "PASS RATE",
            "0%",
            self.orange
        )

        # =================================================
        # ANALYTICS SECTION
        # =================================================

        analytics = tk.Frame(
            main,
            bg=self.bg
        )

        analytics.pack(
            fill="x",
            padx=30,
            pady=(0, 18)
        )

        # Grade distribution

        grade_card = tk.Frame(
            analytics,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        grade_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 9)
        )

        tk.Label(
            grade_card,
            text="Grade Distribution",
            font=("Segoe UI Semibold", 12),
            bg=self.card,
            fg=self.text
        ).pack(
            anchor="w",
            padx=18,
            pady=(16, 12)
        )

        self.grade_area = tk.Frame(
            grade_card,
            bg=self.card
        )

        self.grade_area.pack(
            fill="x",
            padx=18,
            pady=(0, 17)
        )

        # Result overview

        overview_card = tk.Frame(
            analytics,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        overview_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(9, 0)
        )

        tk.Label(
            overview_card,
            text="Performance Overview",
            font=("Segoe UI Semibold", 12),
            bg=self.card,
            fg=self.text
        ).pack(
            anchor="w",
            padx=18,
            pady=(16, 12)
        )

        self.performance_area = tk.Frame(
            overview_card,
            bg=self.card
        )

        self.performance_area.pack(
            fill="x",
            padx=18,
            pady=(0, 17)
        )

        # =================================================
        # RESULT TABLE
        # =================================================

        table_card = tk.Frame(
            main,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        table_header = tk.Frame(
            table_card,
            bg=self.card
        )

        table_header.pack(
            fill="x",
            padx=20,
            pady=(17, 12)
        )

        tk.Label(
            table_header,
            text="Student Result Records",
            font=("Segoe UI Semibold", 13),
            bg=self.card,
            fg=self.text
        ).pack(
            side="left"
        )

        self.record_label = tk.Label(
            table_header,
            text="0 Records",
            font=("Segoe UI Semibold", 9),
            bg=self.table_header,
            fg=self.text_secondary,
            padx=10,
            pady=5
        )

        self.record_label.pack(
            side="left",
            padx=12
        )

        tk.Button(
            table_header,
            text="↻  REFRESH RESULTS",
            command=self.load_results,
            font=("Segoe UI Semibold", 9),
            bg=self.table_header,
            fg=self.text_secondary,
            activebackground="#253650",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=14,
            pady=7
        ).pack(
            side="right"
        )

        # Table frame

        table_frame = tk.Frame(
            table_card,
            bg=self.table_bg
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "id",
            "name",
            "course",
            "marks",
            "grade",
            "result"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Result.Treeview",
            selectmode="browse"
        )

        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "name",
            text="STUDENT NAME"
        )

        self.tree.heading(
            "course",
            text="COURSE"
        )

        self.tree.heading(
            "marks",
            text="MARKS"
        )

        self.tree.heading(
            "grade",
            text="GRADE"
        )

        self.tree.heading(
            "result",
            text="RESULT"
        )

        self.tree.column(
            "id",
            width=70,
            anchor="center"
        )

        self.tree.column(
            "name",
            width=280,
            anchor="w"
        )

        self.tree.column(
            "course",
            width=200,
            anchor="w"
        )

        self.tree.column(
            "marks",
            width=110,
            anchor="center"
        )

        self.tree.column(
            "grade",
            width=110,
            anchor="center"
        )

        self.tree.column(
            "result",
            width=130,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview,
            style="Result.Vertical.TScrollbar"
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Row styles

        self.tree.tag_configure(
            "even",
            background=self.table_row,
            foreground=self.text_secondary
        )

        self.tree.tag_configure(
            "odd",
            background=self.table_alt,
            foreground=self.text_secondary
        )

    # =====================================================
    # KPI CARD
    # =====================================================

    def create_kpi(
        self,
        parent,
        title,
        value,
        accent
    ):

        card = tk.Frame(
            parent,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        # Accent line

        tk.Frame(
            card,
            bg=accent,
            height=3
        ).pack(
            fill="x"
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI Semibold", 8),
            bg=self.card,
            fg=self.text_muted
        ).pack(
            anchor="w",
            padx=16,
            pady=(13, 3)
        )

        value_label = tk.Label(
            card,
            text=value,
            font=("Segoe UI Semibold", 22),
            bg=self.card,
            fg=self.text
        )

        value_label.pack(
            anchor="w",
            padx=16,
            pady=(0, 14)
        )

        return value_label

    # =====================================================
    # GRADE ROW
    # =====================================================

    def create_grade_row(
        self,
        grade,
        count,
        total,
        accent
    ):

        row = tk.Frame(
            self.grade_area,
            bg=self.card
        )

        row.pack(
            fill="x",
            pady=3
        )

        tk.Label(
            row,
            text=grade,
            font=("Segoe UI Semibold", 9),
            width=4,
            anchor="w",
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="left"
        )

        bar_bg = tk.Frame(
            row,
            bg="#1b293d",
            height=8
        )

        bar_bg.pack(
            side="left",
            fill="x",
            expand=True,
            padx=8
        )

        if total > 0:
            percentage = count / total
        else:
            percentage = 0

        bar = tk.Frame(
            bar_bg,
            bg=accent,
            height=8
        )

        bar.place(
            relx=0,
            rely=0,
            relwidth=percentage,
            relheight=1
        )

        tk.Label(
            row,
            text=str(count),
            font=("Segoe UI Semibold", 9),
            width=5,
            anchor="e",
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="right"
        )

    # =====================================================
    # PERFORMANCE ROW
    # =====================================================

    def create_performance_row(
        self,
        title,
        value,
        percentage,
        accent
    ):

        row = tk.Frame(
            self.performance_area,
            bg=self.card
        )

        row.pack(
            fill="x",
            pady=5
        )

        top = tk.Frame(
            row,
            bg=self.card
        )

        top.pack(
            fill="x"
        )

        tk.Label(
            top,
            text=title,
            font=("Segoe UI", 9),
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="left"
        )

        tk.Label(
            top,
            text=value,
            font=("Segoe UI Semibold", 9),
            bg=self.card,
            fg=accent
        ).pack(
            side="right"
        )

        bar_bg = tk.Frame(
            row,
            bg="#1b293d",
            height=7
        )

        bar_bg.pack(
            fill="x",
            pady=(5, 0)
        )

        bar = tk.Frame(
            bar_bg,
            bg=accent,
            height=7
        )

        bar.place(
            relx=0,
            rely=0,
            relwidth=percentage,
            relheight=1
        )

    # =====================================================
    # LOAD RESULTS
    # =====================================================

    def load_results(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        connection = connect_database()

        if connection is None:

            messagebox.showerror(
                "Database Error",
                "Unable to connect to database."
            )

            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    StudentID,
                    StudentName,
                    Course,
                    Marks,
                    Status
                FROM Students
                ORDER BY Marks DESC
                """
            )

            rows = cursor.fetchall()

            total = len(rows)
            passed = 0
            failed = 0
            total_marks = 0

            grades = {
                "A+": 0,
                "A": 0,
                "B+": 0,
                "B": 0,
                "C": 0,
                "D": 0,
                "F": 0
            }

            # =============================================
            # PROCESS DATA
            # =============================================

            for row in rows:

                marks = float(row[3])
                status = str(row[4]).upper()

                total_marks += marks

                if status == "PASS":
                    passed += 1
                else:
                    failed += 1

                grade = self.get_grade(marks)

                grades[grade] += 1

            # =============================================
            # KPI VALUES
            # =============================================

            if total > 0:

                average = total_marks / total
                pass_rate = (passed / total) * 100

            else:

                average = 0
                pass_rate = 0

            self.total_card.config(
                text=str(total)
            )

            self.pass_card.config(
                text=str(passed)
            )

            self.fail_card.config(
                text=str(failed)
            )

            self.avg_card.config(
                text=f"{average:.2f}"
            )

            self.rate_card.config(
                text=f"{pass_rate:.1f}%"
            )

            self.record_label.config(
                text=f"{total} Records"
            )

            # =============================================
            # GRADE DISTRIBUTION
            # =============================================

            for widget in self.grade_area.winfo_children():
                widget.destroy()

            for grade, color in [
                ("A+", self.green),
                ("A", self.blue),
                ("B+", self.purple),
                ("B", "#06b6d4"),
                ("C", self.orange),
                ("D", "#f97316"),
                ("F", self.red)
            ]:

                self.create_grade_row(
                    grade,
                    grades[grade],
                    total,
                    color
                )

            # =============================================
            # PERFORMANCE OVERVIEW
            # =============================================

            for widget in self.performance_area.winfo_children():
                widget.destroy()

            self.create_performance_row(
                "Passed Students",
                str(passed),
                passed / total if total > 0 else 0,
                self.green
            )

            self.create_performance_row(
                "Failed Students",
                str(failed),
                failed / total if total > 0 else 0,
                self.red
            )

            self.create_performance_row(
                "Average Marks",
                f"{average:.2f}",
                min(average / 100, 1),
                self.blue
            )

            self.create_performance_row(
                "Pass Rate",
                f"{pass_rate:.1f}%",
                min(pass_rate / 100, 1),
                self.orange
            )

            # =============================================
            # TABLE
            # =============================================

            for index, row in enumerate(rows):

                marks = float(row[3])
                grade = self.get_grade(marks)

                status = str(row[4]).upper()

                tag = "even" if index % 2 == 0 else "odd"

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        f"{marks:.2f}",
                        grade,
                        status
                    ),
                    tags=(tag,)
                )

        except Exception as e:

            messagebox.showerror(
                "Results Error",
                str(e)
            )

        finally:

            connection.close()

    # =====================================================
    # GRADE CALCULATION
    # =====================================================

    def get_grade(self, marks):

        if marks >= 90:
            return "A+"

        elif marks >= 80:
            return "A"

        elif marks >= 70:
            return "B+"

        elif marks >= 60:
            return "B"

        elif marks >= 50:
            return "C"

        elif marks >= 40:
            return "D"

        else:
=======
import tkinter as tk
from tkinter import ttk, messagebox

from database import connect_database


class Results:

    def __init__(self, parent, app):

        self.parent = parent
        self.app = app

        # =====================================================
        # COLORS
        # =====================================================

        self.bg = "#0a0f1c"
        self.card = "#121b2b"
        self.card2 = "#0f1929"

        self.table_bg = "#0d1626"
        self.table_row = "#111c2e"
        self.table_alt = "#0e192a"
        self.table_header = "#18253a"

        self.border = "#24334b"

        self.blue = "#3b82f6"
        self.green = "#22c55e"
        self.red = "#ef4444"
        self.orange = "#f59e0b"
        self.purple = "#8b5cf6"

        self.text = "#f8fafc"
        self.text_secondary = "#cbd5e1"
        self.text_muted = "#718096"

        self.create_styles()
        self.create_page()
        self.load_results()

    # =====================================================
    # STYLES
    # =====================================================

    def create_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Result.Treeview",
            background=self.table_bg,
            foreground=self.text_secondary,
            fieldbackground=self.table_bg,
            rowheight=46,
            borderwidth=0,
            relief="flat",
            font=("Segoe UI", 10)
        )

        style.map(
            "Result.Treeview",
            background=[
                ("selected", self.blue)
            ],
            foreground=[
                ("selected", "white")
            ]
        )

        style.configure(
            "Result.Treeview.Heading",
            background=self.table_header,
            foreground=self.text,
            font=("Segoe UI Semibold", 10),
            borderwidth=0,
            relief="flat",
            padding=(10, 13)
        )

        style.map(
            "Result.Treeview.Heading",
            background=[
                ("active", "#223552")
            ]
        )

        style.configure(
            "Result.Vertical.TScrollbar",
            background="#18253a",
            troughcolor=self.bg,
            bordercolor=self.bg,
            arrowcolor=self.text_secondary
        )

    # =====================================================
    # MAIN PAGE
    # =====================================================

    def create_page(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        main = tk.Frame(
            self.parent,
            bg=self.bg
        )

        main.pack(
            fill="both",
            expand=True
        )

        # =================================================
        # HEADER
        # =================================================

        header = tk.Frame(
            main,
            bg=self.bg
        )

        header.pack(
            fill="x",
            padx=30,
            pady=(25, 18)
        )

        title_area = tk.Frame(
            header,
            bg=self.bg
        )

        title_area.pack(
            side="left"
        )

        tk.Label(
            title_area,
            text="Results & Analytics",
            font=("Segoe UI Semibold", 24),
            bg=self.bg,
            fg=self.text
        ).pack(
            anchor="w"
        )

        tk.Label(
            title_area,
            text="Monitor academic performance, grades and overall results",
            font=("Segoe UI", 10),
            bg=self.bg,
            fg=self.text_muted
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # Database status

        status_box = tk.Frame(
            header,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        status_box.pack(
            side="right"
        )

        tk.Label(
            status_box,
            text="●",
            font=("Segoe UI", 12),
            bg=self.card,
            fg=self.green
        ).pack(
            side="left",
            padx=(12, 5),
            pady=9
        )

        tk.Label(
            status_box,
            text="Live Results",
            font=("Segoe UI Semibold", 9),
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="left",
            padx=(0, 12)
        )

        # =================================================
        # KPI SECTION
        # =================================================

        kpi_frame = tk.Frame(
            main,
            bg=self.bg
        )

        kpi_frame.pack(
            fill="x",
            padx=30,
            pady=(0, 18)
        )

        self.total_card = self.create_kpi(
            kpi_frame,
            "TOTAL STUDENTS",
            "0",
            self.blue
        )

        self.pass_card = self.create_kpi(
            kpi_frame,
            "PASSED",
            "0",
            self.green
        )

        self.fail_card = self.create_kpi(
            kpi_frame,
            "FAILED",
            "0",
            self.red
        )

        self.avg_card = self.create_kpi(
            kpi_frame,
            "AVERAGE MARKS",
            "0.00",
            self.purple
        )

        self.rate_card = self.create_kpi(
            kpi_frame,
            "PASS RATE",
            "0%",
            self.orange
        )

        # =================================================
        # ANALYTICS SECTION
        # =================================================

        analytics = tk.Frame(
            main,
            bg=self.bg
        )

        analytics.pack(
            fill="x",
            padx=30,
            pady=(0, 18)
        )

        # Grade distribution

        grade_card = tk.Frame(
            analytics,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        grade_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(0, 9)
        )

        tk.Label(
            grade_card,
            text="Grade Distribution",
            font=("Segoe UI Semibold", 12),
            bg=self.card,
            fg=self.text
        ).pack(
            anchor="w",
            padx=18,
            pady=(16, 12)
        )

        self.grade_area = tk.Frame(
            grade_card,
            bg=self.card
        )

        self.grade_area.pack(
            fill="x",
            padx=18,
            pady=(0, 17)
        )

        # Result overview

        overview_card = tk.Frame(
            analytics,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        overview_card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=(9, 0)
        )

        tk.Label(
            overview_card,
            text="Performance Overview",
            font=("Segoe UI Semibold", 12),
            bg=self.card,
            fg=self.text
        ).pack(
            anchor="w",
            padx=18,
            pady=(16, 12)
        )

        self.performance_area = tk.Frame(
            overview_card,
            bg=self.card
        )

        self.performance_area.pack(
            fill="x",
            padx=18,
            pady=(0, 17)
        )

        # =================================================
        # RESULT TABLE
        # =================================================

        table_card = tk.Frame(
            main,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        table_card.pack(
            fill="both",
            expand=True,
            padx=30,
            pady=(0, 25)
        )

        table_header = tk.Frame(
            table_card,
            bg=self.card
        )

        table_header.pack(
            fill="x",
            padx=20,
            pady=(17, 12)
        )

        tk.Label(
            table_header,
            text="Student Result Records",
            font=("Segoe UI Semibold", 13),
            bg=self.card,
            fg=self.text
        ).pack(
            side="left"
        )

        self.record_label = tk.Label(
            table_header,
            text="0 Records",
            font=("Segoe UI Semibold", 9),
            bg=self.table_header,
            fg=self.text_secondary,
            padx=10,
            pady=5
        )

        self.record_label.pack(
            side="left",
            padx=12
        )

        tk.Button(
            table_header,
            text="↻  REFRESH RESULTS",
            command=self.load_results,
            font=("Segoe UI Semibold", 9),
            bg=self.table_header,
            fg=self.text_secondary,
            activebackground="#253650",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=14,
            pady=7
        ).pack(
            side="right"
        )

        # Table frame

        table_frame = tk.Frame(
            table_card,
            bg=self.table_bg
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=(0, 20)
        )

        columns = (
            "id",
            "name",
            "course",
            "marks",
            "grade",
            "result"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Result.Treeview",
            selectmode="browse"
        )

        self.tree.heading(
            "id",
            text="ID"
        )

        self.tree.heading(
            "name",
            text="STUDENT NAME"
        )

        self.tree.heading(
            "course",
            text="COURSE"
        )

        self.tree.heading(
            "marks",
            text="MARKS"
        )

        self.tree.heading(
            "grade",
            text="GRADE"
        )

        self.tree.heading(
            "result",
            text="RESULT"
        )

        self.tree.column(
            "id",
            width=70,
            anchor="center"
        )

        self.tree.column(
            "name",
            width=280,
            anchor="w"
        )

        self.tree.column(
            "course",
            width=200,
            anchor="w"
        )

        self.tree.column(
            "marks",
            width=110,
            anchor="center"
        )

        self.tree.column(
            "grade",
            width=110,
            anchor="center"
        )

        self.tree.column(
            "result",
            width=130,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview,
            style="Result.Vertical.TScrollbar"
        )

        self.tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        # Row styles

        self.tree.tag_configure(
            "even",
            background=self.table_row,
            foreground=self.text_secondary
        )

        self.tree.tag_configure(
            "odd",
            background=self.table_alt,
            foreground=self.text_secondary
        )

    # =====================================================
    # KPI CARD
    # =====================================================

    def create_kpi(
        self,
        parent,
        title,
        value,
        accent
    ):

        card = tk.Frame(
            parent,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )

        card.pack(
            side="left",
            fill="both",
            expand=True,
            padx=5
        )

        # Accent line

        tk.Frame(
            card,
            bg=accent,
            height=3
        ).pack(
            fill="x"
        )

        tk.Label(
            card,
            text=title,
            font=("Segoe UI Semibold", 8),
            bg=self.card,
            fg=self.text_muted
        ).pack(
            anchor="w",
            padx=16,
            pady=(13, 3)
        )

        value_label = tk.Label(
            card,
            text=value,
            font=("Segoe UI Semibold", 22),
            bg=self.card,
            fg=self.text
        )

        value_label.pack(
            anchor="w",
            padx=16,
            pady=(0, 14)
        )

        return value_label

    # =====================================================
    # GRADE ROW
    # =====================================================

    def create_grade_row(
        self,
        grade,
        count,
        total,
        accent
    ):

        row = tk.Frame(
            self.grade_area,
            bg=self.card
        )

        row.pack(
            fill="x",
            pady=3
        )

        tk.Label(
            row,
            text=grade,
            font=("Segoe UI Semibold", 9),
            width=4,
            anchor="w",
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="left"
        )

        bar_bg = tk.Frame(
            row,
            bg="#1b293d",
            height=8
        )

        bar_bg.pack(
            side="left",
            fill="x",
            expand=True,
            padx=8
        )

        if total > 0:
            percentage = count / total
        else:
            percentage = 0

        bar = tk.Frame(
            bar_bg,
            bg=accent,
            height=8
        )

        bar.place(
            relx=0,
            rely=0,
            relwidth=percentage,
            relheight=1
        )

        tk.Label(
            row,
            text=str(count),
            font=("Segoe UI Semibold", 9),
            width=5,
            anchor="e",
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="right"
        )

    # =====================================================
    # PERFORMANCE ROW
    # =====================================================

    def create_performance_row(
        self,
        title,
        value,
        percentage,
        accent
    ):

        row = tk.Frame(
            self.performance_area,
            bg=self.card
        )

        row.pack(
            fill="x",
            pady=5
        )

        top = tk.Frame(
            row,
            bg=self.card
        )

        top.pack(
            fill="x"
        )

        tk.Label(
            top,
            text=title,
            font=("Segoe UI", 9),
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="left"
        )

        tk.Label(
            top,
            text=value,
            font=("Segoe UI Semibold", 9),
            bg=self.card,
            fg=accent
        ).pack(
            side="right"
        )

        bar_bg = tk.Frame(
            row,
            bg="#1b293d",
            height=7
        )

        bar_bg.pack(
            fill="x",
            pady=(5, 0)
        )

        bar = tk.Frame(
            bar_bg,
            bg=accent,
            height=7
        )

        bar.place(
            relx=0,
            rely=0,
            relwidth=percentage,
            relheight=1
        )

    # =====================================================
    # LOAD RESULTS
    # =====================================================

    def load_results(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        connection = connect_database()

        if connection is None:

            messagebox.showerror(
                "Database Error",
                "Unable to connect to database."
            )

            return

        try:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT
                    StudentID,
                    StudentName,
                    Course,
                    Marks,
                    Status
                FROM Students
                ORDER BY Marks DESC
                """
            )

            rows = cursor.fetchall()

            total = len(rows)
            passed = 0
            failed = 0
            total_marks = 0

            grades = {
                "A+": 0,
                "A": 0,
                "B+": 0,
                "B": 0,
                "C": 0,
                "D": 0,
                "F": 0
            }

            # =============================================
            # PROCESS DATA
            # =============================================

            for row in rows:

                marks = float(row[3])
                status = str(row[4]).upper()

                total_marks += marks

                if status == "PASS":
                    passed += 1
                else:
                    failed += 1

                grade = self.get_grade(marks)

                grades[grade] += 1

            # =============================================
            # KPI VALUES
            # =============================================

            if total > 0:

                average = total_marks / total
                pass_rate = (passed / total) * 100

            else:

                average = 0
                pass_rate = 0

            self.total_card.config(
                text=str(total)
            )

            self.pass_card.config(
                text=str(passed)
            )

            self.fail_card.config(
                text=str(failed)
            )

            self.avg_card.config(
                text=f"{average:.2f}"
            )

            self.rate_card.config(
                text=f"{pass_rate:.1f}%"
            )

            self.record_label.config(
                text=f"{total} Records"
            )

            # =============================================
            # GRADE DISTRIBUTION
            # =============================================

            for widget in self.grade_area.winfo_children():
                widget.destroy()

            for grade, color in [
                ("A+", self.green),
                ("A", self.blue),
                ("B+", self.purple),
                ("B", "#06b6d4"),
                ("C", self.orange),
                ("D", "#f97316"),
                ("F", self.red)
            ]:

                self.create_grade_row(
                    grade,
                    grades[grade],
                    total,
                    color
                )

            # =============================================
            # PERFORMANCE OVERVIEW
            # =============================================

            for widget in self.performance_area.winfo_children():
                widget.destroy()

            self.create_performance_row(
                "Passed Students",
                str(passed),
                passed / total if total > 0 else 0,
                self.green
            )

            self.create_performance_row(
                "Failed Students",
                str(failed),
                failed / total if total > 0 else 0,
                self.red
            )

            self.create_performance_row(
                "Average Marks",
                f"{average:.2f}",
                min(average / 100, 1),
                self.blue
            )

            self.create_performance_row(
                "Pass Rate",
                f"{pass_rate:.1f}%",
                min(pass_rate / 100, 1),
                self.orange
            )

            # =============================================
            # TABLE
            # =============================================

            for index, row in enumerate(rows):

                marks = float(row[3])
                grade = self.get_grade(marks)

                status = str(row[4]).upper()

                tag = "even" if index % 2 == 0 else "odd"

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        f"{marks:.2f}",
                        grade,
                        status
                    ),
                    tags=(tag,)
                )

        except Exception as e:

            messagebox.showerror(
                "Results Error",
                str(e)
            )

        finally:

            connection.close()

    # =====================================================
    # GRADE CALCULATION
    # =====================================================

    def get_grade(self, marks):

        if marks >= 90:
            return "A+"

        elif marks >= 80:
            return "A"

        elif marks >= 70:
            return "B+"

        elif marks >= 60:
            return "B"

        elif marks >= 50:
            return "C"

        elif marks >= 40:
            return "D"

        else:
>>>>>>> master
            return "F"