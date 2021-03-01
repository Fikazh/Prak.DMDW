negara_asean = set(['indonesia', 'singapura', 'malaysia'])
print('indonesia' in negara_asean)
print('italia' in negara_asean)

negara_asean2 = negara_asean

negara_asean3 = negara_asean.copy()
negara_asean3.add('filipina')

print(negara_asean3)
print(negara_asean3.issuperset(negara_asean))
print(negara_asean2 & negara_asean3)
print(negara_asean2.intersection(negara_asean))

# negara_asean3.remove('amerika')

# print(negara_asean2.issuperset(negara_asean))

# negara_asean2.remove('singapura')
# print(negara_asean & negara_asean!)
