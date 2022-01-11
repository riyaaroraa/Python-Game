########################################################################################################################################

# Series of different sub modules that are available in tkinter. 
# Not import them all at once so we imported them all separately

import tkinter as tk #importing the basics of the tkinter module
import random
from tkinter import Entry #importing module in order to create entry boxes
from tkinter import ttk
from tkinter import Radiobutton #importing module to create multiple choice button
from tkinter import Listbox #importing module to create a option list
from tkinter import EXTENDED
from tkinter import END
from tkinter import PhotoImage

infolist = [] #creating list to store all of the users vitals, such as age, weight, height 

r = tk.Tk() #this indicates that everytime we create a new variable in tkinter, we need
#the letter r before it, so that tkinter can understand this module
class main:

    #this definition is creating the window for the app. The window will allow for further writing to be displayed on the screen
    def __init__(self,master):
        r.geometry('1280x720') #creating the size of the window 
        r.frame=tk.Frame(r,height=1280, width=720)
        r.frame.pack()
        r.title('MyHealth') #this creates a title that outputs whatever is in the brackets
        frame = tk.Frame(r) 
        frame.pack(fill='both', expand='yes')
        r.resizable(0,0)
        self.start()
        


        
        
    def start(self):
    
        r.titletext = tk.Label(r.frame,text="MyHealth",font=("Malgun Gothic Semilight",100))
        r.titletext.pack() #in order for any GUI to appear on the screen, you need to pack it. This command will allow the the GUI to appear on the screen.
        r.titletext.place(x=120, y=100)

        r.startbutton = tk.Button(r.frame,text="Get Started",font=("Malgun Gothic Semilight",30), bg="lightgreen",command=self.name)
        r.startbutton.pack()
        r.startbutton.place(x=250, y=400) #.place indicates the x and y cordinate of any GUI. With this command you can have any GUI anywhere on the window

        

    def name(self):

        r.titletext.destroy() #the .destroy() command destroys whatever variable it was told to do so. When the variable is destroyed it is uncallable after this point
        r.startbutton.destroy()
        
        r.introtext = tk.Label(r.frame,text="Welcome to MyHealth, to get started, enter your first and last name:",font=("Malgun Gothic Semilight",20))
        r.introtext.pack(side=tk.TOP, pady=250)

        r.fnamelabel = tk.Label(r.frame,text="First Name:",font=("Malgun Gothic Semilight",20))#.Label command creates a label or heading on the screen.
        #just like a print statement, whatever that is in quotations, is what is being outputed on the screen
        r.fnamelabel.pack()
        r.fnamelabel.place (x=250, y=330)




        r.lnamelabel = tk.Label(r.frame,text="Last Name:",font=("Malgun Gothic Semilight",20)) #throughout our whole code we also set our font to
        #Malgun Gothic Semilight. You can change this to anything as long as it is compatibile in python
        r.lnamelabel.pack()
        r.lnamelabel.place (x=250, y=380)

        #the two blocks below are indicating that an entry box is being displayed for user input. This entry box is used so that the
        #user can enter in their full name 
        r.fname = Entry(r) 
        r.fname.pack()
        r.fname.place (x=650, y=345)

        r.lname = Entry(r)
        r.lname.pack()
        r.lname.place (x=650, y=395)

        #as we can see now it is tk.Button which means it is a button. command.self is an important command within tkinter as this is
        #the feature that allows for the window to be changed once a button has been pressed. The last part that says .age is another
        #definition withing our code so that once you click on the button it will redirect you to that new definition.
        r.nextagebutton = tk.Button(r.frame, text="Next ->", font=("Malgun Gothic Semilight",30), bg="lightgreen",command=self.age)
        r.nextagebutton.pack()
        r.nextagebutton.place(x=630, y=440)

        
            



    def age (self): #this definition will allow the user to enter their age 


        #in order for user input in tkinter to be recallable you need to initializes the entry box variable to a new variable so that the
        #computer understands that this is what you want to input
        global fName 
        global lName
        fName = r.fname.get() #this .get() command will get the entry box variable and set it to the new variable
        lName = r.lname.get()
        print(fName, lName)
        
        infolist.append(fName) #adding the users first and last name to the vitals list so that this information can be stored
        infolist.append(lName)
        print(infolist)
        
        r.introtext.destroy() #we destroy labels and buttons that have been created on a previous windown so that it does not appear on the next window
        r.fnamelabel.destroy()
        r.lnamelabel.destroy()
        r.fname.destroy()
        r.lname.destroy()
        r.nextagebutton.destroy()       

        #this block of code gives greetings to this user, using there first and last name that they entered in the entry box
        r.hello = tk.Label(r.frame,text= "Hello, " + fName + " " + lName,font=("Malgun Gothic Semilight",20))
        r.hello.pack()
        r.hello.place(x=300, y=50)




        #this block of code is creating a small slider for the user to enter their age
        r.agetext = tk.Label(r.frame,text="Please enter your age:",font=("Malgun Gothic Semilight",20))
        r.agetext.pack()
        
        agevar = tk.IntVar()
        agevar.set(0) #this sets the orginal age of the user to 0, however it will be changed


        #this two line code will create a scale. The .scale allows for a slider and the scale can be set to whatever you want
        r.agescale=tk.Scale(r.frame,orient='horizontal',length=1000,width=50,sliderlength=30, from_=0,to=130, variable = agevar) 
        r.agescale.pack()

        #this creates a next button, the user will press this once they have answered all of the questions that are asked of
        r.nextheightbutton = tk.Button(r.frame, text="Next ->", font=("Malgun Gothic Semilight",30), bg="lightgreen",command=self.height)
        r.nextheightbutton.pack(side=tk.BOTTOM,pady=220,padx=125)
        
        r.age=tk.Label(r.frame,textvariable = agevar,font=("Malgun Gothic Semilight",30))
        r.age.pack()

 
    def height(self): #this definition will allow the user to enter their height 

        global Age #in order for the users age to be recallable it has to be assessed as a global variable
        Age = r.agescale.get()
        print(Age)

        infolist.append(Age) #adding the users age to the list of vitals 
        print (infolist)

        #below are a set of variable that will be destroyed because the code is shifting to a new definition 
        r.hello.destroy()
        r.agetext.destroy()
        r.agescale.destroy()
        r.age.destroy()
        r.nextheightbutton.destroy()

        #this small block of code is the same as the age however now it is asking for the users height
        r.heightentry=tk.Label(r.frame,text="Enter your height(cm)",font=("Malgun Gothic Semilight",30))
        r.heightentry.pack()

        heightvar = tk.IntVar()
        heightvar.set(0)

        #resolution 0.1 allows the number to have one digit after the decimal
        r.heightscale=tk.Scale(r.frame,orient='horizontal',length=1000,width=50,sliderlength=30, from_=0,to=300, variable = heightvar, resolution=0.1)
        r.heightscale.pack()

        r.nextweightbutton = tk.Button(r.frame, text="Next ->", font=("Malgun Gothic Semilight",30), bg="lightgreen",command=self.weight)
        r.nextweightbutton.pack(side=tk.BOTTOM,pady=220,padx=125)
        
        r.height=tk.Label(r.frame,textvariable = heightvar,font=("Malgun Gothic Semilight",30))
        r.height.pack()
        


    def weight(self): #this definition allows the user to enter their weight

        #this definition has the same code as the age and weight, but now is asking for something different 
        global Height
        Height = r.heightscale.get()
        print(Height)

        infolist.append(Height)
        print (infolist)
        
        r.heightentry.destroy()
        r.heightscale.destroy()
        r.nextweightbutton.destroy()
        r.height.destroy()

        r.weightentry=tk.Label(r.frame,text="Enter your weight(kg)",font=("Malgun Gothic Semilight",30))
        r.weightentry.pack()

        weightvar = tk.IntVar()
        weightvar.set(0)
        
        r.weightscale=tk.Scale(r.frame,orient='horizontal',length=1000,width=50,sliderlength=30, from_=0,to=450, variable = weightvar, resolution=0.1)
        r.weightscale.pack()

        r.nextmainmenubutton = tk.Button(r.frame, text="Next ->", font=("Malgun Gothic Semilight",30), bg="lightgreen",command=self.mainmenu)
        r.nextmainmenubutton.pack(side=tk.BOTTOM,pady=220,padx=125)
        
        r.weight=tk.Label(r.frame,textvariable = weightvar,font=("Malgun Gothic Semilight",30))
        r.weight.pack()

    def mainmenu(self): #this definition is the main menu of the app. In this definition you will be able to access your info,
        #tips to help better your diet, and ideas for potential meals.

        global Weight
        Weight = r.weightscale.get()
        print(Weight)

        infolist.append(Weight)
        print (infolist)

        r.weightentry.destroy()
        r.weightscale.destroy()
        r.nextmainmenubutton.destroy()
        r.weight.destroy()

        #this button is created for the user if they want to see their info 
        r.myinfobutton = tk.Button(r.frame, text="My Info", font=("Malgun Gothic Semilight",30), bg="lightblue", command=self.info)
        r.myinfobutton.pack()
        r.myinfobutton.place(x=410, y=100)

        #this button is created for the user if they want to see their tips
        r.mytipsbutton = tk.Button(r.frame, text="My Tips", font=("Malgun Gothic Semilight",30), bg="magenta", command=self.tips)
        r.mytipsbutton.pack()
        r.mytipsbutton.place(x=410, y=200)

        #this button is created for the user if they want to see meal plans
        r.mymealsbutton = tk.Button(r.frame, text="My Meals", font=("Malgun Gothic Semilight",30), bg="red", command=self.meals)
        r.mymealsbutton.pack()
        r.mymealsbutton.place(x=395, y=300)



    def info(self): #this defintion will allow the user to change any of their vital information that they entered previously
        
        global i
        i = tk.Tk()
        i.geometry('1280x720')
        i.frame=tk.Frame(i,height=1280, width=720)
        i.frame.pack()
        i.title('MyInfo')
        frame = tk.Frame(i)
        frame.pack(fill='both', expand='yes')
        i.resizable(0,0)
        i.configure(background='lightblue')

        i.infoinstructtext = tk.Label(i.frame,text="Close the window and come back, to see new changes",font=("Malgun Gothic Semilight",20))
        #.frame indicates which window this label will appear on
        i.infoinstructtext.pack()
        i.infoinstructtext.place(x=65, y=10)

        #this block of code below, allows the user to change their first name if desired. It will ouput your original name that you inputed before
        #then there will be an entry box, if you want to change it.
        i.whatfname = tk.Label(i.frame,text="First Name: " + fName, font=("Malgun Gothic Semilight",10))
        i.whatfname.pack()
        i.whatfname.place (x=100, y=100)

        i.fname = Entry(i)
        i.fname.pack()
        i.fname.place (x=700, y=100)

        i.editfnamebutton = tk.Button(i, text="Change", bg="lightgreen", command=self.newfname) #this button will let this original name to be changed
        #to the new name that you inputed.
        i.editfnamebutton.pack()
        i.editfnamebutton.place (x=850, y=100)

               
        #this code is the same as above however this time you are able to change your last name 
        i.whatlname = tk.Label(i.frame,text="Last Name: " + lName,font=("Malgun Gothic Semilight",10))
        i.whatlname.pack()
        i.whatlname.place (x=100, y=150)

        i.lname = Entry(i)
        i.lname.pack()
        i.lname.place (x=700, y=150)

        i.editlnamebutton = tk.Button(i, text="Change", bg="lightgreen", command=self.newlname) 
        i.editlnamebutton.pack()
        i.editlnamebutton.place (x=850, y=150)

        i.whatage = tk.Label(i.frame,text="Age: " + str(Age), font=("Malgun Gothic Semilight",10))
        i.whatage.pack()
        i.whatage.place (x=100, y=200)

        agevar = tk.IntVar()
        agevar.set(0)
        
        #this block of code allows the user to change their age if they want to
        global agescale
        i.agescale=tk.Scale(i.frame,orient='horizontal',length=200,width=10,sliderlength=10, from_=0,to=130, variable=agevar)
        i.agescale.pack()
        i.agescale.place(x=350, y=190)

        i.editagebutton = tk.Button(i, text="Change", bg="lightgreen", command=self.newage) #once change has been clicked, whatver you set
        #on the slider is your new age
        
        i.editagebutton.pack()
        i.editagebutton.place (x=850, y=200)

        i.whatheight = tk.Label(i.frame,text="Height(cm): " + str(Height), font=("Malgun Gothic Semilight",10))
        i.whatheight.pack()
        i.whatheight.place (x=100, y=250)

        heightvar = tk.IntVar()
        heightvar.set(0)
        
        #this block of code is the same as the block above however this time you have the option to change your height 
        global heightscale
        i.heightscale=tk.Scale(i.frame,orient='horizontal',length=200,width=10,sliderlength=10, from_=0,to=300, resolution=0.1, variable=heightvar)
        i.heightscale.pack()
        i.heightscale.place(x=350, y=240)

        i.editheightbutton = tk.Button(i, text="Change", bg="lightgreen", command=self.newheight)
        i.editheightbutton.pack()
        i.editheightbutton.place (x=850, y=250)

        i.whatweight = tk.Label(i.frame,text="Weight(kg): " + str(Weight), font=("Malgun Gothic Semilight",10))
        i.whatweight.pack()
        i.whatweight.place (x=100, y=300)

        weightvar = tk.IntVar()
        weightvar.set(0)
        
        
        #this block of code is the same as the block of code for the height scale and age scale however this time you have the
        #option to change your weight
        global weightscale
        i.weightscale=tk.Scale(i.frame,orient='horizontal',length=200,width=10,sliderlength=10, from_=0,to=450, resolution=0.1, variable=weightvar)
        i.weightscale.pack()
        i.weightscale.place(x=350, y=290)

        i.editweightbutton = tk.Button(i, text="Change", bg="lightgreen", command=self.newweight)
        i.editweightbutton.pack()
        i.editweightbutton.place (x=850, y=300)

        '''i.whatrestrict = tk.Label(i.frame,text="Any allergies/dietary restrictions?" ,font=("Malgun Gothic Semilight",10))
        i.whatrestrict.pack()
        i.whatrestrict.place (x=100, y=350)

        global Restriction1
        Restriction1 = ""
        infolist.append(Restriction1)
        
        i.restrictnum1 = tk.Label(i.frame,text="#1: " + Restriction1,font=("Malgun Gothic Semilight",10))
        i.restrictnum1.pack()
        i.restrictnum1.place (x=300, y=350)

        i.restrict1 = Entry(i)
        i.restrict1.pack()
        i.restrict1.place (x=700, y=350)

        i.addrestrict1button = tk.Button(i, text="Add", bg="lightgreen", command=self.restriction1)
        i.addrestrict1button.pack()
        i.addrestrict1button.place (x=850, y=350)

        global Restriction2
        Restriction2 = ""
        infolist.append(Restriction2)
        
        i.restrictnum2 = tk.Label(i.frame,text="#2: " +  Restriction2,font=("Malgun Gothic Semilight",10))
        i.restrictnum2.pack()
        i.restrictnum2.place (x=300, y=400)

        i.restrict2 = Entry(i)
        i.restrict2.pack()
        i.restrict2.place (x=700, y=400)

        i.addrestrict2button = tk.Button(i, text="Add", bg="lightgreen", command=self.restriction2)
        i.addrestrict2button.pack()
        i.addrestrict2button.place (x=850, y=400)

        global Restriction3
        Restriction3 = ""
        infolist.append(Restriction3)
        
        i.restrictnum3 = tk.Label(i.frame,text="#3: " + Restriction3,font=("Malgun Gothic Semilight",10))
        i.restrictnum3.pack()
        i.restrictnum3.place (x=300, y=450)

        i.restrict3 = Entry(i)
        i.restrict3.pack()
        i.restrict3.place (x=700, y=450)

        i.addrestrict3button = tk.Button(i, text="Add", bg="lightgreen", command=self.restriction3)
        i.addrestrict3button.pack()
        i.addrestrict3button.place (x=850, y=450)

        global Restriction4
        Restriction4 = ""
        infolist.append(Restriction4)
        
        i.restrictnum4 = tk.Label(i.frame,text="#4: " +  Restriction4,font=("Malgun Gothic Semilight",10))
        i.restrictnum4.pack()
        i.restrictnum4.place (x=300, y=500)

        i.restrict4 = Entry(i)
        i.restrict4.pack()
        i.restrict4.place (x=700, y=500)

        i.addrestrict4button = tk.Button(i, text="Add", bg="lightgreen", command=self.restriction4)
        i.addrestrict4button.pack()
        i.addrestrict4button.place (x=850, y=500)

        global Restriction5
        Restriction5 = ""
        infolist.append(Restriction5)
        
        i.restrictnum5 = tk.Label(i.frame,text="#5: " +  Restriction5,font=("Malgun Gothic Semilight",10))
        i.restrictnum5.pack()
        i.restrictnum5.place (x=300, y=550)

        i.restrict5 = Entry(i)
        i.restrict5.pack()
        i.restrict5.place (x=700, y=550)

        i.addrestrict5button = tk.Button(i, text="Add", bg="lightgreen", command=self.restriction5)
        i.addrestrict5button.pack()
        i.addrestrict5button.place (x=850, y=550)'''


#this block of code is fairly simple. If you have changed any of the vitals above, these definitions will remove the old
#vital from the vital list, and add the new vital 
    def newfname(self):
        
        global fName
        infolist.remove(fName)
        
        fName = i.fname.get()
        infolist.insert (0, fName)
        print (infolist)



    def newlname(self):
        
        global lName
        infolist.remove(lName)

        lName = i.lname.get()
        infolist.insert (1, lName)
        print (infolist)



    def newage(self):

        global Age
        del infolist[2]

        Age = i.agescale.get()
        infolist.insert (2, Age)
        print (infolist)



    def newheight(self):

        global Height
        del infolist[3]

        Height = i.heightscale.get()
        infolist.insert (3, Height)
        print (infolist)



    def newweight(self):

        global Weight
        del infolist[4]

        Weight = i.weightscale.get()
        infolist.insert (4, Weight)
        print (infolist)

    '''def restriction1(self):
        
        global Restriction1
        del infolist[5]

        Restriction1 = i.restrict1.get()
        infolist.insert (5, Restriction1)
        print (infolist)
        

    def restriction2(self):
        
        global Restriction2
        del infolist[6]

        Restriction2 = i.restrict2.get()
        infolist.insert (6, Restriction2)
        print (infolist)
        

    def restriction3(self):
        
        global Restriction3
        del infolist[7]

        Restriction3 = i.restrict3.get()
        infolist.insert (7, Restriction3)
        print (infolist)
        

    def restriction4(self):
        
        global Restriction4
        del infolist[8]

        Restriction4 = i.restrict4.get()
        infolist.insert (8, Restriction4)
        print (infolist)
        

    def restriction5(self):
        
        global Restriction5
        del infolist[9]

        Restriction5 = i.restrict5.get()
        infolist.insert (9, Restriction5)
        print (infolist)'''

 

#this definition will execute, if the user has decided that they want to see some tips
#their tips, will be based on their weight in relation to their to the weight
    
    def tips(self):
        global a
        a = tk.Tk()
        a.geometry('1280x720')
        a.frame=tk.Frame(a,height=1280, width=720)
        a.frame.pack()
        a.title('MyTips')
        frame = tk.Frame(a)
        frame.pack(fill='both', expand='yes')
        a.resizable(0,0)
        a.configure(background='magenta')

        a.tipinstructtext = tk.Label(a.frame,text="MyHealth gives you tips for a healthier life, based on the information you entered.",font=("Malgun Gothic Semilight",15))
        a.tipinstructtext.pack()
        a.tipinstructtext.place(x=0, y=10)

        #If you have entered 0 for either your age, height, or weight we will output no tips for you as we will need more information
        #along with telling you your current state we will also give you a few tips to get into shape
        if infolist[2]==0 or infolist[3]==0 or infolist[4]==0:

            a.noinfotip1 = tk.Label(a.frame,text="1. MyHealth has insufficient information about you!",font=("Malgun Gothic Semilight",10))
            a.noinfotip1.pack()
            a.noinfotip1.place(x=0, y=100)

            a.noinfotip2 = tk.Label(a.frame,text="2. Therefore it is unable to give you personalized tips.",font=("Malgun Gothic Semilight",10))
            a.noinfotip2.pack()
            a.noinfotip2.place(x=0, y=150)

            a.noinfotip3 = tk.Label(a.frame,text="3. Please close the window, go to 'My Info', and make sure you have added your age, height, and weight.",font=("Malgun Gothic Semilight",10))
            a.noinfotip3.pack()
            a.noinfotip3.place(x=0, y=200)

            a.noinfotip4 = tk.Label(a.frame,text="4. Then, come back here to see your personalized tips!",font=("Malgun Gothic Semilight",10))
            a.noinfotip4.pack()
            a.noinfotip4.place(x=0, y=250)
        #if your height ans weight are in this range, this block of code will determine that you are fit
        #along with telling you your current state we will also give you a few tips to stay in shape
        elif infolist[3]<150 and infolist[4]<55:

            a.good1tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE FIT!",font=("Malgun Gothic Semilight",10))
            a.good1tip1.pack()
            a.good1tip1.place(x=0, y=100)

            a.good1tip2 = tk.Label(a.frame,text="2. You are within the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.good1tip2.pack()
            a.good1tip2.place(x=0, y=150)

            a.good1tip3 = tk.Label(a.frame,text="3. It is important for you to maintain your body this way, for the best chances to avoid any diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.good1tip3.pack()
            a.good1tip3.place(x=0, y=200)

            a.good1tip4 = tk.Label(a.frame,text="4. To keep your body fit, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.good1tip4.pack()
            a.good1tip4.place(x=0, y=250)

            a.good1tip5 = tk.Label(a.frame,text="5. Get plenty of fresh air and physical activity (60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.good1tip5.pack()
            a.good1tip5.place(x=0, y=300)

            a.good1tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.good1tip6.pack()
            a.good1tip6.place(x=0, y=350)

        elif 150<=infolist[3]<=165 and 44<=infolist[4]<=65:

            a.good2tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE FIT!",font=("Malgun Gothic Semilight",10))
            a.good2tip1.pack()
            a.good2tip1.place(x=0, y=100)

            a.good2tip2 = tk.Label(a.frame,text="2. You are within the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.good2tip2.pack()
            a.good2tip2.place(x=0, y=150)

            a.good2tip3 = tk.Label(a.frame,text="3. It is important for you to maintain your body this way, for the best chances to avoid any diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.good2tip3.pack()
            a.good2tip3.place(x=0, y=200)

            a.good2tip4 = tk.Label(a.frame,text="4. To keep your body fit, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.good2tip4.pack()
            a.good2tip4.place(x=0, y=250)

            a.good2tip5 = tk.Label(a.frame,text="5. Get plenty of fresh air and physical activity (60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.good2tip5.pack()
            a.good2tip5.place(x=0, y=300)

            a.good2tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.good2tip6.pack()
            a.good2tip6.place(x=0, y=350)

            
        elif 165<infolist[3]<=178 and 65<infolist[4]<=76:

            a.good3tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE FIT!",font=("Malgun Gothic Semilight",10))
            a.good3tip1.pack()
            a.good3tip1.place(x=0, y=100)

            a.good3tip2 = tk.Label(a.frame,text="2. You are within the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.good3tip2.pack()
            a.good3tip2.place(x=0, y=150)

            a.good3tip3 = tk.Label(a.frame,text="3. It is important for you to maintain your body this way, for the best chances to avoid any diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.good3tip3.pack()
            a.good3tip3.place(x=0, y=200)

            a.good3tip4 = tk.Label(a.frame,text="4. To keep your body fit, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.good3tip4.pack()
            a.good3tip4.place(x=0, y=250)

            a.good3tip5 = tk.Label(a.frame,text="5. Get plenty of fresh air and physical activity (60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.good3tip5.pack()
            a.good3tip5.place(x=0, y=300)
            
            a.good3tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.good3tip6.pack()
            a.good3tip6.place(x=0, y=350)

        elif 178<infolist[3]<=190 and 76<infolist[4]<=87:

            a.good4tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE FIT!",font=("Malgun Gothic Semilight",10))
            a.good4tip1.pack()
            a.good4tip1.place(x=0, y=100)

            a.good4tip2 = tk.Label(a.frame,text="2. You are within the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.good4tip2.pack()
            a.good4tip2.place(x=0, y=150)

            a.good4tip3 = tk.Label(a.frame,text="3. It is important for you to maintain your body this way, for the best chances to avoid any diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.good4tip3.pack()
            a.good4tip3.place(x=0, y=200)

            a.good4tip4 = tk.Label(a.frame,text="4. To keep your body fit, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.good4tip4.pack()
            a.good4tip4.place(x=0, y=250)

            a.good4tip5 = tk.Label(a.frame,text="5. Get plenty of fresh air and physical activity (60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.good4tip5.pack()
            a.good4tip5.place(x=0, y=300)
            
            a.good4tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.good4tip6.pack()
            a.good4tip6.place(x=0, y=350)

        elif infolist[3]>190 and infolist[4]>70:

            a.good5tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE FIT!",font=("Malgun Gothic Semilight",10))
            a.good5tip1.pack()
            a.good5tip1.place(x=0, y=100)

            a.good5tip2 = tk.Label(a.frame,text="2. You are within the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.good5tip2.pack()
            a.good5tip2.place(x=0, y=150)

            a.good5tip3 = tk.Label(a.frame,text="3. It is important for you to maintain your body this way, for the best chances to avoid any diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.good5tip3.pack()
            a.good5tip3.place(x=0, y=200)

            a.good5tip4 = tk.Label(a.frame,text="4. To keep your body fit, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.good5tip4.pack()
            a.good5tip4.place(x=0, y=250)

            a.good5tip5 = tk.Label(a.frame,text="5. Get plenty of fresh air and physical activity (60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.good5tip5.pack()
            a.good5tip5.place(x=0, y=300)
            
            a.good5tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.good5tip6.pack()
            a.good5tip6.place(x=0, y=350)


        #if your height and weight fall under this category then you are in obese
        #below are a series of tips that you may use to get into shape
        elif infolist[3]<150 and infolist[4]>55:

            a.obese1tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE OVERWEIGHT!",font=("Malgun Gothic Semilight",10))
            a.obese1tip1.pack()
            a.obese1tip1.place(x=0, y=100)

            a.obese1tip2 = tk.Label(a.frame,text="2. You are over the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.obese1tip2.pack()
            a.obese1tip2.place(x=0, y=150)

            a.obese1tip3 = tk.Label(a.frame,text="3. It is important for you to lose more body fat, to decrease your chances of getting diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.obese1tip3.pack()
            a.obese1tip3.place(x=0, y=200)

            a.obese1tip4 = tk.Label(a.frame,text="4. To lose weight, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.obese1tip4.pack()
            a.obese1tip4.place(x=0, y=250)

            a.obese1tip5 = tk.Label(a.frame,text="5. Get more fresh air and physical activity (more than 60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.obese1tip5.pack()
            a.obese1tip5.place(x=0, y=300)

            a.obese1tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.obese1tip6.pack()
            a.obese1tip6.place(x=0, y=350)

            a.obese1tip7 = tk.Label(a.frame,text="7. Consult a doctor if this further concerns you.",font=("Malgun Gothic Semilight",10))
            a.obese1tip7.pack()
            a.obese1tip7.place(x=0, y=400)

        elif 150<=infolist[3]<=165 and infolist[4]>65:

            a.obese2tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE OVERWEIGHT!",font=("Malgun Gothic Semilight",10))
            a.obese2tip1.pack()
            a.obese2tip1.place(x=0, y=100)

            a.obese2tip2 = tk.Label(a.frame,text="2. You are over the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.obese2tip2.pack()
            a.obese2tip2.place(x=0, y=150)

            a.obese2tip3 = tk.Label(a.frame,text="3. It is important for you to lose more body fat, to decrease your chances of getting diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.obese2tip3.pack()
            a.obese2tip3.place(x=0, y=200)

            a.obese2tip4 = tk.Label(a.frame,text="4. To lose weight, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.obese2tip4.pack()
            a.obese2tip4.place(x=0, y=250)

            a.obese2tip5 = tk.Label(a.frame,text="5. Get more fresh air and physical activity (more than 60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.obese2tip5.pack()
            a.obese2tip5.place(x=0, y=300)

            a.obese2tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.obese2tip6.pack()
            a.obese2tip6.place(x=0, y=350)

            a.obese2tip7 = tk.Label(a.frame,text="7. Consult a doctor if this further concerns you.",font=("Malgun Gothic Semilight",10))
            a.obese2tip7.pack()
            a.obese2tip7.place(x=0, y=400)

        elif 165<infolist[3]<=178 and infolist[4]>76:

            a.obese3tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE OVERWEIGHT!",font=("Malgun Gothic Semilight",10))
            a.obese3tip1.pack()
            a.obese3tip1.place(x=0, y=100)

            a.obese3tip2 = tk.Label(a.frame,text="2. You are over the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.obese3tip2.pack()
            a.obese3tip2.place(x=0, y=150)

            a.obese3tip3 = tk.Label(a.frame,text="3. It is important for you to lose more body fat, to decrease your chances of getting diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.obese3tip3.pack()
            a.obese3tip3.place(x=0, y=200)

            a.obese3tip4 = tk.Label(a.frame,text="4. To lose weight, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.obese3tip4.pack()
            a.obese3tip4.place(x=0, y=250)

            a.obese3tip5 = tk.Label(a.frame,text="5. Get more fresh air and physical activity (more than 60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.obese3tip5.pack()
            a.obese3tip5.place(x=0, y=300)

            a.obese3tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.obese3tip6.pack()
            a.obese3tip6.place(x=0, y=350)

            a.obese3tip7 = tk.Label(a.frame,text="7. Consult a doctor if this further concerns you.",font=("Malgun Gothic Semilight",10))
            a.obese3tip7.pack()
            a.obese3tip7.place(x=0, y=400)

        elif 178<infolist[3]<=190 and infolist[4]>87:

            a.obese4tip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE OVERWEIGHT!",font=("Malgun Gothic Semilight",10))
            a.obese4tip1.pack()
            a.obese4tip1.place(x=0, y=100)

            a.obese4tip2 = tk.Label(a.frame,text="2. You are over the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.obese4tip2.pack()
            a.obese4tip2.place(x=0, y=150)

            a.obese4tip3 = tk.Label(a.frame,text="3. It is important for you to lose more body fat, to decrease your chances of getting diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.obese4tip3.pack()
            a.obese4tip3.place(x=0, y=200)

            a.obese4tip4 = tk.Label(a.frame,text="4. To lose weight, get plenty of rest and sleep (8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.obese4tip4.pack()
            a.obese4tip4.place(x=0, y=250)

            a.obese4tip5 = tk.Label(a.frame,text="5. Get more fresh air and physical activity (more than 60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.obese4tip5.pack()
            a.obese4tip5.place(x=0, y=300)

            a.obese4tip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.obese4tip6.pack()
            a.obese4tip6.place(x=0, y=350)

            a.obese4tip7 = tk.Label(a.frame,text="7. Consult a doctor if this further concerns you.",font=("Malgun Gothic Semilight",10))
            a.obese4tip7.pack()
            a.obese4tip7.place(x=0, y=400)

#########################################################################################################################
            
        #lastly if you fall under this ratio of height to weight then our app has declared you as underweight
        #below are a series of tips to help you get into shape
        else:
            a.underweighttip1 = tk.Label(a.frame,text="1. According to the BMI from the National Institute of Health, YOU ARE UNDERWEIGHT!",font=("Malgun Gothic Semilight",10))
            a.underweighttip1.pack()
            a.underweighttip1.place(x=0, y=100)

            a.underweighttip2 = tk.Label(a.frame,text="2. You are under the recommended range of weight, for your height.",font=("Malgun Gothic Semilight",10))
            a.underweighttip2.pack()
            a.underweighttip2.place(x=0, y=150)

            a.underweighttip3 = tk.Label(a.frame,text="3. It is important for you to gain more body fat, to have stronger immunity against diseases, such as diabetes and cancer.",font=("Malgun Gothic Semilight",10))
            a.underweighttip3.pack()
            a.underweighttip3.place(x=0, y=200)

            a.underweighttip4 = tk.Label(a.frame,text="4. To gain weight, get more rest and sleep (more than 8 hours/day on average).",font=("Malgun Gothic Semilight",10))
            a.underweighttip4.pack()
            a.underweighttip4.place(x=0, y=250)

            a.underweighttip5 = tk.Label(a.frame,text="5. Get fresh air and physical activity (60 minutes/day on average)",font=("Malgun Gothic Semilight",10))
            a.underweighttip5.pack()
            a.underweighttip5.place(x=0, y=300)

            a.underweighttip6 = tk.Label(a.frame,text="6. Close the window, and go to 'My Meals' to get suggestions for healthy meals everyday!",font=("Malgun Gothic Semilight",10))
            a.underweighttip6.pack()
            a.underweighttip6.place(x=0, y=350)

            a.underweighttip7 = tk.Label(a.frame,text="7. Consume fatty foods, such as butter, nuts, cheese, avocados, eggs, and meat.",font=("Malgun Gothic Semilight",10))
            a.underweighttip7.pack()
            a.underweighttip7.place(x=0, y=400)

            a.underweighttip8 = tk.Label(a.frame,text="8. Consult a doctor if this further concerns you.",font=("Malgun Gothic Semilight",10))
            a.underweighttip8.pack()
            a.underweighttip8.place(x=0, y=450)

            

    #this definition will allow the user to look at potential meals that they may want to try out to better their diet       
    def meals(self):
        
        global b
        b = tk.Tk()
        b.geometry('1280x720')
        b.frame=tk.Frame(b,height=1280, width=720)
        b.frame.pack()
        b.title('MyMeals')
        frame = tk.Frame(b)
        frame.pack(fill='both', expand='yes')
        b.resizable(0,0)
        b.configure(background='red')

        b.mealinstructtext = tk.Label(b.frame,text="MyHealth gives you examples of healthy meals for each time of the day.",font=("Malgun Gothic Semilight",15))
        b.mealinstructtext.pack()
        b.mealinstructtext.place(x=70, y=10)

        b.mealsinstructtext = tk.Label(b.frame,text="Feel free to make minor changes to match your preferences.",font=("Malgun Gothic Semilight",15))
        b.mealsinstructtext.pack()
        b.mealsinstructtext.place(x=100, y=50)

        randmeal = random.randint(1, 7) #our app has a total of 7 meals and it will randomize each time so you dont get
        #the same meal each time

        
        #below are a list of meals that our app offers. Each meal is different but delivers the same idea of healthy eating
        if randmeal == 1:

            b.breakfast1 = tk.Label(b.frame,text='''Breakfast: Smoked Salmon & Egg Sandwich- smoked salmon and egg whites on a toasted whole-wheat English muffin,
            paired with a piece of fruit or a glass of 100% juice.''',font=("Malgun Gothic Semilight",10))
            b.breakfast1.pack()
            b.breakfast1.place(x=0, y=100)

            b.lunch1 = tk.Label(b.frame,text='''Lunch: Smoked Turkey and Farro/Barley Salad- lean turkey, farro or barley, bell peppers, celery,
            smoked cheese and avocado, served with baby spinach salad with toasted almonds and creamy garlic dressing.''',font=("Malgun Gothic Semilight",10))
            b.lunch1.pack()
            b.lunch1.place(x=0, y=200)

            b.dinner1 = tk.Label(b.frame,text='''Dinner: Chicken & Spinach Skillet Pasta- pasta, lean chicken breast, sauteed spinach, garlic and lemon.''',font=("Malgun Gothic Semilight",10))
            b.dinner1.pack()
            b.dinner1.place(x=0, y=300)

        elif randmeal == 2:

            b.breakfast2 = tk.Label(b.frame,text='''Breakfast: Breakfast Parfait- slices of berries and fruits of your choice, almonds, granola, and yogourt.''',font=("Malgun Gothic Semilight",10))
            b.breakfast2.pack()
            b.breakfast2.place(x=0, y=100)

            b.lunch2 = tk.Label(b.frame,text='''Lunch: Shrimp Cobb Salad- Cooked, peeled shrimp, boiled egg, tomatoes, cucumbers, lettuce,
            with a salad dressing of your choice.''',font=("Malgun Gothic Semilight",10))
            b.lunch2.pack()
            b.lunch2.place(x=0, y=200)

            b.dinner2 = tk.Label(b.frame,text='''Dinner: Chicken & Mushroom marsala- lean chicken breast, cooked mushrooms,
            mashed potaoes, herbs, and Marsala wine.''',font=("Malgun Gothic Semilight",10))
            b.dinner2.pack()
            b.dinner2.place(x=0, y=300)

        elif randmeal == 3:

            b.breakfast3 = tk.Label(b.frame,text='''Breakfast: Quick Breakfast Taco- taco shells, cheddar cheese, scrambled eggs, and salsa.''',font=("Malgun Gothic Semilight",10))
            b.breakfast3.pack()
            b.breakfast3.place(x=0, y=100)

            b.lunch3 = tk.Label(b.frame,text='''Lunch: Zesty Shrimp & Black Bean Salad- cooked shrimp, black beans, tomatoes, peppers,
            seasoned with cumin and chile, served with tortilla chips.''',font=("Malgun Gothic Semilight",10))
            b.lunch3.pack()
            b.lunch3.place(x=0, y=200)

            b.dinner3 = tk.Label(b.frame,text='''Dinner: Quinoa, Chicken & Broccoli Salad- roasted chicken, raw broccoli, baked quinoa,
            toppped with a roasted lemon mellow dressing.''',font=("Malgun Gothic Semilight",10))
            b.dinner3.pack()
            b.dinner3.place(x=0, y=300)

        elif randmeal == 4:

            b.breakfast4 = tk.Label(b.frame,text='''Breakfast: Citrus Berry Smoothie- a blend of citrus fruits and berries of your choice.''',font=("Malgun Gothic Semilight",10))
            b.breakfast4.pack()
            b.breakfast4.place(x=0, y=100)

            b.lunch4 = tk.Label(b.frame,text='''Lunch: Broccoli, Ham and Cheese Quiche- Cooked broccoli, cheddar cheese, smoky ham, eggs,
            and hash browns for the crust and base.''',font=("Malgun Gothic Semilight",10))
            b.lunch4.pack()
            b.lunch4.place(x=0, y=200)

            b.dinner4 = tk.Label(b.frame,text='''Dinner: Chicken & Sun-Dried Tomato Orzo- chicken, romano cheese, sun-dried tomatoes and rice,
            served with  sauteed fresh spinach or steamed broccoli.''',font=("Malgun Gothic Semilight",10))
            b.dinner4.pack()
            b.dinner4.place(x=0, y=300)

        elif randmeal == 5:

            b.breakfast5 = tk.Label(b.frame,text='''Breakfast: Creamy Wheat Berry Hot Cereal- cooked wheat berries, rolled oats, and fruits and nuts of your choice.''',font=("Malgun Gothic Semilight",10))
            b.breakfast5.pack()
            b.breakfast5.place(x=0, y=100)

            b.lunch5 = tk.Label(b.frame,text='''Lunch: Egg Salad Bento Box- egg salad, lettuce. broccoli tomatoes, paired with bananas, berries and yogourt,
            and chcolate chips, nuts, and crackers as a side.''',font=("Malgun Gothic Semilight",10))
            b.lunch5.pack()
            b.lunch5.place(x=0, y=200)

            b.dinner5 = tk.Label(b.frame,text='''Dinner: Creamy Lemon Chicken Parmesan- chicken parmesan, lemony creamy sauce,
            served with whole-wheat pasta or brown rice.''',font=("Malgun Gothic Semilight",10))
            b.dinner5.pack()
            b.dinner5.place(x=0, y=300)

        elif randmeal == 6:

            b.breakfast6 = tk.Label(b.frame,text='''Breakfast: Crunchy Cereal Trail Mix- nuts, raisins, chocolate chips, and cereals of your choice.''',font=("Malgun Gothic Semilight",10))
            b.breakfast6.pack()
            b.breakfast6.place(x=0, y=100)

            b.lunch6 = tk.Label(b.frame,text='''Lunch: Greek Pasta Salad- pasta, feta cheese, peppers, zucchini, chick peas, tomato, and olive oil for flavour.''',font=("Malgun Gothic Semilight",10))
            b.lunch6.pack()
            b.lunch6.place(x=0, y=200)

            b.dinner6 = tk.Label(b.frame,text='''Dinner: Slow-Cooker Chicken & White Bean Stew- with carrots, spinach, salt and pepper,
            served with crusty bread, a glass of Chianti, and a salad.''',font=("Malgun Gothic Semilight",10))
            b.dinner6.pack()
            b.dinner6.place(x=0, y=300)

        elif randmeal == 7:

            b.breakfast7 = tk.Label(b.frame,text='''Breakfast: Scrambled Egg Burritos with Black Bean Salsa.''',font=("Malgun Gothic Semilight",10))
            b.breakfast7.pack()
            b.breakfast7.place(x=0, y=100)

            b.lunch7 = tk.Label(b.frame,text='''Lunch: Chicken & White Bean Salad- served with any type of salad greens and a sakad dressing of your choice.''',font=("Malgun Gothic Semilight",10))
            b.lunch7.pack()
            b.lunch7.place(x=0, y=200)

            b.dinner7 = tk.Label(b.frame,text='''Dinner: Skillet Chicken Parmesan- chicken cutlets/boneless chicken, tomato sauce, herbs and spices of your choice.''',font=("Malgun Gothic Semilight",10))
            b.dinner7.pack()
            b.dinner7.place(x=0, y=300)

        else:
            
            pass

        b.newmealbutton = tk.Button(b.frame, text="Another Meal", font=("Malgun Gothic Semilight",30), bg="lightgreen", command=self.meals)
        b.newmealbutton.pack()
        b.newmealbutton.place(x=250, y=400)

scr=main(r) #end the whole window loop. Without these two lines of code none of the windows will appear on screen
r.mainloop()
