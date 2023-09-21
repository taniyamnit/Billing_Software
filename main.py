from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import random


class Bill_App:
    def __init__(self,root):
        self.root= root
        self.root.geometry("1530x780+0+0")
        self.root.title("Billing Software")

        ##################################################################
        self.cus_name = StringVar()
        self.cus_mob = StringVar()
        self.Bill_num = StringVar()
        z = random.randint(1000,9999)
        self.Bill_num.set(2)
        self.cus_email=StringVar()
        self.search_bill = StringVar()
        self.prod_name = StringVar()
        self.price = IntVar()
        self.qty= IntVar()
        self.sub_total = StringVar()
        self.tax_inpur =StringVar()
        self.total_amount = StringVar()




        #Product Categories List
        self.Category = ["Select Options", "Clothing", "Lifestyle","Mobiles"]
        
        self.SubCat_Clothing = ["Pants","Tshirt","Shirt"]
        self.Pants=["LEVIS","AND","ZARA"]
        self.price_LEVIS = 5000
        self.price_AND = 2000
        self.price_ZARA = 3000

        self.Tshirt=["HM","MANGO","INDYA"]
        self.price_HM = 1000
        self.price_MANGO = 3000
        self.price_INDYA= 750

        self.Shirt=["RAYMONDS","PETER_ENGLAND","RICHLOOK"]
        self.price_RAYMONDS = 1000
        self.price_PETER_ENGLAND = 3000
        self.price_RICHLOOK= 750

        self.SubCat_Lifestyle =["Bath_Soap","Face_Cream","Hair_Oil"]
        self.Bath_Soap = ["LUX","VIVEL","SANTOOR"]
        self.price_LUX = 100
        self.price_VIVEL = 60
        self.price_SANTOOR= 50

        self.Face_Cream = ["PONDS","NIVEA","HIMALYA"]
        self.price_PONDS = 200
        self.price_NIVEA = 300
        self.price_HIMALYA = 400

        self.Hair_Oil = ["DABUR_AMLA","PARACHUTE","BAJAJ_ALMOND_DROPS"]
        self.price_DABUR_AMLA = 250
        self.price_PARACHUTE = 390
        self.price_BAJAJ_ALMOND_DROPS =600

        self.SubCat_Mobiles= ['Iphone','Samsung',"OnePlus"]
        self.Iphone = ["IPHONE12","IPHONE12PRO", "IPHONE12PROMAX"]
        self.price_IPHONE12 = 100000
        self.price_IPHONE12PRO = 125000
        self.price_IPHONE12PROMAX= 170000
        
        self.Samsung = ["SAMSUNGNOTE1","SAMSUNGNOTE2", "SAMSUNGNOTE3"]
        self.price_SAMSUNGNOTE1 = 15000
        self.price_SAMSUNGNOTE2 = 24000
        self.price_SAMSUNGNOTE3 = 30000

        self.OnePlus = ["ONEPLUSNOTE1","ONEPLUSNOTE2", "ONEPLUSNOTE3"]
        self.price_ONEPLUSNOTE1 = 10000
        self.price_ONEPLUSNOTE2 = 20000
        self.price_ONEPLUSNOTE3 = 30000

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

        lbl_title= Label(self.root,text = "BILLING SOFTWARE USING PYTHON",font = ("times new roman",35,"bold"),bg = "white",fg = "Navy Blue")
        lbl_title.place(x =0,y=130,width =1530, height =45 )

        #Main Frame
        Main_Frame= Frame(self.root,bd = 5,relief = GROOVE,bg = 'white')
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        #Customer Label Frame
        Cust_Frame= LabelFrame(Main_Frame,text="Customer",font =("times New Roman",12,"bold"),bg="white",fg ="red")
        Cust_Frame.place(x=10,y=5,width =350,height =140)
        
        #Mobile
        self.lbl_cus_mob = Label(Cust_Frame, text = "Mobile No.",font =("times New Roman",12,"bold"),bg="white")
        self.lbl_cus_mob.grid(row=0, column=0, stick =W, padx=5, pady=2)
        self.entry_cus_mob= ttk.Entry(Cust_Frame,font =("times New Roman",10,"bold"))
        self.entry_cus_mob.grid(row =0, column =1)

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
        self.lbl_category = Label(Prod_Frame, text = "Select Category",font =("times New Roman",12,"bold"),bd=4,bg="white")
        self.lbl_category.grid(row=0, column=0, stick =W, padx=5, pady=2)
        self.Combo_category = ttk.Combobox(Prod_Frame,font =("times new Roman",10,"bold"),width=24, value = self.Category, state = "readonly")
        self.Combo_category.current(0)
        self.Combo_category.grid(row=0,column=1,stick =W, padx=5, pady=2)
        self.Combo_category.bind("<<ComboboxSelected>>",self.SelectCategories)

        #SubCategory
        self.lbl_sub_category = Label(Prod_Frame, text = "Select Sub Category",font =("times New Roman",12,"bold"),bd=4,bg="white")
        self.lbl_sub_category.grid(row=1, column=0, stick =W, padx=5, pady=2)
        self.Combo_sub_category = ttk.Combobox(Prod_Frame,value = [],font =("times new Roman",10,"bold"),width =24 ,state = "readonly")
        self.Combo_sub_category.grid(row=1,column=1,stick =W, padx=5, pady=2)
        self.Combo_sub_category.bind("<<ComboboxSelected>>",self.SelectSubCategories)

        #Product Name
        self.lbl_prod_name = Label(Prod_Frame, text = "Select Product",font =("times New Roman",12,"bold"),bd=4,bg="white")
        self.lbl_prod_name.grid(row=2, column=0, stick =W, padx=5, pady=2)
        self.Combo_prod_name = ttk.Combobox(Prod_Frame,value=[],font =("times new Roman",10,"bold"),  width = 24,state = "readonly")
        self.Combo_prod_name.grid(row=2,column=1,stick =W, padx=5, pady=2)
        self.Combo_prod_name.bind("<<ComboboxSelected>>",self.SelectPrice)

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
        scroll_y.config(command = self.textarea.yview)
        self.textarea.pack(fill=BOTH, expand =1)

        #Bill Counter Label Frame
        Bottom_Frame= LabelFrame(Main_Frame,text="BILL COUNTER",font =("times new Roman",12,"bold"),bg="white",fg ="red")
        Bottom_Frame.place(x=0,y=485,width =1520,height =140)

        #Subtotal
        self.lbl_Subtotal= Label(Bottom_Frame,text= "Sub Total", font = ("times new Roman",12,"bold"),bd = 4, bg = "white")
        self.lbl_Subtotal.grid(row=0, column=0, stick =W, padx=5, pady=2)
        self.entry_Subtotal= ttk.Entry(Bottom_Frame,font =("times New Roman",10,"bold"), width =26)
        self.entry_Subtotal.grid(row =0, column =1, stick = W, padx=5 , pady=2)

        #Adding Taxes
        self.lbl_tax= Label(Bottom_Frame,text= "Govt. Taxes", font = ("times new Roman",12,"bold"),bd = 4, bg = "white")
        self.lbl_tax.grid(row=1, column=0, stick =W, padx=5, pady=2)
        self.entry_tax= ttk.Entry(Bottom_Frame,font =("times New Roman",10,"bold"), width =26)
        self.entry_tax.grid(row =1, column =1, stick = W, padx=5 , pady=2)

        #Adding Total
        self.lbl_totalamount= Label(Bottom_Frame,text= "Total", font = ("times new Roman",12,"bold"),bd = 4, bg = "white")
        self.lbl_totalamount.grid(row=2, column=0, stick =W, padx=5, pady=2)
        self.entry_totalamount= ttk.Entry(Bottom_Frame,font =("times New Roman",10,"bold"), width =26)
        self.entry_totalamount.grid(row =2, column =1, stick = W, padx=5 , pady=2)

        #Button Frame
        Btn_Frame =  Frame(Bottom_Frame,bd = 2, bg = "white")
        Btn_Frame.place(x=320,y=0)
       
        #AddToCartButton
        self.Btn_AddToCart = Button(Btn_Frame, text="Add to Cart", font =("Arial",15,"bold"),bg ="Navy Blue", fg = "grey",width=15,cursor ="hand2")
        self.Btn_AddToCart.grid(row =0, column=0)

        self.Btn_GenerateBill = Button(Btn_Frame, text="Generate Bill",font =("Arial",15,"bold"),bg ="Navy Blue", fg ="grey",width=15,cursor ="hand2")
        self.Btn_GenerateBill.grid(row =0, column=1)

        self.Btn_SaveBill = Button(Btn_Frame, text="Save Bill",font =("Arial",15,"bold"),bg ="Navy Blue", fg ="grey",width=15,cursor ="hand2")
        self.Btn_SaveBill.grid(row =0, column=2)

        self.Btn_Print = Button(Btn_Frame, text= "Print",font =("Arial",15,"bold"),bg ="Navy Blue", fg ="grey",width=15,cursor = "hand2")
        self.Btn_Print.grid(row =0, column=3)

        self.Btn_Clear = Button(Btn_Frame, text= "Clear",font =("Arial",15,"bold"),bg ="Navy Blue", fg ="grey",width=15,cursor = "hand2")
        self.Btn_Clear.grid(row =0, column=4)

        self.Btn_Exit = Button(Btn_Frame, text= "Exit",font =("Arial",15,"bold"),bg ="Navy Blue", fg ="grey",width=15,cursor = "hand2")
        self.Btn_Exit.grid(row =0, column=5)

        #Search
        Search_Frame = Frame(Main_Frame,bd =2 ,bg = "white")
        Search_Frame.place(x =1000,y=10, width = 500, height = 40)

        self.lbl_Bill = Label(Search_Frame,font =("Arial",10,"bold"), text= "BILL NUMBER", bg = "Navy Blue", fg="Grey")
        self.lbl_Bill.grid(row=0,column=0,sticky=W,padx=1)

        self.txt_BillEntrySearch= ttk.Entry(Search_Frame,font =("Arial",10,"bold"), width=24)
        self.txt_BillEntrySearch.grid(row=0,column=1,sticky=W,padx=1)

        self.Btn_Search = Button(Search_Frame, text= "SEARCH", font =("Arial",10,"bold"),bg = "Navy Blue", fg = "grey",width=9,cursor = "hand2")
        self.Btn_Search.grid(row =0, column=2,sticky=W,padx=1, pady=1)

        #MIDDLE FRAME
        Middle_Frame = Frame(Main_Frame, bd =10)
        Middle_Frame.place(x=10,y=150, width = 980, height =325)

        img4 = Image.open("images/4.jpg")
        img4= img4.resize((490,325),Image.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)
        lbl_image4= Label(Middle_Frame,image= self.photoimg4)
        lbl_image4.place(x=0,y=0,width=485,height =325)

        img5 = Image.open("images/5.jpg")
        img5= img5.resize((490,325),Image.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)
        lbl_image5= Label(Middle_Frame,image= self.photoimg5)
        lbl_image5.place(x=500,y=0,width=485,height =325)

    def SelectCategories(self,event=""):
        subcat_variable = "SubCat_"+self.Combo_category.get()
        self.Combo_sub_category.config(value =getattr(self, subcat_variable))
        self.Combo_sub_category.current(0)
    
    def SelectSubCategories(self,event=""):
        product_variable = self.Combo_sub_category.get()
        self.Combo_prod_name.config(value =getattr(self, product_variable))
        self.Combo_prod_name.current(0)
    
    def SelectPrice(self,event=""):
        product_price = "price_"+self.Combo_prod_name.get()
        self.ComboPrice.config(value = getattr(self,product_price) )
        self.ComboPrice.current(0)
        self.qty.set(1)

if __name__== '__main__':
    root=Tk()
    obj = Bill_App(root)
    root.mainloop()