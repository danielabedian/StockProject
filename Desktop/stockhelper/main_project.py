#!/usr/bin/python3
# feedback_template.py by Barron Stone
# This is an exercise file from Python GUI Development with Tkinter on lynda.com

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from  stockfunctions import user_inputs, get_information, filter_data, give_info

class Feedback:

    def __init__(self, master):    

        master.title('StockHelper')
        self.logo = PhotoImage(file ='tour_logo.gif')
        ttk.Label(master, image = self.logo).place(relx = 0, rely = 0, relwidth = 0.2, relheight = 0.2)
        ttk.Label(master, text = "StockHelper", font = ('Courier', 36, 'bold')).place(relx = 0.5, rely = 0.1, anchor = 'center')
        ttk.Label(master, text = "Find out which month is best to invest!", font = ('Courier', 16, 'bold')).place(relx = 0.5, rely = 0.2, anchor = 'center')
        
        ttk.Label(master, text = "Stock Ticket: ", font = ('Courier', 12, 'bold')).place(relx = 0.2, rely = 0.3)
        ttk.Label(master, text = "Start Month (2 digits): ", font = ('Courier', 12, 'bold')).place(relx = 0.2, rely = 0.35)
        ttk.Label(master, text = "Start Year (4 digits): ", font = ('Courier', 12, 'bold')).place(relx = 0.2, rely = 0.4)
        ttk.Label(master, text = "Time Length (years): ", font = ('Courier', 12, 'bold')).place(relx = 0.2, rely = 0.45)
        ttk.Label(master, text = "Percent Requirement: ", font = ('Courier', 12, 'bold')).place(relx = 0.2, rely = 0.5)
        ttk.Label(master, text = "Above: ", font = ('Courier', 12, 'bold')).place(relx = 0.2, rely = 0.55)
        ttk.Label(master, text = "Below: ", font = ('Courier', 12, 'bold')).place(relx = 0.2, rely = 0.6)
        
        self.month = StringVar()
        self.above_below = StringVar()
        self.year = StringVar()
        self.length = IntVar()
        
        self.entry_stock = ttk.Entry(master, width = 10)
        self.entry_stock.place(relx = 0.6, rely = 0.3)
        self.entry_month = ttk.Spinbox(master, from_ = 1, to = 12, textvariable = self.month)
        self.entry_month.place(relx = 0.6, rely = 0.35)
        self.entry_year = ttk.Spinbox(master, from_ = 1990, to = 2019, textvariable = self.year)
        self.entry_year.place(relx = 0.6, rely = 0.4)
        self.entry_length = ttk.Combobox(master, textvariable = self.length, values = [5, 10, 15, 20])
        self.entry_length.place(relx = 0.6, rely = 0.45)
        self.entry_percent = ttk.Entry(master, width = 10)
        self.entry_percent.place(relx = 0.6, rely = 0.5)
        self.radio_above = ttk.Radiobutton(master, variable = self.above_below, value = 'A')
        self.radio_above.place(relx = 0.6, rely = 0.55)
        self.radio_below = ttk.Radiobutton(master, variable = self.above_below, value = 'B')
        self.radio_below.place(relx = 0.6, rely = 0.6)

        
        ttk.Button(master, text = 'Submit', command = self.submit).place(relx = 0.3, rely = 0.7, anchor = 'center')
        ttk.Button(master, text = 'Clear', command = self.clear).place(relx = 0.6, rely = 0.7, anchor = 'center')
    def submit(self):
        print(self.entry_stock.get(), self.month.get(), self.year.get(), self.length.get(), self.entry_percent.get(), self.above_below.get())
        timestamp_input, start_timestamp = user_inputs(self.entry_stock.get(), self.month.get(), self.year.get(), self.length.get(), self.entry_percent.get(), self.above_below.get())
        get_information(self.entry_stock.get(), start_timestamp, timestamp_input)
        filter_data(self.entry_stock.get(), self.above_below.get(),  self.entry_percent.get())
        give_info( self.entry_stock.get(), self.year.get(), self.entry_percent.get(), self.above_below.get())
        self.clear()
        messagebox.showinfo(title = "Success", message = "go to the data/monthly folder")

    def clear(self):
        self.entry_stock.delete(0, END)
        self.entry_month.set('')
        self.entry_year.set('')
        self.entry_length.delete(0, END)
        self.entry_percent.delete(0, END)
    
            
def main():       
    root = Tk()
    root.geometry('640x480+50+100')
    root.resizable(False, False)
    feedback = Feedback(root)
    root.mainloop()
    
    
if __name__ == "__main__": main()

