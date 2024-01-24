import tkinter as tk

#custom functions
def draw():
    #clear canvas and percents
    canvas.delete("all")
    lblHousPerc.config(text="")
    lblFoodPerc.config(text="")
    lblUtilPerc.config(text="")
    lblTranPerc.config(text="")
    try:
        hous = float(txtHousing.get())
        food = float(txtFood.get())
        util = float(txtUtilities.get())
        tran = float(txtTransportation.get())
        total = hous+food+util+tran #calculate total cost
        #calculate percents of total cost
        housPerc = round(hous/total*100)
        foodPerc = round(food/total*100)
        utilPerc = round(util/total*100)
        tranPerc = round(tran/total*100)
        #write out percents
        lblHousPerc.config(text=str(housPerc)+"%")
        lblFoodPerc.config(text=str(foodPerc)+"%")
        lblUtilPerc.config(text=str(utilPerc)+"%")
        lblTranPerc.config(text=str(tranPerc)+"%")
        #draw pie chart
        canvas.create_arc((10, 10), (200, 200), start=0, extent=round(hous/total*360), style=tk.PIESLICE, width=2, fill="red")
        canvas.create_arc((10, 10), (200, 200), start=round(hous/total*360), extent=round(food/total*360), style=tk.PIESLICE, width=2, fill="green")
        canvas.create_arc((10, 10), (200, 200), start=round(food/total*360), extent=round(util/total*360), style=tk.PIESLICE, width=2, fill="blue")
        canvas.create_arc((10, 10), (200, 200), start=round(util/total*360), extent=0, style=tk.PIESLICE, width=2, fill="yellow")
    except ValueError:
        lblHousPerc.config(text="ERROR: Enter a NUMBER in each texbox")
    except ZeroDivisionError:
        lblHousPerc.config(text="ERROR: Numbers must be positive")

#window properties
window = tk.Tk()
window.title("Graphing with Tkinter")
window.geometry("800x800")


#create labels
lblHousing = tk.Label(window, text="Price of Housing: ")
lblFood = tk.Label(window, text="Price of Food: ")
lblUtilities = tk.Label(window, text="Price of Utilities: ")
lblTransportation = tk.Label(window, text="Price of Transportation: ")
lblHousPerc = tk.Label(window, text="")
lblFoodPerc = tk.Label(window, text="")
lblUtilPerc = tk.Label(window, text="")
lblTranPerc = tk.Label(window, text="")

#create textboxes
txtHousing = tk.Entry(window)
txtFood = tk.Entry(window)
txtUtilities = tk.Entry(window)
txtTransportation = tk.Entry(window)


#buttons
btn = tk.Button(window, text="Draw!", command=draw)

#canvases
canvas = tk.Canvas(window)

#add GUI items to the grid
lblHousing.grid(row=0, column=0)
lblFood.grid(row=1, column=0)
lblUtilities.grid(row=2, column=0)
lblTransportation.grid(row=3, column=0)
txtHousing.grid(row=0, column=1)
txtFood.grid(row=1, column=1)
txtUtilities.grid(row=2, column=1)
txtTransportation.grid(row=3, column=1)
lblHousPerc.grid(row=0, column=2)
lblFoodPerc.grid(row=1, column=2)
lblUtilPerc.grid(row=2, column=2)
lblTranPerc.grid(row=3, column=2)
btn.grid(row=4, column=1, padx=10)
canvas.grid(row=5, column=0)

#build the window
window.mainloop()