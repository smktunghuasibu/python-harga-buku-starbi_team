def harga_bayaran(jenisbuku,kuantiti):
    if jenisbuku==1:
        harga=6.00
        kadar_diskaun=0.1
       
    elif jenisbuku==2:
        harga=7.50
        kadar_diskaun=0.08
       
    else:
        harga=8.90
        kadar_diskaun=0.05
    potongan_harga=harga*kadar_diskaun*kuantiti
    harga_total=(harga*kuantiti)-potongan_harga
    return potongan_harga,harga_total
 

def main():
    print("Senarai belian buku:")
    print("1.Latihan Pasti A,Bahasa Melayu,Tingkatan 1")
    print("2.Latihan Pasti A,Bahasa Melayu,Tingkatan 2")
    print("3.Latihan Pasti A,Bahasa Melayu,Tingkatan 3")
    while True:
        jenisbuku = int(input("Masukkan jenis buku yang dibeli (1-3): "))
        if jenisbuku > 3 or jenisbuku < 1:
            print("Sila masukkan nombor 1 hingga 3 sahaja.")
        else:
            break # exit when no error 
    kuantiti=int(input("Masukkan kuantiti buku yang dibeli:"))
    potongan_harga,harga_total = harga_bayaran(jenisbuku,kuantiti)
    print("Potongan harga yang diperoleh ialah RM", round(potongan_harga,2))
    print("Jumlah harga yang perlu dibayar ialah RM", round(harga_total,2))
    
if __name__ == "__main__":
    main()
