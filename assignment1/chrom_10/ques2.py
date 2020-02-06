import sys
import matplotlib.pyplot as plt

def fafile2dict():
    '''
    Make a scatterplot of the %GC of 100bp non-overlapping windows
    across the genome: x-axis = genome location, y-axis = (#G + #C) / 100.
    
    STDIN:
    ----------------------------------------
    the fasta file
    run as 'python3 ques2.py yeast.fa'
    ----------------------------------------
    '''
    line = sys.stdin.readline().replace('\n','')
    seq = {}
    num = []
    bp_list = []
    n = 0
    chrom_name = []
    while line != '':
        if line[0] == '>':
            name = line.replace('\n','')
            seq[name] = ''
        else:
            seq[name] += line.replace('\n','').strip()
        line = sys.stdin.readline()
        
    for chrom, bp in seq.items():
        bp_list += bp
        n = n + len(bp)/100 
        num.append(n)
        chrom_name.append(chrom.replace('>',''))

    count_list = []
    bp_list = list(bp_list)
    for i in range(int(len(bp_list)/100)):
        bp_frag = bp_list[100*i:(100*i+100)]
        base_gc = 0
        for bp_sort in bp_frag:
            if bp_sort == 'G' or bp_sort == 'C':
                base_gc += 1
        count_list.append(base_gc)

    # draw the figure    
    plt.xlabel('genome location')
    plt.ylabel('(#G + #C) / 100')
    plt.title('question 2.2')
    plt.vlines(num, 0, 80, 'g', 'dashed', linewidths=0.5)
    plt.hlines([30,65], 0, len(count_list),'r', 'dashed', linewidths=2)
    plt.scatter(range(len(count_list)), count_list, s=1, alpha=0.5)
    plt.xticks(num, chrom_name, rotation=90)
    plt.show()


if __name__ == "__main__":
    fafile2dict()