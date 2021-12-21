import numpy as np
import matplotlib.pyplot as plt
import os

p1 = [20, 50, 100, 200] # min_bundle_gap
p2 = [0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8, 9, 10]
p1_size = len(p1)
p2_size = len(p2)

def load_data(tool):
   
    m = np.zeros([p1_size * p2_size,192])
    p = np.zeros([p1_size * p2_size,192])

    dirPath = './HEK293T/' + tool + '/'
    
    for i in range(0, p1_size):
        for j in range(0, p2_size):
            file1 = dirPath + str(p1[i]) + '-' + str(p2[j]) + '.' + tool + '.numMultiTranscripts.results'
            file2 = dirPath + str(p1[i]) + '-' + str(p2[j]) + '.' + tool + '.numMatchIntronChain.results'
            total_num = np.loadtxt(file1)
            match_num = np.loadtxt(file2)
            pre = match_num / total_num * 100
            
            m[int(i*p2_size+j)] = match_num
            p[int(i*p2_size+j)] = pre           

    return m, p

def plot_2d(scallop2_match, stringtie2_match, scallop_match, scallop2_pre, stringtie2_pre, scallop_pre):

    scallop2_match_ave = np.zeros([p1_size,p2_size])
    stringtie2_match_ave = np.zeros([p1_size,p2_size])
    scallop_match_ave = np.zeros([p1_size,p2_size])
    scallop2_match_sd = np.zeros([p1_size,p2_size])
    stringtie2_match_sd = np.zeros([p1_size,p2_size])
    scallop_match_sd = np.zeros([p1_size,p2_size])
    scallop2_pre_ave = np.zeros([p1_size,p2_size])
    stringtie2_pre_ave = np.zeros([p1_size,p2_size])
    scallop_pre_ave = np.zeros([p1_size,p2_size])
    scallop2_pre_sd = np.zeros([p1_size,p2_size])
    stringtie2_pre_sd = np.zeros([p1_size,p2_size])
    scallop_pre_sd = np.zeros([p1_size,p2_size])
    
    for i in range(0, p1_size):
        for j in range(0, p2_size):
            scallop2_match_ave[i][j] = round(np.mean(scallop2_match[i*p2_size+j]), 2)
            stringtie2_match_ave[i][j] = round(np.mean(stringtie2_match[i*p2_size+j]), 2)
            scallop_match_ave[i][j] = round(np.mean(scallop_match[i*p2_size+j]), 2)
            scallop2_pre_ave[i][j] = round(np.mean(scallop2_pre[i*p2_size+j]), 2)
            stringtie2_pre_ave[i][j] = round(np.mean(stringtie2_pre[i*p2_size+j]), 2)
            scallop_pre_ave[i][j] = round(np.mean(scallop_pre[i*p2_size+j]), 2)
            scallop2_match_sd[i][j] = round(np.std(scallop2_match[i*p2_size+j]), 2)
            stringtie2_match_sd[i][j] = round(np.std(stringtie2_match[i*p2_size+j]), 2)
            scallop_match_sd[i][j] = round(np.std(scallop_match[i*p2_size+j]), 2)
            scallop2_pre_sd[i][j] = round(np.std(scallop2_pre[i*p2_size+j]), 2)
            stringtie2_pre_sd[i][j] = round(np.std(stringtie2_pre[i*p2_size+j]), 2)
            scallop_pre_sd[i][j] = round(np.std(scallop_pre[i*p2_size+j]), 2)
    
    idx = ['a', ' ', ' ', ' ']
    markers= ['o', '^', '+', 's']
    for i in range(0, p1_size):

        fig, ax = plt.subplots(1, 1, figsize=(6,6), dpi= 200)
        x1 = scallop2_pre_ave[i]
        y1 = scallop2_match_ave[i]
        x2 = stringtie2_pre_ave[i]
        y2 = stringtie2_match_ave[i]
        x3 = scallop_pre_ave[i]
        y3 = scallop_match_ave[i]

        ax.scatter(x1, y1, c='red', marker=markers[0], label='Scallop2-HISAT2', s=50)
        ax.scatter(x2, y2, c='green', marker=markers[0], label='StringTie2-HISAT2', s=50)
        ax.scatter(x3, y3, c='blue', marker=markers[0], label='Scallop-HISAT2', s=50)
        ax.plot(x1, y1, c='red')
        ax.plot(x2, y2, c='green')
        ax.plot(x3, y3, c='blue')
        
        ax.set(ylim=[400, 2400],xlim=[25, 100])
        plt.xticks(np.arange(25, 101, 30), fontsize=24, horizontalalignment='center')
        plt.yticks(np.arange(400, 2401, 1000), fontsize=24)
        plt.yticks(rotation = 90)

        plt.gca().spines["top"].set_alpha(1)
        plt.gca().spines["bottom"].set_alpha(1)
        plt.gca().spines["right"].set_alpha(1)
        plt.gca().spines["left"].set_alpha(1)

        plt.xlabel("Precision (%)", fontsize=24)
        plt.ylabel("# Matching Transcripts", fontsize=24)
        text = 'minimum gap = ' + str(p1[i])
        plt.text(26, 600, text, fontsize=20)
        plt.text(10, 2300, idx[i], fontsize=30)
        figure_name = './HEK293T/figure/HEK293T-vary-para-' + str(p1[i]) + '-multi-2d.pdf'
        plt.savefig(figure_name, bbox_inches='tight')
        plt.show()
        


def get_adjusted(idx1, idx2, scallop2_match, scallop2_pre, stringtie2_match, stringtie2_pre, scallop_match, scallop_pre):
    
    hi = []
    hni = []
    for i in range(1,193):
        if(int(scallop2_match[i-1]) < int(stringtie2_match[i-1])):
            hi.append(i)
        else:
            hni.append(i)
            
    ad_st = [0]*192
    ad_sc = [0]*192
    for i in range(0,192):
        ad_sc[i]=(float(scallop2_pre[i]))
        ad_st[i]=(float(stringtie2_pre[i]))
    
    for i in hi:
        file1 = './HEK293T/stringtie2/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.stringtie2.me.roc-cor'
        file2 = './HEK293T/stringtie2/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.stringtie2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = scallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(scallop2_pre[i-1]))
                break
            
    for i in hni:
        file1 = './HEK293T/scallop2/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.scallop2.me.roc-cor'
        file2 = './HEK293T/scallop2/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.scallop2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = stringtie2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(stringtie2_pre[i-1]))
                ad_sc[i-1]=(float(pre[j]))
                break

    human_p1_st2 = ad_st
    human_p1_sc2 = ad_sc
    
    hp1_st = round(np.mean(ad_st),2)
    hp1_std = round(np.std(ad_st),2)
    hp1_sc = round(np.mean(ad_sc),2)
    hp1_scd = round(np.std(ad_sc),2)
    
    hi = []
    hni = []
    for i in range(1,193):
        if(int(scallop2_match[i-1]) < int(scallop_match[i-1])):
            hi.append(i)
        else:
            hni.append(i)
            
    ad_st = [0]*192
    ad_sc = [0]*192
    for i in range(0,192):
        ad_sc[i]=(float(scallop2_pre[i]))
        ad_st[i]=(float(scallop_pre[i]))
    
    for i in hi:
        file1 = './HEK293T/scallop/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.scallop.me.roc-cor'
        file2 = './HEK293T/scallop/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.scallop.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = scallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(scallop2_pre[i-1]))
                break
            
    for i in hni:
        if(idx1 == 3 and idx2 == 14 and i == 155):
            ad_st[i-1] = (float(scallop_pre[i-1]))
            ad_sc[i-1] = (float(scallop2_pre[i-1]))
            continue
        file1 = './HEK293T/scallop2/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.scallop2.me.roc-cor'
        file2 = './HEK293T/scallop2/' + str(i) + '.' + str(p1[idx1]) + '-' + str(p2[idx2]) + '.scallop2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = scallop_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(scallop_pre[i-1]))
                ad_sc[i-1]=(float(pre[j]))
                break

    human_p2_sc = ad_st
    human_p2_sc2 = ad_sc

    hp2_st = round(np.mean(ad_st),2)
    hp2_std = round(np.std(ad_st),2)
    hp2_sc = round(np.mean(ad_sc),2)
    hp2_scd = round(np.std(ad_sc),2)
    
    return hp1_sc, hp1_st, hp2_sc, hp2_st, hp1_scd, hp1_std, hp2_scd, hp2_std

def plot_adjusted_bar(scallop2_match, stringtie2_match, scallop_match, scallop2_pre, stringtie2_pre, scallop_pre):

    pair = ['SC2-ST2', 'SC2-SC']
    scallop2_adjusted1_ave = np.zeros([p1_size,p2_size])
    stringtie2_adjusted_ave = np.zeros([p1_size,p2_size])
    scallop2_adjusted2_ave = np.zeros([p1_size,p2_size])
    scallop_adjusted_ave = np.zeros([p1_size,p2_size])
    scallop2_adjusted1_sd = np.zeros([p1_size,p2_size])
    stringtie2_adjusted_sd = np.zeros([p1_size,p2_size])
    scallop2_adjusted2_sd = np.zeros([p1_size,p2_size])
    scallop_adjusted_sd = np.zeros([p1_size,p2_size])

    for i in range(0, p1_size):
        for j in range(0, p2_size):
            scallop2_adjusted1_ave[i][j], stringtie2_adjusted_ave[i][j], scallop2_adjusted2_ave[i][j], scallop_adjusted_ave[i][j], scallop2_adjusted1_sd[i][j], stringtie2_adjusted_sd[i][j], scallop2_adjusted2_sd[i][j], scallop_adjusted_sd[i][j] = get_adjusted(i, j, scallop2_match[int(i*p2_size+j)], scallop2_pre[int(i*p2_size+j)],stringtie2_match[int(i*p2_size+j)], stringtie2_pre[int(i*p2_size+j)], scallop_match[int(i*p2_size+j)], scallop_pre[int(i*p2_size+j)])

    idx = ['a', ' ', ' ', ' ']
    for i in range(0, p1_size):
        fig, ax = plt.subplots(1, 1, figsize=(12,1.6), dpi= 200)
        size = p2_size
        x = np.arange(size)
        p1_scallop2 = scallop2_adjusted1_ave[i]
        p1_scallop2_SD = scallop2_adjusted1_sd[i]
        p1_stringtie2 = stringtie2_adjusted_ave[i]
        p1_stringtie2_SD = stringtie2_adjusted_sd[i]

        p2_scallop2 = scallop2_adjusted2_ave[i]
        p2_scallop2_SD = scallop2_adjusted2_sd[i]
        p2_scallop = scallop_adjusted_ave[i]
        p2_scallop_SD = scallop_adjusted_sd[i]

        total_width, n = 0.78, 4
        width = total_width / n
        x = x - (total_width - width) / 2

        xlabels = p2
        xlabels[14] = '10'
        plt.bar(x, p1_scallop2, color='r', edgecolor='black',width=width, yerr = p1_scallop2_SD, error_kw=dict(lw=1,capsize=3,capthick=1),label='Scallop2')
        plt.bar(x + width, p1_stringtie2, color='g', edgecolor='black',width=width, yerr = p1_stringtie2_SD, error_kw=dict(lw=1,capsize=3,capthick=1),label='StringTie2')
        plt.bar(x + 2*width+0.05, p2_scallop2, color='r', edgecolor='black',width=width, yerr = p2_scallop2_SD, error_kw=dict(lw=1,capsize=3,capthick=1), label='Scallop2')
        plt.bar(x + 3*width+0.05, p2_scallop, color='b', edgecolor='black',width=width, yerr = p2_scallop_SD, error_kw=dict(lw=1,capsize=3,capthick=1), label='Scallop')

        ax.set(ylim=[0, 105])
        ax.set(xlim=[-0.5, 14.5])

        plt.yticks(np.arange(0, 101, 50), fontsize=14)
        plt.yticks(rotation = 90)
        plt.xticks(x+width*1.5+0.025,xlabels,fontsize=14)

        plt.gca().spines["top"].set_alpha(0)
        plt.gca().spines["bottom"].set_alpha(0)
        plt.gca().spines["right"].set_alpha(0)
        plt.gca().spines["left"].set_alpha(1)

        plt.ylabel("Adjusted Precision (%)", fontsize=12)
        plt.text(-1.7,110,idx[i], fontsize=18)
        text = 'minimum gap = ' + str(p1[i])
        plt.text(-0.2, 90, text, fontsize=14)

        figure_name = './HEK293T/figure/HEK293T-vary-para-adjusted' + str(p1[i]) +'-multi.pdf'
        plt.savefig(figure_name, bbox_inches='tight')

        
def main():

    scallop2_match, scallop2_pre = load_data('scallop2')
    stringtie2_match, stringtie2_pre = load_data('stringtie2')
    scallop_match, scallop_pre = load_data('scallop')

    plot_2d(scallop2_match, stringtie2_match, scallop_match, scallop2_pre, stringtie2_pre, scallop_pre)
    plot_adjusted_bar(scallop2_match, stringtie2_match, scallop_match, scallop2_pre, stringtie2_pre, scallop_pre)

if __name__ == '__main__':
    main()

