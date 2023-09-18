from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk


class Bill_App:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")
        
        #Image1
        img1 = Image.open("images/1.jpg")
        img1= img1.resize((520,130),Image.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        lbl_image1= Label(self.root,image= self.photoimg1)
        lbl_image1.place(x=0,y=0,width=500,height =130)

        #Image2
        img2 = Image.open("images/2.jpg")
        img2= img2.resize((500,130),Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lbl_image2= Label(self.root,image= self.photoimg2)
        lbl_image2.place(x=520,y=0,width=500,height =130)

        #Image3
        img3 = Image.open("images/3.jpg")
        img3= img3.resize((520,130),Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        lbl_image3= Label(self.root,image= self.photoimg3)
        lbl_image3.place(x=1000,y=0,width=520,height =130)

        lbl_title= Label(self.root,text = "BILLING SOFTWARE USING PYTHON",font = ("times new roman",35,"bold"),bg = "white",fg = "red")
        lbl_title.place(x =0,y=130,width =1530, height =45 )

        #Main Frame
        Main_Frame= Frame(self.root,bd = 5,relief = GROOVE,bg = 'white')
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer Label Frame
        Cust_Frame= LabelFrame(Main_Frame,text="Customer",font =("times New Roman",12,"bold"),bg="white",fg ="red")
        Cust_Frame.place(x=10,y=5,width =350,height =140)
        
        #Mobile
        self.lbl_mob = Label(Cust_Frame, text = "Mobile No.",font =("times New Roman",12,"bold"),bg="white")
        self.lbl_mob.grid(row=0, column=0, stick =W, padx=5, pady=2)
        self.entry_mob= ttk.Entry(Cust_Frame,font =("times New Roman",10,"bold"))
        self.entry_mob.grid(row =0, column =1)

        #Customer Name
        self.lbl_cus_name = Label(Cust_Frame, text = "Customer Name",font =("times New Roman",12,"bold"),bg="white")
        self.lbl_cus_name.grid(row=1, column=0, stick =W, padx=5, pady=2)
        self.entry_mob= ttk.Entry(Cust_Frame,font =("times New Roman",10,"bold"))
        self.entry_mob.grid(row =1, column =1)

        #Email
        self.lbl_cus_email = Label(Cust_Frame, text = "Email",font =("times New Roman",12,"bold"),bg="white")
        self.lbl_cus_email.grid(row=2, column=0, stick =W, padx=5, pady=2)
        self.entry_cus_email= ttk.Entry(Cust_Frame,font =("times New Roman",10,"bold"))
        self.entry_cus_email.grid(row =2, column =1)

        #Product Label Frame
        Prod_Frame= LabelFrame(Main_Frame,text="Product",font =("times new Roman",12,"bold"),bg="white",fg ="red")
        Prod_Frame.place(x=370,y=5,width =620,height =140)

        #Category
        self.lbl_category = Label(Prod_Frame, text = "Select Catgory",font =("times New Roman",12,"bold"),bd=4,bg="white")
        self.lbl_category.grid(row=0, column=0, stick =W, padx=5, pady=2)
        self.Combo_category = ttk.Combobox(Prod_Frame,font =("times new Roman",10,"bold"),width=24, state = "readonly",)
        self.Combo_category.grid(row=0,column=1,stick =W, padx=5, pady=2)

        #SubCategory
        self.lbl_sub_category = Label(Prod_Frame, text = "Select Sub Catgory",font =("times New Roman",12,"bold"),bd=4,bg="white")
        self.lbl_sub_category.grid(row=1, column=0, stick =W, padx=5, pady=2)
        self.Combo_sub_category = ttk.Combobox(Prod_Frame,font =("times new Roman",10,"bold"),width =24 ,state = "readonly")
        self.Combo_sub_category.grid(row=1,column=1,stick =W, padx=5, pady=2)

        #Product Name
        self.lbl_prod_name = Label(Prod_Frame, text = "Select Product",font =("times New Roman",12,"bold"),bd=4,bg="white")
        self.lbl_prod_name.grid(row=2, column=0, stick =W, padx=5, pady=2)
        self.Combo_prod_name = ttk.Combobox(Prod_Frame,font =("times new Roman",10,"bold"), width = 24,state = "readonly")
        self.Combo_prod_name.grid(row=2,column=1,stick =W, padx=5, pady=2)

        #Price
        self.lblPrice= Label(Prod_Frame,text = "Price",font =("times New Roman",12,"bold"),bd=4,bg="white")
        self.lblPrice.grid(row=0, column=2, stick =W, padx=5, pady=2)
        self.ComboPrice = ttk.Combobox(Prod_Frame,font =("times new Roman",10,"bold"), width = 24,state = "readonly")
        self.ComboPrice.grid(row=0,column=3,stick =W, padx=5, pady=2)

        #Quantity
        self.lblqty= Label(Prod_Frame,text= "Qty", font = ("times new Roman",12,"bold"),bd = 4, bg = "white")
        self.lblqty.grid(row=1, column=2, stick =W, padx=5, pady=2)
        self.entry_qty= ttk.Entry(Prod_Frame,font =("times New Roman",10,"bold"), width =26)
        self.entry_qty.grid(row =1, column =3, stick = W, padx=5 , pady=2)
 
        #Right Frame Bill Area
        RightLabelFrame = LabelFrame(Main_Frame,text="BILLING AREA",font =("times new Roman",12,"bold"),bg="white",fg ="red")
        RightLabelFrame.place(x=1000,y=45,width =480,height =440)
        
        scroll_y = Scrollbar(RightLabelFrame, orient= VERTICAL)
        self.textarea = Text(RightLabelFrame, yscrollcommand=scroll_y.set, bg= "white" , fg = "blue", font =("times new Roman",12,"bold") )
        scroll_y.pack(side=RIGHT,fill = Y)
        














        





if __name__== '__main__':
    root=Tk()
    obj = Bill_App(root)
    root.mainloop()