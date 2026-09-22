import tkinter as tk
from tkinter import ttk, messagebox

from database import connect_database


class Students:

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

        self.border = "#24334b"

        self.blue = "#3b82f6"
        self.blue_dark = "#2563eb"
        self.green = "#22c55e"
        self.red = "#ef4444"
        self.orange = "#f59e0b"

        self.text = "#f8fafc"
        self.text_secondary = "#cbd5e1"
        self.text_muted = "#718096"

        self.selected_student_id = None

        self.create_styles()
        self.create_page()
        self.load_students()

    # =====================================================
    # TREEVIEW STYLE
    # =====================================================

    def create_styles(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "Professional.Treeview",
            background=self.table_bg,
            foreground=self.text_secondary,
            fieldbackground=self.table_bg,
            rowheight=48,
            borderwidth=0,
            relief="flat",
            font=("Segoe UI", 10)
        )

        style.map(
            "Professional.Treeview",
            background=[
                ("selected", self.blue)
            ],
            foreground=[
                ("selected", "#ffffff")
            ]
        )

        style.configure(
            "Professional.Treeview.Heading",
            background="#18253a",
            foreground=self.text,
            font=("Segoe UI Semibold", 10),
            borderwidth=0,
            relief="flat",
            padding=(10, 14)
        )

        style.map(
            "Professional.Treeview.Heading",
            background=[
                ("active", "#1f304a")
            ]
        )

        style.configure(
            "Dark.Vertical.TScrollbar",
            background="#18253a",
            troughcolor="#0a0f1c",
            bordercolor="#0a0f1c",
            arrowcolor="#cbd5e1"
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
        # PAGE HEADER
        # =================================================

        header = tk.Frame(
            main,
            bg=self.bg
        )
        header.pack(
            fill="x",
            padx=30,
            pady=(25, 15)
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
            text="Student Management",
            font=("Segoe UI Semibold", 24),
            bg=self.bg,
            fg=self.text
        ).pack(anchor="w")

        tk.Label(
            title_area,
            text="Manage student records, academic details and results",
            font=("Segoe UI", 10),
            bg=self.bg,
            fg=self.text_muted
        ).pack(
            anchor="w",
            pady=(5, 0)
        )

        # =================================================
        # DATABASE STATUS
        # =================================================

        status_frame = tk.Frame(
            header,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )
        status_frame.pack(
            side="right",
            padx=(10, 0)
        )

        tk.Label(
            status_frame,
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
            status_frame,
            text="Database Connected",
            font=("Segoe UI Semibold", 9),
            bg=self.card,
            fg=self.text_secondary
        ).pack(
            side="left",
            padx=(0, 12)
        )

        # =================================================
        # FORM CARD
        # =================================================

        form_card = tk.Frame(
            main,
            bg=self.card,
            highlightbackground=self.border,
            highlightthickness=1
        )
        form_card.pack(
            fill="x",
            padx=30,
            pady=(0, 18)
        )

        # Form title

        form_header = tk.Frame(
            form_card,
            bg=self.card
        )
        form_header.pack(
            fill="x",
            padx=20,
            pady=(18, 5)
        )

        tk.Label(
            form_header,
            text="Student Information",
            font=("Segoe UI Semibold", 13),
            bg=self.card,
            fg=self.text
        ).pack(side="left")

        tk.Label(
            form_header,
            text="Add new student or edit selected record",
            font=("Segoe UI", 9),
            bg=self.card,
            fg=self.text_muted
        ).pack(
            side="left",
            padx=15
        )

        # =================================================
        # FORM AREA
        # =================================================

        form = tk.Frame(
            form_card,
            bg=self.card
        )
        form.pack(
            fill="x",
            padx=20,
            pady=(8, 20)
        )

        # Student Name

        name_box = tk.Frame(
            form,
            bg=self.card
        )
        name_box.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 12)
        )

        tk.Label(
            name_box,
            text="STUDENT NAME",
            font=("Segoe UI Semibold", 8),
            bg=self.card,
            fg=self.text_muted
        ).pack(anchor="w")

        self.name_entry = tk.Entry(
            name_box,
            font=("Segoe UI", 10),
            bg="#0b1424",
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            highlightbackground=self.border,
            highlightcolor=self.blue,
            highlightthickness=1
        )
        self.name_entry.pack(
            fill="x",
            ipady=9,
            pady=(6, 0)
        )

        # Course

        course_box = tk.Frame(
            form,
            bg=self.card
        )
        course_box.pack(
            side="left",
            fill="x",
            expand=True,
            padx=12
        )

        tk.Label(
            course_box,
            text="COURSE",
            font=("Segoe UI Semibold", 8),
            bg=self.card,
            fg=self.text_muted
        ).pack(anchor="w")

        self.course_entry = tk.Entry(
            course_box,
            font=("Segoe UI", 10),
            bg="#0b1424",
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            highlightbackground=self.border,
            highlightcolor=self.blue,
            highlightthickness=1
        )
        self.course_entry.pack(
            fill="x",
            ipady=9,
            pady=(6, 0)
        )

        # Marks

        marks_box = tk.Frame(
            form,
            bg=self.card
        )
        marks_box.pack(
            side="left",
            fill="x",
            expand=True,
            padx=12
        )

        tk.Label(
            marks_box,
            text="MARKS",
            font=("Segoe UI Semibold", 8),
            bg=self.card,
            fg=self.text_muted
        ).pack(anchor="w")

        self.marks_entry = tk.Entry(
            marks_box,
            font=("Segoe UI", 10),
            bg="#0b1424",
            fg=self.text,
            insertbackground=self.text,
            relief="flat",
            highlightbackground=self.border,
            highlightcolor=self.blue,
            highlightthickness=1
        )
        self.marks_entry.pack(
            fill="x",
            ipady=9,
            pady=(6, 0)
        )

        # Buttons

        button_box = tk.Frame(
            form,
            bg=self.card
        )
        button_box.pack(
            side="left",
            padx=(15, 0),
            pady=(15, 0)
        )

        self.add_button = tk.Button(
            button_box,
            text="＋  ADD STUDENT",
            command=self.add_student,
            font=("Segoe UI Semibold", 9),
            bg=self.blue,
            fg="white",
            activebackground=self.blue_dark,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=16,
            pady=10
        )
        self.add_button.pack(
            side="left",
            padx=4
        )

        self.update_button = tk.Button(
            button_box,
            text="✎  UPDATE",
            command=self.update_student,
            font=("Segoe UI Semibold", 9),
            bg="#1d4ed8",
            fg="white",
            activebackground=self.blue_dark,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=16,
            pady=10
        )
        self.update_button.pack(
            side="left",
            padx=4
        )

        tk.Button(
            button_box,
            text="CLEAR",
            command=self.clear_form,
            font=("Segoe UI Semibold", 9),
            bg="#1a2639",
            fg=self.text_secondary,
            activebackground="#253650",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=16,
            pady=10
        ).pack(
            side="left",
            padx=4
        )

        # =================================================
        # TABLE CARD
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

        # Table Header

        table_header = tk.Frame(
            table_card,
            bg=self.card
        )
        table_header.pack(
            fill="x",
            padx=20,
            pady=(18, 12)
        )

        tk.Label(
            table_header,
            text="Student Records",
            font=("Segoe UI Semibold", 13),
            bg=self.card,
            fg=self.text
        ).pack(side="left")

        self.record_count_label = tk.Label(
            table_header,
            text="0 Records",
            font=("Segoe UI Semibold", 9),
            bg="#18253a",
            fg=self.text_secondary,
            padx=10,
            pady=5
        )
        self.record_count_label.pack(
            side="left",
            padx=12
        )

        tk.Button(
            table_header,
            text="↻  REFRESH",
            command=self.load_students,
            font=("Segoe UI Semibold", 9),
            bg="#18253a",
            fg=self.text_secondary,
            activebackground="#253650",
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            padx=14,
            pady=7
        ).pack(side="right")

        # =================================================
        # TABLE
        # =================================================

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
            "status"
        )

        self.tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings",
            style="Professional.Treeview",
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
            "status",
            text="STATUS"
        )

        self.tree.column(
            "id",
            width=80,
            anchor="center"
        )

        self.tree.column(
            "name",
            width=300,
            anchor="w"
        )

        self.tree.column(
            "course",
            width=220,
            anchor="w"
        )

        self.tree.column(
            "marks",
            width=120,
            anchor="center"
        )

        self.tree.column(
            "status",
            width=140,
            anchor="center"
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.tree.yview,
            style="Dark.Vertical.TScrollbar"
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

        # Alternating rows

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

        self.tree.tag_configure(
            "pass",
            foreground="#86efac"
        )

        self.tree.tag_configure(
            "fail",
            foreground="#fca5a5"
        )

        self.tree.bind(
            "<ButtonRelease-1>",
            self.select_student
        )

    # =====================================================
    # ADD STUDENT
    # =====================================================

    def add_student(self):

        name = self.name_entry.get().strip()
        course = self.course_entry.get().strip()
        marks_text = self.marks_entry.get().strip()

        if not name or not course or not marks_text:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all student details."
            )

            return

        try:
            marks = float(marks_text)

        except ValueError:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be a number."
            )

            return

        if marks < 0 or marks > 100:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be between 0 and 100."
            )

            return

        status = "PASS" if marks >= 40 else "FAIL"

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
                INSERT INTO Students
                (StudentName, Course, Marks, Status)
                VALUES (?, ?, ?, ?)
                """,
                (
                    name,
                    course,
                    marks,
                    status
                )
            )

            connection.commit()

            messagebox.showinfo(
                "Success",
                "Student added successfully."
            )

            self.clear_form()
            self.load_students()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            connection.close()

    # =====================================================
    # SELECT STUDENT
    # =====================================================

    def select_student(self, event=None):

        selected = self.tree.selection()

        if not selected:
            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        if not values:
            return

        self.selected_student_id = values[0]

        self.name_entry.delete(0, tk.END)
        self.name_entry.insert(0, values[1])

        self.course_entry.delete(0, tk.END)
        self.course_entry.insert(0, values[2])

        self.marks_entry.delete(0, tk.END)
        self.marks_entry.insert(0, values[3])

    # =====================================================
    # UPDATE STUDENT
    # =====================================================

    def update_student(self):

        if self.selected_student_id is None:

            messagebox.showwarning(
                "Select Student",
                "Please select a student record first."
            )

            return

        name = self.name_entry.get().strip()
        course = self.course_entry.get().strip()
        marks_text = self.marks_entry.get().strip()

        if not name or not course or not marks_text:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all student details."
            )

            return

        try:
            marks = float(marks_text)

        except ValueError:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be a number."
            )

            return

        if marks < 0 or marks > 100:

            messagebox.showerror(
                "Invalid Marks",
                "Marks must be between 0 and 100."
            )

            return

        status = "PASS" if marks >= 40 else "FAIL"

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
                UPDATE Students
                SET StudentName=?,
                    Course=?,
                    Marks=?,
                    Status=?
                WHERE StudentID=?
                """,
                (
                    name,
                    course,
                    marks,
                    status,
                    self.selected_student_id
                )
            )

            connection.commit()

            messagebox.showinfo(
                "Updated",
                "Student record updated successfully."
            )

            self.clear_form()
            self.load_students()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            connection.close()

    # =====================================================
    # DELETE STUDENT
    # =====================================================

    def delete_student(self):

        selected = self.tree.selection()

        if not selected:

            messagebox.showwarning(
                "Select Student",
                "Please select a student first."
            )

            return

        values = self.tree.item(
            selected[0],
            "values"
        )

        student_id = values[0]

        answer = messagebox.askyesno(
            "Delete Student",
            f"Are you sure you want to delete\n"
            f"{values[1]}?"
        )

        if not answer:
            return

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
                "DELETE FROM Students WHERE StudentID=?",
                (student_id,)
            )

            connection.commit()

            messagebox.showinfo(
                "Deleted",
                "Student deleted successfully."
            )

            self.clear_form()
            self.load_students()

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            connection.close()

    # =====================================================
    # CLEAR FORM
    # =====================================================

    def clear_form(self):

        self.selected_student_id = None

        self.name_entry.delete(
            0,
            tk.END
        )

        self.course_entry.delete(
            0,
            tk.END
        )

        self.marks_entry.delete(
            0,
            tk.END
        )

        self.tree.selection_remove(
            self.tree.selection()
        )

        self.name_entry.focus()

    # =====================================================
    # LOAD STUDENTS
    # =====================================================

    def load_students(self):

        for item in self.tree.get_children():
            self.tree.delete(item)

        connection = connect_database()

        if connection is None:

            self.record_count_label.config(
                text="Database Offline"
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
                ORDER BY StudentID DESC
                """
            )

            rows = cursor.fetchall()

            for index, row in enumerate(rows):

                status = str(row[4]).upper()

                tag = "even" if index % 2 == 0 else "odd"

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        status
                    ),
                    tags=(tag,)
                )

            self.record_count_label.config(
                text=f"{len(rows)} Records"
            )

        except Exception as e:

            messagebox.showerror(
                "Database Error",
                str(e)
            )

        finally:

            connection.close()