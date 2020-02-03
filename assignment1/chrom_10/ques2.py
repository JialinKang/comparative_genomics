import sys
import matplotlib.pyplot as plt

def fafile2dict():
    '''
    this function can be used to calculate the As, Cs, Gs, Ts in entire genome
    
    STDIN:
    ----------------------------------------
    the fasta file
    run as 'python3 ques1.py yeast.fa'
    ----------------------------------------

    Return:
    ----------------------------------------
    base_a:int
    the number of As
    base_c:int
    the number of Cs
    base_g:int
    the number of Gs
    base_t:int
    the number of Ts
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
    for bp in seq.values():
        bp_list = list(bp)
        count_list = []
        for i in range(int(len(bp_list)/100)):
            bp_frag = bp_list[(100*i-100):100*i]
            base_gc = 0
            for bp_sort in bp_frag:
                if bp_sort == 'G' or bp_sort == 'C':
                    base_gc += 1
            count_list.append(base_gc)

    plt.scatter(range(len(count_list)), count_list, s=1, alpha=0.5)
    plt.xlabel('genome location')
    plt.ylabel('(#G + #C) / 100')
    plt.title('question 2.2')
    plt.show()



    # print('A:',base_a,'T:',base_t,'C:',base_c,'G:',base_g) 
    # return base_a, base_t, base_c, base_g

if __name__ == "__main__":
    fafile2dict()