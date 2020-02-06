import sys
import matplotlib.pyplot as plt
import numpy as np

def fafile2dict():
    '''
    Make a histogram of the number of genomic bins of a given %GC
    
    STDIN:
    ----------------------------------------
    the fasta file
    run as 'python3 ques3.py < yeast.fa'
    ----------------------------------------
    '''
    line = sys.stdin.readline().replace('\n','')
    seq = {}
    while line != '':
        if line[0] == '>':
            name = line.replace('\n','')
            seq[name] = ''
        else:
            seq[name] += line.replace('\n','').strip()
        line = sys.stdin.readline()
    count_list = []
    for bp in seq.values():
        bp_list = list(bp)
        for i in range(int(len(bp_list)/100)):
            bp_frag = bp_list[(100*i-100):100*i]
            base_gc = 0
            for bp_sort in bp_frag:
                if bp_sort == 'G' or bp_sort == 'C':
                    base_gc += 1
            count_list.append(base_gc)
    
    count_set = set(count_list)

    percentage = []
    num_gc = []

    for item in count_set:
        percentage.append(item)
        num_gc.append(count_list.count(item))
    num_gc = list(map(int, num_gc))
    percentage = list(map(int, percentage))
    plt.bar(percentage, num_gc)
    plt.xlabel("%GC")
    plt.ylabel("# genomic bins with this %GC")
    plt.title('question 2.3')
    plt.show()


if __name__ == "__main__":
    fafile2dict()