protein = []
lipid = []
carbohydrate = []
Saturated_fatty_acids = []
n_6_fatty_acids = []
n_3_fatty_acids = []
Dietary_fiber = []
Vitamin_A = []
Vitamin_D = []
Vitamin_E = []
Vitamin_K = []
Vitamin_B1 = []
Vitamin_B2 = []
Vitamin_B6 = []
Vitamin_B12 = []
Niacin = []
Folic_Acid_RDA = []
Pantothenic_Acid = []
Biotin = []
Vitamin_C = []
Sodium_salt_equivalent = []
Potassium = []
Calcium = []
Magnesium = []
Phosphorus = []
Iron = []
Zinc = []
Copper = []
Manganese = []
lodine = []
Selenium = []
Chromium = []
Molybdenum = []
class Nutrition:
    def __init__(self, ene):
        self.e = ene
        self.x = 0
        self.s_ene = 0
        self.s_pro = 0
        self.s_ipi = 0
        self.s_car = 0
        self.s_sod = 0
        

    def app(self):
        for word in self.e:
            new = self.e[self.x]
            if new == "bread":
                pie = int(input("How many pieces of bread?: "))
                new = 164 * pie
                self.e[self.x] = new
                Pr = 4.9 * pie
                protein.append(Pr)
                li = 2.6 * pie
                lipid.append(li)
                Ca = 30.3 * pie
                carbohydrate.append(Ca)
                So = 0.7 * pie
                Sodium_salt_equivalent.append(So)
                self.x += 1
                print(Sodium_salt_equivalent)
        
            if new == "curry":
                pie = 1
                new = 474 * pie
                self.e[self.x] = new
                Pr = 6.5 * pie
                protein.append(Pr)
                li = 34.1 * pie
                lipid.append(li)
                Ca = 44.7 * pie
                carbohydrate.append(Ca)
                So = 2.2 * pie
                Sodium_salt_equivalent.append(So)
                self.x += 1
                print(Sodium_salt_equivalent)
                
            if new == "noodle":
                pie = 1
                new = 500 * pie
                self.e[self.x] = new
                Pr = 8.6 * pie
                protein.append(Pr)
                li = 17 * pie
                lipid.append(li)
                Ca = 62.6 * pie
                carbohydrate.append(Ca)
                So = 5.8 * pie
                Sodium_salt_equivalent.append(So)
                self.x += 1
                print(Sodium_salt_equivalent)
                

        self.s_ene = sum(self.e)
        self.s_pro = sum(protein)
        self.s_lip = sum(lipid)
        self.s_car = sum(carbohydrate)
        self.s_sod = sum(Sodium_salt_equivalent)
            

        if self.s_ene < 2700:
           ins = 2700 - self.s_ene
           r = "Your intake of energy is insufficient for {}kcal.".format(ins)
           print(r)
        else:
           exc = self.s_ene - 2700
           r = "You have an excess of {}kcal of energy.".format(exc)
           print(r)
       
        if self.s_pro < 65:
           ins = 65 - self.s_pro
           r = "Your intake of protein is insufficient for {} grams.".format(ins)
           print(r)
        elif self.s_pro >= 65 and self.s_pro <= 70:
           r = "Your intake of protein is {} grams , so it is sufficient.".format(self.pro)
           print(r)
        else:
           exc = self.s_pro - 70
           r = "You have an excess of {} grams of protein.".format(exc)
           print(r)
       
        if  self.s_sod < 4:
           ins = 5 - self.s_sod
           r = "Your intake of sodium is insufficient for {}.".format(ins)
           print(r)
        elif self.s_sod >= 4 and self.s_sod <= 5:
           r = "Your intake of sodium is {} grams , so it is sufficient.".format(self.sod)
           print(r)
        else:
           exc = self.s_sod - 5
           r = "You have an excess of {} grams of sodium.".format(exc)
           print(r)

nutr = Nutrition(list(input("Please enter today's meal: ").split()))
nutr.app()
