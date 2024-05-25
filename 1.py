mahasiswa = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
nilai_unik = sorted(set(nilai for nama, nilai in mahasiswa))
nilai_terendah_kedua = nilai_unik [1]
siswa_terendah_kedua = []

for nama, nilai in mahasiswa :
    if nilai == nilai_terendah_kedua :
        siswa_terendah_kedua.append(nama)

siswa_terendah_kedua.sort()

for nama in siswa_terendah_kedua :
    print(nama)
    