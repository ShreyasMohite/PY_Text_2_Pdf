from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
from fpdf import FPDF 


class PDF2TXT:
    def __init__(self,root):
        self.root=root
        self.root.title("PDF 2 TXT")
        self.root.geometry("400x300")
        self.root.iconbitmap("logo451.ico")
        self.root.resizable(0,0)


        save=StringVar()
        path=StringVar()




        def on_enter1(e):
            but_Convert_text['background']="black"
            but_Convert_text['foreground']="cyan"
            
            

        def on_leave1(e):
            but_Convert_text['background']="SystemButtonFace"
            but_Convert_text['foreground']="SystemButtonText"


        def on_enter2(e):
            but_browse['background']="black"
            but_browse['foreground']="cyan"
            
            

        def on_leave2(e):
            but_browse['background']="SystemButtonFace"
            but_browse['foreground']="SystemButtonText"


        def on_enter3(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave3(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"

        
        def clear():
            path.set("")
            save.set("")

        
        def browse():
            global filename
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("Text FILES","*.txt"),("all files","*.*"))) 
            path.set(file_path)


        def convert_pdf():
            if path.get()!="":
                if save.get()!="":
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size = 15)
                    f = open(path.get(), "r")
                    for x in f: 
                        pdf.cell(200, 10, txt = x, ln = 1, align = 'C')
                    pdf.output("{}.pdf".format(save.get())) 
                    

                   
                        
                else:
                    tkinter.messagebox.showerror("Error","Please Enter File name for save")
            else:
                tkinter.messagebox.showerror("Error","Path is not available")
            



#=====================frame======================================================#

        mainframe=Frame(self.root,width=400,height=300,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=394,height=250,relief="ridge",bd=3,bg="#48adf9")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=394,height=43,relief="ridge",bd=3,bg="#008c8c")
        secondframe.place(x=0,y=250)

#========================firstframe----------------------------------------------------------$
        but_browse=Button(firstframe,text="Browse TEXT",width=16,font=('times new roman',12),cursor="hand2",command=browse)
        but_browse.place(x=110,y=20)
        but_browse.bind("<Enter>",on_enter2)
        but_browse.bind("<Leave>",on_leave2)

        lab_path=Label(firstframe,text="Path",font=('times new roman',12),bg="#48adf9",fg="white")
        lab_path.place(x=170,y=70)

        ent_path=Entry(firstframe,width=43,relief="ridge",bd=3,font=('times new roman',12),textvariable=path)
        ent_path.place(x=20,y=100)


        lab_save=Label(firstframe,text="Save as Name",font=('times new roman',12),bg="#48adf9",fg="white")
        lab_save.place(x=10,y=160)


        ent_save=Entry(firstframe,width=20,relief="ridge",bd=3,font=('times new roman',12),textvariable=save)
        ent_save.place(x=130,y=160)
        

#=======================secondframe===========================================================#
        
        but_Convert_text=Button(secondframe,text="Convert PDF",width=16,font=('times new roman',12),cursor="hand2",command=convert_pdf)
        but_Convert_text.place(x=20,y=1)
        but_Convert_text.bind("<Enter>",on_enter1)
        but_Convert_text.bind("<Leave>",on_leave1)


        but_clear=Button(secondframe,text="Clear",width=16,font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=210,y=1)
        but_clear.bind("<Enter>",on_enter3)
        but_clear.bind("<Leave>",on_leave3)







if __name__ == "__main__":
    root=Tk()
    app=PDF2TXT(root)
    root.mainloop()





