daftar_kelompok1 = ['ana', 'budi', 'cinthya', 'deni', 'eka']
print('jumlah anggota kelompok 1 :', len(daftar_kelompok1))

print('anggotanya terdiri dari: ')

print('fatma masuk ke kelompok 1')
daftar_kelompok1.append('fatma')
print('jumlah anggota kelompok 1 :', len(daftar_kelompok1))
print('anggota kelompok 1 sekarang adalah :', daftar_kelompok1)

print('anggota terakhir dalam kelompok 1 adalah', daftar_kelompok1[-1])
anggota_pertama = daftar_kelompok1[0]
print('anggota pertama sudah mendapat giliran presentasi : ',
      anggota_pertama)

del daftar_kelompok1[0]

print('giliran berikutnya adalah selain anggota pertama :',
      daftar_kelompok1)

anggota_kedua = daftar_kelompok1[1]
print('anggota kedua sudah mendapat giliran presentasi : ',
      anggota_kedua)

del daftar_kelompok1[1]

print('giliran berikutnya adalah selain anggota pertama :',
      daftar_kelompok1)
