


 sed -e '44,87s/\(.*\)/    \1/g' nut_test.py > nut.py


ene = list(input("Please enter today's meal: ").split())
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
x = 0
for word in ene:
    new = ene[x]
    if new == "bread":
        pie = int(input("How many pieces of bread?: "))
        new = 164 * pie
        ene[x] = new
        Pr = 4.9 * pie
        protein.append(Pr)
        li = 2.6 * pie
        lipid.append(li)
        Ca = 30.3 * pie
        carbohydrate.append(Ca)
        So = 0.7 * pie
        Sodium_salt_equivalent.append(So)
        x += 1
        print(Sodium_salt_equivalent)

    if new == "curry":
        pie = 1
        new = 474 * pie
        ene[x] = new
        Pr = 6.5 * pie
        protein.append(Pr)
        li = 34.1 * pie
        lipid.append(li)
        Ca = 44.7 * pie
        carbohydrate.append(Ca)
        So = 2.2 * pie
        Sodium_salt_equivalent.append(So)
        x += 1
        print(Sodium_salt_equivalent)

    if new == "noodle":
        pie = 1
        new = 500 * pie
        ene[x] = new
        Pr = 8.6 * pie
        protein.append(Pr)
        li = 17 * pie
        lipid.append(li)
        Ca = 62.6 * pie
        carbohydrate.append(Ca)
        So = 5.8 * pie
        Sodium_salt_equivalent.append(So)
        x += 1
        print(Sodium_salt_equivalent)


s_ene = sum(ene)
s_pro = sum(protein)
s_lip = sum(lipid)
s_car = sum(carbohydrate)
s_sod = sum(Sodium_salt_equivalent)

if s_ene < 2700:
    ins = 2700 - s_ene
    r = "Your intake of ene is insufficient for {}kcal.".format(ins)
    print(r)
else:
    exc = s_ene - 2700
    r = "You have an excess of {}kcal of ene.".format(exc)
    print(r)

if s_pro < 65:
    ins = 65 - s_pro
    r = "Your intake of protein is insufficient for {} grams.".format(ins)
    print(r)
elif s_pro >= 65 and s_pro <= 70:
    r = "Your intake of protein is {} grams , so it is sufficient.".format(s_pro)
    print(r)
else:
    exc = s_pro - 70
    r = "You have an excess of {} grams of protein.".format(exc)
    print(r)

if  s_sod < 4:
    ins = 5 - s_sod
    r = "Your intake of sodium is insufficient for {}.".format(ins)
    print(r)
elif s_sod >= 4 and s_sod <= 5:
    r = "Your intake of sodium is {} grams , so it is sufficient.".format(s_sod)
    print(r)
else:
    exc = s_sod - 5
    r = "You have an excess of {} grams of sodium.".format(exc)
    print(r)






 
























































































r = "Your intake of a is insufficient for {} grams.".format(ins)
print(r)


r = "Your intake of a is {} grams , which is sufficient.".format(suf)
print(r)


r = "Your intake of a is {} grams excess.".format(exc)
print(r)






/new ==/,/eee/{
     s/""/""/
     s/aaa//   #kcal
     s/bbb//   #protein
     s/ccc//   #lipid
     s/ddd//   #carbohydrate
     s/eee//   #Sodium_salt_equivalent
}




    if new == "":
        pie = 1
        new = aaa * pie
        energy[x] = new
        Pr = bbb * pie
        protein.append(Pr)
        li = ccc * pie
        lipid.append(li)
        Ca = ddd * pie
        carbohydrate.append(Ca)
        So = eee * pie
        Sodium_salt_equivalent.append(So)
        x += 1
        print(Sodium_salt_equivalent)








if  s_ < aaa:
    ins = bbb - s_
    r = "Your intake of a is insufficient for {}.".format(ins)
    print(r)
elif s_ >= aaa and s_ <= bbb:
    r = "Your intake of  is {} grams , so it is sufficient.".format(s_)
    print(r)
else:
    exc = s_ - bbb
    r = "Your intake of a is {} grams excess.".format(exc)
    print(r)



















    if new == "":
        pie = int(input("How many ?: "))
        new = aaa * pie
        energy[x] = new
        Pr = bbb * pie
        protein.append(Pr)
        li = ccc * pie
        lipid.append(li)
        Ca = ddd * pie
        carbohydrate.append(Ca)
        x += 1








































    if new == "  ":
        pie = int(input("How many ?: "))
        new = aaa * pie
        energy[x] = new
        Pr = bbb * pie
        protein.append(Pr)
        li = ccc * pie
        lipid.append(li)
        Ca = ddd * pie
        carbohydrate.append(Ca)
        Sa = eee * pie
        Saturated_fatty_acids.append(Sa)
        n_6 = fff * pie
        n_6_fatty_acids.append(n_6)
        n_3 = ggg * pie
        n_3_fatty_acids.append(n_3)
        Di = hhh * pie
        Dietary_fiber.append(Di)
        Va = iii * pie
        Vitamin_A.append(Va)
        Vd = jjj * pie
        Vitamin_D.append(Vd)
        Ve = kkk * pie
        Vitamin_E.append(Ve)
        VK = lll * pie
        Vitamin_K.append(Vk)
        Vb1 = mmm * pie
        Vitamin_B1.append(Vb1)
        Vb2 = nnn * pie
        Vitamin_b2.append(Vb2)
        Vb6 = ooo * pie
        Vitamin_B6.append(Vb6)
        Vb12 = ppp * pie
        Vitamin_B12.append(Vb12)
        Ni = qqq * pie
        Niacin.append(Ni)
        Fo = rrr * pie
        Folic_Acid_RDA.append(Fo)
        Pa = sss * pie
        Pantothenic_Acid.append(Pa)
        Bi = ttt * pie
        Biotin.append(Bi)
        Vc = uuu * pie
        Vitamin_C.append(Vc)
        So = vvv * pie
        Sodium_salt_equivalent.append(So)
        Po = www * pie
        Potassium.append(Po)
        Ca = xxx * pie
        Calcium.append(Ca)
        Ma = yyy * pie
        Magnesium.append(Ma)
        Ph = zzz * pie
        Phosphorus.append(Ph)
        Ir = aab * pie
        Iron.append(Ir)
        Zi = aac * pie
        Zinc.append(Zi)
        Co = aad * pie
        Copper.append(Co)
        Ma = aae * pie
        Manganese.append(Ma)
        Lo = aaf * pie
        lodine.append(Lo)
        Se = aag * pie
        Selenium.append(Se)
        Ch = aah * pie
        Chromium.append(Ch)
        Mo = aai * pie
        Molybdenum.append(Mo)
        x += 1
























身体活動レベル【ふつう】の場合	 []   18～29歳	30歳～49歳	50歳～64歳
[]   []   男性	女性	男性	女性	男性	女性




エネルギー	推定エネルギー必要量	2650kcal	2000kcal	2700kcal	2050kcal	2600kcal	1950kcal
タンパク質	RDA	65g	50g	65g	50g	65g	50g
脂質（目標量）	DG	20～30%	20～30%	20～30%	20～30%	20～30%	20～30%
飽和脂肪酸（目標量）	DG	7%以下	7%以下	7%以下	7%以下	7%以下	7%以下
n-6系脂肪酸（目安量）	AI	11g	8g	10g	8g	10g	8g
n-3系脂肪酸（目安量）	AI	2.0g	1.6g	2.0g	1.6g	2.2g	1.9g
炭水化物（目標量）	DG	50～65%	50～65%	50～65%	50～65%	50～65%	50～65%
食物繊維（目標量）	DG	21g以上	18g以上	21g以上	18g以上	20g以上	18g以上
ビタミンA※1	RDA	850µg	650µg	900µg	700µg	900µg	700µg
ビタミンD（目安量）	AI	8.5µg	8.5µg	8.5µg	8.5µg	8.5µg	8.5µg
ビタミンE（目安量）	AI	6.0mg	5.0mg	6.0mg	5.5mg	7.0mg	6.0mg
ビタミンK（目安量）	AI	150µg	150µg	150µg	150µg	150µg	150µg
ビタミンB1	RDA	1.4mg	1.1mg	1.4mg	1.1mg	1.3mg	1.1mg
ビタミンB2	RDA	1.6mg	1.2mg	1.6mg	1.2mg	1.5mg	1.2mg
ビタミンB6	RDA	1.4mg	1.1mg	1.4mg	1.1mg	1.4mg	1.1mg
ビタミンB12	RDA	2.4µg	2.4µg	2.4µg	2.4µg	2.4µg	2.4µg
ナイアシン	RDA	15mg	11mg	15mg	12mg	14mg	11mg
葉酸	RDA	240µg	240µg	240µg	240µg	240µg	240µg
パントテン酸（目安量）	AI	5mg	5mg	5mg	5mg	6mg	5mg
ビオチン（目安量）	AI	50µg	50µg	50µg	50µg	50µg	50µg
ビタミンC	RDA	100mg	100mg	100mg	100mg	100mg	100mg
ナトリウム（食塩相当量）	DG	7.5g未満	6.5g未満	7.5g未満	6.5g未満	7.5g未満	6.5g未満
カリウム（目安量）	AI	2500mg	2000mg	2500mg	2000mg	2500mg	2000mg
カルシウム	RDA	800mg	650mg	750mg	650mg	750mg	650mg
マグネシウム	RDA	340mg	270mg	370mg	290mg	370mg	290mg
リン（目安量）	AI	1000mg	800mg	1000mg	800mg	1000mg	800mg
鉄	RDA	7.5mg	"月経なし6.5mg
月経あり10.5mg"	7.5mg	"月経なし6.5mg
月経あり10.5mg"	7.5mg	"月経なし6.5mg
月経あり11mg"
亜鉛	RDA	11mg	8mg	11mg	8mg	11mg	8mg
銅	RDA	0.9mg	0.7mg	0.9mg	0.7mg	0.9mg	0.7mg
マンガン（目安量）	AI	4.0mg	3.5mg	4.0mg	3.5mg	4.0mg	3.5mg
ヨウ素	RDA	130µg	130µg	130µg	130µg	130µg	130µg
セレン	RDA	30µg	25µg	30µg	25µg	30µg	25µg
クロム（目安量）	AI	10µg	10µg	10µg	10µg	10µg	10µg
モリブデン	RDA	30µg	25µg	30µg	25µg	30µg	25µg














Physical activity level [normal] 18-29 years old 30-49 years old 50-64 years old
Male Female Male Female Male Female Male Female
Energy Estimated energy requirement 2650kcal 2000kcal 2700kcal 2050kcal 2600kcal 1950kcal
Protein RDA 65g 50g 65g 50g 65g 50g
Lipids (target amount) DG 20-30% 20-30% 20-30% 20-30% 20-30% 20-30% 20-30
Saturated fatty acids (target amount) DG 7% or less 7% or less 7% or less 7% or less
n-6 fatty acids (target amount) AI 11g 8g 10g 8g 10g 8g
n-3 fatty acids (target amount) AI 2.0g 1.6g 2.0g 1.6g 2.2g 1.9g
Carbohydrates (target amount) DG 50-65% 50-65% 50-65% 50-65% 50-65% 50-65%
Dietary fiber (target amount) DG 21g min. 18g min. 21g min. 18g min. 20g min. 18g min.
Vitamin A*1 RDA 850µg 650µg 900µg 700µg 900µg 700µg
Vitamin D (reference amount) AI 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg
Vitamin E (standard amount) AI 6.0mg 5.0mg 6.0mg 5.5mg 7.0mg 6.0mg
Vitamin K (standard dose) AI 150µg 150µg 150µg 150µg 150µg 150µg 150µg 150µg
Vitamin B1 RDA 1.4mg 1.1mg 1.4mg 1.1mg 1.3mg 1.1mg
Vitamin B2 RDA 1.6mg 1.2mg 1.6mg 1.2mg 1.5mg 1.2mg
Vitamin B6 RDA 1.4mg 1.1mg 1.4mg 1.1mg 1.4mg 1.1mg
Vitamin B12 RDA 2.4µg 2.4µg 2.4µg 2.4µg 2.4µg
Niacin RDA 15mg 11mg 15mg 12mg 14mg 11mg
Folic Acid RDA 240µg 240µg 240µg 240µg 240µg 240µg 240µg
Pantothenic Acid (Reference Amount) AI 5mg 5mg 5mg 5mg 5mg 5mg 6mg 5mg
Biotin (standard amount) AI 50µg 50µg 50µg 50µg 50µg 50µg 50µg
Vitamin C RDA 100mg 100mg 100mg 100mg 100mg 100mg
Sodium (salt equivalent) DG Less than 7.5g Less than 6.5g Less than 7.5g Less than 6.5g Less than 6.5g
Potassium (approximate amount) AI 2500mg 2000mg 2500mg 2000mg 2500mg 2000mg
Calcium RDA 800mg 650mg 650mg 750mg 750mg 650mg
Magnesium RDA 340mg 270mg 370mg 290mg 370mg 290mg
Phosphorus (approximate amount) AI 1000mg 800mg 1000mg 800mg 1000mg 800mg
Iron RDA 7.5mg “without menstruation 6.5mg
With menstruation 10.5mg” 7.5mg ”Without menstruation 6.5mg
Menstruation 10.5 mg” 7.5 mg ”without menstruation 6.5 mg
11mg with menstruation"
Zinc RDA 11mg 8mg 11mg 8mg 11mg 8mg
Copper RDA 0.9mg 0.7mg 0.9mg 0.7mg 0.9mg 0.7mg
Manganese (approximate amount) AI 4.0mg 3.5mg 4.0mg 3.5mg 4.0mg 3.5mg
Iodine RDA 130µg 130µg 130µg 130µg 130µg 130µg 130µg
Selenium RDA 30µg 25µg 30µg 25µg 30µg 25µg
Chromium (approximate amount) AI 10µg 10µg 10µg 10µg 10µg 10µg
Molybdenum RDA 30µg 25µg 25µg 30µg 30µg 25µg














































Saturated fatty acids (target amount) DG 7% or less 7% or less 7% or less 7% or less
n-6 fatty acids (target amount) AI 11g 8g 10g 8g 10g 8g
n-3 fatty acids (target amount) AI 2.0g 1.6g 2.0g 1.6g 2.2g 1.9g
Carbohydrates (target amount) DG 50-65% 50-65% 50-65% 50-65% 50-65% 50-65
Dietary fiber (target amount) DG 21g min. 18g min. 21g min. 18g min. 20g min. 18g min.
Vitamin A*1 RDA 850µg 650µg 900µg 700µg 900µg 700µg
Vitamin D (reference amount) AI 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg 8.5µg
Vitamin E (standard amount) AI 6.0mg 5.0mg 6.0mg 5.5mg 7.0mg 6.0mg
Vitamin K (standard dose) AI 150µg 150µg 150µg 150µg 150µg 150µg 150µg 150µg
Vitamin B1 RDA 1.4mg 1.1mg 1.4mg 1.1mg 1.3mg 1.1mg
Vitamin B2 RDA 1.6mg 1.2mg 1.6mg 1.2mg 1.5mg 1.2mg
Vitamin B6 RDA 1.4mg 1.1mg 1.4mg 1.1mg 1.4mg 1.1mg
Vitamin B12 RDA 2.4µg 2.4µg 2.4µg 2.4µg 2.4µg
Niacin RDA 15mg 11mg 15mg 12mg 14mg 11mg
Folic Acid RDA 240µg 240µg 240µg 240µg 240µg 240µg 240µg
Pantothenic Acid (Reference Amount) AI 5mg 5mg 5mg 5mg 5mg 5mg 6mg 5mg
Biotin (standard amount) AI 50µg 50µg 50µg 50µg 50µg 50µg 50µg
Vitamin C RDA 100mg 100mg 100mg 100mg 100mg 100mg
Sodium (salt equivalent) DG Less than 7.5g Less than 6.5g Less than 7.5g Less than 6.5g Less than 6.5g
Potassium (approximate amount) AI 2500mg 2000mg 2500mg 2000mg 2500mg 2000mg
Calcium RDA 800mg 650mg 650mg 750mg 750mg 650mg
Magnesium RDA 340mg 270mg 370mg 290mg 370mg 290mg
Phosphorus (approximate amount) AI 1000mg 800mg 1000mg 800mg 1000mg 800mg
Iron RDA 7.5mg “without menstruation 6.5mg
With menstruation 10.5mg” 7.5mg ”Without menstruation 6.5mg
Menstruation 10.5 mg” 7.5 mg ”without menstruation 6.5 mg
11mg with menstruation"
Zinc RDA 11mg 8mg 11mg 8mg 11mg 8mg
Copper RDA 0.9mg 0.7mg 0.9mg 0.7mg 0.9mg 0.7mg
Manganese (approximate amount) AI 4.0mg 3.5mg 4.0mg 3.5mg 4.0mg 3.5mg
Iodine RDA 130µg 130µg 130µg 130µg 130µg 130µg 130µg
Selenium RDA 30µg 25µg 30µg 25µg 30µg 25µg
Chromium (approximate amount) AI 10µg 10µg 10µg 10µg 10µg 10µg
Molybdenum
