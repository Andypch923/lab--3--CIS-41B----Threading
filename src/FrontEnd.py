from tkinter.constants import CENTER, LEFT, TOP
import tkinter as tk
from tkinter import Canvas, Text
import os

root = tk.Tk()
root.title('Fossil CO2 Emissions 2017')
root.geometry("700x700")
apps = []

canvas = tk.Canvas(root, height = 700, width = 700, bg ="#263D42")
canvas.pack()

frame = tk.Frame(root, bg = "white")
canvas2 = tk.Canvas(frame, height =150, width = 500)
canvas2.create_text(250,50, text="THE NOAA ANNUAL GREENHOUSE GAS INDEX (AGGI)", fill ="black", font = ('Helvetica 18 bold'))
canvas2.create_text(250,100, text="""\n\nClick on a button to display the linear regression for each CO2-equivalent 
mixing ratio.""", fill ="black", font = ('Helvetica 10 italic'))
canvas2.pack(side=TOP,padx=10,pady=10)

pieChart = tk.Button(frame, text = "Pie Chart", padx =205, pady=10, fg="white",bg="#263D42")
pieChart.pack(side=TOP, pady=120)

frame.place(relwidth=0.8, relheight =0.8,relx = 0.1, rely=0.1)

root.mainloop()

