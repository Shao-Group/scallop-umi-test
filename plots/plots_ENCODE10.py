import numpy as np
import matplotlib.pyplot as plt

def load_data(tool):

    dirPath = './ENCODE10/' + tool + '/'

    file1 = dirPath + 'hisat.' + tool + '.numTranscripts.results'
    file2 = dirPath + 'hisat.' + tool + '.numMatchTranscripts.results'
    file3 = dirPath + 'star.' + tool + '.numTranscripts.results'
    file4 = dirPath + 'star.' + tool + '.numMatchTranscripts.results'

    hisat_total_num = np.loadtxt(file1)
    hisat_match_num = np.loadtxt(file2)
    hisat_pre = hisat_match_num / hisat_total_num * 100
    star_total_num = np.loadtxt(file3)
    star_match_num = np.loadtxt(file4)
    star_pre = star_match_num / star_total_num * 100

    return hisat_match_num, hisat_pre, star_match_num, star_pre

def merge(scallop2, stringtie2, scallop, class2):

    bundle = np.array((scallop2, stringtie2, scallop, class2)).T

    return bundle

def plot_sample(hmatch, hpre, smatch, spre):

    samples=['SRR307903','SRR315323','SRR387661','SRR534307','SRR545695','SRR307911','SRR315334','SRR534291','SRR534319','SRR545723']

    for ii in range(1,11):
        fig, ax = plt.subplots(1, 1, figsize=(9,9), dpi= 600)

        markers= ['o', '^', '+', 's']

        i = ii - 1
        x1 = hpre[i][0]
        y1 = hmatch[i][0]/1000
        x2 = hpre[i][1]
        y2 = hmatch[i][1]/1000
        x3 = hpre[i][2]
        y3 = hmatch[i][2]/1000
        x4 = spre[i][0]
        y4 = smatch[i][0]/1000
        x5 = spre[i][1]
        y5 = smatch[i][1]/1000
        x6 = spre[i][2]
        y6 = smatch[i][2]/1000
        x7 = hpre[i][3]
        y7 = hmatch[i][3]/1000
        x8 = spre[i][3]
        y8 = smatch[i][3]/1000

        file1 = './ENCODE10/scallop2/' + samples[i] + '.hisat.roc-cor'
        file2 = './ENCODE10/scallop2/' + samples[i] + '.hisat.roc-pre'
        file3 = './ENCODE10/scallop2/' + samples[i] + '.star.roc-cor'
        file4 = './ENCODE10/scallop2/' + samples[i] + '.star.roc-pre'

        hscor = np.loadtxt(file1)/1000
        hspre = np.loadtxt(file2)
        sscor = np.loadtxt(file3)/1000
        sspre = np.loadtxt(file4)

        ax.plot(hspre,hscor, c='r', linewidth=3)
        ax.plot(sspre,sscor,c='r',linewidth=3)

        ax.scatter(x1, y1, c='red', marker=markers[0], label='Scallop2-HISAT2', s=400)
        ax.scatter(x2, y2, c='green', marker=markers[0], label='StringTie2-HISAT2', s=400)
        ax.scatter(x3, y3, c='blue', marker=markers[0], label='Scallop-HISAT2', s=400)
        ax.scatter(x7, y7, c='y', marker=markers[0], label='CLASS2-HISAT2', s=350)

        ax.scatter(x4, y4, c='red', marker=markers[1], label='Scallop2-STAR', s=400)
        ax.scatter(x5, y5, c='green', marker=markers[1], label='StringTie2-STAR', s=400)
        ax.scatter(x6, y6, c='blue', marker=markers[1], label='Scallop-STAR', s=400)
        ax.scatter(x8, y8, c='y', marker=markers[1], label='CLASS2-STAR', s=350)

        xlist = [x1, x2, x3, x4, x5, x6, x7, x8]
        xminl = int(min(xlist)) - 1

        if(ii == 1):
            xmaxl = int(max(xlist) + 24)
        elif(ii == 2):
            xmaxl = int(max(xlist) + 19)
        elif(ii == 3):
            xmaxl = int(max(xlist) + 17)
        elif(ii == 4):
            xmaxl = int(max(xlist) + 24)
        elif(ii == 5):
            xmaxl = int(max(xlist) + 18)
        elif(ii == 6):
            xmaxl = int(max(xlist) + 24)
        elif(ii == 7):
            xmaxl = int(max(xlist) + 25)
        elif(ii == 9):
            xmaxl = int(max(xlist) + 16)
        else:
            xmaxl = int(max(xlist) + 23)

        ylist = [y1, y2, y3, y4, y5, y6, y7, y8]
        yminl = int((int(min(ylist))))
        if(ii==2 or ii==3):
            ymaxl = int((int(max(ylist))))+2
        else:
            ymaxl = int((int(max(ylist))))+1

        ax.set(ylim=[yminl, ymaxl],xlim=[xminl,xmaxl])
        #ax.legend(loc='upper right', fontsize=16)

        plt.xticks(np.arange(xminl, xmaxl, 6), fontsize=28, horizontalalignment='center')
        plt.yticks(np.arange(yminl, ymaxl+1, 1), fontsize=28)

        plt.gca().spines["top"].set_alpha(1)
        plt.gca().spines["bottom"].set_alpha(1)
        plt.gca().spines["right"].set_alpha(1)
        plt.gca().spines["left"].set_alpha(1)
        
        text = samples[i]
        plt.text((xminl+xmaxl)/2, (ymaxl+yminl)/2+(ymaxl-yminl)/3, text, fontsize=32)

        plt.xlabel("Precision (%)", fontsize=32)
        plt.ylabel("# Matching Transcripts (x$10^3$)", fontsize=32)

        figure_name = './ENCODE10/figure/' + samples[i] + '.pdf'

        plt.savefig(figure_name, bbox_inches='tight')

    return None

def plot_bar_num(hmatch, smatch):
    fig, ax = plt.subplots(1, 1, figsize=(6,10), dpi= 600)
    size = 2
    x = np.arange(size)
    scallop2 = [np.mean(hmatch[:,0]), np.mean(smatch[:,0])]
    scallop2_SD = [np.std(hmatch[:,0]), np.std(smatch[:,0])]
    stringtie2 = [np.mean(hmatch[:,1]), np.mean(smatch[:,1])]
    stringtie2_SD = [np.std(hmatch[:,1]), np.std(smatch[:,1])]
    scallop = [np.mean(hmatch[:,2]), np.mean(smatch[:,2])]
    scallop_SD = [np.std(hmatch[:,2]), np.std(smatch[:,2])]
    class2 = [np.mean(hmatch[:,3]), np.mean(smatch[:,3])]
    class2_SD = [np.std(hmatch[:,3]), np.std(smatch[:,3])]
    
    total_width, n = 0.2, 4
    width = total_width / n
    x = x - (total_width - width) / 2
    x[1] = x[1] - 0.75
    labels = ['HI', 'ST']
    
    plt.bar(x, scallop2, color='r', edgecolor='black', width=width, yerr = scallop2_SD, error_kw=dict(lw=1,capsize=5,capthick=1),label='Scallop2')
    plt.bar(x + width, stringtie2, color='g',edgecolor='black', width=width, yerr = stringtie2_SD, error_kw=dict(lw=1, capsize=5, capthick=1),label='StringTie2')
    plt.bar(x + width*2, scallop, color='b', edgecolor='black', width=width, yerr = scallop_SD, error_kw=dict(lw=1, capsize=5, capthick=1), label='Scallop')
    plt.bar(x + width*3, class2, color='y', edgecolor='black', width=width, yerr = class2_SD, error_kw=dict(lw=1, capsize=5, capthick=1), label='CLASS2')
    
    ax.set(ylim=[0, 21500])
    plt.yticks(np.arange(0, 21501, 5000), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width*1.5,labels,fontsize=32)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.ylabel("# Matching Transcripts", fontsize=32)
    
    figure_name = './ENCODE10/figure/ENCODE10_num.pdf'
    
    plt.savefig(figure_name, bbox_inches='tight')

    return None

def plot_bar_pre(hpre, spre):
    fig, ax = plt.subplots(1, 1, figsize=(6,10), dpi= 600)
    
    size = 2
    x = np.arange(size)
    scallop2 = [np.mean(hpre[:,0]), np.mean(spre[:,0])]
    scallop2_SD = [np.std(hpre[:,0]), np.std(spre[:,0])]
    stringtie2 = [np.mean(hpre[:,1]), np.mean(spre[:,1])]
    stringtie2_SD = [np.std(hpre[:,1]), np.std(spre[:,1])]
    scallop = [np.mean(hpre[:,2]), np.mean(spre[:,2])]
    scallop_SD = [np.std(hpre[:,2]), np.std(spre[:,2])]
    class2 = [np.mean(hpre[:,3]), np.mean(spre[:,3])]
    class2_SD = [np.std(hpre[:,3]), np.std(spre[:,3])]

    total_width, n = 0.2, 4
    width = total_width / n
    x = x - (total_width - width) / 2
    x[1] = x[1] - 0.75
    
    labels = ['HI', 'ST']
    plt.bar(x, scallop2, color='r', edgecolor='black', width=width, yerr = scallop2_SD, error_kw=dict(lw=1,capsize=5,capthick=1),label='Scallop2')
    plt.bar(x + width, stringtie2, color='g',edgecolor='black', width=width, yerr = stringtie2_SD, error_kw=dict(lw=1, capsize=5, capthick=1),label='StringTie2')
    plt.bar(x + width*2, scallop, color='b', edgecolor='black', width=width, yerr = scallop_SD, error_kw=dict(lw=1, capsize=5, capthick=1), label='Scallop')
    plt.bar(x + width*3, class2, color='y', edgecolor='black', width=width, yerr = class2_SD, error_kw=dict(lw=1, capsize=5, capthick=1), label='CLASS2')
    
    ax.set(ylim=[0, 43])
    plt.yticks(np.arange(0, 41, 10), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width*1.5,labels,fontsize=32)

    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.ylabel("Precision (%)", fontsize=32)
    figure_name = './ENCODE10/figure/ENCODE10_pre.pdf'

    plt.savefig(figure_name, bbox_inches='tight')
    return None

def plot_bar_adjusted_pre(hmatch, hpre, smatch, spre):
    samples=['SRR307903','SRR315323','SRR387661','SRR534307','SRR545695','SRR307911','SRR315334','SRR534291','SRR534319','SRR545723']
    hi = []
    hni = []
    for i in range(1,11):
        if(int(hmatch[i-1][0]) < int(hmatch[i-1][1]):
            hi.append(i)
        else:
            hni.append(i)
            
    mi = []
    mni = []
    for i in range(1,11):
        if(int(smatch[i-1][0]) < int(smatch[i-1][1]):
            mi.append(i)
        else:
            mni.append(i)

    ad_st = [0]*10
    ad_sc = [0]*10
    
    for i in hi:
        file1 = './ENCODE10/stringtie2/' + samples[i-1] + '.hisat.roc-cor'
        file2 = './ENCODE10/stringtie2/' + samples[i-1] + '.hisat.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = hmatch[i-1][0]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(hpre[i-1][0]))
                break
    
    for i in hni:
        file1 = './ENCODE10/scallop2/' + samples[i-1] + '.hisat.roc-cor'
        file2 = './ENCODE10/scallop2/' + samples[i-1] + '.hisat.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = hmatch[i-1][1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(hpre[i-1][1]))
                ad_sc[i-1]=(float(pre[j]))
                break
    
    hp1_st = round(np.mean(ad_st),1)
    hp1_std = round(np.std(ad_st),1)
    hp1_sc = round(np.mean(ad_sc),1)
    hp1_scd = round(np.std(ad_sc),1)

    ad_st = [0]*10
    ad_sc = [0]*10

    for i in mi:
        file1 = './ENCODE10/stringtie2/' + samples[i-1] + '.star.roc-cor'
        file2 = './ENCODE10/stringtie2/' + samples[i-1] + '.star.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = smatch[i-1][0]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(spre[i-1][0]))
                break

    for i in mni:
        file1 = './ENCODE10/scallop2/' + samples[i-1] + '.star.roc-cor'
        file2 = './ENCODE10/scallop2/' + samples[i-1] + '.star.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = smatch[i-1][1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(spre[i-1][1]))
                ad_sc[i-1]=(float(pre[j]))
                break

    mp1_st = round(np.mean(ad_st),1)
    mp1_std = round(np.std(ad_st),1)
    mp1_sc = round(np.mean(ad_sc),1)
    mp1_scd = round(np.std(ad_sc),1)

    hi = []
    hni = []
    for i in range(1,11):
        if(int(hmatch[i-1][0]) < int(hmatch[i-1][2]):
            hi.append(i)
        else:
            hni.append(i)
            
    mi = []
    mni = []
    for i in range(1,11):
        if(int(smatch[i-1][0]) < int(smatch[i-1][2]):
            mi.append(i)
        else:
            mni.append(i)

    ad_st = [0]*10
    ad_sc = [0]*10
    
    for i in hi:
        file1 = './ENCODE10/scallop/' + samples[i-1] + '.hisat.roc-cor'
        file2 = './ENCODE10/scallop/' + samples[i-1] + '.hisat.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = hmatch[i-1][0]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(hpre[i-1][0]))
                break
    
    for i in hni:
        file1 = './ENCODE10/scallop2/' + samples[i-1] + '.hisat.roc-cor'
        file2 = './ENCODE10/scallop2/' + samples[i-1] + '.hisat.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_scallop = hmatch[i-1][2]
        for j in range(0, len(cor)):
            if(int(cur_scallop) >= int(cor[j])):
                ad_st[i-1]=(float(hpre[i-1][2]))
                ad_sc[i-1]=(float(pre[j]))
                break
    
    hp2_st = round(np.mean(ad_st),1)
    hp2_std = round(np.std(ad_st),1)
    hp2_sc = round(np.mean(ad_sc),1)
    hp2_scd = round(np.std(ad_sc),1)

    ad_st = [0]*10
    ad_sc = [0]*10

    for i in mi:
        file1 = './ENCODE10/scallop/' + samples[i-1] + '.star.roc-cor'
        file2 = './ENCODE10/scallop/' + samples[i-1] + '.star.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = smatch[i-1][0]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(spre[i-1][0]))
                break

    for i in mni:
        file1 = './ENCODE10/scallop2/' + samples[i-1] + '.star.roc-cor'
        file2 = './ENCODE10/scallop2/' + samples[i-1] + '.star.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_scallop = smatch[i-1][2]
        for j in range(0, len(cor)):
            if(int(cur_scallop) >= int(cor[j])):
                ad_st[i-1]=(float(spre[i-1][2]))
                ad_sc[i-1]=(float(pre[j]))
                break

    mp2_st = round(np.mean(ad_st),1)
    mp2_std = round(np.std(ad_st),1)
    mp2_sc = round(np.mean(ad_sc),1)
    mp2_scd = round(np.std(ad_sc),1)

    hi = []
    hni = []
    for i in range(1,11):
        if(int(hmatch[i-1][0]) < int(hmatch[i-1][3]):
            hi.append(i)
        else:
            hni.append(i)

    mi = []
    mni = []
    for i in range(1,11):
        if(int(smatch[i-1][0]) < int(smatch[i-1][3]):
            mi.append(i)
        else:
            mni.append(i)

    ad_st = [0]*10
    ad_sc = [0]*10

    for i in hi:
        file1 = './ENCODE10/class2/' + samples[i-1] + '.hisat.roc-cor'
        file2 = './ENCODE10/class2/' + samples[i-1] + '.hisat.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = hmatch[i-1][0]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(hpre[i-1][0]))
                break

    for i in hni:
        file1 = './ENCODE10/scallop2/' + samples[i-1] + '.hisat.roc-cor'
        file2 = './ENCODE10/scallop2/' + samples[i-1] + '.hisat.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_class2 = hmatch[i-1][3]
        for j in range(0, len(cor)):
            if(int(cur_class2) >= int(cor[j])):
                ad_st[i-1]=(float(hpre[i-1][3]))
                ad_sc[i-1]=(float(pre[j]))
                break

    hp3_st = round(np.mean(ad_st),1)
    hp3_std = round(np.std(ad_st),1)
    hp3_sc = round(np.mean(ad_sc),1)
    hp3_scd = round(np.std(ad_sc),1)

    ad_st = [0]*10
    ad_sc = [0]*10

    for i in mi:
        file1 = './ENCODE10/class2/' + samples[i-1] + '.star.roc-cor'
        file2 = './ENCODE10/class2/' + samples[i-1] + '.star.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = smatch[i-1][0]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(spre[i-1][0]))
                break

    for i in mni:
        file1 = './ENCODE10/scallop2/' + samples[i-1] + '.star.roc-cor'
        file2 = './ENCODE10/scallop2/' + samples[i-1] + '.star.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_class2 = smatch[i-1][3]
        for j in range(0, len(cor)):
            if(int(cur_class2) >= int(cor[j])):
                ad_st[i-1]=(float(spre[i-1][3]))
                ad_sc[i-1]=(float(pre[j]))
                break

    mp3_st = round(np.mean(ad_st),1)
    mp3_std = round(np.std(ad_st),1)
    mp3_sc = round(np.mean(ad_sc),1)
    mp3_scd = round(np.std(ad_sc),1)
    
    fig, ax = plt.subplots(1, 1, figsize=(6,10), dpi= 600)
    size = 3
    x = np.arange(size)
    c1 = [hp1_st, hp2_st, hp3_st]
    c1_SD = [hp1_std, hp2_std, hp3_std]
    c2 = [hp1_sc, hp2_sc, hp3_sc]
    c2_SD = [hp1_scd, hp2_scd, hp3_scd]
    
    total_width, n = 0.09, 2
    width = total_width / n
    x = x - (total_width - width) / 2
    x[1] = x[1] - 0.88
    x[2] = x[2] - 1.76
    
    labels = ['ST2-SC2', 'SC-SC2','CL2-SC2']
    plt.bar(x, c1, color=['g','b','y'], edgecolor='black', width=width, yerr = c1_SD, error_kw=dict(lw=1,capsize=5,capthick=1))
    plt.bar(x + width, c2, color='r',edgecolor='black', width=width, yerr = c2_SD, error_kw=dict(lw=1, capsize=5, capthick=1))
    ax.set(ylim=[0, 66])
    
    plt.yticks(np.arange(0, 67, 20), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width/2,labels,fontsize=25)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.ylabel("Adjusted precisoin (%)", fontsize=32)
    
    figure_name = './ENCODE10/figure/ENCODE10_adjusted_pre_HISAT.pdf'
    plt.savefig(figure_name, bbox_inches='tight')
    
    fig, ax = plt.subplots(1, 1, figsize=(6,10), dpi= 600)
    
    size = 3
    x = np.arange(size)
    c1 = [mp1_st, mp2_st, mp3_st]
    c1_SD = [mp1_std, mp2_std, mp3_std]
    c2 = [mp1_sc, mp2_sc, mp3_sc]
    c2_SD = [mp1_scd, mp2_scd, mp3_scd]
    
    total_width, n = 0.09, 2
    width = total_width / n
    x = x - (total_width - width) / 2
    x[1] = x[1] - 0.88
    x[2] = x[2] - 1.76
    
    labels = ['ST2-SC2', 'SC-SC2','CL2-SC2']
    plt.bar(x, c1, color=['g','b','y'], edgecolor='black', width=width, yerr = c1_SD, error_kw=dict(lw=1,capsize=5,capthick=1))
    plt.bar(x + width, c2, color='r',edgecolor='black', width=width, yerr = c2_SD, error_kw=dict(lw=1, capsize=5, capthick=1))
    ax.set(ylim=[0, 66])
    
    plt.yticks(np.arange(0, 67, 20), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width/2,labels,fontsize=25)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    plt.ylabel("Adjusted precisoin (%)", fontsize=32)
    
    figure_name = './ENCODE10/figure/ENCODE10_adjusted_pre_STAR.pdf'
    plt.savefig(figure_name, bbox_inches='tight')

    return None

def main():

    hisat_scallop2_match, hisat_scallop2_pre, star_scallop2_match, star_scallop2_pre = load_data('scallop2')
    hisat_stringtie2_match, hisat_stringtie2_pre, star_stringtie2_match, star_stringtie2_pre = load_data('stringtie2')
    hisat_scallop_match, hisat_scallop_pre, star_scallop_match, star_scallop_pre = load_data('scallop')
    hisat_class2_match, hisat_class2_pre, star_class2_match, star_class2_pre = load_data('class2')

    hmatch = merge(hisat_scallop2_match, hisat_stringtie2_match, hisat_scallop_match, hisat_class2_match)
    hpre = merge(hisat_scallop2_pre, hisat_stringtie2_pre, hisat_scallop_pre, hisat_class2_pre)
    smatch = merge(star_scallop2_match, star_stringtie2_match, star_scallop_match, star_class2_match)
    spre = merge(star_scallop2_pre, star_stringtie2_pre, star_scallop_pre, star_class2_pre)

    plot_sample(hmatch, hpre, smatch, spre)
    plot_bar_num(hmatch, smatch)
    plot_bar_pre(hpre, spre)
    plot_bar_adjusted_pre(hmatch, hpre, smatch, spre)

if __name__ == '__main__':
    main()
