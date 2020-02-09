import sys

def fafile2dict():
    '''
    read a single FASTA file (SHH.fa) into a dictionary object
    and calculate the contig N50 size of this FASTA file
    run as :
    python3 N50.py < ./asm/contigs.fasta

    Rerurn
    --------------
    N50:int
    the N50 number of this FASTA file
    --------------
    '''
    # read the file context into a dict
    line = sys.stdin.readline().replace('\n','')
    seq = {}
    while line != '':
        if line[0] == '>':
            name = line.replace('>','')
            seq[name] = ''
        else:
            seq[name] += line.replace('\n','').strip()
        line = sys.stdin.readline()

    val_list = []
    for val in seq.values():
        val_list.append(len(val))
    val_list.sort(reverse=True)

    val_half = sum(val_list)/2
    for i in range(len(val_list)):
        if val_half > 0:
            val_half -= val_list[i]
        else:
            N_50 = val_list[i-1]
            break

    return N_50

if __name__ == "__main__":
    N_50 = fafile2dict()
    print('N50 is ', N_50)