import numpy as np
import matplotlib.pyplot as plt
import plots_multi_Mouse_Fibroblast as pm

def load_data(tool):

    dirPath = './HEK293T/' + tool + '/'

    file1 = dirPath + tool + '.numMultiTranscripts.results'
    file2 = dirPath + tool + '.numMatchIntronChain.results'

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
    x = np.arange(1,193,1)
    y1 = match[:, 0]
    y2 = match[:, 1]
    y3 = match[:, 2]
    y4 = match[:, 3]

    mycolors = ['r', 'g', 'b', 'y']
    columns = ['Scallop2', 'StringTie2', 'Scallop', 'CLASS2']

    fig, ax = plt.subplots(1, 1, figsize=(12,9), dpi= 300)
    ax.fill_between(x, y1=y1, y2=0, label=columns[0], alpha=0.9, color=mycolors[0], linewidth=2)
    ax.fill_between(x, y1=y2, y2=0, label=columns[1], alpha=0.9, color=mycolors[1], linewidth=2)
    ax.fill_between(x, y1=y3, y2=0, label=columns[2], alpha=0.9, color=mycolors[2], linewidth=2)
    ax.fill_between(x, y1=y4, y2=0, label=columns[3], alpha=0.9, color=mycolors[3], linewidth=2)
    
    ax.set(ylim=[0, 4801],xlim=[1,192])
    ax.legend(loc='upper left', fontsize=22)
    plt.xticks(np.arange(1, 193.0, 40), fontsize=30, horizontalalignment='center')
    plt.yticks(np.arange(0, 4801.0, 1600), fontsize=30)
    plt.yticks(rotation = 90)

    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    plt.xlabel("HE Single cells", fontsize=30)
    plt.ylabel("# Matching transcripts", fontsize=30)
    plt.savefig('./HEK293T/figure/cells_transcripts_num_multiExon.pdf', bbox_inches = 'tight')

    # plot precision and cell id
    y1 = pre[:, 0]
    y2 = pre[:, 1]
    y3 = pre[:, 2]
    y4 = pre[:, 3]

    fig, ax = plt.subplots(1, 1, figsize=(12,9), dpi= 600)
    ax.fill_between(x, y1=y1, y2=0, label=columns[0], alpha=0.9, color=mycolors[0], linewidth=2)
    ax.fill_between(x, y1=y3, y2=0, label=columns[2], alpha=0.9, color=mycolors[2], linewidth=2)
    ax.fill_between(x, y1=y2, y2=0, label=columns[1], alpha=0.9, color=mycolors[1], linewidth=2)
    ax.fill_between(x, y1=y4, y2=0, label=columns[3], alpha=0.9, color=mycolors[3], linewidth=2)

    ax.set(ylim=[0, 81],xlim=[1,193])
    ax.legend(loc='upper left', fontsize=22)
    plt.xticks(np.arange(1, 193.0, 40), fontsize=30, horizontalalignment='center')
    plt.yticks(np.arange(0, 81.0, 20), fontsize=30)
    plt.yticks(rotation = 90)
           
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)

    plt.xlabel("HE Single Cells", fontsize=30)
    plt.ylabel("Precision (%)", fontsize=30)
    plt.savefig('./HEK293T/figure/cells_precision_multiExon.pdf', bbox_inches = 'tight')

    return None

def plot_bar(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre):
    mscallop2_match, mscallop2_pre = pm.load_data('scallop2')
    mstringtie2_match, mstringtie2_pre = pm.load_data('stringtie2')
    mscallop_match, mscallop_pre = pm.load_data('scallop')
    mclass2_match, mclass2_pre = pm.load_data('class2')

    fig, ax = plt.subplots(1, 1, figsize=(6,10), dpi= 600)
    size = 2
    x = np.arange(size)
    
    scallop2 = [np.mean(scallop2_match), np.mean(mscallop2_match)]
    scallop2_SD = [np.std(scallop2_match), np.std(mscallop2_match)]
    stringtie2 = [np.mean(stringtie2_match), np.mean(mstringtie2_match)]
    stringtie2_SD = [np.std(stringtie2_match), np.std(mstringtie2_match)]
    scallop = [np.mean(scallop_match), np.mean(mscallop_match)]
    scallop_SD = [np.std(scallop_match), np.std(mscallop_match)]
    class2 = [np.mean(class2_match), np.mean(mclass2_match)]
    class2_SD = [np.std(class2_match), np.std(mclass2_match)]
    
    total_width, n = 0.2, 4
    width = total_width / n
    x = x - (total_width - width) / 2
    x[1] = x[1] - 0.75
    labels = ['HE', 'MF']
    
    plt.bar(x, scallop2, color='r', edgecolor='black',width=width, yerr = scallop2_SD, error_kw=dict(lw=1,capsize=5,capthick=1),label='Scallop2')
    plt.bar(x + width, stringtie2, color='g', edgecolor='black',width=width, yerr = stringtie2_SD, error_kw=dict(lw=1,capsize=5,capthick=1),label='StringTie2')
    plt.bar(x + width*2, scallop, color='b', edgecolor='black',width=width, yerr = scallop_SD, error_kw=dict(lw=1,capsize=5,capthick=1), label='Scallop')
    plt.bar(x + width*3, class2, color='y', edgecolor='black', width=width, yerr = class2_SD, error_kw=dict(lw=1,capsize=5,capthick=1), label='CLASS2')
    
    ax.set(ylim=[0, 3200])
    
    plt.yticks(np.arange(0, 3201, 1000), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width*1.5,labels,fontsize=32)
    
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.ylabel("# Matching Transcripts", fontsize=32)
    
    figure_name = './HEK293T/figure/Smart-seq3_transcripts_num_multiExon.pdf'
    plt.savefig(figure_name, bbox_inches='tight')
    
    fig, ax = plt.subplots(1, 1, figsize=(6,10), dpi= 600)
    
    size = 2
    x = np.arange(size)

    scallop2 = [np.mean(scallop2_pre), np.mean(mscallop2_pre)]
    scallop2_SD = [np.std(scallop2_pre), np.std(mscallop2_pre)]
    stringtie2 = [np.mean(stringtie2_pre), np.mean(mstringtie2_pre)]
    stringtie2_SD = [np.std(stringtie2_pre), np.std(mstringtie2_pre)]
    scallop = [np.mean(scallop_pre), np.mean(mscallop_pre)]
    scallop_SD = [np.std(scallop_pre), np.std(mscallop_pre)]
    class2 = [np.mean(class2_pre), np.mean(mclass2_pre)]
    class2_SD = [np.std(class2_pre), np.std(mclass2_pre)]

    total_width, n = 0.2, 4
    width = total_width / n
    x = x - (total_width - width) / 2
    x[1] = x[1] - 0.75
    labels = ['HE', 'MF']
    
    plt.bar(x, scallop2, color='r', edgecolor='black', width=width, yerr = scallop2_SD, error_kw=dict(lw=1,capsize=5,capthick=1),label='Scallop2')
    plt.bar(x + width, stringtie2, color='g',width=width, yerr = stringtie2_SD, error_kw=dict(lw=1, capsize=5, capthick=1),label='StringTie2')
    plt.bar(x + width*2, scallop, color='b', edgecolor='black', width=width, yerr = scallop_SD, error_kw=dict(lw=1, capsize=5, capthick=1), label='Scallop')
    plt.bar(x + width*3, class2, color='y', edgecolor='black', width=width, yerr = class2_SD, error_kw=dict(lw=1, capsize=5, capthick=1), label='CLASS2')
    
    ax.set(ylim=[0, 60])
    plt.yticks(np.arange(0, 61, 20), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width*1.5,labels,fontsize=32)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.ylabel("Precision (%)", fontsize=32)
    figure_name = './HEK293T/figure/Smart-seq3_transcripts_pre_multiExon.pdf'
    
    plt.savefig(figure_name, bbox_inches='tight')
    
    return None

def plot_adjusted(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre):
    mscallop2_match, mscallop2_pre = pm.load_data('scallop2')
    mstringtie2_match, mstringtie2_pre = pm.load_data('stringtie2')
    mscallop_match, mscallop_pre = pm.load_data('scallop')
    mclass2_match, mclass2_pre = pm.load_data('class2')
    
    hi = []
    hni = []
    for i in range(1,193):
        if(int(scallop2_match[i-1]) < int(stringtie2_match[i-1])):
            hi.append(i)
        else:
            hni.append(i)
            
    mi = []
    mni = []
    for i in range(1,370):
        if(int(mscallop2_match[i-1]) < int(mstringtie2_match[i-1])):
            mi.append(i)
        else:
            mni.append(i)

    ad_st = [0]*192
    ad_sc = [0]*192
    
    for i in hi:
        file1 = './HEK293T/stringtie2/' + str(i) + '.stringtie2.me.roc-cor'
        file2 = './HEK293T/stringtie2/' + str(i) + '.stringtie2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = scallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(scallop2_pre[i-1]))
                break
            
    for i in hni:
        file1 = './HEK293T/scallop2/' + str(i) + '.scallop2.me.roc-cor'
        file2 = './HEK293T/scallop2/' + str(i) + '.scallop2.me.roc-pre'
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
    
    hp1_st = round(np.mean(ad_st),1)
    hp1_std = round(np.std(ad_st),1)
    hp1_sc = round(np.mean(ad_sc),1)
    hp1_scd = round(np.std(ad_sc),1)

    ad_st = [0]*369
    ad_sc = [0]*369
    
    for i in mi:
        file1 = './Mouse-Fibroblast/stringtie2/' + str(i) + '.stringtie2.me.roc-cor'
        file2 = './Mouse-Fibroblast/stringtie2/' + str(i) + '.stringtie2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = mscallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(mscallop2_pre[i-1]))
                break
            
    for i in mni:
        file1 = './Mouse-Fibroblast/scallop2/' + str(i) + '.scallop2.me.roc-cor'
        file2 = './Mouse-Fibroblast/scallop2/' + str(i) + '.scallop2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = mstringtie2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(mstringtie2_pre[i-1]))
                ad_sc[i-1]=(float(pre[j]))
                break

    mouse_p1_st2 = ad_st
    mouse_p1_sc2 = ad_sc
    mp1_st = round(np.mean(ad_st),1)
    mp1_std = round(np.std(ad_st),1)
    mp1_sc = round(np.mean(ad_sc),1)
    mp1_scd = round(np.std(ad_sc),1)

    hi = []
    hni = []
    for i in range(1,193):
        if(int(scallop2_match[i-1]) < int(scallop_match[i-1])):
            hi.append(i)
        else:
            hni.append(i)
            
    mi = []
    mni = []
    for i in range(1,370):
        if(int(mscallop2_match[i-1]) < int(mscallop_match[i-1])):
            mi.append(i)
        else:
            mni.append(i)

    ad_st = [0]*192
    ad_sc = [0]*192
    
    for i in hi:
        file1 = './HEK293T/scallop/' + str(i) + '.scallop.me.roc-cor'
        file2 = './HEK293T/scallop/' + str(i) + '.scallop.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = scallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(scallop2_pre[i-1]))
                break
            
    for i in hni:
        file1 = './HEK293T/scallop2/' + str(i) + '.scallop2.me.roc-cor'
        file2 = './HEK293T/scallop2/' + str(i) + '.scallop2.me.roc-pre'
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

    hp2_st = round(np.mean(ad_st),1)
    hp2_std = round(np.std(ad_st),1)
    hp2_sc = round(np.mean(ad_sc),1)
    hp2_scd = round(np.std(ad_sc),1)

    ad_st = [0]*369
    ad_sc = [0]*369
    
    for i in mi:
        file1 = './Mouse-Fibroblast/scallop/' + str(i) + '.scallop.me.roc-cor'
        file2 = './Mouse-Fibroblast/scallop/' + str(i) + '.scallop.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = mscallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(mscallop2_pre[i-1]))
                break
            
    for i in mni:
        file1 = './Mouse-Fibroblast/scallop2/' + str(i) + '.scallop2.me.roc-cor'
        file2 = './Mouse-Fibroblast/scallop2/' + str(i) + '.scallop2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = mscallop_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(mscallop_pre[i-1]))
                ad_sc[i-1]=(float(pre[j]))
                break

    mouse_p2_sc = ad_st
    mouse_p2_sc2 = ad_sc
    mp2_st = round(np.mean(ad_st),1)
    mp2_std = round(np.std(ad_st),1)
    mp2_sc = round(np.mean(ad_sc),1)
    mp2_scd = round(np.std(ad_sc),1)

    hi = []
    hni = []
    for i in range(1,193):
        if(int(scallop2_match[i-1]) < int(class2_match[i-1])):
            hi.append(i)
        else:
            hni.append(i)
            
    mi = []
    mni = []
    for i in range(1,370):
        if(int(mscallop2_match[i-1]) < int(mclass2_match[i-1])):
            mi.append(i)
        else:
            mni.append(i)

    ad_st = [0]*192
    ad_sc = [0]*192
    
    for i in hi:
        file1 = './HEK293T/class2/' + str(i) + '.class2.me.roc-cor'
        file2 = './HEK293T/class2/' + str(i) + '.class2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = scallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(scallop2_pre[i-1]))
                break
            
    for i in hni:
        file1 = './HEK293T/scallop2/' + str(i) + '.scallop2.me.roc-cor'
        file2 = './HEK293T/scallop2/' + str(i) + '.scallop2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = class2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(class2_pre[i-1]))
                ad_sc[i-1]=(float(pre[j]))
                break

    human_p3_cl = ad_st
    human_p3_sc2 = ad_sc
    hp3_st = round(np.mean(ad_st),1)
    hp3_std = round(np.std(ad_st),1)
    hp3_sc = round(np.mean(ad_sc),1)
    hp3_scd = round(np.std(ad_sc),1)

    ad_st = [0]*369
    ad_sc = [0]*369
    
    for i in mi:
        file1 = './Mouse-Fibroblast/class2/' + str(i) + '.class2.me.roc-cor'
        file2 = './Mouse-Fibroblast/class2/' + str(i) + '.class2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_umi = mscallop2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_umi) >= int(cor[j])):
                ad_st[i-1]=(float(pre[j]))
                ad_sc[i-1]=(float(mscallop2_pre[i-1]))
                break
            
    for i in mni:
        file1 = './Mouse-Fibroblast/scallop2/' + str(i) + '.scallop2.me.roc-cor'
        file2 = './Mouse-Fibroblast/scallop2/' + str(i) + '.scallop2.me.roc-pre'
        cor = np.loadtxt(file1)
        pre = np.loadtxt(file2)
        cur_stringtie = mclass2_match[i-1]
        for j in range(0, len(cor)):
            if(int(cur_stringtie) >= int(cor[j])):
                ad_st[i-1]=(float(mclass2_pre[i-1]))
                ad_sc[i-1]=(float(pre[j]))
                break

    mouse_p3_cl = ad_st
    mouse_p3_sc2 = ad_sc
    mp3_st = round(np.mean(ad_st),1)
    mp3_std = round(np.std(ad_st),1)
    mp3_sc = round(np.mean(ad_sc),1)
    mp3_scd = round(np.std(ad_sc),1)

    human_p1 = np.array((human_p1_sc2, human_p1_st2)).T
    human_p2 = np.array((human_p2_sc2, human_p2_sc)).T
    human_p3 = np.array((human_p3_sc2, human_p3_cl)).T
    mouse_p1 = np.array((mouse_p1_sc2, mouse_p1_st2)).T
    mouse_p2 = np.array((mouse_p2_sc2, mouse_p2_sc)).T
    mouse_p3 = np.array((mouse_p3_sc2, mouse_p3_cl)).T
    
    human_p1 = human_p1[np.argsort(human_p1[:,0])]
    human_p2 = human_p2[np.argsort(human_p2[:,0])]
    human_p3 = human_p3[np.argsort(human_p3[:,0])]
    mouse_p1 = mouse_p1[np.argsort(mouse_p1[:,0])]
    mouse_p2 = mouse_p2[np.argsort(mouse_p2[:,0])]
    mouse_p3 = mouse_p3[np.argsort(mouse_p3[:,0])]

    flist = ['human_p1', 'human_p2', 'human_p3', 'mouse_p1', 'mouse_p2', 'mouse_p3']
    
    for i in range(6):
        if(i < 3):
            x = np.arange(1,193,1)
        else:
            x = np.arange(1,370,1)
            
        y1 = eval(flist[i])[:,0]
        y2 = eval(flist[i])[:,1]
        
        if(i == 0 or i == 3):
            label2 = "StringTie2"
            color2 = 'g'
        elif(i == 1 or i == 4):
            label2 = "Scallop"
            color2 = 'b'
        else:
            label2 = "CLASS2"
            color2 = 'y'
            
        fig, ax = plt.subplots(1, 1, figsize=(9,9), dpi= 600)
        ax.fill_between(x, y1=y1, y2=0, label="Scallop2", alpha=1, color='r', linewidth=2)
        ax.fill_between(x, y1=y2, y2=0, label=label2, alpha=1, color=color2, linewidth=2)
        
        if(i == 0):
            ax.set(ylim=[0, 85],xlim=[1,193])
        elif(i == 1):
            ax.set(ylim=[0, 100],xlim=[1,193])
        elif(i == 2):
            ax.set(ylim=[0, 100],xlim=[1,193])
        elif(i == 3):
            ax.set(ylim=[0, 65],xlim=[1,370])
        elif(i == 4):
            ax.set(ylim=[0, 85],xlim=[1,370])
        else:
            ax.set(ylim=[0, 100],xlim=[1,370])
            
        if(i<3):
            plt.xticks(np.arange(1, 193.0, 40), fontsize=30, horizontalalignment='center')
        else:
            plt.xticks(np.arange(1, 370.0, 80), fontsize=30, horizontalalignment='center')
            
        if(i == 0):
            plt.yticks(np.arange(0, 85, 20), fontsize=30)
        elif(i == 1):
            plt.yticks(np.arange(0, 101, 20), fontsize=30)
        elif(i == 2):
            plt.yticks(np.arange(0, 101, 20), fontsize=30)
        elif(i == 3):
            plt.yticks(np.arange(0, 65, 20), fontsize=30)
        elif(i == 4):
            plt.yticks(np.arange(0, 86, 20), fontsize=30)
        else:
            plt.yticks(np.arange(0, 101, 20), fontsize=30)
            
        ax.legend(loc='upper left', fontsize=25)
        
        plt.gca().spines["top"].set_alpha(0)
        plt.gca().spines["bottom"].set_alpha(1)
        plt.gca().spines["right"].set_alpha(0)
        plt.gca().spines["left"].set_alpha(1)
        
        if(i<3):
            plt.xlabel("HE cells", fontsize=30)
        else:
            plt.xlabel("MF cells", fontsize=30)
            
        plt.ylabel("Adjusted precision (%)", fontsize=30)
        if(i<3):
            filename = "./HEK293T/figure/adjusted_cell_pre" + flist[i] + "_multiExon.pdf"
        else:
            filename = "./Mouse-Fibroblast/figure/adjusted_cell_pre" + flist[i] + "_multiExon.pdf"
        plt.savefig(filename, bbox_inches = 'tight')
        
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
    
    ax.set(ylim=[0, 85])
    plt.yticks(np.arange(0, 85, 20), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width/2,labels,fontsize=25)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.ylabel("Adjusted precisoin (%)", fontsize=32)
    
    figure_name = './HEK293T/figure/adjusted_pre_multiExon.pdf'
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
    
    ax.set(ylim=[0, 70])
    plt.yticks(np.arange(0, 70, 20), fontsize=32)
    plt.yticks(rotation = 90)
    plt.xticks(x+width/2,labels,fontsize=25)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(0)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.ylabel("Adjusted precisoin (%)", fontsize=32)
    
    figure_name = './Mouse-Fibroblast/figure/adjusted_pre_multiExon.pdf'
    plt.savefig(figure_name, bbox_inches='tight')

    return None


def plot_scatter(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre):
    
    fig, ax = plt.subplots(1, 1, figsize=(12,9), dpi= 600)
    plt.scatter(scallop2_pre, scallop2_match, label='Scallop2', color='r', s=30)
    plt.scatter(stringtie2_pre, stringtie2_match, label='StringTie2', color='g', s=30)
    plt.scatter(scallop_pre, scallop_match, label='Scallop', color='b', s=30)
    plt.scatter(class2_pre, class2_match, label='CLASS2', color='y', s=30)
    
    ax.set(ylim=[0, 4801],xlim=[15,82])
    ax.legend(loc='upper right', fontsize=23)
    plt.xticks(np.arange(15, 86, 20), fontsize=30, horizontalalignment='center')
    plt.yticks(np.arange(0, 4801, 1600), fontsize=30)
    plt.gca().spines["top"].set_alpha(0)
    plt.gca().spines["bottom"].set_alpha(1)
    plt.gca().spines["right"].set_alpha(0)
    plt.gca().spines["left"].set_alpha(1)
    
    plt.xlabel("Precision (%)", fontsize=30)
    plt.ylabel("# Matching transcripts", fontsize=30)
    
    plt.savefig('./HEK293T/figure/scatter_multiExon.pdf', bbox_inches = 'tight')
    return None

def main():

    scallop2_match, scallop2_pre = load_data('scallop2')
    stringtie2_match, stringtie2_pre = load_data('stringtie2')
    scallop_match, scallop_pre = load_data('scallop')
    class2_match, class2_pre = load_data('class2')

    sort_match = sort(scallop2_match, stringtie2_match, scallop_match, class2_match)
    sort_pre = sort(scallop2_pre, stringtie2_pre, scallop_pre, class2_pre)

    plot_cells(sort_match, sort_pre)
    plot_bar(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre)
    plot_scatter(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre)
    plot_adjusted(scallop2_match, stringtie2_match, scallop_match, class2_match, scallop2_pre, stringtie2_pre, scallop_pre, class2_pre)

if __name__ == '__main__':
    main()
