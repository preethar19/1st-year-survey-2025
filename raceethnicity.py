import pandas as pd
from matplotlib import pyplot as plt
from csv import writer

data = pd.read_csv('/Users/nadiabey/Documents/Duke/Chronicle/2025_data_2.csv', header=[1])
responses = data['How would you best describe yourself?']
count = {}
percentages = {}
hisp = {'Hispanic/Latinx only': 0}


def statsdict(inp: list, outp: dict) -> dict:
    """make a dict counting up things"""
    for item in inp:
        if item not in outp.keys():
            outp[item] = 0  # make new dict key
        outp[item] += 1  # count all the answers!
    return outp


def get_info() -> list:
    multi = 0
    total = 0
    ret = []
    for x in responses:
        total += 1
        values = x.split(',') # separate answers that have multiple races
        ret.append(values)
        statsdict(values, count)
        if 'Hispanic or Latinx/e' in values:
            if len(values) == 1:
                hisp['Hispanic/Latinx only'] += 1
            else:
                other = [x for x in values if x != 'Hispanic or Latinx/e']
                statsdict(other, hisp)
        if len(values) > 1:
            multi += 1  # count people with two or more races/ethnicities
    for k, v in count.items():
        percentages[k] = str(round((v/total) * 100, 2)) + "%"
    print(multi,"people selected two or more ethnicities.")
    return ret


def make_csv(listy: list):
    head = ['Id', 'Asian', 'Black or African American', 'A race/ethnicity not listed here', 'White',
            'Hispanic or Latinx/e', 'Native American or Alaska Native', 'Native Hawaiian or Pacific Islander']
    out = [head]
    for i in range(len(listy)):
        row = [i]
        for j in range(1, len(head)):
            if head[j] in listy[i]:
                row.append("X")
            else:
                row.append("")
        out.append(row)
    with open('racebreakdown.csv', 'w') as file:
        w = writer(file)
        w.writerows(out)


if __name__ == '__main__':
    #get_info()
    #print(count)
    #for k, v in hisp.items():
    #    print(v, "people who identified as Hispanic or Latinx identified as", k)
    #colorlist = ["#6E143B", "#821548", "#971755", "#AC1862", "#C01A6F", "#D51B7C", "#EA1D89"]
    #plt.pie(count.values(), explode=[0.05, 0.05, 0.05, 0.05, 0.05, 0.4, 0.2], labels=count.keys(), colors=colorlist)
    #plt.show()
    make_csv(get_info())
