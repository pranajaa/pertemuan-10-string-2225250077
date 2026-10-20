
def normalisasi_nama(nama):
    nama = nama.strip()
    return nama.title()


def buat_inisial(nama):
    kata = nama.split()
    inisial = ""

    for k in kata:
        inisial += k[0].upper()

    return inisial


def normalisasi_kode(kode):
    kode = kode.strip().upper()
    kata = kode.split()
    kode_bersih = "-".join(kata)

    return kode_bersih


nama = " "
kode = " "

nama_bersih = normalisasi_nama(nama)
kode_bersih = normalisasi_kode(kode)
jumlah_kata = len(nama_bersih.split())
inisial = buat_inisial(nama_bersih)

print("Nama bersih :", nama_bersih)
print("Kode kelas  :", kode_bersih)
print("Jumlah kata :", jumlah_kata)
print("Inisial     :", inisial)
