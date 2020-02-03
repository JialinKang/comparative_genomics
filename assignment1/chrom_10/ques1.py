import sys

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
    base_a = 0
    base_t = 0
    base_c = 0
    base_g = 0
    for bp in seq.values():
        bp_list = list(bp)
        for bp_sort in bp_list:
            if bp_sort == 'A':
                base_a += 1
            elif bp_sort == 'T':
                base_t += 1
            elif bp_sort == 'C':
                base_c += 1
            else:
                base_g += 1

    print('A:',base_a,'T:',base_t,'C:',base_c,'G:',base_g) 
    return base_a, base_t, base_c, base_g

if __name__ == "__main__":
    fafile2dict()