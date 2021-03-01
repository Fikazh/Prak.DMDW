data_mhs = {'1010511001': 'Andi', '1010511002': 'Betty', '1010511003': 'Cokro'}
print('nama mahasiswa dengan nim 1010511002:', data_mhs['1010511002'])

# menghapus item
del data_mhs['1010511003']
print('terdapat ', len(data_mhs), ' data mahasiswa')

# tambah entri
data_mhs['1010511004'] = 'Denis'
print(data_mhs)

data_mhs['1010511004'] = 'Dika'
print(data_mhs)

data_mhs['1010511004'] = None
print(data_mhs)
