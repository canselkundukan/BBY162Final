from tkinter import *

class Kutuphane:
    def __init__(self,anaSayfa):

        global  kitapadi, kitapAlani
        global yazarAlani, yazaradi
        global yilAlani, yil_Alani
        self.anasayfa = anaSayfa
        anaSayfa.title("Kütüphane kataloğu")

        anaSayfa.configure(background="purple")
        anaSayfa.geometry("400x600")

        kitapadi = ["gözlerini sımsıkı kapat","dönüşüm","geçmişe yolculuk","kürk mantolu madonna","simyacı"]
        yazaradi = ["john verdon", "franz kafka","stefan zweig","sabahattin ali","paulo coelho"]
        yil_Alani = ["2012","1915","1976","1943","1996"]




        istek = Label(anaSayfa, text=" Kitap Adı Giriniz:", bg="purple", fg="white").grid()
        kitapAlani = Entry()
        kitapAlani.grid()
        taraBut = Button(anaSayfa, text="ARA", bg="white", fg="black",font=("calibri", 12), command=self.gir1).grid()


        istek = Label(anaSayfa, text="Yazar Adı Giriniz:", bg="purple", fg="white").grid()
        yazarAlani = Entry()
        yazarAlani.grid()
        taraBut = Button(anaSayfa, text="ARA", bg="white", fg="black" ,font=("calibri", 12), command=self.gir2).grid()



        istek = Label(anaSayfa, text="Kitabın yayın yılını giriniz:", bg="purple", fg="white").grid()
        yilAlani = Entry()
        yilAlani.grid()
        taraBut = Button(anaSayfa, text="ARA", bg="white", fg="black", font=("calibri", 12), command=self.gir3).grid()



    def gir3(self):
        ayad= yilAlani.get()
        if ayad==yil_Alani[0]:

            ab=Label(root,text="KİTAP ADI:Gözlerini Sımsıkı Kapat \n YAZAR ADI:John Verdon\n Yayın Yılı:2012", bg="purple",fg="white").grid()


        elif  ayad==yil_Alani[1]:
            bb = Label(root,text="KİTAP ADI:Dönüşüm \n YAZAR ADI:Franz Kafka \n Yayın Yılı: 1915", bg="purple",fg="white").grid()


        elif  ayad==yil_Alani[2]:
            cb = Label(root,text="KİTAP ADI:Geçmişe Yolculuk \n YAZAR ADI: Stefan Zweig \n Yayın Yılı: 1976",bg="purple", fg="white").grid()

        elif ayad==yil_Alani[3]:
            db = Label(root,text="KİTAP ADI:Kürk Mantolu Madonna \n YAZAR ADI:Sbahattin Ali \n Yayın Yılı:1943",bg="purple", fg="white").grid()
        elif ayad==yil_Alani[4]:
            eb = Label(root,text="KİTAP ADI:Simyacı \n YAZAR ADI:Paulo Coelho \n Yayın Yılı: 1996",bg="purple", fg="white").grid()

        else :
            fb = Label(root,text="Aradığınız kitap kütüphane koleksiyonumuzda yok..." , bg="purple",fg="white").grid()
    def gir2(self):
        yad= yazarAlani.get()
        if yad==yazaradi[0]:

            ab=Label(root,text="KİTAP ADI: Gözlerini Sımsıkı Kapat \n YAZAR ADI:John Verdon \n TÜR:ROMAN \n YAYIN YILI:2012", bg="purple",fg="white").grid()


        elif yad==yazaradi [1]:
            bb = Label(root,text="KİTAP ADI: Dönüşüm \n YAZAR ADI:Franz Kafka \n TÜR:ROMAN \n YAYIN YILI:1915", bg="purple",fg="white").grid()



        elif yad== yazaradi[2]:
            cb = Label(root,text="KİTAP ADI: Geçmişe Yolculuk \n YAZAR ADI: Stefan Zweig \n TÜR:ROMAN \n YAYIN YILI:1976",bg="purple", fg="white").grid()

        elif yad==yazaradi[3]:
            db = Label(root,text="KİTAP ADI:Kürk Mantolu Madonna \n YAZAR ADI:Sabahattin Ali \n TÜR:ROMAN \n YAYIN YILI:1943",bg="purple", fg="white").grid()

        elif yad==yazaradi[4]:
            eb = Label(root,text="KİTAP ADI: Simyacı \n YAZAR ADI: Paulo Coelho \n TÜR: ROMAN \n YAYIN YILI:1996", bg="purple",fg="white").grid()
        else :
            fb = Label(root,text="Aradığınız kitap kütüphane koleksiyonumuzda yok..." , bg="purple",fg="white", font=("calibri", 12)).grid()

    def gir1(self):
        ad = kitapAlani.get()

        if ad == kitapadi[0]:

            ab = Label(root,
                       text="KİTAP ADI: Gözlerini Sımsıkı Kapat \n YAZAR ADI:John Verdon \n TÜR:ROMAN \n YAYIN YILI:2012",
                       bg="purple", fg="white").grid()


        elif ad == kitapadi[1]:
            bb = Label(root,
                       text="KİTAP ADI: Dönüşüm \n YAZAR ADI:Franz Kafka \n TÜR:ROMAN \n YAYIN YILI:1915",
                       bg="purple", fg="white").grid()



        elif ad == kitapadi[2]:
            cb = Label(root, text="KİTAP ADI: Geçmişe Yolculuk \n YAZAR ADI: Stefan Zweig \n TÜR:ROMAN \n YAYIN YILI:1976",
                       bg="purple", fg="white").grid()

        elif ad == kitapadi[3]:
            db =Label(root,text="KİTAP ADI: Kürk Mantolu Madonna \n YAZAR ADI: Sabahattin Ali \n TÜR:ROMAN \n YAYIN YILI:1943",
                      bg="purple",fg="white").grid()
        elif ad == kitapadi[4]:
            eb = Label(root, text="KİTAP ADI: Simyacı \n YAZAR ADI:Paulo Coelho \n TÜR:ROMAN \n YAYIN YILI:1996",
                       bg="purple",fg="white").grid()

        else:
            fb = Label(root, text="Aradığınız kitap kütüphane koleksiyonumuzda yok...", bg="purple", fg="white",
                       font=("calibri", 12)).grid()



root = Tk()
yeniPencere = Kutuphane(root)
root.mainloop()
