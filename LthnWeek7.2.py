def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result

def tampilkan_deret(n):
    for i in range(n, 0, -1):
        nilai_faktorial = factorial(i)
        urutan = " ".join(str(j) for j in range(i, 0, -1))
        print(f"{nilai_faktorial} {urutan}")

n = int(input("Masukkan nilai n: "))
if n > 0:
    tampilkan_deret(n)
else:
    print("Masukkan bilangan positif.")
