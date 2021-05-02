from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
from PIL import ImageTk,Image
import mysql.connector


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        self.Patientname=StringVar()
        self.NameOftablets=StringVar()
        self.PatientId=StringVar()
        self.ReferanceNo=StringVar()
        self.Patientadress=StringVar()
        self.Dateofbirth=StringVar()
        self.Furtherinformation=StringVar()
        self.Dose=StringVar()
        self.Medicine=StringVar()
        self.Issuedate=StringVar()
        self.Expdate=StringVar()
        self.Contactno=StringVar()
        self.search_by=StringVar()
        self.search_txt=StringVar()
        self.DataframeLast=Image.open("C:\\Users\\ASUS\\Downloads\\hospital.png")
        self.DataframeLast=self.DataframeLast.resize((500,350),Image.ANTIALIAS)
        self.DataframeLast=ImageTk.PhotoImage(self.DataframeLast)


        lbltitle = Label(self.root, bd=20, relief=SUNKEN, text="HOSPITAL MANAGEMENT SYSTEM", fg="deepskyblue3",
                         bg="gray72", font=("times new roman", 30, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # =======================================================Dataframe===================================================================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=10, y=80, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=SUNKEN, padx=10,
                                   font=("times new roman", 12, "bold"), text="PATIENT INFORMATION")
        DataframeLeft.place(x=0, y=5, width=480, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, bg="deepskyblue3", padx=10,
                                    font=("times new roman", 12, "bold"), text="PRECIPTION")
        DataframeRight.place(x=490, y=5, width=460, height=350)

        DataframeLast = LabelFrame(Dataframe, bd=10, relief=RIDGE, bg="white", padx=10,
                                    font=("times new roman", 12, "bold"))
        DataframeLast.place(x=965, y=5, width=490, height=350)

        # ======================================================Buttonframe==============================================================

        # Dataframe=Frame(self.root,bd=20,relief=RIDGE)
        # Dataframe.place(x=0,y=530,width=1530,height=70)

        # =============================================================Detailsframe===============================================================

        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=460, width=1530, height=232)
        # =====================================DataframeLeft=======================================

        lblNameTablet = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Name Of Tablets", padx=2)
        lblNameTablet.grid(row=6, column=6, sticky=W)

        comNameTablet = ttk.Combobox(DataframeLeft,textvariable=self.NameOftablets, state="readonly",
                                     font=("times new roman", 12, "bold"), width=35)

        comNameTablet['value'] = ("Corona Vaccine", "Acetamiophen", "Adderall", "Activan")
        comNameTablet.current(0)
        comNameTablet.grid(row=6, column=1)

        lblPatientName = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Name:", padx=2)
        lblPatientName.grid(row=1, column=0, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Patientname,width=35)
        txtPatientName.grid(row=1, column=1)

        lblPatientId = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Id:", padx=2)
        lblPatientId.grid(row=2, column=0, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.PatientId, width=35)
        txtPatientId.grid(row=2, column=1)

        lblrefNo = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Referance No:", padx=2)
        lblrefNo .grid(row=3, column=0, sticky=W)
        txtrefNo = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.ReferanceNo, width=35)
        txtrefNo.grid(row=3, column=1)

        lblAdd = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Patient Adress:", padx=2)
        lblAdd.grid(row=4, column=0, sticky=W)
        txtAdd = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Patientadress, width=35)
        txtAdd.grid(row=4, column=1)

        lblDate = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Date of Birth:", padx=2)
        lblDate.grid(row=5, column=0, sticky=W)
        txtDate = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Dateofbirth, width=35)
        txtDate.grid(row=5, column=1)

        lblNtab = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Further Information:", padx=2)
        lblNtab.grid(row=6, column=6, sticky=W)
        txtNtab = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Furtherinformation, width=35)
        txtNtab.grid(row=6, column=6)

        lblDose = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Dose:", padx=2)
        lblDose.grid(row=7, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Dose, width=35)
        txtDose.grid(row=7, column=1)

        lblmed = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Medicine:", padx=2)
        lblmed.grid(row=8, column=0, sticky=W)
        txtmed = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Medicine, width=35)
        txtmed.grid(row=8, column=1)

        lblref = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Issue Date:", padx=2)
        lblref.grid(row=9, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Issuedate, width=35)
        txtref.grid(row=9, column=1)

        lblref = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Exp date:", padx=2)
        lblref.grid(row=10, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Expdate, width=35)
        txtref.grid(row=10, column=1)


        lblref = Label(DataframeLeft, font=("times new roman", 12, "bold"), text="Contact No:", padx=2)
        lblref.grid(row=12, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("times new roman", 13, "bold"),textvariable=self.Contactno, width=35)
        txtref.grid(row=12, column=1)

        

        # =======================DataframeRight==================

        self.txtPresciption = Text(DataframeRight, font=("times new roman", 12, "bold"), width=45, height=16, padx=2,
                                    pady=6)
        self.txtPresciption.grid(row=0, column=0)

        # =====================Buttons Frame===============
        Framebutton = Frame(self.root, bd=12, relief=RIDGE, padx=2, bg="white")
        Framebutton.place(x=0, y=700, width=1530, height=50)

        btnPresciption = Button(Framebutton,command=self.iPresciption,text="presciption", font=("times new roman", 12, "bold"), width=26,
                                bg="deepskyblue3", fg="white")
        btnPresciption.grid(row=0, column=0)
        

        btnPresciptionData = Button(Framebutton, text="presciption Data", bg="deepskyblue3", fg="white",command=self.ipreciptionData,
                                     font=("times new roman", 12, "bold"), width=27)
        btnPresciptionData.grid(row=0, column=1)

        btnUpdate = Button(Framebutton,command=self.update_data,text="Update", bg="deepskyblue3", fg="white",
                                     font=("times new roman", 12, "bold"), width=27)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Framebutton,command=self.idelete,text="Delete", bg="deepskyblue3", fg="white",
                                     font=("times new roman", 12, "bold"), width=27)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Framebutton,command=self.clear,text="Clear", bg="deepskyblue3", fg="white",
                                     font=("times new roman", 12, "bold"), width=27)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Framebutton,command=self.iExit,text="Exit", bg="deepskyblue3", fg="white",
                                     font=("times new roman", 12, "bold"), width=27)
        btnExit.grid(row=0, column=5)

#===================================Details Frame3============

        lblser = Label(DataframeLast,image=self.DataframeLast,font=("times new roman", 12, "bold"),fg="deepskyblue3",
                  bg="white", text="SEARCH BY:",padx=0)
        lblser.grid(row=1, column=0, sticky=W)
        search_txt = Entry(DataframeLast,textvariable=self.search_txt, font=("times new roman", 13, "bold"), width=10)
        search_txt.grid(row=1, column=1)

        comNamesearch = ttk.Combobox(DataframeLast,textvariable=self.search_by,state="readonly",
                                     font=("times new roman", 12, "bold"), width=10)

        comNamesearch['value'] = ("patient Name", "Contact Number", "Patient Id","Referance No")
        comNamesearch.current(0)
        comNamesearch.grid(row=1, column=1)

        search_entry=ttk.Entry(DataframeLast,font=("times new roman",10,"bold"))
        search_entry.grid(row=1,column=2,padx=10,pady=10,sticky=W)

        search_btn = Button(DataframeLast,command=self.search_data,text="Search", bg="deepskyblue3", fg="white",
                                     font=("times new roman", 10, "bold"), width=12)
        search_btn.grid(row=1, column=3)
        # ===========================Table=============
        # ========================scrollbar=============

        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe, column=("PatientName","PatientId", "refNo", "Add","dob", "med","further", "issue", "exp","not",

                                                                    "contact"),xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("PatientName", text="Patient Name")
        self.hospital_table.heading("PatientId", text="Patient Id")
        self.hospital_table.heading("refNo", text="Referance No")
        self.hospital_table.heading("Add", text="Patient Adress")
        self.hospital_table.heading("dob", text="Date of Birth")
        self.hospital_table.heading("med", text="Medicine")
        self.hospital_table.heading("further", text="Further Information")
        self.hospital_table.heading("issue", text="Issue Date")
        self.hospital_table.heading("exp", text="Exp date")
        self.hospital_table.heading("not", text="Name of Tablet")
        self.hospital_table.heading("contact", text="Contact No")

        self.hospital_table["show"] = "headings"
        #self.hospital_table.pack(fill=BOTH, expand=1)

        self.hospital_table.column("PatientName", width=100)
        self.hospital_table.column("PatientId", width=100)
        self.hospital_table.column("refNo", width=100)
        self.hospital_table.column("Add", width=100)
        self.hospital_table.column("dob", width=100)
        self.hospital_table.column("med", width=100)
        self.hospital_table.column("further", width=100)
        self.hospital_table.column("issue", width=100)
        self.hospital_table.column("exp", width=100)
        self.hospital_table.column("not", width=100)
        self.hospital_table.column("contact", width=100)

        self.hospital_table.pack(fill=BOTH,expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

       

#==========================Functionality Declaration===============
    def ipreciptionData(self):
        if self.Patientname.get()=="" or self.PatientId.get()=="":
            print("caught error")
            messagebox.showerror("Error","All fields are required")
        else:
            
            con=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
            my_cursor=con.cursor()
            my_cursor.execute("INSERT INTO hospital1 VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                              self.Patientname.get(),
                                                                                              self.PatientId.get(),
                                                                                              self.ReferanceNo.get(),
                                                                                              self.Patientadress.get(),
                                                                                              self.Dateofbirth.get(),
                                                                                              self.Medicine.get(),
                                                                                              self.Furtherinformation.get(),
                                                                                              self.Dose.get(),
                                                                                              self.Issuedate.get(),
                                                                                              self.Expdate.get(),
                                                                                              self.NameOftablets.get(),
                                                                                              self.Contactno.get() 
                                                                                              ))

            con.commit()
            self.fetch_data()
            con.close()
            messagebox.showinfo("success","Record has been inserted")
    

    def update_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
        my_cursor=con.cursor()
        my_cursor.execute("update hospital1 set Patientname=%s,PatientId=%s,ReferanceNo=%s,Patientadress=%s,Dateofbirth=%s,Medicine=%s,Furtherinformation=%s, Dose=%s,Issuedate=%s,Expdate=%s,NameOftablets=%s where Contactno=%s",(
                                                                
                                                                                self.Patientname.get(),
                                                                                self.PatientId.get(),
                                                                                self.ReferanceNo.get(),
                                                                                self.Patientadress.get(),
                                                                                self.Dateofbirth.get(),
                                                                                self.Medicine.get(),
                                                                                self.Furtherinformation.get(),
                                                                                self.Dose.get(),
                                                                                self.Issuedate.get(),
                                                                                self.Expdate.get(),
                                                                                self.NameOftablets.get(),
                                                                                self.Contactno.get()
                                                                                ))
        
        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("success","Record has been Updated")

    def fetch_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
        my_cursor=con.cursor()
        my_cursor.execute("select *from hospital1")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            con.commit()
        con.close()


    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.Patientname.set(row[0])
        self.PatientId.set(row[1])
        self.ReferanceNo.set(row[2])
        self.Patientadress.set(row[3])
        self.Dateofbirth.set(row[4])
        self.Medicine.set(row[5])
        self.Furtherinformation.set(row[6])
        self.Dose.set(row[7])
        self.Issuedate.set(row[8])
        self.Expdate.set(row[9])
        self.NameOftablets.set(row[10])
        self.Contactno.set(row[11])


    def iPresciption(self):
        self.txtPresciption.insert(END,"Patientname:\t\t\t" + self.Patientname.get()+"\n")
        self.txtPresciption.insert(END,"Patientadress:\t\t\t" + self.Patientadress.get()+"\n")
        self.txtPresciption.insert(END,"Dateofbirth:\t\t\t" + self.Dateofbirth.get()+"\n")
        self.txtPresciption.insert(END,"Medicine:\t\t\t" + self.Medicine.get()+"\n")
        self.txtPresciption.insert(END,"Dose:\t\t\t" + self.Dose.get()+"\n")

    def idelete(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
        my_cursor=con.cursor()
        query="delete from hospital1 where Patientname=%s"
        value=(self.Patientname.get(),)
        my_cursor.execute(query,value)

        con.commit()
        self.fetch_data()
        con.close()
        messagebox.showinfo("success","Record has been deleted")


    def clear(self):

        self.Patientname.set("")
        self.PatientId.set("")
        self.ReferanceNo.set("")
        self.Patientadress.set("")
        self.Dateofbirth.set("")
        self.Medicine.set("")
        self.Furtherinformation.set("")
        self.Dose.set("")
        self.Issuedate.set("")
        self.Expdate.set("")
        self.NameOftablets.set("")
        self.Contactno.set("")
        self.txtPresciption.delete("1.0",END)

    

    def search_data(self):
        con=mysql.connector.connect(host="localhost",user="root",password="",database="mydatabase")
        my_cursor=con.cursor()
        my_cursor.execute("select * from hospital1 where " +str(self.search_by.get())+" LIKE '%'"+str(self.search_txt.get())+"%'")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                print(i)
            con.commit()
            
        con.close()



    def iExit(self):
        iExit=messagebox.askyesno("Hospital Management System","Confirm you want to exit")
        if iExit>0:
            root.destroy()
            return


        
       
        
        







root = Tk()
obj = Hospital(root)
root.mainloop()
 

        
