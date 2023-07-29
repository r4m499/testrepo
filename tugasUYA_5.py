# Tampilkan daftar harga ayam
print('\nGEROBAK FRIED CHICKEN')
print('-' * 54)
print('Kode\tJenisPotong\t\tHarga')
print('D\t\tDada\t\t\tRp.2500')
print('P\t\tPaha\t\t\tRp.2000')
print('S\t\tSayap\t\t\tRp.1500')
print('-' * 54)

# Harga ayam per potong
dada_harga = 2500
paha_harga = 2000
sayap_harga = 1500

# Input banyak jenis
banyak_jenis = int(input('Banyak Jenis: '))

# Input jenis potong dan banyak beli untuk setiap jenis
total_harga = 0
daftar_beli = []
for i in range(banyak_jenis):
    jenis_ke = i + 1
    print(f'Jenis Ke-{jenis_ke}')
    kode_potong = input('Kode Potong[D/P/S]: ')
    while kode_potong not in ['D', 'P', 'S']:
        kode_potong = input('Kode Potong[D/P/S]: ')
    if kode_potong == 'D':
        jenis_potong = 'Dada'
        harga_satuan = dada_harga
    elif kode_potong == 'P':
        jenis_potong = 'Paha'
        harga_satuan = paha_harga
    elif kode_potong == 'S':
        jenis_potong = 'Sayap'
        harga_satuan = sayap_harga
    banyak_beli = int(input('Banyak Potong: '))
    jumlah_harga = harga_satuan * banyak_beli
    daftar_beli.append([jenis_potong, harga_satuan, banyak_beli, jumlah_harga])
    total_harga += jumlah_harga

# Tampilan layar keluaran
print('\nGEROBAK FRIED CHICKEN')
print('-' * 54)
print('No.\tJenis\t\tHarga\t\tBanyak\tJumlah')
print('\tPotong\t\tSatuan\t\tBeli\tHarga')
no = 1
for i in range(len(daftar_beli)):
    jenis_potong, harga_satuan, banyak_beli, jumlah_harga = daftar_beli[i]
    print(f'{no}\t{jenis_potong}\t\t{harga_satuan}\t\t{banyak_beli}\t\t{jumlah_harga}')
    no += 1
print('-' * 54)
pajak = total_harga * 0.1
total_bayar = total_harga + pajak
print(f'\t\t\t\t\tJumlah Bayar Rp {total_harga}')
print(f'\t\t\t\t\tPajak 10% Rp {pajak}')
print(f'\t\t\t\t\tTotal Bayar Rp {total_bayar}')