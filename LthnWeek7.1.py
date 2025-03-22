def prima(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def terdekat_terkecil_prima(n):
    for i in range(n - 1, 1, -1):
        if prima(i):
            return i
    return None 

n = int(input("Masukkan bilangan: "))
terdekat_prima = terdekat_terkecil_prima(n)
if terdekat_prima:
    print(f"Bilangan prima terdekat yang lebih kecil dari {n} adalah {terdekat_prima}")
else:
    print("Tidak ada bilangan prima yang lebih kecil dari input.")
