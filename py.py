# Verilen bir pozitif tam sayı n için, belirli koşullara göre çeşitli durumları kontrol etmemiz gerekiyor. İşte bu durumları kontrol etme adımları:

# Eğer n tek sayı ise, "Weird" yazdır.
# Eğer n çift sayı ise:
# Eğer n 2 ile 5 arasında (2 ve 5 dahil) ise, "Not Weird" yazdır.
# Eğer n 6 ile 20 arasında (6 ve 20 dahil) ise, "Weird" yazdır.
# Eğer n 20'den büyük bir çift sayı ise, "Not Weird" yazdır.

# def check_number(n):
#     if n%2==1:
#         return 'weird'
#     elif n%2==0:
#         if 2<=n<=5:
#             return 'not weird'
#         elif 6<=n<=20:
#             return 'weird'
#         elif n>=20:
#             return 'not weird'
        
# number = check_number(24)
# print(number)
def simpleArraySum(ar):
    total=0
    for i in ar:
        total+=i
    print(total)
simpleArraySum([1,2,3,4,10,11])   