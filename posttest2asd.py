#List Data
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