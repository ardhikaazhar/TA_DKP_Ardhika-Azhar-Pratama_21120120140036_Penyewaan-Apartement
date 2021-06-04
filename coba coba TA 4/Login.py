class Login():

    def __init__(self, tipe, bln, hasil):
            self.bln = bln
            self.hasil = hasil
            self.tipe = tipe

    def hasil_set(self):
                bln = int(self.bln)
  
                tipe1 = 2700000
                tipe2 = 3000000
                tipe3 = 4500000
                tipe4 = 6000000
                tipe5 = 10000000

                if self.tipe == "Tipe 1":
                    total = bln * tipe1
                    biayakeseluruhan = total
                    self.hasil = ("biaya untuk tipe 1 adalah Rp2.700.000/Bulan total harga yang perlu dibayar adalah ", biayakeseluruhan)
                
                elif self.tipe == "Tipe 2":
                    total = bln * tipe2
                    biayakeseluruhan = total
                    self.hasil = ("biaya untuk tipe 2 adalah Rp3.000.000/Bulan total harga yang perlu dibayar adalah ", biayakeseluruhan)
                
                elif self.tipe == "Tipe 3":
                    total = bln * tipe3
                    biayakeseluruhan = total
                    self.hasil = ("biaya untuk tipe 3 adalah Rp4.500.000/Bulan total harga yang perlu dibayar adalah ", biayakeseluruhan)
                
                elif self.tipe == "Tipe 4":
                    total = bln * tipe4
                    biayakeseluruhan = total
                    self.hasil = ("biaya untuk tipe 4 adalah Rp6.000.000/Bulan total harga yang perlu dibayar adalah ", biayakeseluruhan)
                
                elif self.tipe == "Tipe 5":
                    total = bln * tipe5
                    biayakeseluruhan = total
                    self.hasil = ("biaya untuk tipe 5 adalah Rp10.000.000/Bulan total harga yang perlu dibayar adalah ", biayakeseluruhan)
                

    def hasil_get(self):
        return self.hasil