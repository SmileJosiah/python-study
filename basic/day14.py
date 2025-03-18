import csv
import random

with open('../data.csv', 'w', encoding ='utf-8') as f:
    csvwriter = csv.writer(f,delimiter='|',quoting=csv.QUOTE_ALL)
    csvwriter.writerow(['姓名','语文','数学','英语'])
    names = ['关羽','张飞','赵云','马超','黄忠']
    for name in names:
        scores =  [random.randrange(50,101) for _ in range(3)]
        scores.insert(0,name)
        csvwriter.writerow(scores)



with open('../data.csv', 'r', encoding ='utf-8') as f:
    reader = csv.reader(f,delimiter='|',quoting=csv.QUOTE_ALL)
    for row in reader:
        print(reader.line_num,end='\t')
        for elem in row:
            print(elem,end='\t')
        print()