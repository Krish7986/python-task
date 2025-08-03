class chirajeevi:
    def c_assets(self):
        self.worth = 1000
        print(f"the net worth of chiranjeevi{self.worth} cr")
class ramcharan(chirajeevi):
    def r_assets(self):
        self.worth1 = 500
        print(f" the net worth of ramcharan{self.worth1}")
        super().c_assets()
    def total(self):
        super().c_assets()
        total_worth = self.worth+self.worth1
        print(f"{total_worth}cr")

net=ramcharan()
# chirajeevi.c_assets(net)
print(net.total())
# net.r_assets()

class megastar:
    def __init__(self,pname,ptag):
        self.pname = pname
        self.ptag = ptag
        print(f"{pname} is marked as {ptag}")
class powerstar():
    def __init__(self,cname,ctag):
        # super().__init__(pname,ptag)
        self.cname = cname
        self.ctag = ctag
        print(f"{cname} is came from megaster")
class megapowerstar(megastar,powerstar):
    def __init__(self, pname, ptag,cname,ctag,gname,gtag):
        megastar.__init__(self,pname, ptag)
        powerstar.__init__(self,cname,ctag)
        self.gname = gname
        self.gtag  = gtag
    def tagline(self):
     print(f"the combination of {self.ptag} and {self.ctag} the referene {self.gtag}")

rc= megapowerstar(pname = "cherajevi", ptag="megastar",
                  cname = "pawan",ctag = "power star",
                  gname = "ramcharan",gtag = "megapowerstar")
ps = powerstar(cname="pawan kalyan",ctag="powerstar")
rc.tagline()