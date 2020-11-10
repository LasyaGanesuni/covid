from tkinter import *

root = Tk()
root.geometry("500x250")
root.title("Get Covid-19 Data Country Wise")


# function which will get covid data and will show it
def showdata():
    
    from matplotlib import pyplot as plt
    
    from covid import Covid
    
    import numpy as np

    covid = Covid()
    
    cases = []
    confirmed = []
    active = []
    deaths = []
    recovered = []
    
    try:
        
        countries = data.get()
        country_names = countries.strip()
        country_names = country_names.replace(" ", ",") 
        country_names = country_names.split(",")
        
        for x in country_names:
            cases.append(covid.get_status_by_country_name(x))
        
        for y in cases:
            
            confirmed.append(y["confirmed"])
            
            active.append(y["active"])
            
            deaths.append(y["deaths"])
            
            recovered.append(y["recovered"])

        r=list(np.add(deaths,active))
        c=list(np.add(r,recovered))
        
        plt.bar(country_names, deaths, color='black', label='Deaths')
        plt.bar(country_names, active, color='blue', bottom=deaths, label='Active')
        plt.bar(country_names, recovered, color='green',bottom=r, label='Recovered')
        plt.bar(country_names, confirmed, color='red', bottom=c, label='Confirmed')

        plt.legend()
        
        plt.title('Current Covid Cases')
        plt.xlabel('Country Name')
        plt.ylabel('Cases(in millions)')
        
        plt.show()

    except Exception as e:
        
        data.set("Enter correct details again (or) Check your internet connection")


Label(root, text="COVID-19 Tracker", font=("Times", "30", "bold italic"),bg='black',fg='white').pack(fill=X)
Label(root, text="Enter country names:",font=('ariel' ,15,'bold')).pack(pady=20)
data = StringVar()
data.set("Seperate country names using comma or space(not both)")
entry = Entry(root, textvariable=data, width=70,bd=5).pack()
Label(root).pack()
Button(root, text="Get Data",bg='green',fg='white',font=('ariel' ,10,'bold'), command=showdata).pack()
root.mainloop()

        