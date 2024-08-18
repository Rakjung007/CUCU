import  tkinter as tk

def show_output():
    number = int(number_input.get())

    if number == 0:
        output_label.configure(text='ใส่ทำควยไร 0 มึงโง่หรือป่าว')
        return

    output = ''
    for i in range(1, 13):
        output += str(number) + ' x ' + str(i)
        output += ' = ' + str(number * i) + '\n'

        output_label.configure(text=output)

window = tk.Tk()
window.title('กูทำเอง')
window.minsize(width=400, height=400)

title_lable = tk.Label(master=window, text='แม่สูตรคูณ')
title_lable.pack(pady=20)

number_input = tk.Entry(master=window, width=20)
number_input.pack(pady=20)

go_button = tk.Button(
    master=window, text='ได้แก่',
    command=show_output, width=15, height=1
)
go_button.pack()

output_label = tk.Label(master=window)
output_label.pack()

window.mainloop()