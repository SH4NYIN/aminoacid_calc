# initialization of the elements in use
class elem:
    def __init__(self, enum, name, abbr, mw, isos, mw_use):
        self.enum = enum
        self.name = name
        self.abbr = abbr
        self.mw = mw            # original mw
        self.isos = isos     # isotope mw
        self.mw_use = mw_use    # used mw (for calc)
    def check_marked(self):
        # for name,value in vars(self).items():
        # for self.enum in range (0, 5):
        if Elem_marked == self.abbr or self.name:
            self.mw_use = self.isos

C = elem(1, "Carbon", "C", 12.011, 14.0032, 12.011)
H = elem(2, "Hydrogen", "H", 1.0080, 2.01410, 1.0080)
O = elem(3, "Oxygen", "O", 15.999, 17.9992, 15.999)
N = elem(4, "Nitrogen", "N", 14.007, 15.00011, 14.007)
S = elem(5, "Sulfur", "S", 32.06, 33.9679, 32.06)

# check the elem to be marked
Elem_marked = str(input("Input the element to be marked with isotope: "))
for key in {C:1, H:2, O:3, N:4, S:5}:
    elem.check_marked(key)



class amino_acid:
    def __init__(self, name, C, H, O, N, S, Mw):
        self.name = name
        self.C = C
        self.H = H
        self.O = O
        self.N = N
        self.S = S
        self.Mw = Mw
    def MoleWeight(self):
        # for name,value in vars(self).items():
            # print("%s=%s"%(name,value))
        self.Mw = self.C * C.mw_use + self.H * H.mw_use + self.O * O.mw_use + self.N * N.mw_use + self.S * S.mw_use

Ami_A = amino_acid("Alanine", 3, 5, 1, 1, 0, 0)
# Ami_A.Mw += C.mw * Ami_A.C

Ami_A.MoleWeight()
print("Amino Acid A's Molar Weight is ", Ami_A.Mw)

