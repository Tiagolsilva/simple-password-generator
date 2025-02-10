import tkinter as tk
from generate_password import generate_password

root = tk.Tk()
root.title('Password Generator')
root.geometry('400x200')
root.resizable(False, False)
root.config(bg='black')

label = tk.Label(root, text='Enter the size of the password:', fg='white', bg='black')
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)


def generate():
    try:
        size_password = int(entry.get())
        if size_password <= 0:
            label_result['text'] = 'The size of the password must be greater than 0'
        else:
            password = generate_password(size_password)
            label_result['text'] = f'Generated password: {password}'
    except ValueError:
        label_result['text'] = 'Please enter a valid number'

button = tk.Button(root, text='Generate', command=generate)
button.pack(pady=10)

label_result = tk.Label(root, text='', bg='black', fg='white')
label_result.pack(pady=10)

root.mainloop()