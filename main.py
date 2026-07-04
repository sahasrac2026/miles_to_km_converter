from tkinter import *
window = Tk()
window.title("Mile to KM converter")

def miles_to_km():
    miles = miles_input.get()
    km = float(miles) * 1.60934
    km_output["text"] = str(round(km, 2))


miles_input = Entry()
miles_input.grid(row=0, column=1)

miles = Label(text="     Miles")
miles.grid(row=0, column=2)

is_equal_to = Label(text="is equal to")
is_equal_to.grid(row=2, column=0)

km_output = Label(text="0")
km_output.grid(row=2, column=1)

km_text = Label(text="kilometer")
km_text.grid(row=2, column=2)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(row=3, column=1)


window.mainloop()
