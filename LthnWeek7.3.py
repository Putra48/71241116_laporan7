def generate_series(tinggi, lebar):
    count = 1
    for i in range(tinggi):
        for j in range(lebar):
            print(count, end=" \t" if j < lebar - 1 else "\n")
            count += 1
        if (i + 1) % 3 == 0:  
            print()

tinggi = int(input("Masukkan tinggi: "))
lebar = int(input("Masukkan lebar: "))

generate_series(tinggi, lebar)
