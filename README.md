# SEARCHING
# 1. JUMP SEARCH
Algoritma yang digunakan pada pencarian data dibawah ini menggunakan Jump Search, yang mana Algoritma ini berfungsi untuk pencarian lompat atau pencarian blok

# List Data
var = ["Arsel","Avivah","Daiva",["Wahyu","Wibi"]]

# Pencarian Data Dengan Algoritma Jump Searching
"""Fungsi Pencarian Jump Searching"""
def jump (arr, value):
    n = len (arr)
    step = int (n ** 0.5)

    left, right = 0, 0 
    while left < n and arr [left] <= value:
        right = min(n-1, left + step)
        if arr [left] <= value and arr [right] >= value:
            break

        left += step 
        if left >= n or arr[left] > value:
            return -1 
        
    right = min (n-1, right)
    i = left 
    while i <= right and arr [i] <= value:
        if arr [i] == value:
            return i
        i += 1 
        return -1
    
# Output Pencarian Data dan Menampilkan Data
print("1. Arsel di index: ", var.index("Arsel"))
print("2. Avivah di index: ", var.index("Avivah")) 
print("3. Daiva di index: ", var.index("Daiva")) 
print("4. Wahyu di index 3 pada kolom 0", var[3][0]) 
print("5. Wibi di index 3 pada kolom 1", var[3][1])

# Hasil 
1. Arsel di index:  0
2. Avivah di index:  1
3. Daiva di index:  2
4. Wahyu di index 3 pada kolom 0 Wahyu
5. Wibi di index 3 pada kolom 1 Wibi  

# Penjelasan Cara Kerja Program dan Setiap Elemen yang dipakai
Program di atas ini mengimplementasikan algoritma jump search untuk melakukan pencarian data pada list `var`. Fungsi `jump(arr, value)` akan menerima dua argumen yaitu list yang akan dicari dan nilai yang akan dicari. Algoritma jump search akan mencari nilai yang lebih besar dari value pada setiap langkah atau step dengan jumlah step yang ditentukan oleh variabel `step`. Langkah awal dimulai dari indeks 0 untuk kiri dan indeks `step - 1` untuk kanan. Jika nilai yang dicari berada di antara `arr[left]` dan `arr[right]`, maka pencarian selesai. Jika nilai yang dicari lebih besar dari `arr[right]`, maka akan dilanjutkan ke step berikutnya. Fungsi `var.index(value)` digunakan untuk mencari indeks dari nilai `value` pada list `var`. Sedangkan `var[3][0]` digunakan untuk me-return elemen pada indeks ke-0 dalam list yang berada pada indeks ke-3. Sedangkan `var[3][1]` digunakan untuk me-return elemen pada indeks ke-1 dalam list yang berada pada indeks ke-3.

# 2. Sequential Search
Algoritma yang digunakan pada pencarian data dibawah ini menggunakan Sequential Search. Sequential ini merupakan pencarian sederhana yang bekerja dengan cara mengecek setiap elemen pada suatu list secara berurutan.

# List Data
var = ["Arsel","Avivah","Daiva",["Wahyu","Wibi"]]

# Pencarian Data Dengan algoritma Sequential Searching
"""Fungsi Pencarian Sequtial search"""
def search_data(data,value):

    """iterasi setiap elemen pada list"""
    for i in range (len(data)):
        if isinstance (data[i],list):
            for j in range (len(data[i])):
                if data [i][j] == value:
                    return(i,j)
        else:
            """Jika Nilai Elemen Sama dengan Nilai yang dicari"""
            if data[i] == value:
                return i
    return None

# Output Pencarian Data dan Menampilkan
print ("1. Arsel di index: ",search_data(var,"Arsel"))
print ("   Avivah di index: ",search_data(var,"Avivah"))
print ("   Daiva di index: ",search_data(var,"Daiva"))
print ("2. Wahyu di index: ",search_data(var,"Wahyu"))
print ("3. Wibi di index: ",search_data(var,"Wibi"))

# Hasil
1. Arsel di index:  0
   Avivah di index:  1    
   Daiva di index:  2     
2. Wahyu di index:  (3, 0)
3. Wibi di index:  (3, 1) 

# Penjelasan Cara Kerja Program dan Setiap Elemen yang dipakai
Program di atas menggunakan algoritma sequential search untuk mencari data pada list `var`. Fungsi `search_data(data, value)` menerima dua argumen yaitu list `data` yang akan dicari dan `value` yang akan dicari. Fungsi ini akan mencari nilai `value` pada setiap elemen pada list `data` secara berurutan, dimulai dari indeks 0 hingga indeks terakhir. Jika elemen yang di cek dalam bentuk list, maka fungsi akan mengecek semua elemen pada list yang bersangkutan. Program ini mencari beberapa nilai pada list `var` menggunakan fungsi `search_data`. Jika nilai yang dicari tidak ditemukan, maka dicetak `None`.
