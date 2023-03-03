# probabilties (stocks (lc), bonds(gb), commodities(comm))
import random


def performance_calc():
    lc_probability_list = []
    for i in range(1, 4, 1):
        lc_probability_list.append(1)
    for i in range(1, 5, 1):
        lc_probability_list.append(2)
    for i in range(1, 23, 1):
        lc_probability_list.append(3)
    for i in range(1, 27, 1):
        lc_probability_list.append(4)
    for i in range(1, 29, 1):
        lc_probability_list.append(5)
    for i in range(1, 15, 1):
        lc_probability_list.append(6)
    for i in range(1, 4, 1):
        lc_probability_list.append(7)
    print(lc_probability_list)


performance_calc()
"""vcmge_probability_list = []
    for i in range(1,2,1):
        vcmge_probability_list.append(1)


    gb_probability_list = []
    for i in range(1,6,1):
        gb_probability_list.append(1)
    for i in range(1,24,1):
        gb_probability_list.append(2)
    for i in range(1,39,1):
        gb_probability_list.append(3)
    for i in range(1,18,1):
        gb_probability_list.append(4)
    for i in range(1,11,1):
        gb_probability_list.append(5)
    for i in range(1,5,1):
        gb_probability_list.append(6)
    for i in range(1,3,1):
        gb_probability_list.append(7)
    for i in range(1,2,1):
        gb_probability_list.append(8)

    comm_probability_list = []
    for i in range(1,16,1):
        comm_probability_list.append(1)
    for i in range(1,24,1):
        comm_probability_list.append(2)
    for i in range(1,35,1):
        comm_probability_list.append(3)
    for i in range(1,14,1):
        comm_probability_list.append(4)
    for i in range(1,4,1):
        comm_probability_list.append(5)
    for i in range(1,11,1):
        comm_probability_list.append(6)
    for i in range(1,3,1):
        comm_probability_list.append(7)

    lc = random.choice(lc_probability_list)
    if lc == 1:
        lc = random.randint(-43,-28)
    elif lc ==2:
        lc = random.randint(-28,-13)
    elif lc ==3:
        lc = random.randint(-13,1)
    elif lc ==4:
        lc = random.randint(1,16)
    elif lc ==5:
        lc = random.randint(16,31)
    elif lc ==6:
        lc = random.randint(32,46)
    elif lc ==7:
        lc = random.randint(46,61)

    gb = random.choice(gb_probability_list)
    if gb ==1:
        gb = random.randint(-14,-7)
    elif gb ==2:
        gb = random.randint(-7,0)
    elif gb ==3:
        gb = random.randint(0,7)
    elif gb ==4:
        gb = random.randint(8,15)
    elif gb ==5:
        gb = random.randint(15,22)
    elif gb ==6:
        gb = random.randint(23,30)
    elif gb ==7:
        gb = random.randint(30,37)
    elif gb == 8:
        gb = random.randint(37,45)

    comm = random.choice(comm_probability_list)
    if comm ==1:
        comm = random.randint(-25,-13)
    elif comm ==2:
        comm = random.randint(-12,0)
    elif comm ==3:
        comm = random.randint(0,11)
    elif comm ==4:
        comm = random.randint(11,23)
    elif comm ==5:
        comm = random.randint(23,35)
    elif comm == 6:
        comm = random.randint(35,47)
    elif comm ==7:
        comm = random.randint(47,48)
    elif comm == 8:
        comm = random.randint(37,45)

#performance calcualtion
    cf_perf = random.randint(-1,1)/100*(int(funds[3]["Money Market Fund"])/100)
    performance = (((lc/100)*int(funds[3]["Equity Fund"]))+((gb/100)*int(funds[3]["Bond Fund"]))+((comm/100)*int(funds[3]["Real Assets Fund"]))+cf_perf)
    return performance

"""
