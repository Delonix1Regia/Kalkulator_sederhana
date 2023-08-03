// Kalkulator sederhana menggunakan Python



print('Program Kalkulator Sederhana')

bil1 = float(input('Bilangan pertama : '))
bil2 = float(input('Bilangan kedua : '))
operasi = input('Operasi matematika : ')

if operasi == '+':
    hasil = bil1 + bil2
    print('Hasil penjumlahan dari ', bil1, ' dan ', bil2, ' adalah ', hasil)
elif operasi == '-':
    hasil = bil1 - bil2
    print('Hasil pengurangan dari ', bil1, ' dan ', bil2, ' adalah ', hasil)
elif operasi == '*':
    hasil = bil1 * bil2
    print('Hasil perkalian dari ', bil1, ' dan ', bil2, ' adalah ', hasil)
elif operasi == '/':
    hasil = bil1 / bil2
    print('Hasil pembagian dari ', bil1, ' dan ', bil2, ' adalah ', hasil)
else:
    print('Operasi tidak valid')