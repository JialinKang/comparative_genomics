import numpy as np
import pandas as pd

file_list = ['./ce10.chrom.sizes',
             './dm6.chrom.sizes',
             './ecoli.chrom.sizes',
             './hg38.chrom.sizes',
             './TAIR10.chrom.sizes',
             './tomato.chrom.sizes',
             './wheat.chrom.sizes',
             './yeast.chrom.sizes']

col_list = ['Total','Number', 'max_size', 'max_name', 'min_size', 'min_name', 'mean']
row_list = ['ce10','dm6','ecoli','hg38','TAIR10','tomato','wheat','yeast']

def information(file_list, col_list, row_list):
    '''
    this function is used to produce a excel table of the chromosome information

    Parameters
    ----------------------
    file_list:list
    the files path
    col_list:list
    the table column name list of the excel table
    row_list:list
    the table row name list of the excel table
    ----------------------
    '''

    # open a df data frame
    df = pd.DataFrame(columns=row_list, index = col_list)

    value_total = []
    value_num = []
    max_value = []
    max_value_name = []
    min_value = []
    min_value_name = []
    mean = []
    i=0
    for name in file_list:
        context = {}
        chrom = open(name, 'r')
        line = chrom.readline().replace('\n', '')
        while line != '':
            line_list = line.split()
            context[line_list[0]] = int(line_list[1])
            line = chrom.readline().replace('\n', '')
        value_list = []
        for value in context.values():
            value_list.append(value)

        # calculate the information of the chromosome of a species and put it into a list    
        value_total = np.sum(value_list)
        value_num = len(value_list)
        max_value = np.max(value_list)
        max_value_name = max(context, key=context.get)
        min_value = np.min(value_list)
        min_value_name = min(context, key=context.get)
        mean = np.mean(value_list)
        arr_value = [value_total, value_num, max_value, max_value_name,
            min_value, min_value_name, mean]

        # write the list into dataframes
        df[row_list[i]] = arr_value
        i += 1
        

    df.to_excel('excel.xls')

if __name__ == "__main__":
    information(file_list, col_list, row_list)