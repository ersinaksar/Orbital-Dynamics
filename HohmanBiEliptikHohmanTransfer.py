import math

pi=math.pi
#gezegen=çap km , kütle kg
merkur=[4870,3.30*10**23]
venus=[12104,4.87*10**24]
dunya=[12756,5.98*10**24]
ay=[3474.13,7,3477*10**22]
mars=[6787,6.44*10**23]
jupiter=[142800,1.90*10**27]
saturn=[120660,5.69*10**26]
uranus=[50800,8.76*10**25]
neptun=[48600,1.03*10**26]
pluton=[1187,1.303*10**22]
G=6.62*10**-11 #çekim sabiti (N*m**2)/kg
#gunuplot kütüphanesini kullan grafik için
#gezegen class ı , ayrı ayrı transfer class ı ,hepsini main fonksiyonuna al ,girdi dosyadan ilk iki girdisi sitring
#olan değişkenlerin girdi dosyadaki sırası yeri belli olsun ve ona göre okusun boşuna try exept falan kullanma
"""
classlar

"""
#################
r1a=0 #input
r1p=0 #input
r2a=0 #input
r2p=0 #input
r3a=0 #input
r3p=0 #input
r4a=0 #input
r4p=0 #input
#################
be=[r1a,r1p,r2a,r2p,r3a,r3p,r4a,r4p]
h=[r1a,r1p,r2a,r2p,r3a,r3p,r4a,r4p] #1.yörüngenin en uzak noktası r1a km cinsinden, en yakın noktası r1p km cinsinden ....
transferType=[be,h]
planetFeatureList=[merkur,venus,dunya,ay,mars,jupiter,saturn,uranus,neptun,pluton]
planetNameList=["merkur","venus","dunya","ay","mars","jupiter","saturn","uranus","neptun","pluton"]
transferTypeNameList=["be","h"]
beNameList=["r1a","r1p","r2a","r2p","r3a","r3p","r4a","r4p"]
hNameList=["r1a","r1p","r2a","r2p","r3a","r3p","r4a","r4p"]
#---------------------------------------
toplamSatirListe=[] #toplamSatirListe adında boş bir liste oluştur
with open("deneme3.txt","r") as f: #ismindeki dosyayı aç
    data = f.readlines() #dosyadaki her satırı bir iste şeklinde oku ve data olarak tanımla
f.close() #dosyayı kapat

toplamSatir=len(data) #dosyadaki toplam satır sayısını veriyor
for eleman in range(toplamSatir*2): #dosyadaki satır sayısının iki katı kadar (her satırda iki eleman olduğundan eleman sayısı) kadar çalış
    toplamSatirListe.append(eleman) #dosyadaki eleman sayısı kadar büyüklüğe sahip bir liste oluşturuyor
#print("toplamSatir",toplamSatir)

with open("deneme3.txt","r") as f: #ismindeki dosyayı aç
    data = f.readline() #dosyadaki ilk satırı oku
    wordString=data.split() #satırı parçala
    girdiTransferName=wordString[1] #girilen transfer ismini tanımla
    print("Girilen Transfer:",girdiTransferName)

    data = f.readline() #dosyadaki ikinci satırı oku
    wordString=data.split() #satırı parçala
    girdiPlanetName=wordString[1] #girilen gezegen ismini tanımla
    print("Girilen Gezegen:", girdiPlanetName)

    integerValueNumber=toplamSatir-2 #şuana kadar okunmayan satırların sayısını veriyor

    for j in range(integerValueNumber): #okunmayan satır kadar çalış
        data = f.readline() #en son okunan satırdan sonraki satırı oku
        words = data.split() #satırı parçala
        if girdiTransferName == "be":
            wordString=words[0] #uzaklık ismini tanımla
            wordsInteger=words[1] #uzaklık değerini tanımla
            wordsInteger=float(wordsInteger) #dosyadan okunan string floata çevriliyor
            wordStringNumber=beNameList.index(wordString) #okunan uzaklık isminin beNameList deki index i bulunuyor
            be[wordStringNumber]=wordsInteger #okunan float değer be listesinde ait olduğu indexe atanıyor

        elif girdiTransferName == "h":
            wordString=words[0] #uzaklık ismini tanımla
            wordsInteger=words[1] #uzaklık değerini tanımla
            wordsInteger=float(wordsInteger) #dosyadan okunan string floata çevriliyor
            wordStringNumber=hNameList.index(wordString) #okunan uzaklık isminin hNameList deki index i bulunuyor
            h[wordStringNumber]=wordsInteger #okunan float değer h listesinde ait olduğu indexe atanıyor

f.close() #dosyayı kapat

girdiTransfer=girdiTransferName #input
girdiGezegen=girdiPlanetName #input

def HohmanTransfer(h,planetR,planetM,G):
    planetr=planetR/2 #çapı yarıçap haline getir o gezegen için
    mu=G*planetM*10**-9#gezegene özel mü değeri km**3 /s**2 ye çevirdik
    print("Gezegenin mü değeri:",mu,"km**3/s**2")
    print("Çekim sabiti:",G,"N*m**2/kg")
    print("Gezegenin kütlesi:",planetM,"kg")
    r1a=h[0]
    r1p=h[1]
    r2a=h[6] #hohman ve bi-eliptik hohman kullanınca aynı anda 5. yörüngenin en uzak noktası r5a
    r2p=h[1] #hohman ve bi-eliptik hohman kullanınca aynı anda 5. yörüngenin en yakın noktası r5p
    r3a=h[4]
    r3p=h[5]

    r1a=r1a+planetr
    r1p=r1p+planetr
    r2a=r2a+planetr
    r2p=r2p+planetr
    r3a=r3a+planetr
    r3p=r3p+planetr

    h1=(2*mu*((r1a*r1p)/(r1a+r1p)))**(1/2)
    h2=(2*mu*((r2a*r2p)/(r2a+r2p)))**(1/2)
    h3=(2*mu*((r3a*r3p)/(r3a+r3p)))**(1/2)

    V1A=h1/r1p #A noktasında 1. yörüngenin hızı
    V1At1=h2/r1p #1. yörüngenin A noktasında 1.transfer yörüngesinin hızı
    DVA=abs(V1At1-V1A)#Delta VA
    V3Bt2=h3/r3p #3. yörüngenin B noktasında 2.transfer yörüngesinin hızı
    V2B=h2/r3p
    DVB=abs(V3Bt2-V2B)#Delta VB

    DV=DVA+DVB

    timeForHohmanTransfer=TimeForHohmanTransfer(h,planetR,planetM,G)
    print("Hohman Transferi için geçen süre:",timeForHohmanTransfer,"gün")
    return DV,timeForHohmanTransfer

def BiEliptikHohmanTransfer(be,planetR,planetM,G):
    planetr=planetR/2 #çapı yarıçap haline getir o gezegen için
    mu=G*planetM*10**-9#gezegene özel mü değeri km**3 /s**2 ye çevirdik
    print("Gezegenin mü değeri:",mu,"km**3/s**2")
    print("Çekim sabiti:",G,"N*m**2/kg")
    print("Gezegenin kütlesi:",planetM,"kg")
    r1a=be[0]
    r1p=be[1]
    r2a=be[2]
    r2p=be[3]
    r3a=be[4]
    r3p=be[5]
    r4a=be[6]
    r4p=be[7]
    r1a=r1a+planetr
    r1p=r1p+planetr
    r2a=r2a+planetr
    r2p=r2p+planetr
    r3a=r3a+planetr
    r3p=r3p+planetr
    r4a=r4a+planetr
    r4p=r4p+planetr
    h1=(2*mu*((r1a*r1p)/(r1a+r1p)))**(1/2)
    h2=(2*mu*((r2a*r2p)/(r2a+r2p)))**(1/2)
    h3=(2*mu*((r3a*r3p)/(r3a+r3p)))**(1/2)
    h4=(2*mu*((r4a*r4p)/(r4a+r4p)))**(1/2)
    V1A=h1/r1p # 1. yörüngenin A noktasında hızı

    V2A=h2/r1p #2. yörüngenin A noktasındaki hızı
    V2B=h2/r2a #2. yörüngenin  B noktasındaki hızı
    V3B=h3/r3a #3. yörüngenin  B noktasındaki hızı
    V3C=h3/r3p #3. yörüngenin  C noktasındaki hızı
    V4C=h4/r4p #4. yörüngenin  C noktasındaki hızı

    DVA=abs(V2A-V1A)#Delta VA
    DVB=abs(V3B-V2B)#Delta VB
    DVC=abs(V4C-V3C)#Delta VC

    DV=DVA+DVB+DVC

    timeForBiEliptikHohmanTransfer=TimeForBiEliptikHohmanTransfer(be,planetR,planetM,G)
    print("Bi-Eliptih Hohman Transferi için geçen süre:",timeForBiEliptikHohmanTransfer,"gün")
    return DV,timeForBiEliptikHohmanTransfer

def TimeForBiEliptikHohmanTransfer(be,planetR,planetM,G):
    planetr=planetR/2 #çapı yarıçap haline getir o gezegen için
    mu=G*planetM*10**-9#gezegene özel mü değeri km**3 /s**2 ye çevirdik

    r2a=be[2]
    r2p=be[3]
    r3a=be[4]
    r3p=be[5]

    r2a=r2a+planetr
    r2p=r2p+planetr
    r3a=r3a+planetr
    r3p=r3p+planetr

    a2=(r2a+r2p)/2 #km
    a3=(r3a+r3p)/2 #km

    timeForBiEliptikHohmanTransfer1=(pi*(a2**(3/2)))/(mu**(1/2)) #saniye cinsinden
    timeForBiEliptikHohmanTransfer1=timeForBiEliptikHohmanTransfer1/(60*60*24) # gün cinsinden
    timeForBiEliptikHohmanTransfer2=(pi*(a3**(3/2)))/(mu**(1/2)) #saniye cinsinden
    timeForBiEliptikHohmanTransfer2=timeForBiEliptikHohmanTransfer2/(60*60*24) # gün cinsinden
    timeForBiEliptikHohmanTransfer=timeForBiEliptikHohmanTransfer1+timeForBiEliptikHohmanTransfer2 #bi eliptik hohmanda iki yörüngede geçen süreyi topluyoruz
    return timeForBiEliptikHohmanTransfer

def TimeForHohmanTransfer(h,planetR,planetM,G):
    planetr=planetR/2 #çapı yarıçap haline getir o gezegen için
    mu=G*planetM*10**-9#gezegene özel mü değeri km**3 /s**2 ye çevirdik

    r2a=h[6]
    r2p=h[1]

    r2a=r2a+planetr
    r2p=r2p+planetr

    a2=(r2a+r2p)/2 #km
    timeForHohmanTransfer=(pi*(a2**(3/2)))/(mu**(1/2)) #saniye cinsinden
    timeForHohmanTransfer=timeForHohmanTransfer/(60*60*24) # gün cinsinden
    return timeForHohmanTransfer

if girdiTransfer in transferTypeNameList: #transfer ismi transfer ismi listesinde var is
    transferNumber=transferTypeNameList.index(girdiTransfer) #liste içinde transferin bulunduğu sırayı bul

if girdiGezegen in planetNameList: #girdi gezegen gezegen ismi listesinde var ise
    planetNumber=planetNameList.index(girdiGezegen) #liste içinde gezegenin bulunduğu sırayı bul

transferName=transferTypeNameList[transferNumber] #sıraya karşılık gelen ismi ver
planetR,planetM=planetFeatureList[planetNumber] #siraya karşılık gelen gezegeni ver
"""
def TransferKarsilastir(h,be,planetR,planetM,G):

    DVHohman,timeForHohmanTransfer=HohmanTransfer(h,planetR,planetM,G)
    DVHohmanTransfer=round(DVHohman,4) #virgülden sonra 4 basamağa yuvarladık
    print("Hohman Transferi için toplam hız değişimi:",DVHohmanTransfer)
    DVBiEliptik,timeForBiEliptikHohmanTransfer=BiEliptikHohmanTransfer(be,planetR,planetM,G)
    DVBiEliptikHohmanTransfer=round(DVBiEliptik,4)
    print("Bi-Eliptik Hohman Transferi için toplam hız değişimi:",DVBiEliptikHohmanTransfer)
TransferKarsilastir(h,be,planetR,planetM,G)
"""
if transferName=="h":
    DVHohman,timeForHohmanTransfer=HohmanTransfer(h,planetR,planetM,G)
    DVHohmanTransfer=round(DVHohman,4) #virgülden sonra 4 basamağa yuvarladık
    print("Hohman Transferi için toplam hız değişimi:",DVHohmanTransfer)
elif transferName=="be":
    DVBiEliptik,timeForBiEliptikHohmanTransfer=BiEliptikHohmanTransfer(be,planetR,planetM,G)
    DVBiEliptikHohmanTransfer=round(DVBiEliptik,4)
    print("Bi-Eliptik Hohman Transferi için toplam hız değişimi:",DVBiEliptikHohmanTransfer)
