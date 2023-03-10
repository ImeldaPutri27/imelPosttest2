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
        # Jika nilai yang dicari berada di antara arr[left] dan arr[right], Maka pencarian selesai
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