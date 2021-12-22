import numpy as np
import matplotlib.pyplot as plt
import os

def load_data(tool):
    database=['hisat', 'star']
    level = ['low', 'middle', 'high']
    
    hmatch = np.zeros([3, 10])
    hpre = np.zeros([3, 10])
    smatch = np.zeros([3, 10])
    spre = np.zeros([3, 10])
    
    for i in range(0, 2):
        dirPath = './ENCODE10/' + tool + '/' + database[i] + '.'
        for j in range(0, 3):
            file1 = dirPath + level[j] + '.numMultiTranscripts.results'
            file2 = dirPath + level[j] + '.numMatchIntronChain.results'
            total_num = np.loadtxt(file1)
            match_num = np.loadtxt(file2)
            pre = match_num / total_num * 100
            if(i == 0):
                hmatch[j] = match_num
                hpre[j] = pre
            else:
                smatch[j] = match_num
                spre[j] = pre

    return hmatch, hpre, smatch, spre

def get_ave_and_std(hmatch, hpre, smatch, spre):
    all_match = np.zeros([4,3])
    all_pre = np.zeros([4,3])
    
    for i in range(0, 3):
        all_match[0][i] = np.around(np.mean(hmatch[i]), 2)
        all_match[1][i] = np.around(np.std(hmatch[i]), 2)
        all_pre[0][i] = np.around(np.mean(hpre[i]),2)
        all_pre[1][i] = np.around(np.std(hpre[i]),2)
        
        all_match[2][i] = np.around(np.mean(smatch[i]), 2)
        all_match[3][i] = np.around(np.std(smatch[i]), 2)
        all_pre[2][i] = np.around(np.mean(spre[i]),2)
        all_pre[3][i] = np.around(np.std(spre[i]),2)
    
    return all_match, all_pre

def plot_2d(scallop2_match, stringtie2_match, scallop_match, scallop2_pre, stringtie2_pre, scallop_pre):
    labels = ['Low', 'Middle', 'High']
    markers= ['s', '^', 'o', '+']
    idx = ['a', ' ', ' ']
    
    x1 = scallop2_pre[0]
    y1 = scallop2_match[0]
    x2 = stringtie2_pre[0]
    y2 = stringtie2_match[0]
    x3 = scallop_pre[0]
    y3 = scallop_match[0]
    
    x4 = scallop2_pre[2]
    y4 = scallop2_match[2]
    x5 = stringtie2_pre[2]
    y5 = stringtie2_match[2]
    x6 = scallop_pre[2]
    y6 = scallop_match[2]

    fig, ax = plt.subplots(1, 1, figsize=(6,6), dpi= 200)

    for i in range(0,3):
        ax.scatter(x1[i], y1[i], c='red', marker=markers[i], label='Scallop2-HISAT2', s=150)
        ax.scatter(x2[i], y2[i], c='green', marker=markers[i], label='StringTie2-HISAT2', s=150)
        ax.scatter(x3[i], y3[i], c='blue', marker=markers[i], label='Scallop-HISAT2', s=150)

    ax.set(ylim=[0, 10000],xlim=[0, 26])
    plt.xticks(np.arange(0, 27, 13), fontsize=24, horizontalalignment='center')
    plt.yticks(np.arange(0, 10001, 5000), fontsize=24)
    plt.yticks(rotation = 90)

    plt.gca().spines["top"].set_alpha(1)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(1)
    plt.gca().spines["left"].set_alpha(1)

    plt.ylabel("# Matching Transcripts", fontsize=24)
    plt.xlabel("Precision (%)", fontsize=24)
    plt.text(11, 2000, 'ENCODE10-HISAT2', fontsize=20)
    plt.text(-6, 9600, ' ', fontsize=30)
    figure_name = "./ENCODE10/figure/encode10-hisat-quant-2d.pdf"
    plt.savefig(figure_name, bbox_inches='tight')
    plt.show()
    fig, ax = plt.subplots(1, 1, figsize=(6,6), dpi= 200)
    
    for i in range(0,3):
        ax.scatter(x1[i], y1[i], c='red', marker=markers[i], label='Scallop2-HISAT2', s=150)
        ax.scatter(x2[i], y2[i], c='green', marker=markers[i], label='StringTie2-HISAT2', s=150)
        ax.scatter(x3[i], y3[i], c='blue', marker=markers[i], label='Scallop-HISAT2', s=150)

    ax.set(ylim=[0, 10000],xlim=[0, 26])
    plt.xticks(np.arange(0, 27, 13), fontsize=24, horizontalalignment='center')
    plt.yticks(np.arange(0, 10001, 5000), fontsize=24)
    plt.yticks(rotation = 90)

    plt.gca().spines["top"].set_alpha(1)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(1)
    plt.gca().spines["left"].set_alpha(1)

    plt.ylabel("# Matching Transcripts", fontsize=24)
    plt.xlabel("Precision (%)", fontsize=24)
    plt.text(11, 2000, 'ENCODE10-STAR', fontsize=20)
    plt.text(-6, 9600, ' ', fontsize=30)
    figure_name = "./ENCODE10/figure/encode10-star-quant-2d.pdf"
    plt.savefig(figure_name, bbox_inches='tight')
    plt.show()
    
def get_adjusted(dataset, idx, scallop2_match, scallop2_pre, stringtie2_match, stringtie2_pre, scallop_match, scallop_pre):
    size = 10
    samples=['SRR307903','SRR315323','SRR387661','SRR534307','SRR545695','SRR307911','SRR315334','SRR534291','SRR534319','SRR545723']
    levels = ['low', 'middle', 'high']

    hi = []
    hni = []
    for i in range(1,size + 1):
        if(int(scallop2_match[i-1]) < int(stringtie2_match[i-1])):
            hi.append(i)
        else:
            hni.append(i)
            
    ad_st = [0]*size
    ad_sc = [0]*size
    
    for i in hi:
        file1 = './ENCODE10' + '/stringtie2/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-cor'
        file2 = './ENCODE10' + '/stringtie2/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = scallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(scallop2_pre[i-1]))
                break
            
    for i in hni:
        file1 = './ENCODE10' + '/scallop2/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-cor'
        file2 = './ENCODE10' + '/scallop2/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-pre'
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
    for i in range(1,size + 1):
        if(int(scallop2_match[i-1]) < int(scallop_match[i-1])):
            hi.append(i)
        else:
            hni.append(i)
            
    ad_st = [0]*size
    ad_sc = [0]*size
    
    for i in hi:
        file1 = './ENCODE10' + '/scallop/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-cor'
        file2 = './ENCODE10' + '/scallop/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = scallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(scallop2_pre[i-1]))
                break
            
    for i in hni:
        file1 = './ENCODE10' + '/scallop2/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-cor'
        file2 = './ENCODE10' + '/scallop2/' + samples[i-1] + '.' + dataset + '.' + levels[idx] + '.roc-pre'
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
        
def plot_adjusted_bar(dataset, scallop2_match, scallop2_pre, stringtie2_match, stringtie2_pre, scallop_match, scallop_pre):
    labels = ['Low', 'Middle', 'High']
    pair = ['SC2-ST2', 'SC2-SC']
    scallop2_adjusted1_ave = np.zeros(3)
    stringtie2_adjusted_ave = np.zeros(3)
    scallop2_adjusted2_ave = np.zeros(3)
    scallop_adjusted_ave = np.zeros(3)
    scallop2_adjusted1_sd = np.zeros(3)
    stringtie2_adjusted_sd = np.zeros(3)
    scallop2_adjusted2_sd = np.zeros(3)
    scallop_adjusted_sd = np.zeros(3)
    
    for i in range(0,3):
        scallop2_adjusted1_ave[i], stringtie2_adjusted_ave[i], scallop2_adjusted2_ave[i], scallop_adjusted_ave[i], scallop2_adjusted1_sd[i], stringtie2_adjusted_sd[i], scallop2_adjusted2_sd[i], scallop_adjusted_sd[i] = get_adjusted(dataset, i, scallop2_match[i], scallop2_pre[i],stringtie2_match[i], stringtie2_pre[i], scallop_match[i], scallop_pre[i])
 
    idx = ['d', ' ',' ']
    if(dataset == 'star'):
        idx = ['e', ' ',' ']
    for i in range(0, 3):
        fig, ax = plt.subplots(1, 1, figsize=(6,6), dpi= 200)
        size = 2;
        x = np.arange(size)
        c1 = [scallop2_adjusted1_ave[i], scallop2_adjusted2_ave[i]]
        c1_SD = [scallop2_adjusted1_sd[i], scallop2_adjusted2_sd[i]]
        c2 = [stringtie2_adjusted_ave[i], scallop_adjusted_ave[i]]
        c2_SD = [stringtie2_adjusted_sd[i], scallop_adjusted_sd[i]]
        total_width, n = 0.6, 2
        width = total_width / n
        x = x - (total_width - width) / 2
        x[1] = x[1] - 0.3
        plt.bar(x, c1, color='r', edgecolor='black', width=width, yerr = c1_SD, error_kw=dict(lw=1,capsize=5,capthick=1))
        plt.bar(x + width, c2, color=['g','b','y'],edgecolor='black', width=width, yerr = c2_SD, error_kw=dict(lw=1, capsize=5, capthick=1))
        
        ax.set(ylim=[0, 4])
        plt.yticks(np.arange(0, 5, 2), fontsize=32)
        if(i == 1):
            ax.set(ylim=[0,13])
            plt.yticks(np.arange(0,13,6), fontsize=32)
        elif(i == 2):
            ax.set(ylim=[0,46])
            plt.yticks(np.arange(0, 41.0, 20.0), fontsize=32)
        plt.yticks(rotation = 90)
        plt.xticks(x+width*0.5,pair,fontsize=32)
        
        if(dataset == 'star'):
            ax.set(ylim=[0, 4])
            plt.yticks(np.arange(0, 5, 2), fontsize=32)
            if(i == 1):
                ax.set(ylim=[0,13])
                plt.yticks(np.arange(0, 14, 6), fontsize=32)
            elif(i == 2):
                ax.set(ylim=[0,48])
                plt.yticks(np.arange(0, 42.0, 20.0), fontsize=32)

        plt.gca().spines["top"].set_alpha(0)
        plt.gca().spines["bottom"].set_alpha(0)
        plt.gca().spines["right"].set_alpha(0)
        plt.gca().spines["left"].set_alpha(1)

        plt.ylabel("Adjusted precision (%)", fontsize=32)
        ymax=4
        if(i == 1):
            ymax = 13
        elif(i == 2):
            ymax = 48
        plt.text(-0.9,ymax*0.95,idx[i], fontsize = 42)
        plt.xlabel(labels[i], fontsize=32)
        figure_name = "./ENCODE10/figure/" + dataset + "-" + labels[i] + "-adjusted-precision-quant.pdf"
        plt.savefig(figure_name, bbox_inches='tight')
        plt.show()
        
def main():

    hscallop2_match, hscallop2_pre, sscallop2_match, sscallop2_pre = load_data('scallop2')
    hstringtie2_match, hstringtie2_pre, sstringtie2_match, sstringtie2_pre = load_data('stringtie2')
    hscallop_match, hscallop_pre, sscallop_match, sscallop_pre = load_data('scallop')
    
    scallop2_match, scallop2_pre = get_ave_and_std(hscallop2_match, hscallop2_pre, sscallop2_match, sscallop2_pre)
    stringtie2_match, stringtie2_pre = get_ave_and_std(hstringtie2_match, hstringtie2_pre, sstringtie2_match, sstringtie2_pre)
    scallop_match, scallop_pre = get_ave_and_std(hscallop_match, hscallop_pre, sscallop_match, sscallop_pre)
    plot_2d(scallop2_match, stringtie2_match, scallop_match, scallop2_pre, stringtie2_pre, scallop_pre)

    plot_adjusted_bar('hisat', hscallop2_match, hscallop2_pre, hstringtie2_match, hstringtie2_pre, hscallop_match, hscallop_pre)
    plot_adjusted_bar('star', sscallop2_match, sscallop2_pre, sstringtie2_match, sstringtie2_pre, sscallop_match, sscallop_pre)

if __name__ == '__main__':
    main()

