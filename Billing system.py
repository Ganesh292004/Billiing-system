from contextlib import nullcontext
from tkinter import *
from tkinter import messagebox
import random,os,tempfile,smtplib
#FUNCTIONALITY PARTS
#==============================Email function=======================
def clear():
    nventry.insert(0, 0)
    palaventry.insert(0, 0)
    parotaentry.insert(0, 0)
    dambiryanientry.insert(0, 0)
    frybiryanientry.insert(0, 0)
    grillchickenentry.insert(0, 0)
    grillchicken2entry.insert(0, 0)


    vegcurryentry.insert(0, 0)
    vegbiryanientry.insert(0, 0)
    andhramealsentry.insert(0, 0)
    fullmealsentry.insert(0, 0)
    halfmealsentry.insert(0, 0)
    rotientry.insert(0, 0)

    wineentry.insert(0, 0)
    mansionhouseentry.insert(0, 0)
    kingentry.insert(0, 0)
    goldenentry.insert(0, 0)
    wodkaentry.insert(0, 0)
    whiskyentry.insert(0, 0)


    nonvegprice.delete(0, END)
    vegprice.delete(0, END)
    alcoholprice.delete(0, END)

    nonvegtaxentry.delete(0, END)
    vegtaxentry.delete(0, END)
    alcoholtaxentry.delete(0, END)

    nameentry.detele(0,END)
    phoneentry.delete(0, END)
    billnumberentry.delete(0, END)

    textarea.delete(0, END)








def send_mail():
    def send_gmail():
         try:
              obj = smtplib.SMTP('smtp.gmail.com', 587)
              obj.starttls()#starttls-secure connection
              obj.login(gmailidentry.get(),passwordentry.get())
              message=emailtexarea.get(1.0,END)
              receiver_address= Receiverentry.get()
              obj.sendmail(gmailidentry.get(),receiver_address,message)
              obj.quit()
              messagebox.showinfo("Success", "Bill sent successfully",parent=gani1)
         except:
             messagebox.showerror("Error", "Something went wrong",parent=gani1)
    if textarea.get(1.0,END)=='/n':
        messagebox.showerror('Error','Mail is empty')
    else:
        gani1=Toplevel()
        gani1.grab_set()
        gani1.title('send Mail')
        gani1.config(bg='grey')
        gani1.resizable(2,2)


        sendframe=LabelFrame(gani1,text='SENDER',font=('arial',20,'bold'))
        sendframe.grid(row=0,column=0)


        gmailidlabel=Label(sendframe,text="Sender's email",font=('arial',18,'bold'),fg='black')
        gmailidlabel.grid(row=0,column=0,pady=10)
        gmailidentry=Entry(sendframe,font=('arial',18,'bold'),bg='red',fg='white')
        gmailidentry.grid(row=0,column=1,padx=10)

        Passwordlabel = Label(sendframe, text="Password", font=('arial', 18, 'bold'), fg='black')
        Passwordlabel.grid(row=1, column=0)
        passwordentry = Entry(sendframe, font=('arial', 18, 'bold'),bg='red',fg='white',show='*')
        passwordentry.grid(row=1, column=1)

        recipientframe = LabelFrame(gani1, text='RECEIPENT', font=('arial', 20, 'bold'))
        recipientframe.grid(row=2, column=0,pady=30,padx=40)


        Receiverlabel = Label(recipientframe, text="Receiver Email", font=('arial', 18, 'bold'), fg='black')
        Receiverlabel.grid(row=0, column=0)
        Receiverentry = Entry(recipientframe, font=('arial', 18, 'bold'),bg='red',fg='white')
        Receiverentry.grid(row=0, column=1)

        messagelabel = Label(recipientframe, text="Message", font=('arial', 18, 'bold'), fg='black')
        messagelabel.grid(row=1, column=0)

        emailtexarea=Text(recipientframe,font=('arial',10,'bold'),fg='black',bd='2',bg='white',relief=SUNKEN ,width=42,height=11)
        emailtexarea.grid(row=2,column=0,columnspan=20)
        emailtexarea.delete('1.0',END)
        emailtexarea.insert(END,textarea.get(1.0,END).replace('=','').replace('*','').replace('\t\t\t','\t\t'))

        sendbutton=Button(gani1,text='SEND', font=('arial', 18, 'bold'),bd='2',bg='green',fg='white',command=send_gmail)
        sendbutton.grid(row=3,column=0,pady=20)


        gani1.mainloop()




#=========================================print function====================
def print_bill():
    if textarea.get(1.0,END)=='/n':
       messagebox.showerror('Error','Bill is empty ')
    else:
        file=tempfile.mkstemp('.txt')
        open(file[1],'w').write(textarea.get(1.0,END))
        os.startfile(file[1],'print')

#============================bill number function==============================
def search_bill():
    for i in os.listdir('bills/'):
        if i.split('.')[0]==billnumberentry.get():
            f=open(f'bills/{i}','r')
            textarea.delete('1.0',END)
            for data in f:
                textarea.insert(END,data)
            f.close()
            break
    else:
        messagebox.showerror('Error','No such file')
#===============================================================================


if not os.path.exists('bills'):
    os.mkdir('bills')
def save_bill():
    global BillNumber
    result=messagebox.askyesno('confirm','Do you want to save your bill?')
    if result:
        bill_content=textarea.get('1.0',END)
        file=open(f'bills/{BillNumber}.txt','w')
        file.write(bill_content)
        file.close()
        messagebox.showinfo('Bill Saved',f' Bill number {BillNumber} is saved successfully!')
        BillNumber=random.randint(100,1000)



BillNumber=random.randint(100,1000)
def bill_area():
    textarea.delete(1.0,END)
    if nameentry.get()==''or phoneentry.get()=='':
        messagebox.showerror('Error','Please enter customer details')
    elif nonvegprice.get()=='' and vegprice.get()=='' and alcoholprice.get()=='':
        messagebox.showerror('Error','Please enter product details')
    elif nonvegprice.get() == '0 Rs' and vegprice.get() == '0 Rs' and alcoholprice.get() == '0 Rs':
        messagebox.showerror('Error','Please enter product details')
    else:
        textarea.insert(END,'\t\t***Welcome to Mart***')
        textarea.insert(END,f'\nBill number:{BillNumber}')
        textarea.insert(END,f'\nCustomer name:{nameentry.get()}')
        textarea.insert(END,f'\nCustomer phone:{phoneentry.get()}\n')
        textarea.insert(END,'==========================================================\n')
        textarea.insert(END,f'Item''\t\t\tQTY''\t\t\tPrice')
        textarea.insert(END, '\n==========================================================')

        if nventry.get() != '0':
            textarea.insert(END, f'\nnvcurries\t\t\t{nventry.get()}\t\t\t{nvcurries}')
        if palaventry.get() != '0':
            textarea.insert(END, f'\nPalav\t\t\t{palaventry.get()}\t\t\t{palav}')
        if parotaentry.get() != '0':
            textarea.insert(END, f'\nParota\t\t\t{parotaentry.get()}\t\t\t{parota}')
        if dambiryanientry.get() != '0':
            textarea.insert(END, f'\nDambiryani \t\t\t{dambiryanientry.get()}\t\t\t{dambiryani}')
        if frybiryanientry.get() != '0':
            textarea.insert(END, f'\nFrybiryani \t\t\t{frybiryanientry.get()}\t\t\t{frybiryani}')
        if grillchickenentry.get() != '0':
            textarea.insert(END, f'\nGrillchik-Full \t\t\t{grillchickenentry.get()}\t\t\t{grillfull}')
        if grillchicken2entry.get() != '0':
            textarea.insert(END, f'\nGrillchik-Half \t\t\t{grillchicken2entry.get()}\t\t\t{grillhalf}')

        if vegcurryentry.get() != '0':
            textarea.insert(END, f'\nVeg-curries \t\t\t{vegcurryentry.get()}\t\t\t{vegcurry}')
        if vegbiryanientry.get() != '0':
            textarea.insert(END, f'\nVeg-biryani \t\t\t{vegbiryanientry.get()}\t\t\t{vegbiryani}')
        if andhramealsentry.get() != '0':
            textarea.insert(END, f'\nAndhra-taali \t\t\t{andhramealsentry.get()}\t\t\t{Andhrameals}')
        if fullmealsentry.get() != '0':
            textarea.insert(END, f'\nFull-meals \t\t\t{fullmealsentry.get()}\t\t\t{Fullmeals}')
        if halfmealsentry.get() != '0':
            textarea.insert(END, f'\nHalf-meals \t\t\t{halfmealsentry.get()}\t\t\t{Halfmeals}')
        if rotientry.get() != '0':
            textarea.insert(END, f'\nRoti \t\t\t{rotientry.get()}\t\t\t{Roti}')

        if wineentry.get() != '0':
           textarea.insert(END, f'\nWine\t\t\t{wineentry.get()}\t\t\t{wine}')
        if mansionhouseentry.get() != '0':
           textarea.insert(END, f'\nMansion house \t\t\t{mansionhouseentry.get()}\t\t\t{mansionhouse}')
        if kingentry.get() != '0':
           textarea.insert(END, f'\nKingfisher \t\t\t{kingentry.get()}\t\t\t{kingfisher}')
        if goldenentry.get() != '0':
           textarea.insert(END, f'\nGoldenstrips \t\t\t{goldenentry.get()}\t\t\t{goldenstrips}')
        if wodkaentry.get() != '0':
           textarea.insert(END, f'\nWodka \t\t\t{wodkaentry.get()}\t\t\t{wodka}')
        if whiskyentry.get() != '0':
           textarea.insert(END, f'\nWhisky \t\t\t{whiskyentry.get()}\t\t\t{whisky}')

        textarea.insert(END,'\n***********************************************************')
#================================Tax part=========================
        textarea.insert(END,f'\nItem name\t\t\t Total tax')
        if nonvegtaxentry.get()!=0:
         textarea.insert(END, f'\nNon-veg tax\t\t\t{nonvegtaxentry.get()}')
        if vegtaxentry.get() != 0:
         textarea.insert(END, f'\nVeg tax\t\t\t{vegtaxentry.get()}')
         if alcoholtaxentry.get() != 0:
             textarea.insert(END, f'\nAlcohol tax\t\t\t{alcoholtaxentry.get()}\n')

        #===============Total Bill==============
        textarea.insert(END,f'\nTotal Bill\t\t\t{totalbill}')
        textarea.insert(END, '\n***********************************************************')
        save_bill()







def total():
    global nvcurries , palav ,parota ,dambiryani ,frybiryani,grillfull,grillhalf,vegcurry
    global vegbiryani,Andhrameals,Fullmeals,Halfmeals,Roti,wine,mansionhouse,kingfisher,goldenstrips,wodka,whisky
    global totalbill


    #Non veg
    nvcurries=int(nventry.get())*50
    print(nvcurries)
    palav= int(palaventry.get())*80
    print(palav)
    parota = int(parotaentry.get())*30
    print(parota)
    dambiryani= int(dambiryanientry.get())*150
    print(dambiryani)
    frybiryani= int(frybiryanientry.get())*150
    print(frybiryani)
    grillfull = int(grillchickenentry.get())*250
    print(grillfull)
    grillhalf= int(grillchicken2entry.get())*150
    print(grillhalf)
#========================Veg================

    vegcurry = int(vegcurryentry.get()) * 25
    print(vegcurry)
    vegbiryani = int(vegbiryanientry.get()) *100
    print(vegbiryani)
    Andhrameals = int(andhramealsentry.get()) *200
    print(Andhrameals)
    Fullmeals= int(fullmealsentry.get()) * 120
    print(Fullmeals)
    Halfmeals = int(halfmealsentry.get()) * 80
    print(Halfmeals)
    Roti= int(rotientry.get()) * 35
    print(Roti)


#==================================alcohol======================#
    wine = int(wineentry.get()) *2000
    print(vegcurry)
    mansionhouse= int(mansionhouseentry.get()) * 1800
    print(vegbiryani)
    kingfisher = int(kingentry.get()) *250
    print(Andhrameals)
    goldenstrips = int(goldenentry.get()) *700
    print(Fullmeals)
    wodka= int(wodkaentry.get()) *1400
    print(Halfmeals)
    whisky= int(whiskyentry.get()) *1600
    print(Roti)
#===========================total nonveg price=========================
    totalnonvegprice=nvcurries+palav+parota+dambiryani+frybiryani+grillfull+grillhalf
    nonvegprice.delete(0,END)
    nonvegprice.insert(0,str(totalnonvegprice)+'Rs')
    nonvegtax=totalnonvegprice*0.03
    nonvegtaxentry.delete(0,END)
    nonvegtaxentry.insert(0,f'{nonvegtax}Rs')

#===========================total veg price===========================
    totalvegprice=vegcurry+vegbiryani+Andhrameals+Fullmeals+Halfmeals+Roti
    vegprice.delete(0,END)
    vegprice.insert(0,str(totalvegprice)+'Rs')
    vegtax=totalvegprice*0.02
    vegtaxentry.delete(0,END)
    vegtaxentry.insert(0,f'{vegtax}Rs')

#==================Alcohol============================
    totalalcoholprice=wine+mansionhouse+kingfisher+goldenstrips+wodka+whisky
    alcoholprice.delete(0,END)
    alcoholprice.insert(0,str(totalalcoholprice)+'Rs')
    alcoholtax=totalalcoholprice*0.05
    alcoholtaxentry.delete(0,END)
    alcoholtaxentry.insert(0,f'{alcoholtax}Rs')
##==================================Total bill======================
    totalbill=totalnonvegprice+totalvegprice+totalalcoholprice+nonvegtax+vegtax+alcoholtax

#==========================GUI PART===============================
gani=Tk()
gani.geometry("1000x900")
gani.title("Advanced Billing")
gani.iconbitmap("C:/Users/Ganesh Reddy/Downloads/cash-register.png")

#======================================Top heading================================#
headinglabel = Label(gani, text="restarent billing system",font=("algerian",20) ,bg="dark blue",fg="white", bd=12,relief="groove")
headinglabel.pack(fill="x")

#======================================Customer Details=======================================#
customer_details_frame=LabelFrame(gani,text="CUSTOMER DETAILS",font=("times new roman",12,'bold') ,bg="green",fg="yellow")
customer_details_frame.pack(fill="x")
#==================name label==============#
nameLabel=Label(customer_details_frame,text="Name",font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
nameLabel.grid(row=0 ,column=0,padx=8,pady=2)
nameentry=Entry(customer_details_frame, font=("arial",18,'bold'),bd=10, relief="groove")
nameentry.grid(row=0,column=1,padx=20)

#=======phone label===========#
phoneLabel=Label(customer_details_frame,text='Phone number',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
phoneLabel.grid(row=0 ,column=2,padx=20,pady=10)
phoneentry=Entry(customer_details_frame, font=("arial",18,'bold'),bd=10, relief="groove")
phoneentry.grid(row=0,column=3,padx=20)

#=======gmail label===========#
billnumberLabel=Label(customer_details_frame,text='Bill number',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
billnumberLabel.grid(row=0 ,column=4,padx=20,pady=10)
billnumberentry=Entry(customer_details_frame, font=("arial",18,'bold'),bd=10, relief="groove")
billnumberentry.grid(row=0,column=5)

#============================= Search button============================#
search_button=Button(customer_details_frame,text='Search',font=("arial",10 , 'bold') ,fg="gold" , bg='dark blue',bd=15, relief="groove",command=search_bill)
search_button.grid(row=0,column=6,padx=12)

#================================Products frame==========================#
productframe=Frame(gani)
productframe.pack()

#============================NON-veg section==============================#

Nonveg_details_frame=LabelFrame(productframe,text="NON VEG-ITEMS",font=("times new roman",12,'bold') ,bg="green",fg="yellow")
Nonveg_details_frame.grid(row=0,column=0,padx=10,pady=10)


nvcurries=Label(Nonveg_details_frame,text='Non-veg curries',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
nvcurries.grid(row=0,column=0,padx=10,pady=10)

nventry=Entry(Nonveg_details_frame, font=("arial",20,'bold'),bd=5, relief="groove",width=5)
nventry.grid(row=0,column=1,padx=20)
nventry.insert(0,0)
#========1 item==========#

palav=Label(Nonveg_details_frame,text='Palav',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10 , relief='groove')
palav.grid(row=1,column=0,padx=2)

palaventry=Entry(Nonveg_details_frame, font=("arial",20,'bold'),bd=5, relief="groove",width=5)
palaventry.grid(row=1,column=1,padx=2)
palaventry.insert(0,0)
#========2 item==========#
parota=Label(Nonveg_details_frame,text='Parota',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
parota.grid(row=2,column=0,padx=2,pady=10)

parotaentry=Entry(Nonveg_details_frame, font=("arial",20,'bold'),bd=5, relief="groove",width=5)
parotaentry.grid(row=2,column=1,padx=2)
parotaentry.insert(0,0)
#========3 item==========#
dambiryani=Label(Nonveg_details_frame,text='Dam-biryani',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
dambiryani.grid(row=3,column=0,padx=2,pady=10)

dambiryanientry=Entry(Nonveg_details_frame, font=("arial",20,'bold'),bd=5, relief="groove",width=5)
dambiryanientry.grid(row=3,column=1,padx=2)
dambiryanientry.insert(0,0)
#========4 item==========#
frybiryani=Label(Nonveg_details_frame,text='fry piece-biryani',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
frybiryani.grid(row=4,column=0,padx=2,pady=10)

frybiryanientry=Entry(Nonveg_details_frame, font=("arial",20,'bold'),bd=5, relief="groove",width=5)
frybiryanientry.grid(row=4,column=1,padx=2)
frybiryanientry.insert(0,0)
#==========5 item===============#
grillchicken=Label(Nonveg_details_frame,text='Grill-chicken (Full) ',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
grillchicken.grid(row=5,column=0,padx=2,pady=10)

grillchickenentry=Entry(Nonveg_details_frame, font=("arial",20,'bold'),bd=5, relief="groove",width=5)
grillchickenentry.grid(row=5,column=1,padx=2)
grillchickenentry.insert(0,0)

#==================6 item=======================#
grillchicken2=Label(Nonveg_details_frame,text='Grill-chicken (Half) ',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
grillchicken2.grid(row=6,column=0,padx=2)

grillchicken2entry=Entry(Nonveg_details_frame, font=("arial",20,'bold'),bd=5, relief="groove",width=5)
grillchicken2entry.grid(row=6,column=1,padx=2)
grillchicken2entry.insert(0,0)

#========================veg section===========================#
veg_details_frame=LabelFrame(productframe,text="VEG-ITEMS",font=("times new roman",12,'bold') ,bg="green",fg="yellow")
veg_details_frame.grid(row=0,column=1,padx=10,pady=10)

vegcurry=Label(veg_details_frame,text='Veg-Curries',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
vegcurry.grid(row=0,column=0,padx=10,pady=10)
vegcurryentry=Entry(veg_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
vegcurryentry.grid(row=0,column=1,padx=2,pady=10)
vegcurryentry.insert(0,0)

vegbiryani=Label(veg_details_frame,text='Veg-biryani',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
vegbiryani.grid(row=1,column=0,padx=2,pady=10)
vegbiryanientry=Entry(veg_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
vegbiryanientry.grid(row=1,column=1,padx=10,pady=10)
vegbiryanientry.insert(0,0)

andhrameals=Label(veg_details_frame,text='Andhra Veg-meals',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
andhrameals.grid(row=3,column=0,padx=2,pady=10)
andhramealsentry=Entry(veg_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
andhramealsentry.grid(row=3,column=1,padx=10,pady=10)
andhramealsentry.insert(0,0)

fullmeals=Label(veg_details_frame,text='Full meals',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
fullmeals.grid(row=4,column=0,padx=10,pady=10)
fullmealsentry=Entry(veg_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
fullmealsentry.grid(row=4,column=1,padx=10,pady=10)
fullmealsentry.insert(0,0)


halfmeals=Label(veg_details_frame,text='Half Meals',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
halfmeals.grid(row=5,column=0,padx=2,pady=10)
halfmealsentry=Entry(veg_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
halfmealsentry.grid(row=5,column=1,padx=10,pady=10)
halfmealsentry.insert(0,0)

roti=Label(veg_details_frame,text='Roti',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
roti.grid(row=6,column=0,padx=2,pady=10)
rotientry=Entry(veg_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
rotientry.grid(row=6,column=1,padx=10,pady=10)
rotientry.insert(0,0)
#========================Cooled section===========================#
drink_details_frame=LabelFrame(productframe,text="ALCOHOL",font=("times new roman",12,'bold') ,bg="green",fg="yellow")
drink_details_frame.grid(row=0,column=2,padx=10,pady=10)

wine=Label(drink_details_frame,text='Wine',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
wine.grid(row=0,column=0,padx=10,pady=10)
wineentry=Entry(drink_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
wineentry.grid(row=0,column=1,padx=2,pady=10)
wineentry.insert(0,0)

mansionhouse=Label(drink_details_frame,text='Mansion House',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
mansionhouse.grid(row=1,column=0,padx=2,pady=10)
mansionhouseentry=Entry(drink_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
mansionhouseentry.grid(row=1,column=1,padx=10,pady=10)
mansionhouseentry.insert(0,0)

king=Label(drink_details_frame,text='Kingfisher',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
king.grid(row=3,column=0,padx=2,pady=10)
kingentry=Entry(drink_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
kingentry.grid(row=3,column=1,padx=10,pady=10)
kingentry.insert(0,0)

golden=Label(drink_details_frame,text='Golden strips',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
golden.grid(row=4,column=0,padx=10,pady=10)
goldenentry=Entry(drink_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
goldenentry.grid(row=4,column=1,padx=10,pady=10)
goldenentry.insert(0,0)

wodka=Label(drink_details_frame,text='Wodka',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
wodka.grid(row=5,column=0,padx=2,pady=10)
wodkaentry=Entry(drink_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
wodkaentry.grid(row=5,column=1,padx=10,pady=10)
wodkaentry.insert(0,0)

whisky=Label(drink_details_frame,text='Whisky',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=10, relief="groove")
whisky.grid(row=6,column=0,padx=2,pady=10)
whiskyentry=Entry(drink_details_frame,font=("arial",20,'bold'),bd=5, relief="groove",width=5)
whiskyentry.grid(row=6,column=1,padx=10,pady=10)
whiskyentry.insert(0,0)
#======================================Bill Area========#
billframe=Frame(productframe)
billframe.grid(row=0,column=3)
billarea=Label(billframe,text='Bill Area',font=('arial',15,'bold') , bd=10, relief="groove")
billarea.pack(fill='x')
scrollbar=Scrollbar(billframe ,orient=VERTICAL)
scrollbar.pack(side=RIGHT,fill=Y)
textarea=Text(billframe,height=22,width=60,yscrollcommand=scrollbar.set)
textarea.pack()
scrollbar.config(command=textarea.yview)
#=========================billmenu==============#

billmenuframe=LabelFrame(gani,text="Bill menu",font=("times new roman",12,'bold') ,bg="green",fg="yellow",bd=5)
billmenuframe.pack()

nonvegprice=Label(billmenuframe,text='Nonveg',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green')
nonvegprice.grid(row=0,column=0,padx=9,pady=10)
nonvegprice=Entry(billmenuframe,font=("arial",20,'bold'),bd=3 ,width=10)
nonvegprice.grid(row=0,column=1)


vegprice=Label(billmenuframe,text='Veg',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=2)
vegprice.grid(row=1,column=0)
vegprice=Entry(billmenuframe,font=("arial",20,'bold'),bd=3 ,width=10)
vegprice.grid(row=1,column=1 )

alcoholprice=Label(billmenuframe,text='alcohol',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=2 )
alcoholprice.grid(row=2,column=0)
alcoholprice=Entry(billmenuframe,font=("arial",20,'bold'),bd=3 ,width=10)
alcoholprice.grid(row=2,column=1 )


#================================TAX======================================#
nonvegtax=Label(billmenuframe,text='Nonveg Tax',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=2)
nonvegtax.grid(row=0,column=3,padx=5)
nonvegtaxentry=Entry(billmenuframe,font=("arial",20,'bold'),bd=3,width=10)
nonvegtaxentry.grid(row=0,column=4)

vegtax=Label(billmenuframe,text='Veg Tax',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=2)
vegtax.grid(row=1,column=3)
vegtaxentry=Entry(billmenuframe,font=("arial",20,'bold'),bd=3,width=10)
vegtaxentry.grid(row=1,column=4,padx=5)

alcoholtax=Label(billmenuframe,text='AlcoholTax',font=("arial",10 , 'bold') ,fg="gold" , bg='dark green',bd=2)
alcoholtax.grid(row=2,column=3)
alcoholtaxentry=Entry(billmenuframe,font=("arial",20,'bold'),bd=3,width=10)
alcoholtaxentry.grid(row=2,column=4,padx=5)

#=======================================BUTTON==================================
buttonframe=Frame(billmenuframe,bd=5,relief="groove",width=10,height=10)
buttonframe.grid(row=0,column=5 ,rowspan=3)

total=Button(buttonframe,text='Total' , bg='red' ,fg='gold',font=("arial",10 ,'bold'),relief="groove" ,bd=5,width=20,command=total)
total.grid(row=0,column=0,pady=20)

Bill=Button(buttonframe,text='Bill' , bg='red' ,fg='gold',font=("arial",10 ,'bold'),relief="groove" ,bd=5,width=20
                                   ,command=bill_area)
Bill.grid(row=0,column=1,pady=20,padx=10)

Email=Button(buttonframe,text='Email' , bg='red' ,fg='gold',font=("arial",10 ,'bold'),relief="groove" ,bd=5,width=20,command=send_mail)
Email.grid(row=0,column=2,pady=20,padx=10)

Print=Button(buttonframe,text='Print' , bg='red' ,fg='gold',font=("arial",10 ,'bold'),relief="groove" ,bd=5,width=20 ,command=print_bill)
Print.grid(row=0,column=3,pady=20,padx=10)

Clearbutton=Button(buttonframe,text='Clear' , bg='red' ,fg='gold',font=("arial",10 ,'bold'),relief="groove" ,bd=5,width=10,command='clear')
Clearbutton.grid(row=0,column=4,pady=20,padx=10)

gani.mainloop()
