# test program to calculate loading

import xlrd
import loading

designPath = 'R:\4312 Ford House, Prestbury - Design\loading.xlsx'
book = xlrd.open_workbook('R:\4312 Ford House, Prestbury - Design\loading.xlsx')
data=book.sheet_by_index(0)

# read the basic load refs
elements = []
for i in range(1,data.ncols):
    elements.append(data.cell_value(0,i))

# read the dead loads - the first value is the reference
dead_loads = []
for i in range(0,data.ncols):
    dead_loads.append(data.cell_value(1,i))

# read the imposed loads
imposed_loads = []
for i in range(0,data.ncols):
    imposed_loads.append(data.cell_value(2,i))

basic_dead=loading.BasicLoading(dead_loads,elements)
basic_imposed=loading.BasicLoading(imposed_loads,elements)

outPut = basic_dead.results()+'\n'
outPut=outPut+basic_imposed.results()+'\n'


# get references and load lengths

geom = [[]]

for i in range(3,data.nrows):
    geom.append([])

for i in range(3,data.nrows):
    for k in range(0,data.ncols):
        geom[i-3].append(data.cell_value(i,k))


for k in range(3,data.nrows):
    d = loading.Udl(basic_dead,geom[k-3])
    i = loading.Udl(basic_imposed,geom[k-3])
    s=d.load+i.load
    u = 1.35*d.load+1.5*i.load
    outPut=outPut+"{} :\n".format(d.ref)
    for j in range(1, len(basic_dead.loads)):
        a = geom[k-3][j]
        b = basic_dead.loads[j]
        c = basic_imposed.loads[j]
        outPut=outPut+'{} {}: {} x {} = {:.2f} \t\t{} {}: {} x {}= {:.2f}\n'.format(elements[j-1],d.nature,a,b,a*b, elements[j-1],i.nature,a,c, a*c)

    outPut=outPut+'dead = {:.2f} kN/m\timposed = {:.2f} kN/m\tSLS = {:.2f} kN/m\tULS = {:.2f}kN/m\n\n'.format(d.load,i.load,s,u)

f = open('R:\4312 Ford House, Prestbury - Design\load.txt','w')
f.write(outPut)
f.close()






