from tkinter import *
from tkinter.messagebox import *



def presentinc():

    fen5=Tk()
    fen5.title('Present')
    fen5['background']='#324270'

    type1=Frame(fen5, borderwidth=2, relief=GROOVE, bg='#324270')
    type1.pack(side=TOP, padx=5, pady=5)

    Button(type1, text="Auxiliaire", command=presentinaux).pack()
    Button(type1, text="1er groupe", command=presentin1).pack()
    Button(type1, text="2eme groupe", command=presentin2).pack()
    Button(type1, text="3eme groupe", command=presentin3).pack()
    Button(type1, text="Fermer", command=fen5.destroy, background="red").pack()

    fen.mainloop()

def presentin1():
    fen11= Tk()
    fen11.title('Present')

    fen11['background']='light pink'

    prgroupe1ld = Label(fen11, text = "Entrer votre radical:")
    conditionnel = Label(fen11, text = "........................................", background = 'light pink', fg = 'black')

    prgroupe1r = Entry(fen11)
    def prgroupe1a():
        conditionnel['text']=prgroupe1r.get() + "e, es, e, ons, ez, ent"

    def prgroupe1():
        prgroupe1ld.pack()
        prgroupe1r.pack()
        okpr.pack()

    def peser1():
        conditionnel['text']="je pèse, es, e, ons, ez, ent"

    def jeter1():
        conditionnel['text']="je jette, es, e, ons, ez, ent"

    def modeler1():
        conditionnel['text']="je modèle, es, e, ons, ez, ent"

    def broyer1():
        conditionnel['text']="je broie, es, e, nous broyons, ez, ils broient"

    def envoyer1():
        conditionnel['text']="je envois, s, t, nous envoyons, ez, ils envoient"

    frame2copr=Frame(fen11, borderwidth=2, relief = GROOVE, bg='light pink')
    frame2copr.pack(side=TOP, padx=10,pady=10)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okpr=Button(fen11, text = 'Valider', command=prgroupe1a)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'yellow').grid(row=1,column=1)

    Button(frame2copr, text = "Peser", command=peser1, background = 'yellow').grid(row=1,column=2)

    Button(frame2copr, text = "Jeter", command=jeter1, background = 'yellow').grid(row=2,column=1)

    Button(frame2copr, text = "Modeler", command=modeler1, background = 'yellow').grid(row=2,column=2)

    Button(frame2copr, text = "Broyer", command=broyer1, background = 'yellow').grid(row=3,column=1)

    Button(frame2copr, text = "Envoyer", command=envoyer1, background = 'yellow').grid(row=3,column=2)


    conditionnel.pack(side=TOP)
    Button(fen11, text = 'Fermer', command=fen11.destroy, background = 'red').pack(side=TOP)

    fen.mainloop()

def presentin2():
    fen12= Tk()
    fen12.title('Present')

    fen12['background']='#324270'

    degroupe1ld = Label(fen12, text = "Entrer votre radical:")
    conditionnel = Label(fen12, text = "........................................", background = '#324270', fg = 'white')

    degroupe1r = Entry(fen12)
    def degroupe1a():
        conditionnel['text']=degroupe1r.get() + "is, is, it, ons, ez, ent"

    def degroupe1():
        degroupe1ld.pack()
        degroupe1r.pack()
        okde.pack()

    def hair1():
        conditionnel['text']="je hais, s, t, nous haïssons, ez, ent"

    frame1copr=Frame(fen12, borderwidth=2, relief = GROOVE, bg='#324270')
    frame1copr.pack(side=TOP, padx=10,pady=10)

    Button(frame1copr, text = 'Verbe du deuxième groupe', command=degroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okde=Button(fen12, text = 'Valider', command=degroupe1a)
    Button(frame1copr, text = 'Haïr', command=hair1, background = 'black', fg = 'white').grid(row=2,column=1)

    conditionnel.pack(side=TOP)
    Button(fen12, text = 'Fermer', command=fen12.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def presentin3():
    fen13= Tk()
    fen13.title('Present')

    fen13['background']='PaleGreen2'

    conditionnel = Label(fen13, text = "........................................", background = 'PaleGreen2', fg = 'black')

    def aller1():
        conditionnel['text']="je vais, s, t, nous allons, ez, ils vont"

    def tenir1():
        conditionnel['text']="je tiens, s, t, ons, ez, ent"

    def acquerir1():
        conditionnel['text']="j'acquiers, s, t, ons, ez, ent"

    def sentir1():
        conditionnel['text']="je sentis, s, t, ons, ez, ent"

    def vetir1():
        conditionnel['text']="je vêtis, s, t, ons, ez, ent"

    def couvrir1():
        conditionnel['text']="je couvre, e, t, ons, ez, ent"

    def ceuillir1():
        conditionnel['text']="je cueilles, s, t, ons, ez, ent"

    def assaillir1():
        conditionnel['text']="je assaillis, s, t, ons, ez, ent"

    def faillir1():
        conditionnel['text']="je faus, s, t, nous faillons, ez, issent"

    def bouillir1():
        conditionnel['text']="je bous, s, t, nous bouillons, ez, ils bouent"

    def dormir1():
        conditionnel['text']="je dormis, s, t, ons, ez, ent"

    def courir1():
        conditionnel['text']="je cours, s, t, ons, ez, ent"

    def mourir1():
        conditionnel['text']="je meurs, s, t, nous mourrons, ez, ils meurrent"

    def servir1():
        conditionnel['text']="je sers, s, t, vons, vez, vent"

    def fuir1():
        conditionnel['text']="je fuis, s, t, nous fuiyons, ez, ils fuient"

    def recevoir1():
        conditionnel['text']="je reçois, s, t, nous recevons, ez, ils reçoient"

    def voir1():
        conditionnel['text']="je vois, s, t, nous voyons, ez, ils voient"

    def savoir1():
        conditonnel['text']="je sais, s, t, ons, ez, ent"

    def devoir1():
        conditionnel['text']="je dois, s, t, ons, ez, ent"

    def pouvoir1():
        conditionnel['text']="je peux, x, t, ons, ez, ent"

    def vouloir1():
        conditionnel['']="je veux, x, il t, ons, ez, ent"

    def rendre1():
        conditionnel['text']="je rends, s, t, ons, ez, ent"

    def prendre1():
        conditionnel['text']="je prends, s, t, ons, ez, ent"

    def battre1():
        conditionnel['text']="je bats, s, t, ons, ez, ent"

    def mettre1():
        conditionnel['text']="je mets, s, t, ons, ez, ent"

    def peindre1():
        conditionnel['text']="je peins, s, t, ons, ez, ent"

    def joindre1():
        conditionnel['text']="je joinds, s, t, ons, ez, ent"

    def craindre1():
        conditionnel['text']="je crainds, s, t, ons, ez, ent"

    def vaincre1():
        conditionnel['text']="je vaincs, s, t, ons, ez, ent"

    def connaitre1():
        conditionnel['text']="je connais, s, t, ons, ez, ent"

    def croire1():
        conditionnel['text']="je crois, s, t, ons, ez, ent"

    def boire1():
        conditionnel['text']="je bois, s, t, ons, ez, ent"

    def conclure1():
        conditionnel['text']="je conclus, s, t, ons, ez, ent"

    def coudre1():
        conditionnel['text']="je couds, s, t, ons, ez, ent"

    def suivre1():
        conditionnel['text']="je suis, s, t, ons, ez, ent"

    def vivre1():
        conditionnel['text']="je vis, s, t, ons, ez, ent"

    def lire1():
        conditionnel['text']="je lis, s, t, ons, ez, ent"

    def dire1():
        conditionnel['text']="je dis, s, t, ons, ez, ent"

    def rire1():
        conditionnel['text']="je ris, s, t, ons, ez, ent"

    def ecrire1():
        conditionnel['text']="j'écris, s, t, ons, ez, ent"

    def cuire1():
        conditionnel['text']="je cuis, s, t, ons, ez, ent"

    frame3copr=Frame(fen13, borderwidth=2, relief = GROOVE, bg='PaleGreen2')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    Button(frame3copr, text = 'Aller', command=aller1, background = 'cyan').grid(row=1,column=1)

    Button(frame3copr, text = 'Tenir', command=tenir1, background = 'cyan').grid(row=1,column=2)

    Button(frame3copr, text = 'Acquérir', command=acquerir1, background = 'cyan').grid(row=1,column=3)

    Button(frame3copr, text = 'Sentir', command=sentir1, background = 'cyan').grid(row=2,column=1)

    Button(frame3copr, text = 'Vêtir', command=vetir1, background = 'cyan').grid(row=2,column=2)

    Button(frame3copr, text = 'Couvrir', command=couvrir1, background = 'cyan').grid(row=2,column=3)

    Button(frame3copr, text = 'Ceuillir', command=ceuillir1, background = 'cyan').grid(row=3,column=1)

    Button(frame3copr, text = 'Assaillir', command=assaillir1, background = 'cyan').grid(row=3,column=2)

    Button(frame3copr, text = 'Faillir', command=faillir1, background = 'cyan').grid(row=3,column=3)

    Button(frame3copr, text = 'Bouillir', command=bouillir1, background = 'cyan').grid(row=4,column=1)

    Button(frame3copr, text = 'Dormir', command=dormir1, background = 'cyan').grid(row=4,column=2)

    Button(frame3copr, text = 'Courir', command=courir1, background = 'cyan').grid(row=4,column=3)

    Button(frame3copr, text = 'Mourir', command=mourir1, background = 'cyan').grid(row=5,column=1)

    Button(frame3copr, text = 'Servir', command=servir1, background = 'cyan').grid(row=5,column=2)

    Button(frame3copr, text = 'Fuir', command=fuir1, background = 'cyan').grid(row=5,column=3)

    Button(frame3copr, text = 'Recevoir', command=recevoir1, background = 'cyan').grid(row=6,column=1)

    Button(frame3copr, text = 'Voir', command=voir1, background = 'cyan').grid(row=6,column=2)

    Button(frame3copr, text = 'Savoir', command=savoir1, background = 'cyan').grid(row=6,column=3)

    Button(frame3copr, text = 'Devoir', command=devoir1, background = 'cyan').grid(row=7,column=1)

    Button(frame3copr, text = 'Pouvoir', command=pouvoir1, background = 'cyan').grid(row=7,column=2)

    Button(frame3copr, text = 'Vouloir', command=vouloir1, background = 'cyan').grid(row=7,column=3)

    Button(frame3copr, text = 'Rendre', command=rendre1, background = 'cyan').grid(row=8,column=1)

    Button(frame3copr, text = 'Prendre', command=prendre1, background = 'cyan').grid(row=8,column=2)

    Button(frame3copr, text = 'Battre', command=battre1, background = 'cyan').grid(row=8,column=3)

    Button(frame3copr, text = 'Mettre', command=mettre1, background = 'cyan').grid(row=9,column=1)

    Button(frame3copr, text = 'Peindre', command=peindre1, background = 'cyan').grid(row=9,column=2)

    Button(frame3copr, text = 'Joindre', command=joindre1, background = 'cyan').grid(row=9,column=3)

    Button(frame3copr, text = 'Craindre', command=craindre1, background = 'cyan').grid(row=10,column=1)

    Button(frame3copr, text = 'Vaincre', command=vaincre1, background = 'cyan').grid(row=10,column=2)

    Button(frame3copr, text = 'Connaître', command=connaitre1, background = 'cyan').grid(row=10,column=3)

    Button(frame3copr, text = 'Croire', command=croire1, background = 'cyan').grid(row=11,column=1)

    Button(frame3copr, text = 'Boire', command=boire1, background = 'cyan').grid(row=11,column=2)

    Button(frame3copr, text = 'Conclure', command=conclure1, background = 'cyan').grid(row=11,column=3)

    Button(frame3copr, text = 'Coudre', command=coudre1, background = 'cyan').grid(row=12,column=1)

    Button(frame3copr, text = 'Suivre', command=suivre1, background = 'cyan').grid(row=12,column=2)

    Button(frame3copr, text = 'Vivre', command=vivre1, background = 'cyan').grid(row=12,column=3)

    Button(frame3copr, text = 'Lire', command=lire1, background = 'cyan').grid(row=13,column=1)

    Button(frame3copr, text = 'Dire', command=dire1, background = 'cyan').grid(row=13,column=2)

    Button(frame3copr, text = 'Rire', command=rire1, background = 'cyan').grid(row=13,column=3)

    Button(frame3copr, text = 'Ecrire', command=ecrire1, background = 'cyan').grid(row=14,column=1)

    Button(frame3copr, text = 'Cuire', command=cuire1, background = 'cyan').grid(row=14,column=2)

    conditionnel.pack(side=TOP)

    Button(fen13, text = 'Fermer', command=fen13.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def presentinaux():
    fen2 = Tk()
    fen2.title('Present')

    fen2['background']='PaleTurquoise3'

    #Label des résultats

    conditionnel = Label(fen2, text = "........................................", background = 'PaleTurquoise3', fg = 'black')


    #Définition des verbes

    def etre1() :
        conditionnel['text']="suis, es, est, sommes, etes, sont"

    def avoir1() :
        conditionnel['text']="ai, as, a, avons, avez, ont"


    #champs des verbe

    conditionnel.pack(side=TOP)

    #auxiliaire


    frame3copr=Frame(fen2, borderwidth=2, relief = GROOVE, background='PaleTurquoise3')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    etre=Button(frame3copr, text = 'Etre', command=etre1, fg = 'white', background = 'green').grid(row=0,column=1)

    Button(frame3copr, text = 'Avoir', command=avoir1, fg = 'white', background = 'green').grid(row=1,column=1)





    #bouton fermer
    Button(fen2, text = 'Fermer', command=fen2.destroy, background = 'red').pack(side=BOTTOM)





    fen.mainloop()



def futurinc():
    fen5=Tk()
    fen5.title('Futur')

    fen5['background']='#324270'

    type1=Frame(fen5, borderwidth=2, relief=GROOVE, bg='#324270')
    type1.pack(side=TOP, padx=5, pady=5)

    Button(type1, text="Auxiliaire", command=futurinaux).pack()
    Button(type1, text="1er groupe", command=futurin1).pack()
    Button(type1, text="2eme groupe", command=futurin2).pack()
    Button(type1, text="3eme groupe", command=futurin3).pack()
    Button(type1, text="Fermer", command=fen5.destroy, background="red").pack()

    fen.mainloop()

def futurin1():
    fen11= Tk()
    fen11.title('Futur')

    fen11['background']='light pink'

    prgroupe1ld = Label(fen11, text = "Entrer votre radical:")
    conditionnel = Label(fen11, text = "........................................", background = 'light pink', fg = 'black')

    prgroupe1r = Entry(fen11)
    def prgroupe1a():
        conditionnel['text']=prgroupe1r.get() + "ai, as, a, ons, ez, ont"

    def prgroupe1():
        prgroupe1ld.pack()
        prgroupe1r.pack()
        okpr.pack()

    def peser1():
        conditionnel['text']="je pèserai, as, a, ons, ez, ont"

    def jeter1():
        conditionnel['text']="je jetterai, as, a, ons, ez, ont"

    def modeler1():
        conditionnel['text']="je modèlerai, as, a, ons, ez, ont"

    def broyer1():
        conditionnel['text']="je broierai, as, a, ons, ez, ont"

    def envoyer1():
        conditionnel['text']="je enverrai, as, a, ons, ez, ont"

    frame2copr=Frame(fen11, borderwidth=2, relief = GROOVE, bg='light pink')
    frame2copr.pack(side=TOP, padx=10,pady=10)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okpr=Button(fen11, text = 'Valider', command=prgroupe1a)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'yellow').grid(row=1,column=1)

    Button(frame2copr, text = "Peser", command=peser1, background = 'yellow').grid(row=1,column=2)

    Button(frame2copr, text = "Jeter", command=jeter1, background = 'yellow').grid(row=2,column=1)

    Button(frame2copr, text = "Modeler", command=modeler1, background = 'yellow').grid(row=2,column=2)

    Button(frame2copr, text = "Broyer", command=broyer1, background = 'yellow').grid(row=3,column=1)

    Button(frame2copr, text = "Envoyer", command=envoyer1, background = 'yellow').grid(row=3,column=2)


    conditionnel.pack(side=TOP)
    Button(fen11, text = 'Fermer', command=fen11.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def futurin2():
    fen12= Tk()
    fen12.title('Futur')

    fen12['background']='#324270'

    degroupe1ld = Label(fen12, text = "Entrer votre radical:")
    conditionnel = Label(fen12, text = "........................................", background = '#324270', fg = 'white')

    degroupe1r = Entry(fen12)
    def degroupe1a():
        conditionnel['text']=degroupe1r.get() + "irai, iras, ira, irons, irez, iront"

    def degroupe1():
        degroupe1ld.pack()
        degroupe1r.pack()
        okde.pack()

    def hair1():
        conditionnel['text']="je haïrai, as, a, ons, ez, ont"

    frame1copr=Frame(fen12, borderwidth=2, relief = GROOVE, bg='#324270')
    frame1copr.pack(side=TOP, padx=10,pady=10)

    Button(frame1copr, text = 'Verbe du deuxième groupe', command=degroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okde=Button(fen12, text = 'Valider', command=degroupe1a)
    Button(frame1copr, text = 'Haïr', command=hair1, background = 'black', fg = 'white').grid(row=2,column=1)

    conditionnel.pack(side=TOP)
    Button(fen12, text = 'Fermer', command=fen12.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def futurin3():
    fen13= Tk()
    fen13.title('Futur')

    fen13['background']='PaleGreen2'

    conditionnel = Label(fen13, text = "........................................", background = 'PaleGreen2', fg = 'black')

    def aller1():
        conditionnel['text']="j'irai, as, a, ons, ez, ont"

    def tenir1():
        conditionnel['text']="je tiendrai, as, a, ons, ez, ont"

    def acquerir1():
        conditionnel['text']="j'acquerrai, as, a, ons, ez, ont"

    def sentir1():
        conditionnel['text']="je sentirai, as, a, ons, ez, ont"

    def vetir1():
        conditionnel['text']="je vêtrirai, as, a, ons, ez, ont"

    def couvrir1():
        conditionnel['text']="je couvrirai, as, a, ons, ez, ont"

    def ceuillir1():
        conditionnel['text']="je cueillerai, as, a, ons, ez, ont"

    def assaillir1():
        conditionnel['text']="je assaillirai, as, a, ons, ez, ont"

    def faillir1():
        conditionnel['text']="je faillirai, as, a, ons, ez, ont"

    def bouillir1():
        conditionnel['text']="je boillirai, as, a, ons, ez, ont"

    def dormir1():
        conditionnel['text']="je dormirai, as, a, ons, ez, ont"

    def courir1():
        conditionnel['text']="je courrai, as, a, ons, ez, ont"

    def mourir1():
        conditionnel['text']="je mourrai, as, a, ons, ez, ont"

    def servir1():
        conditionnel['text']="je servirai, as, a, ons, ez, ont"

    def fuir1():
        conditionnel['text']="je fuirai, as, a, ons, ez, ont"

    def recevoir1():
        conditionnel['text']="je recevrai, as, a, ons, ez, ont"

    def voir1():
        conditionnel['text']="je verrai, as, a, ons, ez, ont"

    def savoir1():
        conditonnel['text']="je saurai, as, a, ons, ez, ont"

    def devoir1():
        conditionnel['text']="je devrai, as, a, ons, ez, ont"

    def pouvoir1():
        conditionnel['text']="je pourrai, as, a, ons, ez, ont"

    def vouloir1():
        conditionnel['']="je voudrai, as, a, ons, ez, ont"

    def rendre1():
        conditionnel['text']="je rendrai, as, a, ons, ez, ont"

    def prendre1():
        conditionnel['text']="je prendrai, as, a, ons, ez, ont"

    def battre1():
        conditionnel['text']="je battrai, as, a, ons, ez, ont"

    def mettre1():
        conditionnel['text']="je mettrai, as, a, ons, ez, ont"

    def peindre1():
        conditionnel['text']="je peindrai, as, a, ons, ez, ont"

    def joindre1():
        conditionnel['text']="je joindrai, as, a, ons, ez, ont"

    def craindre1():
        conditionnel['text']="je craindrai, as, a, ons, ez, ont"

    def vaincre1():
        conditionnel['text']="je vaincrai, as, a, ons, ez, ont"

    def connaitre1():
        conditionnel['text']="je connaitrai, as, a, ons, ez, ont"

    def croire1():
        conditionnel['text']="je croirai, as, a, ons, ez, ont"

    def boire1():
        conditionnel['text']="je boirai, as, a, ons, ez, ont"

    def conclure1():
        conditionnel['text']="je conclurai, as, a, ons, ez, ont"

    def coudre1():
        conditionnel['text']="je coudrai, as, a, ons, ez, ont"

    def suivre1():
        conditionnel['text']="je suivrai, as, a, ons, ez, ont"

    def vivre1():
        conditionnel['text']="je vivrai, as, a, ons, ez, ont"

    def lire1():
        conditionnel['text']="je lirai, as, a, ons, ez, ont"

    def dire1():
        conditionnel['text']="je dirai, as, a, ons, ez, ont"

    def rire1():
        conditionnel['text']="je rirai, as, a, ons, ez, ont"

    def ecrire1():
        conditionnel['text']="j'écrirai, as, a, ons, ez, ont"

    def cuire1():
        conditionnel['text']="je cuirai, as, a, ons, ez, ont"

    frame3copr=Frame(fen13, borderwidth=2, relief = GROOVE, bg='PaleGreen2')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    Button(frame3copr, text = 'Aller', command=aller1, background = 'cyan').grid(row=1,column=1)

    Button(frame3copr, text = 'Tenir', command=tenir1, background = 'cyan').grid(row=1,column=2)

    Button(frame3copr, text = 'Acquérir', command=acquerir1, background = 'cyan').grid(row=1,column=3)

    Button(frame3copr, text = 'Sentir', command=sentir1, background = 'cyan').grid(row=2,column=1)

    Button(frame3copr, text = 'Vêtir', command=vetir1, background = 'cyan').grid(row=2,column=2)

    Button(frame3copr, text = 'Couvrir', command=couvrir1, background = 'cyan').grid(row=2,column=3)

    Button(frame3copr, text = 'Ceuillir', command=ceuillir1, background = 'cyan').grid(row=3,column=1)

    Button(frame3copr, text = 'Assaillir', command=assaillir1, background = 'cyan').grid(row=3,column=2)

    Button(frame3copr, text = 'Faillir', command=faillir1, background = 'cyan').grid(row=3,column=3)

    Button(frame3copr, text = 'Bouillir', command=bouillir1, background = 'cyan').grid(row=4,column=1)

    Button(frame3copr, text = 'Dormir', command=dormir1, background = 'cyan').grid(row=4,column=2)

    Button(frame3copr, text = 'Courir', command=courir1, background = 'cyan').grid(row=4,column=3)

    Button(frame3copr, text = 'Mourir', command=mourir1, background = 'cyan').grid(row=5,column=1)

    Button(frame3copr, text = 'Servir', command=servir1, background = 'cyan').grid(row=5,column=2)

    Button(frame3copr, text = 'Fuir', command=fuir1, background = 'cyan').grid(row=5,column=3)

    Button(frame3copr, text = 'Recevoir', command=recevoir1, background = 'cyan').grid(row=6,column=1)

    Button(frame3copr, text = 'Voir', command=voir1, background = 'cyan').grid(row=6,column=2)

    Button(frame3copr, text = 'Savoir', command=savoir1, background = 'cyan').grid(row=6,column=3)

    Button(frame3copr, text = 'Devoir', command=devoir1, background = 'cyan').grid(row=7,column=1)

    Button(frame3copr, text = 'Pouvoir', command=pouvoir1, background = 'cyan').grid(row=7,column=2)

    Button(frame3copr, text = 'Vouloir', command=vouloir1, background = 'cyan').grid(row=7,column=3)

    Button(frame3copr, text = 'Rendre', command=rendre1, background = 'cyan').grid(row=8,column=1)

    Button(frame3copr, text = 'Prendre', command=prendre1, background = 'cyan').grid(row=8,column=2)

    Button(frame3copr, text = 'Battre', command=battre1, background = 'cyan').grid(row=8,column=3)

    Button(frame3copr, text = 'Mettre', command=mettre1, background = 'cyan').grid(row=9,column=1)

    Button(frame3copr, text = 'Peindre', command=peindre1, background = 'cyan').grid(row=9,column=2)

    Button(frame3copr, text = 'Joindre', command=joindre1, background = 'cyan').grid(row=9,column=3)

    Button(frame3copr, text = 'Craindre', command=craindre1, background = 'cyan').grid(row=10,column=1)

    Button(frame3copr, text = 'Vaincre', command=vaincre1, background = 'cyan').grid(row=10,column=2)

    Button(frame3copr, text = 'Connaître', command=connaitre1, background = 'cyan').grid(row=10,column=3)

    Button(frame3copr, text = 'Croire', command=croire1, background = 'cyan').grid(row=11,column=1)

    Button(frame3copr, text = 'Boire', command=boire1, background = 'cyan').grid(row=11,column=2)

    Button(frame3copr, text = 'Conclure', command=conclure1, background = 'cyan').grid(row=11,column=3)

    Button(frame3copr, text = 'Coudre', command=coudre1, background = 'cyan').grid(row=12,column=1)

    Button(frame3copr, text = 'Suivre', command=suivre1, background = 'cyan').grid(row=12,column=2)

    Button(frame3copr, text = 'Vivre', command=vivre1, background = 'cyan').grid(row=12,column=3)

    Button(frame3copr, text = 'Lire', command=lire1, background = 'cyan').grid(row=13,column=1)

    Button(frame3copr, text = 'Dire', command=dire1, background = 'cyan').grid(row=13,column=2)

    Button(frame3copr, text = 'Rire', command=rire1, background = 'cyan').grid(row=13,column=3)

    Button(frame3copr, text = 'Ecrire', command=ecrire1, background = 'cyan').grid(row=14,column=1)

    Button(frame3copr, text = 'Cuire', command=cuire1, background = 'cyan').grid(row=14,column=2)

    conditionnel.pack(side=TOP)

    Button(fen13, text = 'Fermer', command=fen13.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def futurinaux():
    fen2 = Tk()
    fen2.title('Futur')

    fen2['background']='PaleTurquoise3'

    #Label des résultats

    conditionnel = Label(fen2, text = "........................................", background = 'PaleTurquoise3', fg = 'black')


    #Définition des verbes

    def etre1() :
        conditionnel['text']="serai, seras, sera, serons, serez, seront"

    def avoir1() :
        conditionnel['text']="aurai, auras, aura, aurons, aurez, auront"


    #champs des verbe

    conditionnel.pack(side=TOP)

    #auxiliaire


    frame3copr=Frame(fen2, borderwidth=2, relief = GROOVE, background='PaleTurquoise3')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    etre=Button(frame3copr, text = 'Etre', command=etre1, fg = 'white', background = 'green').grid(row=0,column=1)

    Button(frame3copr, text = 'Avoir', command=avoir1, fg = 'white', background = 'green').grid(row=1,column=1)





    #bouton fermer
    Button(fen2, text = 'Fermer', command=fen2.destroy, background = 'red').pack(side=BOTTOM)





    fen.mainloop()



def imparfaitinc():
    fen5=Tk()
    fen5.title('Imparfait')

    fen5['background']='#324270'

    type1=Frame(fen5, borderwidth=2, relief=GROOVE, bg='#324270')
    type1.pack(side=TOP, padx=5, pady=5)

    Button(type1, text="Auxiliaire", command=imparfaitinaux).pack()
    Button(type1, text="1er groupe", command=imparfaitin1).pack()
    Button(type1, text="2eme groupe", command=imparfaitin2).pack()
    Button(type1, text="3eme groupe", command=imparfaitin3).pack()
    Button(type1, text="Fermer", command=fen5.destroy, background="red").pack()

    fen.mainloop()

def imparfaitin1():
    fen11= Tk()
    fen11.title('Imparfait')

    fen11['background']='light pink'

    prgroupe1ld = Label(fen11, text = "Entrer votre radical:")
    conditionnel = Label(fen11, text = "........................................", background = 'light pink', fg = 'black')

    prgroupe1r = Entry(fen11)
    def prgroupe1a():
        conditionnel['text']=prgroupe1r.get() + "ais, ais, ait, ions, iez, aient"

    def prgroupe1():
        prgroupe1ld.pack()
        prgroupe1r.pack()
        okpr.pack()

    def peser1():
        conditionnel['text']="je pèsais, ais, ait, ions, iez, aient"

    def jeter1():
        conditionnel['text']="je jettais, ais, ait, ions, iez, aient"

    def modeler1():
        conditionnel['text']="je modèlais, ais, ait, ions, iez, aient"

    def broyer1():
        conditionnel['text']="je broyais, ais, ait, ions, iez, aient"

    def envoyer1():
        conditionnel['text']="je envoyais, ais, ait, ions, iez, aient"

    frame2copr=Frame(fen11, borderwidth=2, relief = GROOVE, bg='light pink')
    frame2copr.pack(side=TOP, padx=10,pady=10)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okpr=Button(fen11, text = 'Valider', command=prgroupe1a)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'yellow').grid(row=1,column=1)

    Button(frame2copr, text = "Peser", command=peser1, background = 'yellow').grid(row=1,column=2)

    Button(frame2copr, text = "Jeter", command=jeter1, background = 'yellow').grid(row=2,column=1)

    Button(frame2copr, text = "Modeler", command=modeler1, background = 'yellow').grid(row=2,column=2)

    Button(frame2copr, text = "Broyer", command=broyer1, background = 'yellow').grid(row=3,column=1)

    Button(frame2copr, text = "Envoyer", command=envoyer1, background = 'yellow').grid(row=3,column=2)


    conditionnel.pack(side=TOP)
    Button(fen11, text = 'Fermer', command=fen11.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def imparfaitin2():
    fen12= Tk()
    fen12.title('Imparfait')

    fen12['background']='#324270'

    degroupe1ld = Label(fen12, text = "Entrer votre radical:")
    conditionnel = Label(fen12, text = "........................................", background = '#324270', fg = 'white')

    degroupe1r = Entry(fen12)
    def degroupe1a():
        conditionnel['text']=degroupe1r.get() + "irais, irais, irait, irions, iriez, iraient"

    def degroupe1():
        degroupe1ld.pack()
        degroupe1r.pack()
        okde.pack()

    def hair1():
        conditionnel['text']="je haïssais, ais, ait, ions, iez, aient"

    frame1copr=Frame(fen12, borderwidth=2, relief = GROOVE, bg='#324270')
    frame1copr.pack(side=TOP, padx=10,pady=10)

    Button(frame1copr, text = 'Verbe du deuxième groupe', command=degroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okde=Button(fen12, text = 'Valider', command=degroupe1a)
    Button(frame1copr, text = 'Haïr', command=hair1, background = 'black', fg = 'white').grid(row=2,column=1)

    conditionnel.pack(side=TOP)
    Button(fen12, text = 'Fermer', command=fen12.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def imparfaitin3():
    fen13= Tk()
    fen13.title('Imparfait')

    fen13['background']='PaleGreen2'

    conditionnel = Label(fen13, text = "........................................", background = 'PaleGreen2', fg = 'black')

    def aller1():
        conditionnel['text']="j'allais, ais, ait, ions, iez, aient"

    def tenir1():
        conditionnel['text']="je tenais, ais, ait, ions, iez, aient"

    def acquerir1():
        conditionnel['text']="j'acquerais, ais, ait, ions, iez, aient"

    def sentir1():
        conditionnel['text']="je sentais, ais, ait, ions, iez, aient"

    def vetir1():
        conditionnel['text']="je vêtais, ais, ait, ions, iez, aient"

    def couvrir1():
        conditionnel['text']="je couvrais, ais, ait, ions, iez, aient"

    def ceuillir1():
        conditionnel['text']="je cueillais, ais, ait, ions, iez, aient"

    def assaillir1():
        conditionnel['text']="je assaillais, ais, ait, ions, iez, aient"

    def faillir1():
        conditionnel['text']="je faillais, ais, ait, ions, iez, aient"

    def bouillir1():
        conditionnel['text']="je boillais, ais, ait, ions, iez, aient"

    def dormir1():
        conditionnel['text']="je dormais, ais, ait, ions, iez, aient"

    def courir1():
        conditionnel['text']="je courais, ais, ait, ions, iez, aient"

    def mourir1():
        conditionnel['text']="je mourais, ais, ait, ions, iez, aient"

    def servir1():
        conditionnel['text']="je servais, ais, ait, ions, iez, aient"

    def fuir1():
        conditionnel['text']="je fuyais, ais, ait, ions, iez, aient"

    def recevoir1():
        conditionnel['text']="je recevais, ais, ait, ions, iez, aient"

    def voir1():
        conditionnel['text']="je voirais, ais, ait, ions, iez, aient"

    def savoir1():
        conditonnel['text']="je savais, ais, ait, ions, iez, aient"

    def devoir1():
        conditionnel['text']="je devais, ais, ait, ions, iez, aient"

    def pouvoir1():
        conditionnel['text']="je pouvais, ais, ait, ions, iez, aient"

    def vouloir1():
        conditionnel['text']="je voulais, ais, ait, ions, iez, aient"

    def rendre1():
        conditionnel['text']="je rendais, ais, ait, ions, iez, aient"

    def prendre1():
        conditionnel['text']="je prennais, ais, ait, ions, iez, aient"

    def battre1():
        conditionnel['text']="je battais, ais, ait, ions, iez, aient"

    def mettre1():
        conditionnel['text']="je mettais, ais, ait, ions, iez, aient"

    def peindre1():
        conditionnel['text']="je peignais, ais, ait, ions, iez, aient"

    def joindre1():
        conditionnel['text']="je joignais, ais, ait, ions, iez, aient"

    def craindre1():
        conditionnel['text']="je craingnais, ais, ait, ions, iez, aient"

    def vaincre1():
        conditionnel['text']="je vainquais, ais, ait, ions, iez, aient"

    def connaitre1():
        conditionnel['text']="je connaissais, ais, ait, ions, iez, aient"

    def croire1():
        conditionnel['text']="je croyais, ais, ait, ions, iez, aient"

    def boire1():
        conditionnel['text']="je buvais, ais, ait, ions, iez, aient"

    def conclure1():
        conditionnel['text']="je concluais, ais, ait, ions, iez, aient"

    def coudre1():
        conditionnel['text']="je cousais, ais, ait, ions, iez, aient"

    def suivre1():
        conditionnel['text']="je suivais, ais, ait, ions, iez, aient"

    def vivre1():
        conditionnel['text']="je vivais, ais, ait, ions, iez, aient"

    def lire1():
        conditionnel['text']="je lisais, ais, ait, ions, iez, aient"

    def dire1():
        conditionnel['text']="je disais, ais, ait, ions, iez, aient"

    def rire1():
        conditionnel['text']="je riais, ais, ait, ions, iez, aient"

    def ecrire1():
        conditionnel['text']="j'écrivais, ais, ait, ions, iez, aient"

    def cuire1():
        conditionnel['text']="je cuisais, ais, ait, ions, iez, aient"

    frame3copr=Frame(fen13, borderwidth=2, relief = GROOVE, bg='PaleGreen2')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    Button(frame3copr, text = 'Aller', command=aller1, background = 'cyan').grid(row=1,column=1)

    Button(frame3copr, text = 'Tenir', command=tenir1, background = 'cyan').grid(row=1,column=2)

    Button(frame3copr, text = 'Acquérir', command=acquerir1, background = 'cyan').grid(row=1,column=3)

    Button(frame3copr, text = 'Sentir', command=sentir1, background = 'cyan').grid(row=2,column=1)

    Button(frame3copr, text = 'Vêtir', command=vetir1, background = 'cyan').grid(row=2,column=2)

    Button(frame3copr, text = 'Couvrir', command=couvrir1, background = 'cyan').grid(row=2,column=3)

    Button(frame3copr, text = 'Ceuillir', command=ceuillir1, background = 'cyan').grid(row=3,column=1)

    Button(frame3copr, text = 'Assaillir', command=assaillir1, background = 'cyan').grid(row=3,column=2)

    Button(frame3copr, text = 'Faillir', command=faillir1, background = 'cyan').grid(row=3,column=3)

    Button(frame3copr, text = 'Bouillir', command=bouillir1, background = 'cyan').grid(row=4,column=1)

    Button(frame3copr, text = 'Dormir', command=dormir1, background = 'cyan').grid(row=4,column=2)

    Button(frame3copr, text = 'Courir', command=courir1, background = 'cyan').grid(row=4,column=3)

    Button(frame3copr, text = 'Mourir', command=mourir1, background = 'cyan').grid(row=5,column=1)

    Button(frame3copr, text = 'Servir', command=servir1, background = 'cyan').grid(row=5,column=2)

    Button(frame3copr, text = 'Fuir', command=fuir1, background = 'cyan').grid(row=5,column=3)

    Button(frame3copr, text = 'Recevoir', command=recevoir1, background = 'cyan').grid(row=6,column=1)

    Button(frame3copr, text = 'Voir', command=voir1, background = 'cyan').grid(row=6,column=2)

    Button(frame3copr, text = 'Savoir', command=savoir1, background = 'cyan').grid(row=6,column=3)

    Button(frame3copr, text = 'Devoir', command=devoir1, background = 'cyan').grid(row=7,column=1)

    Button(frame3copr, text = 'Pouvoir', command=pouvoir1, background = 'cyan').grid(row=7,column=2)

    Button(frame3copr, text = 'Vouloir', command=vouloir1, background = 'cyan').grid(row=7,column=3)

    Button(frame3copr, text = 'Rendre', command=rendre1, background = 'cyan').grid(row=8,column=1)

    Button(frame3copr, text = 'Prendre', command=prendre1, background = 'cyan').grid(row=8,column=2)

    Button(frame3copr, text = 'Battre', command=battre1, background = 'cyan').grid(row=8,column=3)

    Button(frame3copr, text = 'Mettre', command=mettre1, background = 'cyan').grid(row=9,column=1)

    Button(frame3copr, text = 'Peindre', command=peindre1, background = 'cyan').grid(row=9,column=2)

    Button(frame3copr, text = 'Joindre', command=joindre1, background = 'cyan').grid(row=9,column=3)

    Button(frame3copr, text = 'Craindre', command=craindre1, background = 'cyan').grid(row=10,column=1)

    Button(frame3copr, text = 'Vaincre', command=vaincre1, background = 'cyan').grid(row=10,column=2)

    Button(frame3copr, text = 'Connaître', command=connaitre1, background = 'cyan').grid(row=10,column=3)

    Button(frame3copr, text = 'Croire', command=croire1, background = 'cyan').grid(row=11,column=1)

    Button(frame3copr, text = 'Boire', command=boire1, background = 'cyan').grid(row=11,column=2)

    Button(frame3copr, text = 'Conclure', command=conclure1, background = 'cyan').grid(row=11,column=3)

    Button(frame3copr, text = 'Coudre', command=coudre1, background = 'cyan').grid(row=12,column=1)

    Button(frame3copr, text = 'Suivre', command=suivre1, background = 'cyan').grid(row=12,column=2)

    Button(frame3copr, text = 'Vivre', command=vivre1, background = 'cyan').grid(row=12,column=3)

    Button(frame3copr, text = 'Lire', command=lire1, background = 'cyan').grid(row=13,column=1)

    Button(frame3copr, text = 'Dire', command=dire1, background = 'cyan').grid(row=13,column=2)

    Button(frame3copr, text = 'Rire', command=rire1, background = 'cyan').grid(row=13,column=3)

    Button(frame3copr, text = 'Ecrire', command=ecrire1, background = 'cyan').grid(row=14,column=1)

    Button(frame3copr, text = 'Cuire', command=cuire1, background = 'cyan').grid(row=14,column=2)

    conditionnel.pack(side=TOP)

    Button(fen13, text = 'Fermer', command=fen13.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def imparfaitinaux():
    fen2 = Tk()
    fen2.title('Imparfait')

    fen2['background']='PaleTurquoise3'

    #Label des résultats

    conditionnel = Label(fen2, text = "........................................", background = 'PaleTurquoise3', fg = 'black')


    #Définition des verbes

    def etre1() :
        conditionnel['text']="étais, étais, était, étions, étiez, étaient"

    def avoir1() :
        conditionnel['text']="avais, avais, avait, avions, aviez, avaient"


    #champs des verbe

    conditionnel.pack(side=TOP)

    #auxiliaire


    frame3copr=Frame(fen2, borderwidth=2, relief = GROOVE, background='PaleTurquoise3')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    etre=Button(frame3copr, text = 'Etre', command=etre1, fg = 'white', background = 'green').grid(row=0,column=1)

    Button(frame3copr, text = 'Avoir', command=avoir1, fg = 'white', background = 'green').grid(row=1,column=1)





    #bouton fermer
    Button(fen2, text = 'Fermer', command=fen2.destroy, background = 'red').pack(side=BOTTOM)





    fen.mainloop()



def subjonctifprc():
    fen5=Tk()
    fen5.title('Subjonctif Présent')

    fen5['background']='#324270'

    type1=Frame(fen5, borderwidth=2, relief=GROOVE, bg='#324270')
    type1.pack(side=TOP, padx=5, pady=5)

    Button(type1, text="Auxiliaire", command=subjonctifpraux).pack()
    Button(type1, text="1er groupe", command=subjonctifpr1).pack()
    Button(type1, text="2eme groupe", command=subjonctifpr2).pack()
    Button(type1, text="3eme groupe", command=subjonctifpr3).pack()
    Button(type1, text="Fermer", command=fen5.destroy, background="red").pack()

    fen.mainloop()

def subjonctifpr1():
    fen11= Tk()
    fen11.title('Subjonctif Présent')

    fen11['background']='light pink'

    prgroupe1ld = Label(fen11, text = "Entrer votre radical:")
    conditionnel = Label(fen11, text = "........................................", background = 'light pink', fg = 'black')

    prgroupe1r = Entry(fen11)
    def prgroupe1a():
        conditionnel['text']=prgroupe1r.get() + "e, es, e, ions, iez, ent"

    def prgroupe1():
        prgroupe1ld.pack()
        prgroupe1r.pack()
        okpr.pack()

    def peser1():
        conditionnel['text']="je pèse, es, e, ions, iez, ent"

    def jeter1():
        conditionnel['text']="je jette, es, e, ions, iez, ent"

    def modeler1():
        conditionnel['text']="je modèle, es, e, ions, iez, ent"

    def broyer1():
        conditionnel['text']="je broie, es, e, ions, iez, ent"

    def envoyer1():
        conditionnel['text']="je envoie, es, e, ions, iez, ent"

    frame2copr=Frame(fen11, borderwidth=2, relief = GROOVE, bg='light pink')
    frame2copr.pack(side=TOP, padx=10,pady=10)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okpr=Button(fen11, text = 'Valider', command=prgroupe1a)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'yellow').grid(row=1,column=1)

    Button(frame2copr, text = "Peser", command=peser1, background = 'yellow').grid(row=1,column=2)

    Button(frame2copr, text = "Jeter", command=jeter1, background = 'yellow').grid(row=2,column=1)

    Button(frame2copr, text = "Modeler", command=modeler1, background = 'yellow').grid(row=2,column=2)

    Button(frame2copr, text = "Broyer", command=broyer1, background = 'yellow').grid(row=3,column=1)

    Button(frame2copr, text = "Envoyer", command=envoyer1, background = 'yellow').grid(row=3,column=2)


    conditionnel.pack(side=TOP)
    Button(fen11, text = 'Fermer', command=fen11.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def subjonctifpr2():
    fen12= Tk()
    fen12.title('Subjonctif Présent')

    fen12['background']='#324270'

    degroupe1ld = Label(fen12, text = "Entrer votre radical:")
    conditionnel = Label(fen12, text = "........................................", background = '#324270', fg = 'white')

    degroupe1r = Entry(fen12)
    def degroupe1a():
        conditionnel['text']=degroupe1r.get() + "sse, sses, sse, ssions, ssiez, ssent"

    def degroupe1():
        degroupe1ld.pack()
        degroupe1r.pack()
        okde.pack()

    def hair1():
        conditionnel['text']="je haïsse, es, e, ions, iez, ent"

    frame1copr=Frame(fen12, borderwidth=2, relief = GROOVE, bg='#324270')
    frame1copr.pack(side=TOP, padx=10,pady=10)

    Button(frame1copr, text = 'Verbe du deuxième groupe', command=degroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okde=Button(fen12, text = 'Valider', command=degroupe1a)
    Button(frame1copr, text = 'Haïr', command=hair1, background = 'black', fg = 'white').grid(row=2,column=1)

    conditionnel.pack(side=TOP)
    Button(fen12, text = 'Fermer', command=fen12.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def subjonctifpr3():
    fen13= Tk()
    fen13.title('Subjonctif Présent')

    fen13['background']='PaleGreen2'

    conditionnel = Label(fen13, text = "........................................", background = 'PaleGreen2', fg = 'black')

    def aller1():
        conditionnel['text']="j'aille, es, e, ions, iez, ent"

    def tenir1():
        conditionnel['text']="je tienne, es, e, ions, iez, ent"

    def acquerir1():
        conditionnel['text']="j'acquière, es, e, ions, iez, ent"

    def sentir1():
        conditionnel['text']="je sente, es, e, ions, iez, ent"

    def vetir1():
        conditionnel['text']="je vête, es, e, ions, iez, ent"

    def couvrir1():
        conditionnel['text']="je couvre, es, e, ions, iez, ent"

    def ceuillir1():
        conditionnel['text']="je cueille, es, e, ions, iez, ent"

    def assaillir1():
        conditionnel['text']="j'assaille, es, e, ions, iez, ent"

    def faillir1():
        conditionnel['text']="je faillisse, es, e, ions, iez, ent"

    def bouillir1():
        conditionnel['text']="je bouille, es, e, ions, iez, ent"

    def dormir1():
        conditionnel['text']="je dorme, es, e, ions, iez, ent"

    def courir1():
        conditionnel['text']="je coure, es, e, ions, iez, ent"

    def mourir1():
        conditionnel['text']="je meure, es, e, ions, iez, ent"

    def servir1():
        conditionnel['text']="je serve, es, e, ions, iez, ent"

    def fuir1():
        conditionnel['text']="je fuie, es, e, ions, iez, ent"

    def recevoir1():
        conditionnel['text']="je reçoive, es, e, ions, iez, ent"

    def voir1():
        conditionnel['text']="je voie, es, e, ions, iez, ent"

    def savoir1():
        conditonnel['text']="je sache, es, e, ions, iez, ent"

    def devoir1():
        conditionnel['text']="je doive, es, e, ions, iez, ent"

    def pouvoir1():
        conditionnel['text']="je puisse, es, e, ions, iez, ent"

    def vouloir1():
        conditionnel['text']="je veuille, es, e, ions, iez, ent"

    def rendre1():
        conditionnel['text']="je rende, es, e, ions, iez, ent"

    def prendre1():
        conditionnel['text']="je prenne, es, e, ions, iez, ent"

    def battre1():
        conditionnel['text']="je batte, es, e, ions, iez, ent"

    def mettre1():
        conditionnel['text']="je mette, es, e, ions, iez, ent"

    def peindre1():
        conditionnel['text']="je peigne, es, e, ions, iez, ent"

    def joindre1():
        conditionnel['text']="je joigne, es, e, ions, iez, ent"

    def craindre1():
        conditionnel['text']="je craigne, es, e, ions, iez, ent"

    def vaincre1():
        conditionnel['text']="je vainque, es, e, ions, iez, ent"

    def connaitre1():
        conditionnel['text']="je connaisse, es, e, ions, iez, ent"

    def croire1():
        conditionnel['text']="je croie, es, e, ions, iez, ent"

    def boire1():
        conditionnel['text']="je boive, es, e, ions, iez, ent"

    def conclure1():
        conditionnel['text']="je conclue, es, e, ions, iez, ent"

    def coudre1():
        conditionnel['text']="je couse, es, e, ions, iez, ent"

    def suivre1():
        conditionnel['text']="je suive, es, e, ions, iez, ent"

    def vivre1():
        conditionnel['text']="je vive, es, e, ions, iez, ent"

    def lire1():
        conditionnel['text']="je lise, es, e, ions, iez, ent"

    def dire1():
        conditionnel['text']="je dise, es, e, ions, iez, ent"

    def rire1():
        conditionnel['text']="je rie, es, e, ions, iez, ent"

    def ecrire1():
        conditionnel['text']="j'écrive, es, e, ions, iez, ent"

    def cuire1():
        conditionnel['text']="je cuise, es, e, ions, iez, ent"

    frame3copr=Frame(fen13, borderwidth=2, relief = GROOVE, bg='PaleGreen2')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    Button(frame3copr, text = 'Aller', command=aller1, background = 'cyan').grid(row=1,column=1)

    Button(frame3copr, text = 'Tenir', command=tenir1, background = 'cyan').grid(row=1,column=2)

    Button(frame3copr, text = 'Acquérir', command=acquerir1, background = 'cyan').grid(row=1,column=3)

    Button(frame3copr, text = 'Sentir', command=sentir1, background = 'cyan').grid(row=2,column=1)

    Button(frame3copr, text = 'Vêtir', command=vetir1, background = 'cyan').grid(row=2,column=2)

    Button(frame3copr, text = 'Couvrir', command=couvrir1, background = 'cyan').grid(row=2,column=3)

    Button(frame3copr, text = 'Ceuillir', command=ceuillir1, background = 'cyan').grid(row=3,column=1)

    Button(frame3copr, text = 'Assaillir', command=assaillir1, background = 'cyan').grid(row=3,column=2)

    Button(frame3copr, text = 'Faillir', command=faillir1, background = 'cyan').grid(row=3,column=3)

    Button(frame3copr, text = 'Bouillir', command=bouillir1, background = 'cyan').grid(row=4,column=1)

    Button(frame3copr, text = 'Dormir', command=dormir1, background = 'cyan').grid(row=4,column=2)

    Button(frame3copr, text = 'Courir', command=courir1, background = 'cyan').grid(row=4,column=3)

    Button(frame3copr, text = 'Mourir', command=mourir1, background = 'cyan').grid(row=5,column=1)

    Button(frame3copr, text = 'Servir', command=servir1, background = 'cyan').grid(row=5,column=2)

    Button(frame3copr, text = 'Fuir', command=fuir1, background = 'cyan').grid(row=5,column=3)

    Button(frame3copr, text = 'Recevoir', command=recevoir1, background = 'cyan').grid(row=6,column=1)

    Button(frame3copr, text = 'Voir', command=voir1, background = 'cyan').grid(row=6,column=2)

    Button(frame3copr, text = 'Savoir', command=savoir1, background = 'cyan').grid(row=6,column=3)

    Button(frame3copr, text = 'Devoir', command=devoir1, background = 'cyan').grid(row=7,column=1)

    Button(frame3copr, text = 'Pouvoir', command=pouvoir1, background = 'cyan').grid(row=7,column=2)

    Button(frame3copr, text = 'Vouloir', command=vouloir1, background = 'cyan').grid(row=7,column=3)

    Button(frame3copr, text = 'Rendre', command=rendre1, background = 'cyan').grid(row=8,column=1)

    Button(frame3copr, text = 'Prendre', command=prendre1, background = 'cyan').grid(row=8,column=2)

    Button(frame3copr, text = 'Battre', command=battre1, background = 'cyan').grid(row=8,column=3)

    Button(frame3copr, text = 'Mettre', command=mettre1, background = 'cyan').grid(row=9,column=1)

    Button(frame3copr, text = 'Peindre', command=peindre1, background = 'cyan').grid(row=9,column=2)

    Button(frame3copr, text = 'Joindre', command=joindre1, background = 'cyan').grid(row=9,column=3)

    Button(frame3copr, text = 'Craindre', command=craindre1, background = 'cyan').grid(row=10,column=1)

    Button(frame3copr, text = 'Vaincre', command=vaincre1, background = 'cyan').grid(row=10,column=2)

    Button(frame3copr, text = 'Connaître', command=connaitre1, background = 'cyan').grid(row=10,column=3)

    Button(frame3copr, text = 'Croire', command=croire1, background = 'cyan').grid(row=11,column=1)

    Button(frame3copr, text = 'Boire', command=boire1, background = 'cyan').grid(row=11,column=2)

    Button(frame3copr, text = 'Conclure', command=conclure1, background = 'cyan').grid(row=11,column=3)

    Button(frame3copr, text = 'Coudre', command=coudre1, background = 'cyan').grid(row=12,column=1)

    Button(frame3copr, text = 'Suivre', command=suivre1, background = 'cyan').grid(row=12,column=2)

    Button(frame3copr, text = 'Vivre', command=vivre1, background = 'cyan').grid(row=12,column=3)

    Button(frame3copr, text = 'Lire', command=lire1, background = 'cyan').grid(row=13,column=1)

    Button(frame3copr, text = 'Dire', command=dire1, background = 'cyan').grid(row=13,column=2)

    Button(frame3copr, text = 'Rire', command=rire1, background = 'cyan').grid(row=13,column=3)

    Button(frame3copr, text = 'Ecrire', command=ecrire1, background = 'cyan').grid(row=14,column=1)

    Button(frame3copr, text = 'Cuire', command=cuire1, background = 'cyan').grid(row=14,column=2)

    conditionnel.pack(side=TOP)

    Button(fen13, text = 'Fermer', command=fen13.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def subjonctifpraux():
    fen2 = Tk()
    fen2.title('Subjonctif Présent')

    fen2['background']='PaleTurquoise3'

    #Label des résultats

    conditionnel = Label(fen2, text = "........................................", background = 'PaleTurquoise3', fg = 'black')


    #Définition des verbes

    def etre1() :
        conditionnel['text']="sois, sois, soit, soyons, soyez, soient"

    def avoir1() :
        conditionnel['text']="aie, aies, ait, ayons, ayez, aient"


    #champs des verbe

    conditionnel.pack(side=TOP)

    #auxiliaire


    frame3copr=Frame(fen2, borderwidth=2, relief = GROOVE, background='PaleTurquoise3')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    etre=Button(frame3copr, text = 'Etre', command=etre1, fg = 'white', background = 'green').grid(row=0,column=1)

    Button(frame3copr, text = 'Avoir', command=avoir1, fg = 'white', background = 'green').grid(row=1,column=1)




    #bouton fermer
    Button(fen2, text = 'Fermer', command=fen2.destroy, background = 'red').pack(side=BOTTOM)





    fen.mainloop()



def conditionnelprc():
    fen10=Tk()
    fen10.title('Conditionnel Présent')

    fen10['background']='#324270'

    type1=Frame(fen10, borderwidth=2, relief=GROOVE, bg='#324270')
    type1.pack(side=TOP, padx=5, pady=5)

    Button(type1, text="Auxiliaire", command=conditionnelpraux).pack()
    Button(type1, text="1er groupe", command=conditionnelpr1).pack()
    Button(type1, text="2eme groupe", command=conditionnelpr2).pack()
    Button(type1, text="3eme groupe", command=conditionnelpr3).pack()
    Button(type1, text="Fermer", command=fen10.destroy, background="red").pack()

    fen.mainloop()

def conditionnelpr1():
    fen11= Tk()
    fen11.title('Conditionnel Présent')

    fen11['background']='light pink'

    prgroupe1ld = Label(fen11, text = "Entrer votre radical:")
    conditionnel = Label(fen11, text = "........................................", background = 'light pink', fg = 'black')

    prgroupe1r = Entry(fen11)
    def prgroupe1a():
        conditionnel['text']=prgroupe1r.get() + "erais, erais, erait, erions, eriez, eraient"

    def prgroupe1():
        prgroupe1ld.pack()
        prgroupe1r.pack()
        okpr.pack()

    def peser1():
        conditionnel['text']="pèserais, ais, ait, ions, iez, aient"

    def jeter1():
        conditionnel['text']="jetterais, ais, ait, ions, iez, aient"

    def modeler1():
        conditionnel['text']="modèlerais, ais, ait, ions, iez, aient"

    def broyer1():
        conditionnel['text']="broierais, ais, ait, ions, iez, aient"

    def envoyer1():
        conditionnel['text']="enverrais, ais, ait, ions, iez, aient"

    frame2copr=Frame(fen11, borderwidth=2, relief = GROOVE, bg='light pink')
    frame2copr.pack(side=TOP, padx=10,pady=10)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okpr=Button(fen11, text = 'Valider', command=prgroupe1a)

    Button(frame2copr, text = 'Verbe du premier groupe', command=prgroupe1, background = 'yellow').grid(row=1,column=1)

    Button(frame2copr, text = "Peser", command=peser1, background = 'yellow').grid(row=1,column=2)

    Button(frame2copr, text = "Jeter", command=jeter1, background = 'yellow').grid(row=2,column=1)

    Button(frame2copr, text = "Modeler", command=modeler1, background = 'yellow').grid(row=2,column=2)

    Button(frame2copr, text = "Broyer", command=broyer1, background = 'yellow').grid(row=3,column=1)

    Button(frame2copr, text = "Envoyer", command=envoyer1, background = 'yellow').grid(row=3,column=2)


    conditionnel.pack(side=TOP)
    Button(fen11, text = 'Fermer', command=fen11.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def conditionnelpr2():
    fen12= Tk()
    fen12.title('Conditionnel Présent')

    fen12['background']='#324270'

    degroupe1ld = Label(fen12, text = "Entrer votre radical:")
    conditionnel = Label(fen12, text = "........................................", background = '#324270', fg = 'white')

    degroupe1r = Entry(fen12)
    def degroupe1a():
        conditionnel['text']=degroupe1r.get() + "irais, irais, irait, irions, iriez, iraient"

    def degroupe1():
        degroupe1ld.pack()
        degroupe1r.pack()
        okde.pack()

    def hair1():
        conditionnel['text']="haïrais, ais, ait, ions, iez, aient"

    frame1copr=Frame(fen12, borderwidth=2, relief = GROOVE, bg='#324270')
    frame1copr.pack(side=TOP, padx=10,pady=10)

    Button(frame1copr, text = 'Verbe du deuxième groupe', command=degroupe1, background = 'black', fg = 'white').grid(row=1,column=1)

    okde=Button(fen12, text = 'Valider', command=degroupe1a)
    Button(frame1copr, text = 'Haïr', command=hair1, background = 'black', fg = 'white').grid(row=2,column=1)

    conditionnel.pack(side=TOP)
    Button(fen12, text = 'Fermer', command=fen12.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def conditionnelpr3():
    fen13= Tk()
    fen13.title('Conditionnel Présent')

    fen13['background']='PaleGreen2'

    conditionnel = Label(fen13, text = "........................................", background = 'PaleGreen2', fg = 'black')

    def aller1():
        conditionnel['text']="j'irais, ais, ait, ions, iez, aient"

    def tenir1():
        conditionnel['text']="je tiendrais, ais, ait, ions, iez, aient"

    def acquerir1():
        conditionnel['text']="j'acquerrais, ais, ait, ions, iez, aient"

    def sentir1():
        conditionnel['text']="je sentirais, ais, ait, ions, iez, aient"

    def vetir1():
        conditionnel['text']="je vêtirais, ais, ait, ions, iez, aient"

    def couvrir1():
        conditionnel['text']="je couvrirais, ais, ait, ions, iez, aient"

    def ceuillir1():
        conditionnel['text']="je cueillerais, ais, ait, ions, iez, aient"

    def assaillir1():
        conditionnel['text']="je assaillirais, ais, ait, ions, iez, aient"

    def faillir1():
        conditionnel['text']="je faillirais, ais, ait, ions, iez, aient"

    def bouillir1():
        conditionnel['text']="je boillirais, ais, ait, ions, iez, aient"

    def dormir1():
        conditionnel['text']="je dormirais, ais, ait, ions, iez, aient"

    def courir1():
        conditionnel['text']="je courrais, ais, ait, ions, iez, aient"

    def mourir1():
        conditionnel['text']="je mourrais, ais, ait, ions, iez, aient"

    def servir1():
        conditionnel['text']="je servirais, ais, ait, ions, iez, aient"

    def fuir1():
        conditionnel['text']="je fuirais, ais, ait, ions, iez, aient"

    def recevoir1():
        conditionnel['text']="je recevrais, ais, ait, ions, iez, aient"

    def voir1():
        conditionnel['text']="je verrais, ais, ait, ions, iez, aient"

    def savoir1():
        conditonnel['text']="je saurais, ais, ait, ions, iez, aient"

    def devoir1():
        conditionnel['text']="je devrais, ais, ait, ions, iez, aient"

    def pouvoir1():
        conditionnel['text']="je pourrais, ais, ait, ions, iez, aient"

    def vouloir1():
        conditionnel['text']="je voudrais, ais, ait, ions, iez, aient"

    def rendre1():
        conditionnel['text']="je rendrais, ais, ait, ions, iez, aient"

    def prendre1():
        conditionnel['text']="je prendrais, ais, ait, ions, iez, aient"

    def battre1():
        conditionnel['text']="je battrais, ais, ait, ions, iez, aient"

    def mettre1():
        conditionnel['text']="je mettrais, ais, ait, ions, iez, aient"

    def peindre1():
        conditionnel['text']="je peindrais, ais, ait, ions, iez, aient"

    def joindre1():
        conditionnel['text']="je joindrais, ais, ait, ions, iez, aient"

    def craindre1():
        conditionnel['text']="je craindrais, ais, ait, ions, iez, aient"

    def vaincre1():
        conditionnel['text']="je vaincrais, ais, ait, ions, iez, aient"

    def connaitre1():
        conditionnel['text']="je connaitrais, ais, ait, ions, iez, aient"

    def croire1():
        conditionnel['text']="je croirais, ais, ait, ions, iez, aient"

    def boire1():
        conditionnel['text']="je boirais, ais, ait, ions, iez, aient"

    def conclure1():
        conditionnel['text']="je conclurais, ais, ait, ions, iez, aient"

    def coudre1():
        conditionnel['text']="je coudrais, ais, ait, ions, iez, aient"

    def suivre1():
        conditionnel['text']="je suivrais, ais, ait, ions, iez, aient"

    def vivre1():
        conditionnel['text']="je vivrais, ais, ait, ions, iez, aient"

    def lire1():
        conditionnel['text']="je lirais, ais, ait, ions, iez, aient"

    def dire1():
        conditionnel['text']="je dirais, ais, ait, ions, iez, aient"

    def rire1():
        conditionnel['text']="je rirais, ais, ait, ions, iez, aient"

    def ecrire1():
        conditionnel['text']="j'écrirais, ais, ait, ions, iez, aient"

    def cuire1():
        conditionnel['text']="je cuirais, ais, ait, ions, iez, aient"

    frame3copr=Frame(fen13, borderwidth=2, relief = GROOVE, bg='PaleGreen2')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    Button(frame3copr, text = 'Aller', command=aller1, background = 'cyan').grid(row=1,column=1)

    Button(frame3copr, text = 'Tenir', command=tenir1, background = 'cyan').grid(row=1,column=2)

    Button(frame3copr, text = 'Acquérir', command=acquerir1, background = 'cyan').grid(row=1,column=3)

    Button(frame3copr, text = 'Sentir', command=sentir1, background = 'cyan').grid(row=2,column=1)

    Button(frame3copr, text = 'Vêtir', command=vetir1, background = 'cyan').grid(row=2,column=2)

    Button(frame3copr, text = 'Couvrir', command=couvrir1, background = 'cyan').grid(row=2,column=3)

    Button(frame3copr, text = 'Ceuillir', command=ceuillir1, background = 'cyan').grid(row=3,column=1)

    Button(frame3copr, text = 'Assaillir', command=assaillir1, background = 'cyan').grid(row=3,column=2)

    Button(frame3copr, text = 'Faillir', command=faillir1, background = 'cyan').grid(row=3,column=3)

    Button(frame3copr, text = 'Bouillir', command=bouillir1, background = 'cyan').grid(row=4,column=1)

    Button(frame3copr, text = 'Dormir', command=dormir1, background = 'cyan').grid(row=4,column=2)

    Button(frame3copr, text = 'Courir', command=courir1, background = 'cyan').grid(row=4,column=3)

    Button(frame3copr, text = 'Mourir', command=mourir1, background = 'cyan').grid(row=5,column=1)

    Button(frame3copr, text = 'Servir', command=servir1, background = 'cyan').grid(row=5,column=2)

    Button(frame3copr, text = 'Fuir', command=fuir1, background = 'cyan').grid(row=5,column=3)

    Button(frame3copr, text = 'Recevoir', command=recevoir1, background = 'cyan').grid(row=6,column=1)

    Button(frame3copr, text = 'Voir', command=voir1, background = 'cyan').grid(row=6,column=2)

    Button(frame3copr, text = 'Savoir', command=savoir1, background = 'cyan').grid(row=6,column=3)

    Button(frame3copr, text = 'Devoir', command=devoir1, background = 'cyan').grid(row=7,column=1)

    Button(frame3copr, text = 'Pouvoir', command=pouvoir1, background = 'cyan').grid(row=7,column=2)

    Button(frame3copr, text = 'Vouloir', command=vouloir1, background = 'cyan').grid(row=7,column=3)

    Button(frame3copr, text = 'Rendre', command=rendre1, background = 'cyan').grid(row=8,column=1)

    Button(frame3copr, text = 'Prendre', command=prendre1, background = 'cyan').grid(row=8,column=2)

    Button(frame3copr, text = 'Battre', command=battre1, background = 'cyan').grid(row=8,column=3)

    Button(frame3copr, text = 'Mettre', command=mettre1, background = 'cyan').grid(row=9,column=1)

    Button(frame3copr, text = 'Peindre', command=peindre1, background = 'cyan').grid(row=9,column=2)

    Button(frame3copr, text = 'Joindre', command=joindre1, background = 'cyan').grid(row=9,column=3)

    Button(frame3copr, text = 'Craindre', command=craindre1, background = 'cyan').grid(row=10,column=1)

    Button(frame3copr, text = 'Vaincre', command=vaincre1, background = 'cyan').grid(row=10,column=2)

    Button(frame3copr, text = 'Connaître', command=connaitre1, background = 'cyan').grid(row=10,column=3)

    Button(frame3copr, text = 'Croire', command=croire1, background = 'cyan').grid(row=11,column=1)

    Button(frame3copr, text = 'Boire', command=boire1, background = 'cyan').grid(row=11,column=2)

    Button(frame3copr, text = 'Conclure', command=conclure1, background = 'cyan').grid(row=11,column=3)

    Button(frame3copr, text = 'Coudre', command=coudre1, background = 'cyan').grid(row=12,column=1)

    Button(frame3copr, text = 'Suivre', command=suivre1, background = 'cyan').grid(row=12,column=2)

    Button(frame3copr, text = 'Vivre', command=vivre1, background = 'cyan').grid(row=12,column=3)

    Button(frame3copr, text = 'Lire', command=lire1, background = 'cyan').grid(row=13,column=1)

    Button(frame3copr, text = 'Dire', command=dire1, background = 'cyan').grid(row=13,column=2)

    Button(frame3copr, text = 'Rire', command=rire1, background = 'cyan').grid(row=13,column=3)

    Button(frame3copr, text = 'Ecrire', command=ecrire1, background = 'cyan').grid(row=14,column=1)

    Button(frame3copr, text = 'Cuire', command=cuire1, background = 'cyan').grid(row=14,column=2)

    conditionnel.pack(side=TOP)

    Button(fen13, text = 'Fermer', command=fen13.destroy, background = 'red').pack(side=BOTTOM)

    fen.mainloop()

def conditionnelpraux():
    fen2 = Tk()
    fen2.title('Conditionnel Présent')

    fen2['background']='PaleTurquoise3'

    #Label des résultats

    conditionnel = Label(fen2, text = "........................................", background = 'PaleTurquoise3', fg = 'black')




    #Définition des verbes

    def etre1() :
        conditionnel['text']="serais, serais, serait, serions, seriez, seraient"

    def avoir1() :
        conditionnel['text']="aurais, aurais, aurait, aurions, auriez, auraient"


    #champs des verbe

    conditionnel.pack(side=TOP)

    #auxiliaire

    frame3copr=Frame(fen2, borderwidth=2, relief = GROOVE, background='PaleTurquoise3')
    frame3copr.pack(side=TOP, padx=10,pady=10)

    etre=Button(frame3copr, text = 'Etre', command=etre1, fg = 'white', background = 'green').grid(row=0,column=1)

    Button(frame3copr, text = 'Avoir', command=avoir1, fg = 'white', background = 'green').grid(row=1,column=1)





    #bouton fermer
    Button(fen2, text = 'Fermer', command=fen2.destroy, background = 'red').pack(side=BOTTOM)





    fen.mainloop()









fen = Tk()
fen.title('Fenetre principal')
fen.geometry("230x450")
fen['background']='dark orchid'




temps=Frame(fen, borderwidth=2, relief=GROOVE, background='dark orchid')
temps.pack(side=TOP, padx=5, pady=5)


Button(temps, text = "              Présent              ", command=presentinc).pack()

Button(temps, text = "                Futur               ", command=futurinc).pack()

Button(temps, text = "            Imparfait            ", command=imparfaitinc).pack()

Button(temps, text = "  Présent du subjonctif  ", command=subjonctifprc).pack()

Button(temps, text = "Présent du Conditionnel", command=conditionnelprc).pack()


Button(fen, text="QUITTER", command=fen.destroy, background='red').pack(side=BOTTOM)



fen.mainloop()

