import tkinter as tk

#custom functions
def calc():
    #clear canvas and percents
    canvas.delete("all")
    lblHousPerc.config(text="")
    lblFoodPerc.config(text="")
    lblUtilPerc.config(text="")
    lblTranPerc.config(text="")
    try:
        #get values from textboxes
        hous = float(txtHousing.get())
        food = float(txtFood.get())
        util = float(txtUtilities.get())
        tran = float(txtTransportation.get())
        total = hous+food+util+tran #calculate total cost
        if hous<0 or food<0 or util<0 or tran<0: #checks for negative numbers
            lblHousPerc.config(text="ERROR: Costs must be positive")
        elif round(hous, 2)==round(total, 2) or round(food, 2)==round(total, 2) or round(util, 2)==round(total, 2) or round(tran, 2)==round(total, 2): #checks for one input being too much larger than other inputs
            lblHousPerc.config(text="ERROR: One input is too much larger than the other inputs")
        else:
            #calculate percents of total cost
            housPerc = round(hous/total*100, 2)
            foodPerc = round(food/total*100, 2)
            utilPerc = round(util/total*100, 2)
            tranPerc = round(tran/total*100, 2)
            #write out percents
            lblHousPerc.config(text=str(housPerc)+"%")
            lblFoodPerc.config(text=str(foodPerc)+"%")
            lblUtilPerc.config(text=str(utilPerc)+"%")
            lblTranPerc.config(text=str(tranPerc)+"%")
            #draw pie chart
            canvas.create_arc((5, 5), (200, 200), start=0, extent=hous/total*360, style=tk.PIESLICE, width=2, fill="#fff947")
            canvas.create_arc((5, 5), (200, 200), start=hous/total*360, extent=food/total*360, style=tk.PIESLICE, width=2, fill="#3abf2e")
            canvas.create_arc((5, 5), (200, 200), start=(hous+food)/total*360, extent=util/total*360, style=tk.PIESLICE, width=2, fill="#8166e3")
            canvas.create_arc((5, 5), (200, 200), start=(hous+food+util)/total*360, extent=tran/total*360, style=tk.PIESLICE, width=2, fill="#c24e4e")
    except ValueError:
        lblHousPerc.config(text="ERROR: Enter a NUMBER in every textbox")
    except ZeroDivisionError:
        lblHousPerc.config(text="ERROR: The total cost must be positive")

#window properties
window = tk.Tk()
window.title("Graphing with Tkinter")
window.geometry("800x800")
window.configure(bg="#5ecfd1")
window.iconbitmap("PieChart.ico")

#create labels
lblHousing = tk.Label(window, text="Price of Housing: ($)", bg="#5ecfd1")
lblFood = tk.Label(window, text="Price of Food: ($)", bg="#5ecfd1")
lblUtilities = tk.Label(window, text="Price of Utilities: ($)", bg="#5ecfd1")
lblTransportation = tk.Label(window, text="Price of Transportation: ($)", bg="#5ecfd1")
lblHousPerc = tk.Label(window, text="", bg="#5ecfd1")
lblFoodPerc = tk.Label(window, text="", bg="#5ecfd1")
lblUtilPerc = tk.Label(window, text="", bg="#5ecfd1")
lblTranPerc = tk.Label(window, text="", bg="#5ecfd1")
lblTitle = tk.Label(window, text="Expenses Percentage Calculator", bg="#5ecfd1", font=("times new roman", 15))
#instructions for user
lblInstruction1 = tk.Label(window, text="1) Input the values for the quadratic in the textboxes", bg="#5ecfd1", font=("times_new_roman", 10))
lblInstruction2 = tk.Label(window, text="2) Click the calculate button", bg="#5ecfd1", font=("times_new_roman", 10))
lblInstruction3 = tk.Label(window, text="3) Read the answer, correct any errors if necessary", bg="#5ecfd1", font=("times_new_roman", 10))

#create textboxes
txtHousing = tk.Entry(window, bg="#fff947")
txtFood = tk.Entry(window, bg="#3abf2e")
txtUtilities = tk.Entry(window, bg="#8166e3")
txtTransportation = tk.Entry(window, bg="#c24e4e")


#buttons
btn = tk.Button(window, text="Calculate!", command=calc, bg="#5ecfd1", activebackground="#2cc4c7")

#canvases
canvas = tk.Canvas(window, width=205, height=205, highlightthickness=0, bg="#5ecfd1")

#add GUI items to the grid
lblTitle.grid(row=0, column=0)
lblHousing.grid(row=1, column=0)
lblFood.grid(row=2, column=0)
lblUtilities.grid(row=3, column=0)
lblTransportation.grid(row=4, column=0)
txtHousing.grid(row=1, column=1)
txtFood.grid(row=2, column=1)
txtUtilities.grid(row=3, column=1)
txtTransportation.grid(row=4, column=1)
lblHousPerc.grid(row=1, column=2)
lblFoodPerc.grid(row=2, column=2)
lblUtilPerc.grid(row=3, column=2)
lblTranPerc.grid(row=4, column=2)
btn.grid(row=5, column=1, padx=10)
canvas.grid(row=9, column=0)
lblInstruction1.grid(row=6, column=0)
lblInstruction2.grid(row=7, column=0)
lblInstruction3.grid(row=8, column=0)

#build the window
window.mainloop()