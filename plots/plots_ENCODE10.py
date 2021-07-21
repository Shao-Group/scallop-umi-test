import numpy as np
import matplotlib.pyplot as plt

def load_data(tool):

    dirPath = './ENCODE10/' + tool + '/'

    file1 = dirPath + 'hisat' + tool + '.numTranscripts.results'
    file2 = dirPath + 'hisat' + tool + '.numMatchTranscripts.results'
    file3 = dirPath + 'star' + tool + '.numTranscripts.results'
    file4 = dirPath + 'star' + tool + '.numMatchTranscripts.results'

    hisat_total_num = np.loadtxt(file1)
    hisat_match_num = np.loadtxt(file2)
    hisat_pre = match_num / total_num * 100
    star_total_num = np.loadtxt(file3)
    star_match_num = np.loadtxt(file4)
    star_pre = match_num / total_num * 100

    return hisat_match_num, hisat_pre, star_match_num, star_pre

def merge(scallop2, stringtie2, scallop, class2):

    bundle = np.array((scallop2, stringtie2, scallop, class2)).T

    return bundle

def plot(hmatch, hpre, smatch, spre):

    samples=['SRR307903','SRR315323','SRR387661','SRR534307','SRR545695','SRR307911','SRR315334','SRR534291','SRR534319','SRR545723']

    for ii in range(1,11):
        fig, ax = plt.subplots(1, 1, figsize=(12,9), dpi= 300)

        markers= ['o', '^', '+', 's']

        i = ii - 1
        x1 = hpre[i,0]
        y1 = hmatch[i,0]
        x2 = hpre[i,1]
        y2 = hmatch[i,1]
        x3 = hpre[i,2]
        y3 = hmatch[i,2]
        x4 = spre[i,0]
        y4 = smatch[i,0]
        x5 = spre[i,1]
        y5 = smatch[i,1]
        x6 = spre[i,2]
        y6 = smatch[i,2]
        x7 = hpre[i,3]
        y7 = hmatch[i,3]
        x8 = spre[i,3]
        y8 = smatch[i,3]

        file1 = './ENCODE10/' + samples[i] + '.hisat.roc-cor'
        file2 = './ENCODE10/' + samples[i] + '.hisat.roc-pre'
        file3 = './ENCODE10/' + samples[i] + '.star.roc-cor'
        file4 = './ENCODE10/' + samples[i] + '.star.roc-pre'

        hcor = np.loadtxt(file1)
        hpre = np.loadtxt(file2)
        scor = np.loadtxt(file3)
        spre = np.loadtxt(file4)

        ax.plot(hpre,hcor, c='r')
        ax.plot(spre,scor,c='b')

        ax.scatter(x1, y1, c='w', edgecolors='red', marker=markers[0], label='Scallop2-HISAT2', s=300)
        ax.scatter(x2, y2, c='w', edgecolors='red', marker=markers[1], label='StringTie2-HISAT2', s=300)
        ax.scatter(x3, y3, c='red', marker=markers[2], label='Scallop-HISAT2', s=300)
        ax.scatter(x7, y7, c='w', edgecolors='red', marker=markers[3], label='CLASS2-HISAT2', s=250)

        ax.scatter(x4, y4, c='w', edgecolors='blue', marker=markers[0], label='Scallop2-STAR', s=300)
        ax.scatter(x5, y5, c='w', edgecolors='blue', marker=markers[1], label='StringTie2-STAR', s=300)
        ax.scatter(x6, y6, c='blue', marker=markers[2], label='Scallop-STAR', s=300)
        ax.scatter(x8, y8, c='w', edgecolors='blue', marker=markers[3], label='CLASS2-STAR', s=250)

        xlist = [x1, x2, x3, x4, x5, x6, x7, x8]
        xminl = int(min(xlist)) - 1

        if(ii == 1):
            xmaxl = int(max(xlist) + 25)
        elif(ii == 2):
            xmaxl = int(max(xlist) + 19)
        elif(ii == 3):
            xmaxl = int(max(xlist) + 17)
        elif(ii == 4):
            xmaxl = int(max(xlist) + 24)
        elif(ii == 5):
            xmaxl = int(max(xlist) + 18)
        elif(ii == 6):
            xmaxl = int(max(xlist) + 23)
        elif(ii == 7):
            xmaxl = int(max(xlist) + 25)
        elif(ii == 9):
            xmaxl = int(max(xlist) + 15)
        else:
            xmaxl = int(max(xlist) + 23)

    ylist = [y1, y2, y3, y4, y5, y6, y7, y8]
    yminl = int((int(min(ylist)/1000))*1000)
    if(ii==7):
        ymaxl = int((int(max(ylist)/1000)))*1000+2001
    else:
        ymaxl = int((int(max(ylist)/1000)))*1000+1001

    ax.set(ylim=[yminl, ymaxl],xlim=[xminl,xmaxl])
    ax.legend(loc='upper right', fontsize=12)

    plt.xticks(np.arange(xminl, xmaxl, 6), fontsize=28, horizontalalignment='center')
    plt.yticks(np.arange(yminl, ymaxl, 1000), fontsize=28)

    for y in np.arange(yminl, ymaxl+1,1000):
        plt.hlines(y, xmin=xminl, xmax=xmaxl, colors='black', alpha=0.6, linestyles="--", lw=0.5)

    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)

    plt.xlabel("Precision (%)", fontsize=30)
    plt.ylabel("# Matching transcripts", fontsize=30)

    figure_name = './ENCODE10/figure/' + samples[i] + '.pdf'

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

    plot(hmatch, hpre, smatch, spre)

if __name__ == '__main__':
    main()
