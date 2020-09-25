# -*- coding: utf-8 -*-
"""

"""

def RX(theta, q, qc):
    return qc + '.rx(' + theta + ',' + q + ')\n'
def RZ(theta, q, qc):
    return qc + '.rz(' + theta + ',' + q + ')\n'
def CZ(q1, q2, qc):
    return qc + '.cz(' + q1 + ',' + q2 + ')\n'


def I(q, qc):
    return RZ('0', q, qc)
def H(q, qc):
    return RZ('pi/2', q, qc) + RX('pi/2', q, qc) + RZ('pi/2', q, qc)
def X(q, qc):
    return RX( 'pi', q, qc) + RZ('pi', q, qc)
def Y(q, qc):
    return RX('pi', q, qc) + RZ('-pi', q ,qc)
def Z(q, qc):
    return RZ('-pi', q, qc)
def RY(q2, q1, qc):
    return RZ('pi/2', q1, qc) + RX(q2, q1, qc) + RZ('-pi/2', q1, qc)
def CNOT(q1, q2, qc):
    return H(q2, qc) + CZ(q1, q2, qc) + H(q2, qc)


def Rewrite_op(row, op, q1, q2, qc):
    operation = ''
    if (len(op) == 1):
        if op == 'h':
            operation= H(q1, qc)
        else:
            if op == 'x':
                operation = X(q1, qc)
            else: 
                if op == 'y':
                    operation = Y(q1, qc)
                else:  
                    if op == 'z':
                        operation = Z(q1, qc)
    else:
        if op == 'id':
            operation = I(q1, qc)
        else:
            if op == 'cx':
                operation = CNOT(q1, q2, qc)
            else:
                if op == 'ry': 
                    operation = RY(q2, q1, qc)
                # else:
                #     # if op == 'rx' or op == 'rz' or op == 'cz':
                #     operation = row
    return operation


def Convert(row):
    q1, q2, body, qc = '', '', '', ''
    start, i, j = 0,0,0
    num_par = 1
    if ('.id(' in row):
        qc_end= row.find('.id(')
        start = row.find('.id(') + 4
        op = 'id'
    else: 
        if ('.x(' in row):
            qc_end = row.find('.x(')
            start = row.find('.x(') + 3
            op = 'x'
        else: 
            if ('.y(' in row):
                qc_end= row.find('.y(')
                start = row.find('.y(') +3
                op = 'y'
            else: 
                if ('.z(' in row):
                    qc_end =row.find('.z(')
                    start = row.find('.z(') + 3 
                    op = 'z'
                else: 
                    if ('.ry(' in row):
                        qc_end = row.find('.ry(')
                        start = row.find('.ry(') + 4
                        op = 'ry'
                    else: 
                        if ('.cx(' in row):
                            qc_end = row.find('.cx(')
                            start = row.find('.cx(') + 4
                            op = 'cx'
                            
    if start == 0:
        return row
    qc_start = 0
    for i in range(len(row[:qc_end])):
        if not row[-i].lower() in 'abcdefghijklmnopqrstuvwxyz_-':
            qc_start = qc_end-i-1
            break        
    # print(row[:qc_end ], '   ', qc_start, ' e la fine ', qc_end, '  cioè ', row[qc_end-qc_start-1 : qc_end] )
    qc = row[qc_start : qc_end]
        
    for c in range(start, len(row)):
        if row[c] == '(':
            num_par = num_par + 1
        if row[c] == ')':
            num_par = num_par - 1
        if num_par == 0:
            end = c
            break
        body = body + row[c]
    # print(body)
    
    for j in range(0, len(body)):
        if body[j] == ',':
            break
        q1 = q1 + body[j]
    
    for i in range(j +1 , len(body)):
        q2= q2 + body[i]
        
    # print('\nNew row', row, body, ': ', qc , 'made of: op:',  op, ' q1: ', q1, '  q2: ', q2 , 'len: ', len(body))
    if qc_start == 0:
        intro = row[0 : qc_start]
    else: 
        intro = row[0 : qc_start] + ' '
    return intro + Rewrite_op(body, op, q1, q2, qc) + row[end + 1:]
    
    

file = './ciao.txt'
fh = open(file, 'r', encoding="utf-8") 
i = file[2:].find('.')
filename = file[2:i+2]
f = open('./' + filename + '_conv.' + file[i+3:], 'w', encoding="utf-8")


for line in fh:
    row = line.replace(" ", "")
    f.write(Convert(row))
f.close()




