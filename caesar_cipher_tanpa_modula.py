#membuat program enkripsi dan dekripsi caesar menggunakan python

#Rumus Enkripsi : (n + key) 
#Rumus Dekripsi : (n - key)

#n = merupakan urutan dari abjad yang diinput
#key = merupakan kunci dekripsi atau enkripsi 


print("****************** Program Caesar Cipher *******************")

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#alphabet berfungsi untuk menampung nilai alphabet yang ada

#fungsi enkripsi dengan parameter alphabet
def enkripsi(alphabet):
    str = input("Plaintext : ")        #input plaintext yang akan di enkripsi
    key = int(input("Key : "))      #kunci untuk pergeseran alphabet (enkripsi)
    
    str = str.lower()       #string dikonversi ke huruf kecil semua
    result = ''             #deklarasi variable result dengan nilai awal adalah kosong
    
    for char in str:        #membuat perulangan untuk pergeseran abjad dari string
        if char in alphabet:   #abjad string dipecah satu satu dan di cek apakah terdapat dalam value alphabet
            n = alphabet.index(char)   #jika ada maka nilai index dari alphabet yang ditemukan disimpan dalam variabel n
            encrypt = (n + key)   #rumus enkripsi
            convert = alphabet[encrypt]    #konversi nilai string ke hasil enkripsi
            result = result + convert   #alphabet yang sudah dikonversi disimpan dalam variabel result dalam string
        else:
            result = result + ' '   #jika alphabet dari string tidak ditemukan dalam index alphabet, maka akan dirubah dalam bentuk spasi
            
    print(f"Result : {result}")      #hasil dari perulangan untuk enkripsi string ditampilkan
    
#fungsi dekripsi dengan parameter alphabet
def dekripsi(alphabet):
    str = input("Ciphertext : ")   #input Ciphertext yang akan di dekripsi
    key = int(input("Key : "))      #kunci untuk pergeseran alphabet (dekripsi)
    
    str = str.lower()       #string dikonversi ke huruf kecil semua
    result = ''             #deklarasi variable result dengan nilai awal adalah kosong
    
    for char in str:        #membuat perulangan untuk pergeseran alphabet dari string
        if char in alphabet:   #abjad string dipecah satu satu dan di cek apakah terdapat dalam value alphabet
            n = alphabet.index(char)   #jika ada maka nilai index dari alphabet yang ditemukan disimpan dalam variabel n
            encrypt = (n - key)   #rumus dekripsi
            convert = alphabet[encrypt]    #konversi nilai string ke hasil dekripsi
            result = result + convert   #alphabet yang sudah dikonversi disimpan dalam variabel result dalam string
        else:
            result = result + ' '   #jika alphabet dari string tidak ditemukan dalam index alphabet, maka akan dirubah dalam bentuk spasi
            
    print(f"Result : {result} ")      #hasil dari perulangan untuk dekripsi string ditampilkan

#pembuatan menu
pilihan = 'y'

while (pilihan == 'y'):
    print("Masukkan Pilihan :")
    print("1. Enkripsi Data")
    print("2. Dekripsi Data")
    print("3. Keluar")
    
    menu =input("Menu yang dipilih : ")
    print("********************")
    
    if menu == '1':
        print("Menu Enkripsi Data")
        enkripsi(alphabet)
    elif menu == '2':
        print("Menu Dekripsi Data")
        dekripsi(alphabet)
    elif menu == '3':
        print("Program Selesai")
        break
    else:
        print("Menu tidak valid!!")
    
    
    print("********************")
    pilihan = input("Apakah Anda ingin melanjutkan ? (y/n) : ")
    print("********************")
    







    
    
