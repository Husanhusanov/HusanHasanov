11 #dars mavzu
1
# yosh = int(input('Yoshingiz nechida'))
# if yosh<=4:
#     print('Sizga kirish bepul')
# elif yosh<=12:
#     print(" Sizga kirish 5000 so'm")    
# elif yosh<=18:
#     print(" Sizga kirish 7000 so'm")
# else:
#     print(" Sizga kirish 10000 so'm")        
2
# yosh = int(input('Yoshingiz nechida'))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000   
# elif yosh<=65:
#     price = 10000
# elif yosh<=80:
#     price = 8000    
# else: # 80 yoshdan kattalarga tekin
#     price = 'tekin 0'  
# print(f"Sizga kirish {price} s'om")
3
# yosh = int(input('Yoshingiz nechida'))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000   
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000    
# print(f"Sizga kirish {price} s'om")
4 
# kun = input("Bugun haftaning kun qaysi kuni?")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print(f"Bugun {kun} dam olish kuni")
# else:
#     print(f"Bugun {kun} ish kuni")
5
# kun = input("Bugun haftaning kun qaysi kuni ? ")
# harorat = float(input("Havo harorati qanday ? "))
# if kun.lower() =='yakshanba' and harorat>=30:
#     print(f"Bugun {kun} Cho'milgani ketdik!")
# elif kun.lower() =='yakshanba' and harorat<=30:
#     print(f"Uyda {kun} dam olamiz!")
# else:
#     print("Bugun ish kuni")
6
# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print(f"{kun} Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print(f"Uyda {kun} dam olamiz!")
# elif (kun.lower()==kun or kun.lower()==kun) and harorat>=30:
#     print(f"Bugun {kun} ish kuni")   
7
# narx = 15000 
# choy = True
# salat = False
# if choy and salat:
#     narx=narx+10000
# elif choy or salat:
#     narx=narx+5000
# print(f"Jami {narx} so'm")
8         
# narx = 15000 
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:
#     print("Mijoz choy oldi")
#     narx = narx+3000
# if salat:
#     print("Mijoz salat oldi")
#     narx = narx + 5000
# if non:
#     print("Mijoz non oldi")
#     narx = narx + 2000
# if kompot:
#     print("Mijoz kompot oldi")
#     narx = narx + 5000
# if assorti:
#     print("Mijjoz assorti oldi")
#     narx = narx + 15000
# print(f"Jami {narx} s'om")    
9
# narx = 15000 
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:
#     print("Mijoz choy oldi")
#     narx = narx+3000
# if salat:
#     print("Mijoz salat oldi")
#     narx = narx + 5000
# if non:
#     print("Mijoz non oldi")
#     narx = narx + 2000
# if kompot:
#     print("Mijoz kompot oldi")
#     narx = narx + 5000
# if assorti:
#     print("Mijjoz assorti oldi")
#     narx = narx + 15000
# print(f"Jami {narx} s'om")    
10
# menu = ['osh','qazonkabob', 'xod dog','pizza','shashlik','norin','somsa', 'lavash','chisburger','manti','billish perashka', "lagmon",'kichra', 'mastava', 'serdak xamir ovqat', 'shirgurich',"sho'rva",'muzqaymoq']
# ovqat = input('Nima ovqat yeysiz? ')
# if ovqat.lower() in menu:
#     print(f"Siz {ovqat} buyurtma qildingiz 5 daqiqada olib kelamiz")
# else:
#     print(f"Afsuski bizda {ovqat} bunday ovqat yo'q iltimos boshqa ovqat buyuring bizning menu {menu} ")
11
# menu = ['osh','qazonkabob', 'xod dog','pizza','shashlik','norin','somsa', 'lavash','chisburger',
#         'manti','billish perashka', "lagmon",'kichra', 'mastava', 'serdak xamir ovqat', 'shirgurich',"sho'rva",'muzqaymoq']
# ovqat = input('Nima ovqat yeysiz? ')
# for taom in menu:
#     if taom in ovqat:
#         print(f"Siz {ovqat} buyurtma qildingiz 5 daqiqada olib kelamiz")
# else:
#     print(f"Afsuski bizda {ovqat} bunday ovqat yo'q iltimos boshqa ovqat buyuring bizning menu {menu} ")
12
# menu = ['osh','qazonkabob', 'xod dog','pizza','shashlik','norin','somsa', 'lavash','chisburger',
#         'manti','billish perashka', "lagmon",'kichra', 'mastava', 'serdak xamir ovqat', 'shirgurich',"sho'rva",'muzqaymoq']
# ovqat = input('Nima ovqat yeysiz? ')
# if ovqat.lower() not in menu:
#     print(f"Afsuski bizda {ovqat} bunday ovqat yo'q iltimos boshqa ovqat buyuring bizning menu {menu} ")
# else:
#     print(f"Siz {ovqat} buyurtma qildingiz 5 daqiqada olib kelamiz")
13
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ['osh','qazonkabob', 'xod dog','pizza','shashlik','norin','somsa', 'lavash','chisburger', 'shashlik']
# if buyurtmalar:
#   for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: 
#     print("Savatchangiz bo'sh!")
1 #vazifalar 
# son =int(input("Juft son kiriting"))
# if (son%2==0):
#     print('Bu juft son rahmat')
# else:
#     print('Bu juft son emas')
2
# yosh = int(input('Yoshingiz nechida'))
# if yosh<=4 or yosh>=60:
#     print('Sizga kirish bepul')
# elif yosh<=12:
#     print(" Sizga kirish 5000 so'm")    
# elif yosh<=18:
#     print(" Sizga kirish 10000 so'm")
# else:
#     print(" Sizga kirish 20000 so'm")   
3
# son_bir = float(input("Birinchi soni kiriting"))
# son_ikki = float(input("Ikkinchi soni kiriting"))
# if (son_bir==son_ikki):
#     print(f" Son_bir va Son_ikki sonlar teng {son_bir}={son_ikki}")
# if (son_bir>son_ikki):
#     print(f"Son_bir son katta {son_bir}>{son_ikki}") 
# if (son_bir<son_ikki):
#     print(f"Son_ikki son katta {son_bir}<{son_ikki}")        
4
# maxsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#         'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing "))
# print(savat)
# for m in savat:
#     if m in maxsulotlar:
#         print(f"Do'konimizda {m} bor")
#     else:
#         print(f"Do'konimizda uzur {m} yo'q")    
5
# maxsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', "mo'l go'shti"
#         'kartoshka', 'olma', 'banan', 'uzum', 'qovun',"qo'y go'shti"]
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing "))
# bor_maxsulotlar = []
# mavjud_emas = []    
# for maxsulot in savat:
#     if maxsulot in maxsulotlar:
#         bor_maxsulotlar.append(maxsulot)
#     else:
#         mavjud_emas.append(maxsulot) 
# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")    
6
# user = ['Husan', "Hasan", "Alisher", "Umar", 'Aziza']
# login = input("Yangi login tanlang")
# if login in user:
#     print("Login band yangi logini tanlang")
# else:
#     print(f"Hush kelibsiz {login.title()}!")  
7
# son = int(input("Istalgan butun soni kiriting"))
# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} qoldiqsiz bo'linadi")