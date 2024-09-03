#Dict yapısını gördük burada key -> value yapısının çalışma mantığını öğrendik .
#d = {'CRINGE': 'Utanç Verici' , 'Overrated':'Abartılmış'}
#print(d['Overrated'],d['CRINGE'])

#ogrenci = {'Deniz': {'Not':80,'ogrenci_no': 715},'Ahmet': {'Not':60,'ogrenci_no': 850}}
#ogrenci['Deniz']['Not'] = ogrenci['Deniz']['Not']+5
#ogrenci['Ayşe'] = {'Not': 40,'ogrenci_no':452}

my_dict = {}


#while True:
#    key = input('Lütfen anahtar(key) bilgisini girin (Çıkmak için "exit" yazın ')
#    if key.lower() == 'exit':
#        break
    
#    value = input(f"Lütfen [key] için bir (value) girin : ")
#    my_dict[key] = value
#    print('Sözlükteki değerler : ')
#    print(my_dict)



# Boş bir sözlük oluşturuyoruz
my_dict = {}

# Döngü sayısını belirliyoruz
num_iterations = 5

# Belirtilen sayıda kez döngü
for i in range(num_iterations):
    # Anahtar bilgisi alıyoruz
    key = input(f"Lütfen {i+1}. anahtar (key) bilgisini girin: ")
    
    # Değer bilgisi alıyoruz
    value = input(f"Lütfen '{key}' için değer (value) girin: ")
    
    # Anahtar-değer çiftini sözlüğe ekliyoruz
    my_dict[key] = value

# Sözlüğü ekrana yazdırıyoruz
print("Sözlükteki değerler:")
print(my_dict)


