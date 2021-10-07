import numpy as np
import matplotlib.pyplot as plt

def load_data(tool):

    dirPath = './Mouse-Fibroblast/' + tool + '/'

    file1 = dirPath + tool + '.numTranscripts.results'
    file2 = dirPath + tool + '.numMatchTranscripts.results'

    total_num = np.loadtxt(file1)
    match_num = np.loadtxt(file2)
    pre = match_num / total_num * 100

    return match_num, pre

def sort(scallop2, stringtie2, scallop, class2):

    bundle = np.array((scallop2, stringtie2, scallop, class2)).T
    bundle = bundle[np.argsort(bundle[:,0])]
    
    return bundle

def plot_cells(match, pre):

    # plot the number of match transcripts and cell id
    x = np.arange(1,370,1)
    y1 = match[:, 0]
    y2 = match[:, 1]
    y3 = match[:, 2]
    y4 = match[:, 3]

    mycolors = ['tab:red', 'tab:blue', 'tab:green', 'tab:orange']
    columns = ['Scallop2', 'StringTie2', 'Scallop', 'CLASS2']

    fig, ax = plt.subplots(1, 1, figsize=(9,9), dpi= 300)
    ax.fill_between(x, y1=y1, y2=0, label=columns[0], alpha=0.8, color=mycolors[0], linewidth=2)
    ax.fill_between(x, y1=y2, y2=0, label=columns[1], alpha=0.8, color=mycolors[1], linewidth=2)
    ax.fill_between(x, y1=y4, y2=0, label=columns[3], alpha=0.8, color=mycolors[3], linewidth=2)
    ax.fill_between(x, y1=y3, y2=0, label=columns[2], alpha=0.8, color=mycolors[2], linewidth=2)
    
    ax.set(ylim=[0, 4201],xlim=[1,370])
    ax.legend(loc='upper left', fontsize=22)
    plt.xticks(np.arange(1, 370.0, 60), fontsize=24, horizontalalignment='center')
    plt.yticks(np.arange(0, 4201.0, 700), fontsize=24)

    for y in np.arange(0, 4201.0, 700):    
        plt.hlines(y, xmin=0, xmax=len(x), colors='black', alpha=0.6, linestyles="--", lw=0.5)

    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)
    plt.xlabel("Mouse cell", fontsize=24)
    plt.ylabel("# Matching transcripts", fontsize=24)
    plt.savefig('./Mouse-Fibroblast/figure/transcripts_num.pdf', bbox_inches = 'tight')

    # plot precision and cell id
    y1 = pre[:, 0]
    y2 = pre[:, 1]
    y3 = pre[:, 2]
    y4 = pre[:, 3]

    fig, ax = plt.subplots(1, 1, figsize=(9,8.6), dpi= 300)
    ax.fill_between(x, y1=y1, y2=0, label=columns[0], alpha=0.8, color=mycolors[0], linewidth=2)
    ax.fill_between(x, y1=y3, y2=0, label=columns[2], alpha=0.8, color=mycolors[2], linewidth=2)
    ax.fill_between(x, y1=y4, y2=0, label=columns[3], alpha=0.8, color=mycolors[3], linewidth=2)
    ax.fill_between(x, y1=y2, y2=0, label=columns[1], alpha=0.8, color=mycolors[1], linewidth=2)

    ax.set(ylim=[0, 71],xlim=[1,370])
    ax.legend(loc='upper left', fontsize=21)
    plt.xticks(np.arange(1, 370.0, 60), fontsize=24, horizontalalignment='center')
    plt.yticks(np.arange(0, 71.0, 10), fontsize=24)
           
    for y in np.arange(0, 71.0, 10):    
        plt.hlines(y, xmin=0, xmax=len(x), colors='black', alpha=0.6, linestyles="--", lw=0.5)

    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(.3)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(.3)

    plt.xlabel("Mouse cell", fontsize=24)
    plt.ylabel("Precision (%)", fontsize=24)
    plt.savefig('./Mouse-Fibroblast/figure/precision.pdf', bbox_inches = 'tight')

    return None

def plot_scatter(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre):
    
    fig, ax = plt.subplots(1, 1, figsize=(12,9), dpi= 600)
    plt.scatter(scallop2_pre, scallop2_match, label='Scallop2', color='r', s=30)
    plt.scatter(stringtie2_pre, stringtie2_match, label='StringTie2', color='g', s=30)
    plt.scatter(scallop_pre, scallop_match, label='Scallop', color='b', s=30)
    plt.scatter(class2_pre, class2_match, label='CLASS2', color='y', s=30)

    ax.set(ylim=[0, 4801],xlim=[15,72])
    ax.legend(loc='upper right', fontsize=23)
    plt.xticks(np.arange(15, 75, 15), fontsize=30, horizontalalignment='center')
    plt.yticks(np.arange(0, 4501, 1500), fontsize=30)
    
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.xlabel("Precision (%)", fontsize=30)
    plt.ylabel("# Matching transcripts", fontsize=30)

    plt.savefig('./Mouse-Fibroblast/figure/scatter.pdf', bbox_inches = 'tight')
    return None

def main():

    scallop2_match, scallop2_pre = load_data('scallop2')
    stringtie2_match, stringtie2_pre = load_data('stringtie2')
    scallop_match, scallop_pre = load_data('scallop')
    class2_match, class2_pre = load_data('class2')

    sort_match = sort(scallop2_match, stringtie2_match, scallop_match, class2_match)
    sort_pre = sort(scallop2_pre, stringtie2_pre, scallop_pre, class2_pre)

    plot_cells(sort_match, sort_pre)
    plot_scatter(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre)

if __name__ == '__main__':
    main()
