import os
import pandas as pd


file_list = ['./ce10.chrom.sizes',
             './dm6.chrom.sizes',
             './ecoli.chrom.sizes',
             './hg38.chrom.sizes',
             './TAIR10.chrom.sizes',
             './tomato.chrom.sizes',
             './wheat.chrom.sizes',
             './yeast.chrom.sizes']

sheet_list = ['ce10','dm6','ecoli','hg38','TAIR10','tomato','wheat','yeast']

os.system("echo species_name Total_genome_size Number_of_chromosomes Largest_chromosome_size Smallest_chromosome_size Mean_chromosome_length > collect.txt")



for i in range(8):
    os.system('echo -n {}\ >> collect.txt && datamash mean 2 max 2 min 2 count 2 sum 2 < {} >> collect.txt'.format(sheet_list[i],file_list[i]))

# sort -k 2 -r -n ./ce10.chrom.sizes | head -n 1 ./ce10.chrom.sizes > head.txt | tail -n 1 ./ce10.chrom.sizes > tail.txt && cut -f1 -n head.txt >> collect.
# txt  && cut -f1 -n tail.txt >> collect.txt

