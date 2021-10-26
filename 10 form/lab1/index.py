import tkinter as tk

def show_slipknot():
    w = tk.Toplevel()
    w.geometry('800x500')
    w.title('Slipknot')

    s="Slipknot — американський ню-метал гурт, створений у 1995 році в Де-Мойн (штат Айова) барабанщиком Джої Джордісоном, \n\
    басистом Полом Греєм та перкусіоністом Шоном Креханом. \n\
    Гурт відомий своїм провокаційним іміджем, який дуже добре привертає увагу,\n\
    агресивною музикою та скандальними концертами. Група стрімко здобула славу після випуску свого\n\
    однойменного дебютного альбому в 1999 році. Наступний альбом «Iowa», який вийшов у 2001 році зробив групу ще популярнішою.\n\
    Після короткої перерви група повернулась в 2004 році з альбомом «Vol. 3: (The Subliminal Verses)». В 2008 році з четвертим \n\
    альбомом «All Hope Is Gone», який дебютував на першому місці в чарті «Billboard 200». Після смерті Грея та звільнення\n\
    Джордісона виходить у 2014 році п'ятий альбом «.5: The Gray Chapter».\n\
    А у 2019 році виходить альбом «We Are Not Your Kind»."

    image = tk.PhotoImage(file="10 form\lab1\slipknot.png")
    image_label = tk.Label(w, image=image)
    image_label.grid(row=0,column=0)

    t = tk.Label(w, text=s)
    t.grid(row=1,column=0,pady=5)

    w.mainloop()

def show_soad():
    w = tk.Toplevel()
    w.geometry('800x500')
    w.title('System of a Down')

    s="System of a Down (акронім SOAD, іноді трапляється скорочення System) — відомий американський (всі учасники гурту \n\
    вірменського походження) метал-гурт з Лос-Анджелеса, лауреат премії Grammy. На початку своєї кар'єри музиканти виконували \n\
    музику в стилі ню-метал, однак зараз\n\
    певного стилю їх музика не має. Гурт був заснований у 1995 році, колишніми учасниками каліфорнійського гурту Soil.\n\
    Всі члени групи мають вірменське походження. System of a Down складається з Сержа Танкяна, \n\
    Джона Долмаяна, Шаво Одадж'яна та Дарона Малакяна.\n\
    З 1998 по 2005 рік, гурт випустив п'ять студійних альбомів. Найуспішнішим став другий альбом — Toxicity — який \n\
    розійшовся по світу 6-мільйонним тиражем, а у США став мультиплатиновим. Загальний тираж проданих записів гурту \n\
    сягає 20 мільйонів екземплярів." 

    image = tk.PhotoImage(file="10 form\lab1\soad.png")
    image_label = tk.Label(w, image=image)
    image_label.grid(row=0,column=0)

    t = tk.Label(w, text=s)
    t.grid(row=1,column=0,pady=5)

    w.mainloop()

def show_antihype():
    w = tk.Toplevel()
    w.geometry('700x500')
    w.title('Antihype')

    s="Antihype — об'єднання виконавців епохи постмодерну. Головні члени: Слава КПСС ака Гнойный ака \n\
    Соня Мармеладова aka Валентин Дядька aka Птичий Пепел і Хан Замай. Стиль — реп. Ідеологія — панк." 

    image = tk.PhotoImage(file="10 form\lab1\\antihype.png")
    image_label = tk.Label(w, image=image)
    image_label.grid(row=0,column=0)

    t = tk.Label(w, text=s)
    t.grid(row=1,column=0,pady=5)

    w.mainloop()

def show_grob():
    w = tk.Toplevel()
    w.geometry('700x500')
    w.title('Antihype')

    s="«Гражданская оборона» — радянський та російський рок-гурт, заснований 8 листопада 1984 в Омську Єгором Лєтовим\n\
        і Костянтином Рябиновим, найбільш помітний представник сибірського панк-року. Музика \n\
        колективу на початковому етапі являла собою панк-рок з сильним гаражним впливом, що \n\
        зберігався протягом творчої діяльності гурту, а в 1990-х роках її стилістика змістилася в\n\
        бік психоделічного року. «Гражданская оборона» була однією з найвпливовіших панк-рок-гуртів СРСР\n\
        і Росії. Гурт розпався в 2008 році після загибелі Єгора Лєтова. " 

    image = tk.PhotoImage(file="10 form\lab1\gr-oborona.png")
    image_label = tk.Label(w, image=image)
    image_label.grid(row=0,column=0)

    t = tk.Label(w, text=s)
    t.grid(row=1,column=0,pady=5)

    w.mainloop()

root = tk.Tk()
root.title('Петухон — топ')
root.geometry('800x600')

text = tk.Label(root, text='Мої улюбленні виконавці', font='20')
text.grid(row=0,column=0, columnspan=3)

b1 = tk.Button(text="Slipknot", width=15, height=3, command=show_slipknot)
b1.grid(row=1,column=0)
b2 = tk.Button(text="System Of a Down", width=15, height=3, command=show_soad)
b2.grid(row=1,column=1)
b3 = tk.Button(text="Antihype", width=15, height=3, command=show_antihype)
b3.grid(row=1,column=2)
b4 = tk.Button(text="ГрОб", width=15, height=3, command=show_grob)
b4.grid(row=1,column=3)

root.mainloop()