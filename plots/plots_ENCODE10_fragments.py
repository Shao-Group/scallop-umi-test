import numpy as np
import matplotlib.pyplot as plt
import os

def load_data(tool, alig, t_type):
    scallop2 = np.zeros([10,16]) # 1 total + 15 code class
    dirPath = './ENCODE10/scallop2/scallop2-' + t_type + '/'
    samples=['SRR307903','SRR315323','SRR387661','SRR534307','SRR545695','SRR307911','SRR315334','SRR534291','SRR534319','SRR545723']

    for i in range(0, 10):
        file1 = dirPath + samples[i] + '.' + alig + '.codes'
        codes = []
        with open(file1, 'r') as f:
            next(f)
            lines = f.readlines()
            for line in lines:
                line = line.replace('\n','')
                codes.append(line)

        scallop2[i][0] = len(codes)

        d = {'=':0,'c':0,'k':0,'m':0,'n':0,'j':0,'e':0,'o':0,'s':0,'x':0,'i':0,'y':0,'p':0,'r':0,'u':0,}
        for code in codes:
            d[code] = d[code] + 1

        scallop2[i][1] = d['=']
        scallop2[i][2] = d['c']
        scallop2[i][3] = d['k']
        scallop2[i][4] = d['m']
        scallop2[i][5] = d['n']
        scallop2[i][6] = d['j']
        scallop2[i][7] = d['e']
        scallop2[i][8] = d['o']
        scallop2[i][9] = d['s']
        scallop2[i][10] = d['x']
        scallop2[i][11] = d['i']
        scallop2[i][12] = d['y']
        scallop2[i][13] = d['p']
        scallop2[i][14] = d['r']
        scallop2[i][15] = d['u']

    return scallop2

def plot_table(scallop2_hisat, scallop2_star, t_type):
    ave = np.zeros([2,16])
    col = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    col = ['total', '=','c','k','m','n','j','e','o','s','x','i','y','p','r','u']
    row = ["hisat ave", "star ave"]
    
    hscallop2_t = scallop2_hisat.T
    sscallop2_t = scallop2_star.T
    for i in range(0,16):
        ave[0][i] = np.around(np.mean(hscallop2_t[i]), 2)
        ave[1][i] = np.around(np.mean(sscallop2_t[i]), 2)
    
    plt.figure(figsize=(12,4))
    tab = plt.table(cellText = ave,
                    colLabels = col,
                    rowLabels = row,
                    loc = 'center',
                    cellLoc = 'center',
                    rowLoc = 'center')
    tab.scale(1,2)
    plt.axis('off')
    tl = "ENCODE10 " + t_type
    plt.title(tl)
    plt.show()
    
def get_pre(scallop2):
    scallop2_t = scallop2.T
    
    ave = np.zeros(9)
    ave[0] = np.mean(scallop2_t[1]) / np.mean(scallop2_t[0]) * 100
    ave[1] = np.mean(scallop2_t[2]) / np.mean(scallop2_t[0]) * 100
    ave[2] = np.mean(scallop2_t[4]) / np.mean(scallop2_t[0]) * 100
    ave[3] = np.mean(scallop2_t[5]) / np.mean(scallop2_t[0]) * 100
    ave[4] = np.mean(scallop2_t[6]) / np.mean(scallop2_t[0]) * 100
    ave[5] = np.mean(scallop2_t[10]) / np.mean(scallop2_t[0]) * 100
    ave[6] = np.mean(scallop2_t[11]) / np.mean(scallop2_t[0]) * 100
    ave[7] = np.mean(scallop2_t[15]) / np.mean(scallop2_t[0]) * 100
    
    other = 0
    other_list = [3, 7, 8, 9, 12, 13, 14]
    for i in other_list:
        other = other + np.mean(scallop2_t[i])
    ave[8] = other / np.mean(scallop2_t[0]) * 100
    
    st = np.zeros(9)
    st[0] = np.std((scallop2_t[1]/scallop2_t[0])*100)
    st[1] = np.std((scallop2_t[2]/scallop2_t[0])*100)
    st[2] = np.std((scallop2_t[4]/scallop2_t[0])*100)
    st[3] = np.std((scallop2_t[5]/scallop2_t[0])*100)
    st[4] = np.std((scallop2_t[6]/scallop2_t[0])*100)
    st[5] = np.std((scallop2_t[10]/scallop2_t[0])*100)
    st[6] = np.std((scallop2_t[11]/scallop2_t[0])*100)
    st[7] = np.std((scallop2_t[15]/scallop2_t[0])*100)
    
    other_st = np.zeros([1,10])
    for i in other_list:
        other_st = other_st + scallop2_t[i]
    st[8] = np.std((other_st/scallop2_t[0])*100)
    return ave, st

def plot_bar(alig, nf_ave, nf_sd, f_ave, f_sd):
    t_class = ['=', 'c', 'm', 'n', 'j', 'x', 'i', 'u','other']
    fig, ax = plt.subplots(1, 1, figsize=(6,2), dpi= 200)
    size = 9
    x = np.arange(size)
    idx = 'c'
    if(alig == 'star'):
        idx = 'd'
    c2 = nf_ave
    c2_SD = nf_sd
    c1 = f_ave
    c1_SD = f_sd
    total_width, n = 0.8, 2
    width = total_width / n
    x = x - (total_width - width) / 2
    plt.bar(x, c1, color='r', edgecolor='black', width=width, yerr = c1_SD, error_kw=dict(lw=1,capsize=5,capthick=1), label='Full')
    plt.bar(x + width, c2, color='b',edgecolor='black', width=width, yerr = c2_SD, error_kw=dict(lw=1, capsize=5, capthick=1), label='Non-full')
     
    ax.set(ylim=[0, 55])
    ax.set(xlim=[-0.6, 8.5])
    plt.yticks(np.arange(0, 55, 25), fontsize=16)
    plt.xticks(x+width*0.5,t_class,fontsize=16)

    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)

    plt.ylabel("Percentage (%)", fontsize=16)
    plt.text(-2.5,52,idx, fontsize=18)
    figure_name = "./ENCODE10/figure/" + alig + "-fragments.pdf"
    plt.savefig(figure_name, bbox_inches='tight')
    plt.show()
  
def main():

    nonfull_scallop2_hisat = load_data('scallop2', 'hisat', 'non-full')
    nonfull_scallop2_star = load_data('scallop2', 'star', 'non-full')
    
    plot_table(nonfull_scallop2_hisat, nonfull_scallop2_star, 'non-full')

    full_scallop2_hisat = load_data('scallop2', 'hisat', 'full')
    full_scallop2_star = load_data('scallop2', 'star', 'full')

    plot_table(full_scallop2_hisat, full_scallop2_star, 'full')
    
    nf_ave, nf_sd = get_pre(nonfull_scallop2_hisat)
    f_ave, f_sd = get_pre(full_scallop2_hisat)
    plot_bar('hisat', nf_ave, nf_sd, f_ave, f_sd)
    
    nf_ave, nf_sd = get_pre(nonfull_scallop2_star)
    f_ave, f_sd = get_pre(full_scallop2_star)
    plot_bar('star', nf_ave, nf_sd, f_ave, f_sd)

if __name__ == '__main__':
    main()

