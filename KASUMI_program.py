import sys
import os
import tkinter as tk
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__))))

from KASUMI import KASUMI_EncryptData, KASUMI_DecryptData

def encrypt():
  name_file_input = file_input.get("1.0", tk.END).strip()
  name_file_output = file_output.get("1.0", tk.END).strip()
  name_key_file = key_file.get("1.0", tk.END).strip()

  if not os.path.exists(name_file_input):
    result.delete("1.0", tk.END)
    result.insert(tk.END, "Error: Input file not found")
    return
  
  if not os.path.exists(name_key_file):
    result.delete("1.0", tk.END)
    result.insert(tk.END, "Error: Key file not found")
    return

  if not name_file_output:
    base, ext = os.path.splitext(name_file_input)
    name_file_output = f"{base}.kasumi"

  with open(name_file_input, "rb") as file:
            I = file.read()

  with open(name_key_file, "rb") as f:
      K = f.read()

  result_encrypt = KASUMI_EncryptData(I, K)

  if result_encrypt[0] == False:
    result.delete("1.0", tk.END)
    result.insert(tk.END, "Eror :" + result_encrypt[1])
    return

  with open(name_file_output, "wb") as file:
            file.write(result_encrypt[1])

  result.delete("1.0", tk.END)
  result.insert(tk.END, "Encryption successful. Written to: " + name_file_output)

def decrypt():
  name_file_input = file_input.get("1.0", tk.END).strip()
  name_file_output = file_output.get("1.0", tk.END).strip()
  name_key_file = key_file.get("1.0", tk.END).strip()

  if not os.path.exists(name_file_input):
    result.delete("1.0", tk.END)
    result.insert(tk.END, "Error: Input file not found")
    return
  
  if not os.path.exists(name_key_file):
    result.delete("1.0", tk.END)
    result.insert(tk.END, "Error: Key file not found")
    return

  if not name_file_output:
    base, ext = os.path.splitext(name_file_input)
    name_file_output = f"{base}.txt"

  with open(name_file_input, "rb") as file:
            I = file.read()

  with open(name_key_file, "rb") as file:
            K = file.read()

  result_decrypt = KASUMI_DecryptData(I, K)
  
  if result_decrypt[0] == False:
    result.delete("1.0", tk.END)
    result.insert(tk.END, "Eror: " + result_decrypt[1])
    return

  with open(name_file_output, "wb") as file:
            file.write(result_decrypt[1])

  result.delete("1.0", tk.END)
  result.insert(tk.END, "Decryption successful. Written to: " + name_file_output)

def clear():
  file_input.delete(1.0, tk.END)
  file_output.delete(1.0, tk.END)
  key_file.delete(1.0, tk.END)
  result.delete(1.0, tk.END)

#-----------------------------Головне вікно-----------------------------

master = tk.Tk()
master.title("KASUMI")

label1 = tk.Label(master, text="File input:")
label1.grid(row=0, column=0)

file_input = tk.Text(master, height=1, width=75)
file_input.grid(row=0, column=1)

label2 = tk.Label(master, text="File output:")
label2.grid(row=1, column=0)

file_output = tk.Text(master, height=1, width=75)
file_output.grid(row=1, column=1)

label2 = tk.Label(master, text="Key file:")
label2.grid(row=2, column=0)

key_file = tk.Text(master, height=1, width=75)
key_file.grid(row=2, column=1)

result_label = tk.Label(master, text="Result:")
result_label.grid(row=3, column=0)

result = tk.Text(master, height=1, width=75)
result.grid(row=3, column=1)

button_frame = tk.Frame(master)
button_frame.grid(row=4, column=0, columnspan=2, pady=10)

buttons = [
    ("Encrypt", encrypt),
    ("Decrypt", decrypt)
]

for i, (text, command) in enumerate(buttons):
    row, col = divmod(i, 2)
    btn = tk.Button(button_frame, text=text, command=command, width=20)
    btn.grid(row=row, column=col, padx=5, pady=5)

clear_button = tk.Button(master, text="Clear", command=clear, width=20, bg="red", fg="white")
clear_button.grid(row=5, column=0, columnspan=2, pady=10)

master.mainloop()
