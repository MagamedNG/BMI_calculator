from tkinter import *
root = Tk()

def bmi(event):
	weight = int(input_1.get())
	height = int(input_2.get())
	result = float('{0:.2f}'.format(weight / ((height / 100) * (height / 100))))
	label_3['text'] = 'Твой BMI {0}'.format(result)

	if( result <=16):
		label_4['fg'] = '#eb4d4b'
		label_4['text'] =' Высокий дефицит массы тела'
	elif( result >=16 and result <= 18.5):
		label_4['fg'] = '#f39c12'
		label_4['text']=' Недостаточная масса тела'
	elif( result >=18.5 and result <= 25):
		label_4['fg'] = '#2ecc71'
		label_4['text']=' Ваш вес в порядке'
	elif( result >=25 and result <=30):
		label_4['fg'] = '#f39c12'
		label_4['text']=' Избыточная масса тела'
	elif( result >=30 and result <=35):
		label_4['fg'] = '#eb4d4b'
		label_4['text']=' Ожирение 1 степени'
	elif( result >=35 and result <=40):
		label_4['fg'] = '#eb4d4b'
		label_4['text']=' Ожирение 2 степени'
	elif( result > 40):
		label_4['fg'] = '#eb4d4b'
		label_4['text']=' Ожирение 3 степениe'

root.geometry('250x130')
root.title('BMI v2.0')
root.configure(bg='#999')

root.resizable(height=False,width=False)
label_1 = Label(root,text='Введи свой вес(Weight)',fg='#fff',font=10,width=20,bg='#bbb')
label_2 = Label(root,text='Введи свой рост(Height)',fg='#fff',font=10,width=20,bg='#bbb')
label_3 = Label(root,text='',bg='#999',font=13,fg='#fff')
label_4 = Label(root,text='',bg='#999',font=13)

input_1 = Entry(root,bg='#777',fg='#fff',font=5,width=100)
input_2 = Entry(root,bg='#777',fg='#fff',font=5,width=100)

button = Button(root,fg='#fff',bg='#777',text='Расчитать',width=10,font=15)

label_1.grid(row=0,column=0,sticky=W)
label_2.grid(row=1,column=0,sticky=W)
input_1.grid(row=0,column=1)
input_2.grid(row=1,column=1)
button.grid(row=2,column=0)
label_3.grid(row=3,column=0)
label_4.grid(row=4,column=0)

button.bind('<Button-1>',bmi)
root.mainloop()
