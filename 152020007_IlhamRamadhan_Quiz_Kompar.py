import multiprocessing
import tkinter as tk
from tkinter import messagebox

# ================= FUNCTION =================
def rata_rata(data, result):
    result["avg"] = sum(data) / len(data)

def maksimum(data, result):
    result["max"] = max(data)

def minimum(data, result):
    result["min"] = min(data)

def lulus(data, result):
    result["lulus"] = len([x for x in data if x >= 75])

def tidak_lulus(data, result):
    result["tidak"] = len([x for x in data if x < 75])

def proses_data():
    try:
        data_input = entry.get()
        data = list(map(int, data_input.split(",")))

        manager = multiprocessing.Manager()
        result = manager.dict()

        processes = [
            multiprocessing.Process(target=rata_rata, args=(data, result)),
            multiprocessing.Process(target=maksimum, args=(data, result)),
            multiprocessing.Process(target=minimum, args=(data, result)),
            multiprocessing.Process(target=lulus, args=(data, result)),
            multiprocessing.Process(target=tidak_lulus, args=(data, result)),
        ]

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        # Update UI
        lbl_avg.config(text=f"{result['avg']:.2f}")
        lbl_max.config(text=f"{result['max']}")
        lbl_min.config(text=f"{result['min']}")
        lbl_lulus.config(text=f"{result['lulus']}")
        lbl_tidak.config(text=f"{result['tidak']}")

    except:
        messagebox.showerror("Error", "Format salah! Contoh: 75,80,90")

# ================= UI =================
root = tk.Tk()
root.title("Dashboard Nilai Mahasiswa")
root.geometry("520x420")
root.configure(bg="#1e1e2f")

# Header
tk.Label(root, text="🎓 Dashboard Analisis Nilai",
         bg="#1e1e2f", fg="white",
         font=("Segoe UI", 16, "bold")).pack(pady=15)

# Input Box
frame_input = tk.Frame(root, bg="#2b2b3c")
frame_input.pack(padx=20, pady=10, fill="x")

tk.Label(frame_input, text="Masukkan Nilai:",
         bg="#2b2b3c", fg="white").pack(anchor="w", padx=10, pady=5)

entry = tk.Entry(frame_input, font=("Segoe UI", 10))
entry.pack(padx=10, pady=5, fill="x")

# Button
tk.Button(root, text="🚀 Proses Analisis",
          command=proses_data,
          bg="#2196F3", fg="white",
          font=("Segoe UI", 10, "bold"),
          relief="flat", padx=10, pady=5).pack(pady=10)

# Output Cards
frame_output = tk.Frame(root, bg="#2b2b3c")
frame_output.pack(padx=20, pady=10, fill="both", expand=True)

def card(parent, title):
    f = tk.Frame(parent, bg="#3a3a4f", padx=10, pady=10)
    f.pack(fill="x", pady=5)

    tk.Label(f, text=title, bg="#3a3a4f", fg="#bbbbbb").pack(anchor="w")

    val = tk.Label(f, text="-",
                   bg="#3a3a4f", fg="white",
                   font=("Segoe UI", 12, "bold"))
    val.pack(anchor="w")
    return val

lbl_avg = card(frame_output, "Rata-rata")
lbl_max = card(frame_output, "Nilai Tertinggi")
lbl_min = card(frame_output, "Nilai Terendah")
lbl_lulus = card(frame_output, "Jumlah Lulus (≥75)")
lbl_tidak = card(frame_output, "Tidak Lulus (<75)")

# Run
if __name__ == "__main__":
    root.mainloop()