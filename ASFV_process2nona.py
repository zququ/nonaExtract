#Extract the special words
f = open('sequence.fasta', 'r')   #input file
f_countAA = open('deSample_output.txt', 'a')

for each_line in f:
    print(each_line)
    if each_line[0]=='>':
        f_countAA.write('@')
    else:
        f_countAA.write(each_line)
f.close()
f_countAA.close()

f2 = open('deSample_output.txt')
flist = []
n = 0
for each_str in f2.read():
    n += 1

    if each_str == '\n':
        flist.append('')
    else:
        flist.append(each_str)

f3 = open('deSample_output_deenter.txt', 'w+')
ls = ''.join(flist)
f3.write(ls)

f2.close()
f3.close()


f4 = open('deSample_output_deenter.txt', 'r')
f5 = open('process2nona_output.txt', 'w+')
lst = []
n = 0

for each in f4:
    lst.extend(each)
    #print(lst)

for i in range(len(lst)-9):
    #print(lst[i:i+9])   FOR TEST
    ls_out = ''.join(lst[i:i+9])
    print(ls_out)
    output = str(ls_out)
    f5.write(output + '\n')


#print(lst_nona)

#def score_1():
f4.close()
f5.close()


f6 = open('deSample_output_deenter.txt', 'r')
f7 = open('count_result.txt', 'w+')
list1 = []
n = 0

for each_str in f6.read():
    n += 1
    if each_str == '@':
        print(n-9)  #n-1
        n_str = str(n)
        f7.write(n_str + '\n')
        n = 0
    else:
        continue

f6.close()
f7.close()

