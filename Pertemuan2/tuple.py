nama_musim = ('semi', 'panas', 'gugur', 'dingin')
print('jumlah musim non tropis:', len(nama_musim))

nama_musim_lengkap = 'hujan', 'kemarau', nama_musim
print('jumlah musim keseluruhan:', len(nama_musim_lengkap))
print('nama-nama musim tropis dan non tropis adalah:', nama_musim_lengkap)
print('nama musim tropis:', nama_musim_lengkap[0:2])
print('nama musim non tropis:', nama_musim_lengkap[2])
print('nama musim terakhir dari musim non tropis: ', nama_musim_lengkap[2][-1])

jumlah_musim = len(nama_musim_lengkap) - 1 + len(nama_musim_lengkap[2])

print('jumlah musim keseluruhan sebenarnya adalah :', jumlah_musim)
