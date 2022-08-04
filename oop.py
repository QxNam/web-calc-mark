import csv
from js import document
import matplotlib.pyplot as plt
import numpy as np

def diem10():
    tk = [float(i) for i in [Element('tk1').value, Element('tk2').value, Element('tk3').value, Element('tk4').value] if i != '']
    th = [float(i) for i in [Element('th1').value, Element('th2').value, Element('th3').value] if i != '']
    s = ((sum(tk)/len(tk)*2) + float(Element('gk').value)*3 + float(Element('ck').value)*5)/10
    if len(th)==0:
        return s
    return (s*(int(Element('tc').value) - 1) + (sum(th)/len(th))) / int(Element('tc').value)

def xepHang():
    xh = list({4: 'A+: Xuất sắc', 3.8: 'A: Giỏi', 3.5: 'B+: Khá', 3: 'B: Khá', 2.5: 'C+: Trung bình', 2: 'C: Trung bình', 1.5: 'D+: Trung bình yếu', 1: 'D: Trung bình yếu', 0: 'F: Kém'}.items())
    d10 = diem10()
    lstd10 = [9, 8.5, 8, 7, 6, 5.5, 5, 4, 0]
    for i in range(len(lstd10)):
        if d10>=lstd10[i]:
            return (xh[i][0], xh[i][1])

def res(*args, **kwargs):
    rank, loai = xepHang()[1].split(':')[0], xepHang()[1].split(':')[1]
    pyscript.write('out1', 'Điểm hệ 10: {}'.format(round(diem10(), 1)))
    pyscript.write('out2', 'Điểm hệ 4: {}'.format(xepHang()[0]))
    pyscript.write('out3', 'Điểm chữ: {}'.format(rank))
    pyscript.write('out4', 'Xếp loại: {}'.format(loai))
stt = [0]
sub = []
mark = []
def danhsach(*args, **kwargs):
    stt.append(stt[-1]+1)
    sub.append(Element('subject').value)
    mark.append(round(diem10(),1))

    node = document.getElementById('msgs')
    r = document.createElement('tr')
    for i in [stt[-1], sub[-1], mark[-1]]:
        d = document.createElement('td')
        d.textContent = str(i)
        r.appendChild(d)
    node.appendChild(r)
    
    tb = round(sum(mark)/len(mark), 2)
    pyscript.write('outtb', '{}'.format(tb))
    nx = 'có'
    if tb < 8:
        nx = 'không'
    pyscript.write('complain', 'Bạn {} thể nhận học bổng'.format(nx))


fig = plt.figure(figsize = (10, 6))
plt.bar(['a', 'b', 'c'], [6, 10, 8], color ='maroon')
plt.text(0, 10, "chức năng chưa được phát triển do tác giả quá gà :>>", style = 'italic', fontsize = 15, color = "y")
plt.xlabel("Môn học")
plt.ylabel("Điểm")
plt.title("Biểu đồ học tập của bạn")
plt