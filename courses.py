import tkinter as tk
from tkinter import messagebox

from database import connect_database


class Courses:

    def __init__(self, parent, app):

        self.parent = parent
        self.app = app

        # =====================================================
        # COLORS
        # =====================================================

        self.bg = "#0a0f1c"
        self.card = "#121b2b"
        self.card_hover = "#17243a"

        self.border = "#24334b"

        self.blue = "#3b82f6"
        self.green = "#22c55e"
        self.orange = "#f59e0b"
        self.purple = "#8b5cf6"
        self.cyan = "#06b6d4"

        self.text = "#f8fafc"
        self.text_secondary = "#cbd5e1"
        self.text_muted = "#718096"

        self.create_page()
        self.load_courses()

    # =====================================================
    # MAIN PAGE
    # =====================================================

    def create_page(self):

        for widget in self.parent.winfo_children():
            widget.destroy()

        main = tk.Frame(self.parent, bg=self.bg)

        main.pack(fill="both", expand=True)

        # =================================================
        # HEADER
        # =================================================

        header = tk.Frame(main, bg=self.bg)

        header.pack(fill="x", padx=30, pady=(25, 18))

        title_area = tk.Frame(header, bg=self.bg)

        title_area.pack(side="left")

        tk.Label(
            title_area,
            text="Courses",
            font=("Segoe UI Semibold", 24),
            bg=self.bg,
            fg=self.text,
        ).pack(anchor="w")

        tk.Label(
            title_area,
            text="Manage academic programs and monitor course performance",
            font=("Segoe UI", 10),
            bg=self.bg,
            fg=self.text_muted,
        ).pack(anchor="w", pady=(5, 0))

        # Live status

        status_box = tk.Frame(
            header,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1,
        )

        status_box.pack(side="right")

        tk.Label(
            status_box,
            text="●",
            font=("Segoe UI", 12),
            bg=self.card,
            fg=self.green,
        ).pack(side="left", padx=(12, 5), pady=9)

        tk.Label(
            status_box,
            text="Academic Database",
            font=("Segoe UI Semibold", 9),
            bg=self.card,
            fg=self.text_secondary,
        ).pack(side="left", padx=(0, 12))

        # =================================================
        # SUMMARY CARDS
        # =================================================

        summary = tk.Frame(main, bg=self.bg)

        summary.pack(fill="x", padx=30, pady=(0, 20))

        self.total_courses_label = self.create_summary_card(
            summary, "ACTIVE COURSES", "0", self.blue
        )

        self.total_students_label = self.create_summary_card(
            summary, "TOTAL STUDENTS", "0", self.green
        )

        self.average_label = self.create_summary_card(
            summary, "OVERALL AVERAGE", "0.00", self.purple
        )

        self.top_course_label = self.create_summary_card(
            summary, "TOP COURSE", "—", self.orange
        )

        # =================================================
        # SECTION HEADER
        # =================================================

        section_header = tk.Frame(main, bg=self.bg)

        section_header.pack(fill="x", padx=30, pady=(0, 12))

        tk.Label(
            section_header,
            text="Academic Programs",
            font=("Segoe UI Semibold", 14),
            bg=self.bg,
            fg=self.text,
        ).pack(side="left")

        tk.Label(
            section_header,
            text="Course-wise student performance",
            font=("Segoe UI", 9),
            bg=self.bg,
            fg=self.text_muted,
        ).pack(side="left", padx=15)

        tk.Button(
            section_header,
            text="↻  REFRESH",
            command=self.load_courses,
            font=("Segoe UI Semibold", 9),
            bg="#18253a",
            fg=self.text_secondary,
            activebackground="#253650",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=14,
            pady=7,
        ).pack(side="right")

        # =================================================
        # COURSE AREA
        # =================================================

        self.course_area = tk.Frame(main, bg=self.bg)

        self.course_area.pack(
            fill="both", expand=True, padx=30, pady=(0, 25)
        )

    # =====================================================
    # SUMMARY CARD
    # =====================================================

    def create_summary_card(self, parent, title, value, accent):

        card = tk.Frame(
            parent,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1,
        )

        card.pack(side="left", fill="both", expand=True, padx=5)

        tk.Frame(card, bg=accent, height=3).pack(fill="x")

        tk.Label(
            card,
            text=title,
            font=("Segoe UI Semibold", 8),
            bg=self.card,
            fg=self.text_muted,
        ).pack(anchor="w", padx=16, pady=(13, 3))

        value_label = tk.Label(
            card,
            text=value,
            font=("Segoe UI Semibold", 21),
            bg=self.card,
            fg=self.text,
        )

        value_label.pack(anchor="w", padx=16, pady=(0, 14))

        return value_label

    # =====================================================
    # COURSE CARD
    # =====================================================

    def create_course_card(
        self, parent, course_name, description, students, average, accent
    ):

        card = tk.Frame(
            parent,
            bg=self.card,
            width=500,
            height=250,
            highlightbackground=self.border,
            highlightthickness=1,
        )

        card.pack(side="left", fill="both", expand=True, padx=7, pady=7)

        # Makes every course card same size
        card.pack_propagate(False)

        # Top Accent
        tk.Frame(card, bg=accent, height=4).pack(fill="x")

        # Header
        top = tk.Frame(card, bg=self.card)
        top.pack(fill="x", padx=18, pady=(16, 8))

        # Icon Box
        icon_box = tk.Frame(top, bg=accent, width=48, height=48)
        icon_box.pack(side="left")
        icon_box.pack_propagate(False)

        icon = self.get_course_icon(course_name)

        tk.Label(
            icon_box,
            text=icon,
            font=("Segoe UI Semibold", 16),
            bg=accent,
            fg="white",
        ).pack(expand=True)

        # Title Box
        title_box = tk.Frame(top, bg=self.card)
        title_box.pack(side="left", padx=12)

        tk.Label(
            title_box,
            text=course_name,
            font=("Segoe UI Semibold", 15),
            bg=self.card,
            fg=self.text,
        ).pack(anchor="w")

        tk.Label(
            title_box,
            text="ACADEMIC PROGRAM",
            font=("Segoe UI Semibold", 7),
            bg=self.card,
            fg=self.text_muted,
        ).pack(anchor="w", pady=(3, 0))

        # Description
        tk.Label(
            card,
            text=description,
            font=("Segoe UI", 9),
            bg=self.card,
            fg=self.text_secondary,
            justify="left",
            anchor="nw",
            wraplength=400,
        ).pack(fill="x", padx=18, pady=(3, 12))

        # Divider
        tk.Frame(card, bg=self.border, height=1).pack(fill="x", padx=18)

        # Statistics
        stats = tk.Frame(card, bg=self.card)
        stats.pack(fill="x", padx=18, pady=12)

        # Students
        student_box = tk.Frame(stats, bg=self.card)
        student_box.pack(side="left", fill="x", expand=True)

        tk.Label(
            student_box,
            text="STUDENTS",
            font=("Segoe UI Semibold", 7),
            bg=self.card,
            fg=self.text_muted,
        ).pack(anchor="w")

        tk.Label(
            student_box,
            text=str(students),
            font=("Segoe UI Semibold", 16),
            bg=self.card,
            fg=self.text,
        ).pack(anchor="w", pady=(2, 0))

        # Average
        average_box = tk.Frame(stats, bg=self.card)
        average_box.pack(side="left", fill="x", expand=True)

        tk.Label(
            average_box,
            text="AVG MARKS",
            font=("Segoe UI Semibold", 7),
            bg=self.card,
            fg=self.text_muted,
        ).pack(anchor="w")

        tk.Label(
            average_box,
            text=f"{average:.2f}",
            font=("Segoe UI Semibold", 16),
            bg=self.card,
            fg=accent,
        ).pack(anchor="w", pady=(2, 0))

        # Performance Bar
        tk.Label(
            card,
            text="ACADEMIC PERFORMANCE",
            font=("Segoe UI Semibold", 7),
            bg=self.card,
            fg=self.text_muted,
        ).pack(anchor="w", padx=18)

        performance = min(max(average / 100, 0), 1)

        bar_bg = tk.Frame(card, bg="#1b293d", height=7)
        bar_bg.pack(fill="x", padx=18, pady=(5, 15))

        bar = tk.Frame(bar_bg, bg=accent, height=7)
        bar.place(relx=0, rely=0, relwidth=performance, relheight=1)

    # =====================================================
    # COURSE ICON
    # =====================================================

    def get_course_icon(self, course):

        icons = {
            "BCA": "⌘",
            "BBA": "◈",
            "B.Sc CS": "◇",
            "MCA": "⚙",
            "MBA": "◆",
        }

        return icons.get(course, "●")

    # =====================================================
    # LOAD COURSES
    # =====================================================

    def load_courses(self):

        # Clear old cards
        for widget in self.course_area.winfo_children():
            widget.destroy()

        connection = connect_database()

        if connection is None:
            messagebox.showerror(
                "Database Error", "Unable to connect to database."
            )
            return

        try:
            cursor = connection.cursor()

            # =============================================
            # GET COURSE DATA
            # =============================================

            cursor.execute(
                """
                SELECT
                    Course,
                    COUNT(*) AS StudentCount,
                    AVG(CAST(Marks AS FLOAT)) AS AverageMarks
                FROM Students
                GROUP BY Course
                ORDER BY Course
                """
            )

            rows = cursor.fetchall()

            # =============================================
            # SUMMARY
            # =============================================

            total_students = 0
            total_marks = 0
            top_course = "—"
            top_average = -1

            for row in rows:
                course = str(row[0])
                students = int(row[1])
                average = float(row[2]) if row[2] is not None else 0

                total_students += students
                total_marks += average * students

                if average > top_average:
                    top_average = average
                    top_course = course

            if total_students > 0:
                overall_average = total_marks / total_students
            else:
                overall_average = 0

            self.total_courses_label.config(text=str(len(rows)))
            self.total_students_label.config(text=str(total_students))
            self.average_label.config(text=f"{overall_average:.2f}")
            self.top_course_label.config(text=top_course)

            # =============================================
            # COURSE DESCRIPTIONS
            # =============================================

            descriptions = {
                "BCA": (
                    "Bachelor of Computer Applications — focused on"
                    " programming, software development and computer"
                    " applications."
                ),
                "BBA": (
                    "Bachelor of Business Administration — focused on business"
                    " management, finance, marketing and administration."
                ),
                "B.Sc CS": (
                    "Bachelor of Science in Computer Science — focused on"
                    " computing, programming, databases and software"
                    " technologies."
                ),
                "MCA": (
                    "Master of Computer Applications — advanced study of"
                    " software engineering, applications and computing."
                ),
                "MBA": (
                    "Master of Business Administration — advanced management,"
                    " leadership and business strategy program."
                ),
            }

            colors = [
                self.blue,
                self.green,
                self.purple,
                self.orange,
                self.cyan,
            ]

            # =============================================
            # CREATE CARDS
            # =============================================

            row_frame = None

            for index, row in enumerate(rows):
                if index % 2 == 0:
                    row_frame = tk.Frame(
                        self.course_area, bg=self.bg, height=270
                    )
                    row_frame.pack(fill="x")
                    row_frame.pack_propagate(False)

                course = str(row[0])
                students = int(row[1])
                average = float(row[2]) if row[2] is not None else 0

                description = descriptions.get(
                    course,
                    "Academic program registered in the Student Result"
                    " Management System.",
                )

                accent = colors[index % len(colors)]

                self.create_course_card(
                    row_frame,
                    course,
                    description,
                    students,
                    average,
                    accent,
                )

            # =============================================
            # NO DATA
            # =============================================

            if len(rows) == 0:
                empty = tk.Frame(
                    self.course_area,
                    bg=self.card,
                    highlightbackground=self.border,
                    highlightthickness=1,
                )
                empty.pack(fill="both", expand=True, padx=7, pady=7)

                tk.Label(
                    empty,
                    text="No Course Data Available",
                    font=("Segoe UI Semibold", 16),
                    bg=self.card,
                    fg=self.text,
                ).pack(pady=(100, 5))

                tk.Label(
                    empty,
                    text=(
                        "Add students with a course name from the Students"
                        " page."
                    ),
                    font=("Segoe UI", 10),
                    bg=self.card,
                    fg=self.text_muted,
                ).pack()

        except Exception as e:
            messagebox.showerror("Courses Error", str(e))

        finally:
            connection.close()