from tkinter import *
import os
from tkinter import ttk
from tkinter import messagebox 
from Login import Login



def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Silahkan Login").pack()
    Label(login_screen, text="").pack()
 
    global nama_verify
    global umur_verify
 
    nama_verify = StringVar()
    umur_verify = StringVar()
 
    global nama_login_entry
    global umur_login_entry
 
    Label(login_screen, text="Nama").pack()
    nama_login_entry = Entry(login_screen, textvariable=nama_verify)
    nama_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Umur").pack()
    umur_login_entry = Entry(login_screen, textvariable=umur_verify)
    umur_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=17, height=1, command = login_sucess).pack()

def login_sucess():
    global login_sucess_screen
    login_sucess_screen = Toplevel(login_screen)
    login_sucess_screen.title("Login berhasil")
    login_sucess_screen.geometry("150x100")
    Label(login_sucess_screen, text="Login berhasil").pack()
    Button(login_sucess_screen, text="OK", command=utama).pack() 



def utama():
    global utama_screen
    global e
    global clicked
    utama_screen = Toplevel(login_sucess_screen)
    utama_screen.geometry("1000x300")
    utama_screen.title("Program Penyewaan Apartement")
    clicked = StringVar()
    e = IntVar()
    drop = OptionMenu(utama_screen, clicked, "Tipe 1", "Tipe 2", "Tipe 3", "Tipe 4", "Tipe 5")
    drop.place(x=10, y=50)

    e = Entry(utama_screen, width=20)
    e.place(x=10, y=100)

    button1 = Button(utama_screen, text = "Pesan", command=hasil_pesanan)
    button1.place(x=10, y=150)

    label2 = Label(utama_screen, text = "Silahkan Pilih Tipe Apartement")
    label3 = Label(utama_screen, text = "Masukkan untuk Berapa Bulan")
    label6 = Label(utama_screen, text = "Pilihan tipe : ")
    label7 = Label(utama_screen, text = "Tipe 1 : Kamar utama,Ruang,Dapur,kamar mandi = Rp2.700.000/Bulan")
    label8 = Label(utama_screen, text = "Tipe 2 : Kamar utama,Ruang keluarga,Dapur,Kamar mandi 2 = Rp3.000.000/Bulan")
    label9 = Label(utama_screen, text = "Tipe 3 : Kamar utama+ 1 kamar tidur,Ruang keluaga, Dapur,Kamar mandi 2 = Rp4.500.000/Bulan")
    label11 = Label(utama_screen, text = "Tipe 4 : Kamar utama+ 2 kamar tidur,Ruang keluarga,Dapur,Kamar mandi 2 = Rp6.000.000/Bulan")
    label12 = Label(utama_screen, text = "Tipe 5 : Kamar utama+ 3 kamar tidur,Ruang keluarga,Dapur,Kamar mandi 2,akses vip swim pool = Rp10.000.000/Bulan")

    label2.place(x=10, y=30)
    label3.place(x=10, y=80)
    label6.place(x=350, y=30)
    label7.place(x=350, y=50)
    label8.place(x=350, y=70)
    label9.place(x=350, y=90)
    label11.place(x=350, y=110)
    label12.place(x=350, y=130)

    
        

    def waktu():
        int(e.get())
        bln = e.get()
        apr = clicked.get()
    
def hasil_pesanan():
   try:
    global hasil_pesanan_screen
    hasil_pesanan_screen = Toplevel(login_sucess_screen)
    hasil_pesanan_screen.geometry("1000x50")
    hasil_pesanan_screen.title("Hasil Penyewaan Apaartement")    
    e_e = e.get()
    clicked_clicked = clicked.get()
    int(e.get())
    bln = e.get()
    apr = clicked.get()
    keluar = Login(clicked.get(), e.get(), "")
    keluar.hasil_set()
    Label(hasil_pesanan_screen, text=keluar.hasil_get()).pack()
   except :
       messagebox.showwarning("Error", "anda belum mengisi tipe apartement/jumlah bulan untuk di sewa")
       return
    

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Program Penyewaan Apartement")
    Label(text="Menu Utama", bg="cyan", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
 
    main_screen.mainloop()

main_account_screen()
