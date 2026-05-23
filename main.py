import tkinter as tk
from tkinter import filedialog, messagebox
import pdfplumber


required_skills = [
    "python",
    "java",
    "sql",
    "machine learning",
    "data science",
    "html",
    "css",
    "javascript"
]


def extract_text(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            text += page.extract_text()

    return text.lower()


def check_resume():

    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not file_path:
        return

    resume_text = extract_text(file_path)

    matched_skills = []

    for skill in required_skills:

        if skill in resume_text:

            matched_skills.append(skill)

    score = (
        len(matched_skills)
        / len(required_skills)
    ) * 100

    result = (
        f"Resume Match Score: {score:.2f}%\n\n"
        f"Matched Skills:\n"
        f"{', '.join(matched_skills)}"
    )

    result_label.config(text=result)


root = tk.Tk()

root.title("Resume Screening System")

root.geometry("600x500")

root.config(bg="#1f1f2e")

title = tk.Label(
    root,
    text="AI Resume Screening System",
    font=("Helvetica", 22, "bold"),
    bg="#1f1f2e",
    fg="white"
)

title.pack(pady=20)

desc = tk.Label(
    root,
    text="Upload Resume PDF to Check Skills Match",
    font=("Helvetica", 12),
    bg="#1f1f2e",
    fg="#bbbbbb"
)

desc.pack()

upload_button = tk.Button(
    root,
    text="Upload Resume",
    command=check_resume,
    font=("Helvetica", 14, "bold"),
    bg="#4CAF50",
    fg="white",
    padx=20,
    pady=10,
    bd=0,
    cursor="hand2"
)

upload_button.pack(pady=30)


result_frame = tk.Frame(
    root,
    bg="#2d2d44"
)

result_frame.pack(
    padx=20,
    pady=20,
    fill="both",
    expand=True
)


result_label = tk.Label(
    result_frame,
    text="",
    font=("Helvetica", 14),
    bg="#2d2d44",
    fg="white",
    justify="left"
)

result_label.pack(pady=30)


footer = tk.Label(
    root,
    text="Created using Python & NLP",
    font=("Helvetica", 10),
    bg="#1f1f2e",
    fg="#888888"
)

footer.pack(side="bottom", pady=10)


root.mainloop()