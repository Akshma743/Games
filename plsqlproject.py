import sqlite3
from tkinter import *
from tkinter import messagebox

# --- Database Setup ---
conn = sqlite3.connect('course_enrollment.db')
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS enrollments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_name TEXT NOT NULL,
    course_name TEXT NOT NULL,
    duration TEXT NOT NULL
)
''')
conn.commit()

# --- Functions ---
def add_record():
    student = student_name.get()
    course = course_name.get()
    time = duration.get()

    if student == "" or course == "" or time == "":
        messagebox.showerror("Error", "All fields are required")
    else:
        c.execute("INSERT INTO enrollments (student_name, course_name, duration) VALUES (?, ?, ?)",
                  (student, course, time))
        conn.commit()
        messagebox.showinfo("Success", "Record added successfully")
        clear_fields()

def update_record():
    if not id_field.get():
        messagebox.showerror("Error", "Enter ID to update")
        return

    c.execute("SELECT * FROM enrollments WHERE id=?", (id_field.get(),))
    if not c.fetchone():
        messagebox.showerror("Error", "No record found with this ID")
        return

    c.execute("UPDATE enrollments SET student_name=?, course_name=?, duration=? WHERE id=?",
              (student_name.get(), course_name.get(), duration.get(), id_field.get()))
    conn.commit()
    messagebox.showinfo("Updated", "Record updated successfully")
    clear_fields()

def delete_record():
    if not id_field.get():
        messagebox.showerror("Error", "Enter ID to delete")
        return

    try:
        record_id = int(id_field.get())
    except ValueError:
        messagebox.showerror("Error", "ID must be a number")
        return

    c.execute("SELECT * FROM enrollments WHERE id=?", (record_id,))
    record = c.fetchone()
    if not record:
        messagebox.showerror("Error", f"No record found with ID {record_id}")
        return

    confirm = messagebox.askyesno("Confirm", f"Delete record for '{record[1]}'?")
    if confirm:
        c.execute("DELETE FROM enrollments WHERE id=?", (record_id,))
        conn.commit()
        messagebox.showinfo("Deleted", "Record deleted successfully")
        clear_fields()
    else:
        messagebox.showinfo("Cancelled", "Deletion cancelled")

def show_records_window():
    view_win = Toplevel(root)
    view_win.title("All Enrollments")
    view_win.geometry("550x400")
    view_win.config(bg="#f9f9f9")

    Label(view_win, text="All Enrolled Students", font=("Arial", 14, "bold"), bg="#f9f9f9").pack(pady=10)

    listbox = Listbox(view_win, width=80, height=15)
    listbox.pack(pady=10)

    c.execute("SELECT * FROM enrollments")
    records = c.fetchall()
    for r in records:
        listbox.insert(END, f"ID:{r[0]} | Student:{r[1]} | Course:{r[2]} | Duration:{r[3]}")

    Button(view_win, text="Close", command=view_win.destroy, bg="#607D8B", fg="white", width=10).pack(pady=5)

def clear_fields():
    id_field.delete(0, END)
    student_name.delete(0, END)
    course_name.delete(0, END)
    duration.delete(0, END)

# --- GUI Setup ---
root = Tk()
root.title("Course Enrollment System")
root.geometry("650x450")
root.configure(bg="#f5f5f5")

Label(root, text="Course Enrollment System", font=("Arial", 18, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)

frame = Frame(root, bg="#f5f5f5")
frame.pack(pady=10)

Label(frame, text="ID:", bg="#f5f5f5").grid(row=0, column=0, padx=5, pady=5)
id_field = Entry(frame)
id_field.grid(row=0, column=1, padx=5, pady=5)

Label(frame, text="Student Name:", bg="#f5f5f5").grid(row=1, column=0, padx=5, pady=5)
student_name = Entry(frame)
student_name.grid(row=1, column=1, padx=5, pady=5)

Label(frame, text="Course Name:", bg="#f5f5f5").grid(row=2, column=0, padx=5, pady=5)
course_name = Entry(frame)
course_name.grid(row=2, column=1, padx=5, pady=5)

Label(frame, text="Duration:", bg="#f5f5f5").grid(row=3, column=0, padx=5, pady=5)
duration = Entry(frame)
duration.grid(row=3, column=1, padx=5, pady=5)

# Buttons
btn_frame = Frame(root, bg="#f5f5f5")
btn_frame.pack(pady=10)

Button(btn_frame, text="Add", width=10, command=add_record, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=5)
Button(btn_frame, text="Update", width=10, command=update_record, bg="#2196F3", fg="white").grid(row=0, column=1, padx=5)
Button(btn_frame, text="Delete", width=10, command=delete_record, bg="#f44336", fg="white").grid(row=0, column=2, padx=5)
Button(btn_frame, text="Show All", width=10, command=show_records_window, bg="#9C27B0", fg="white").grid(row=0, column=3, padx=5)
Button(btn_frame, text="Clear", width=10, command=clear_fields, bg="#607D8B", fg="white").grid(row=0, column=4, padx=5)

root.mainloop()
conn.close()