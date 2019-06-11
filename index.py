from tkinter import Tk,Label,Button

class Kutuphane:

    def __init__(self,anaSayfa):

        self.anasayfa = anaSayfa
        anaSayfa.title("Kütüphane kataloğu")

        anaSayfa.configure(background="purple")
        anaSayfa.geometry("400x400")



        self.etiket = Label(anaSayfa, text="İSTEDİĞİNİZ KİTABI ARAMAK İÇİN -ARA- BUTONUNA BASINIZ")
        self.etiket.grid()

        self.istek = Button(anaSayfa, text="ARA",command=self.yazdir)
        self.istek.grid()


        self.kapatButonu = Button(anaSayfa, text="Kapat", command=anaSayfa.quit)
        self.kapatButonu.grid()



    def yazdir(self):
        with open("C:\\cansel\\katalog.txt") as kitaparama:
            found = False
            while not found:
                b = str(input('Aramak istediğiniz kitabın adını yazınız: '))
                if b == '':
                    break  # allow the search-loop to quit on no input
                for line in kitaparama:
                    if b in line:
                        print(line)
                        found = True
                        break
                else:
                    print("Aradığınız kitap kütüphane koleksiyonumuz da yok")
                    kitaparama.seek(0)  # reset file to the beginning for next search

        kitaparama.close()


root = Tk()
yeniPencere = Kutuphane(root)
root.mainloop()
