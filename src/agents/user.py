from uagents import Agent, Context
from src.messages.currancy import *
import sys
import tkinter as tk
from tkinter import *
from tkinter import ttk
# from plyer import notification
from functools import partial


user = Agent(name='user', seed='converter ')
dragonAddess = "agent1qg5ke2duhdv0d7nw9nj6p3f2c34p9f3mler3yw49ydkufzh3r8wrs0r2zks"

def SETUP(ctx:Context):
    #Initializing the GUI window
    tkWindow1 = tk.Tk()  
    tkWindow1.geometry('800x300')  
    tkWindow1.title('Currancy Bot')
    # Label
    choices=[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTC",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",  
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GGP",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "IMP",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JEP",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SLE",
        "SLL",
        "SOS",
        "SSP",
        "SRD",
        "STD",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XCD",
        "XDR",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW",
        "ZWL"
    ]
    base_curr_label = tk.Label(tkWindow1, text="Enter Base Currency:")
    base_curr_entry= ttk.Combobox(tkWindow1,values=choices)
    base_curr_value=(base_curr_entry.get()).upper()
    #Base currency is the currency unit against which you will be comparing

    #Conditions are used to check if the exchange rate of any other currency defined by the user crosses a user-defined threshold
    ncond_intvar=tk.IntVar()
    ncond_label=tk.Label(tkWindow1, text="Enter Number of Conditions:")
    ncond_entry=tk.Entry(tkWindow1,textvariable=ncond_intvar)
    ncond_value=int(ncond_entry.get())


    #Define callable function with printDetails function and usernameEntry argument

    setup_stage2Callable = partial(setup_stage2,tkWindow1,base_curr_entry,ncond_entry,ctx)
    # Submit button
    submitButton = tk.Button(tkWindow1, text="Enter", command=setup_stage2Callable)

    # Place label, entry, and button in grid
    base_curr_label.pack(anchor=tk.W,padx=10)
    base_curr_entry.pack(anchor=tk.W,padx=10) 
    ncond_label.pack(anchor=tk.W,padx=10)
    ncond_entry.pack(anchor=tk.W,padx=10) 
    submitButton.pack(anchor=tk.W,padx=10) 

    # Main loop
    tkWindow1.mainloop()



    
def setup_stage2(win1,base_curr,ncond,ctx:Context) :
    base_curr_text= (base_curr.get()).upper()
    #print("user entered :", base_curr_text)
    ncond_int=int(ncond.get())
    #print(ncond_int, type(ncond_int))
    conditions_type = []
    conditions_curr=[]
    conditions_thres=[]
    tkWindow2 = tk.Tk() 
    tkWindow2.geometry('800x300')  
    tkWindow2.title('Currancy Bot')
    main_frame=Frame(tkWindow2)
    main_frame.pack(fill=BOTH,expand=1)

    canvas=Canvas(main_frame)
    canvas.pack(side=LEFT,fill=BOTH,expand=1)
    scroll_bar=ttk.Scrollbar(main_frame, orient=VERTICAL, command=canvas.yview)
    scroll_bar.pack(side=RIGHT,fill=Y)

    canvas.configure(yscrollcommand=scroll_bar.set)
    canvas.bind('<Configure>',lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

    sec_frame=Frame(canvas)
    canvas.create_window((0,0),window=sec_frame,anchor="nw")
    for i in range(ncond_int):  
        
        lab1=tk.Label(sec_frame,text='Enter type of condition Upper[u] or Lower[l]:')
        lab1.pack(anchor=tk.W,padx=10)
        choices = [
        "u",
        "l",
        
        ] #etc
        en1 = ttk.Combobox(sec_frame,values=choices)
        en1.pack(anchor=tk.W,padx=10)
        #lab1.grid(row=(3*i)+1, column=0)
        #en1.grid(row=(3*i)+1, column=1)
        choices2=[
        "AED",
        "AFN",
        "ALL",
        "AMD",
        "ANG",
        "AOA",
        "ARS",
        "AUD",
        "AWG",
        "AZN",
        "BAM",
        "BBD",
        "BDT",
        "BGN",
        "BHD",
        "BIF",
        "BMD",
        "BND",
        "BOB",
        "BRL",
        "BSD",
        "BTC",
        "BTN",
        "BWP",
        "BYN",
        "BYR",
        "BZD",
        "CAD",
        "CDF",
        "CHF",
        "CLF",
        "CLP",
        "CNY",
        "COP",
        "CRC",
        "CUC",
        "CUP",
        "CVE",
        "CZK",
        "DJF",
        "DKK",
        "DOP",
        "DZD",
        "EGP",
        "ERN",
        "ETB",
        "EUR",  
        "FJD",
        "FKP",
        "GBP",
        "GEL",
        "GGP",
        "GHS",
        "GIP",
        "GMD",
        "GNF",
        "GTQ",
        "GYD",
        "HKD",
        "HNL",
        "HRK",
        "HTG",
        "HUF",
        "IDR",
        "ILS",
        "IMP",
        "INR",
        "IQD",
        "IRR",
        "ISK",
        "JEP",
        "JMD",
        "JOD",
        "JPY",
        "KES",
        "KGS",
        "KHR",
        "KMF",
        "KPW",
        "KRW",
        "KWD",
        "KYD",
        "KZT",
        "LAK",
        "LBP",
        "LKR",
        "LRD",
        "LSL",
        "LTL",
        "LVL",
        "LYD",
        "MAD",
        "MDL",
        "MGA",
        "MKD",
        "MMK",
        "MNT",
        "MOP",
        "MRO",
        "MUR",
        "MVR",
        "MWK",
        "MXN",
        "MYR",
        "MZN",
        "NAD",
        "NGN",
        "NIO",
        "NOK",
        "NPR",
        "NZD",
        "OMR",
        "PAB",
        "PEN",
        "PGK",
        "PHP",
        "PKR",
        "PLN",
        "PYG",
        "QAR",
        "RON",
        "RSD",
        "RUB",
        "RWF",
        "SAR",
        "SBD",
        "SCR",
        "SDG",
        "SEK",
        "SGD",
        "SHP",
        "SLE",
        "SLL",
        "SOS",
        "SSP",
        "SRD",
        "STD",
        "SYP",
        "SZL",
        "THB",
        "TJS",
        "TMT",
        "TND",
        "TOP",
        "TRY",
        "TTD",
        "TWD",
        "TZS",
        "UAH",
        "UGX",
        "USD",
        "UYU",
        "UZS",
        "VEF",
        "VES",
        "VND",
        "VUV",
        "WST",
        "XAF",
        "XAG",
        "XAU",
        "XCD",
        "XDR",
        "XOF",
        "XPF",
        "YER",
        "ZAR",
        "ZMK",
        "ZMW", 
        "ZWL"
        ]
        lab2=tk.Label(sec_frame,text='Enter Currancy (eg: INR):')
        lab2.pack(anchor=tk.W,padx=10)
        en2=ttk.Combobox(sec_frame,values=choices2)
        en2.pack(anchor=tk.W,padx=10)
        #lab2.grid(row=(3*i)+2, column=0)
        #en2.grid(row=(3*i)+2, column=1)
        en3_str=tk.DoubleVar()
        lab3=tk.Label(sec_frame,text='Enter Threshold:')
        lab3.pack(anchor=tk.W,padx=10)
        en3=tk.Entry(sec_frame,textvariable=en3_str)
        en3.pack(anchor=tk.W,padx=10)
        #lab3.grid(row=(3*i)+3, column=0)
        #en3.grid(row=(3*i)+3, column=1)
        conditions_type.append(en1)
        conditions_curr.append(en2)
        conditions_thres.append(en3)
    setup_stage3Callable=partial(setup_stage3,win1,tkWindow2,base_curr,ncond,conditions_type,conditions_curr,conditions_thres,ctx)
    submitButton = tk.Button(sec_frame, text="Enter", command=setup_stage3Callable)
    submitButton.pack(anchor=tk.W,padx=10)

    #submitButton = tk.Button(sec_frame, text="Enter", command=setup_stage3Callable)
    #submitButton.pack(anchor=tk.W,padx=10) 
    tkWindow2.mainloop()
    #win2close.destroy()
    return    



def setup_stage3(win1,win2,base_curr,ncond_en,conditions_type,conditions_curr,conditions_thres,ctx:Context):
    
    Base=(base_curr.get()).upper()
    numConditions = int(ncond_en.get())
    conditions = []
    for i in range(numConditions):
        condition = {
            'type': (conditions_type[i].get()).upper()[0],
            'currancy': (conditions_curr[i].get()).upper(),
            'Threshold': float(conditions_thres[i].get())
        }
        conditions.append(condition)
    
    ctx.storage.set('Conditions', conditions)
    ctx.storage.set('conditionsCount', numConditions)
    ctx.storage.set('Base', Base)
    destroy(win1,win2)

def destroy(win1,win2):
    win1.destroy()
    win2.destroy()

#This block basically calls the SETUP() functin once every three seconds
@user.on_interval(period=3.0, messages=ConvertRequest)
async def main(ctx: Context):
    setup = ctx.storage.get("setup") or 0
    if not setup:
        ctx.logger.info(f"Starting Setup....")
        SETUP(ctx)
        ctx.logger.info(f"Setup completed.")
        ctx.storage.set('setup', True)

    base = ctx.storage.get('Base')
    curs = [i['currancy'] for i in ctx.storage.get('Conditions')]
    await ctx.send(dragonAddess, ConvertRequest(base=base, curs=curs, address=user.address))

#This block provides alert to user if the exchange rate crosses the defined threshold/s
@user.on_message(ConvertResponse)
async def warn(ctx: Context, _sender: str, msg: ConvertResponse):
    base = ctx.storage.get('Base')
    for condition in ctx.storage.get('Conditions'):
        rate = msg.rates[condition['currancy']]
        if (condition['type'] == 'U' and rate > condition['Threshold']) or (condition['type'] == 'L' and rate < condition['Threshold']):
            mssg=f"{base} has crossed the threshold of {condition['Threshold']} {condition['currancy']}"
            ctx.logger.warning(mssg)

if __name__ == "__main__":
    user.run()
