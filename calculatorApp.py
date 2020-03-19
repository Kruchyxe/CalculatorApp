from tkinter import *

root = Tk()
root.title('Calculator')
root.geometry('400x550+850+200')
root.resizable(False, False)


##########enterNumber##########################
def enterNumber(x):
	if entry_box.get() == 'O':
		entry_box.delete(0, 'end')
		entry_box.insert(0, str(x))
	else:
		length = len(entry_box.get())
		entry_box.insert(length, str(x))


def enterOperator(x):
	if entry_box.get() != "O":
		length = len(entry_box.get())
		entry_box.insert(length, klawisz_operatora[x]['text'])


def funcClear():
	entry_box.delete(0, END)
	entry_box.insert(0, 'O')


result = 0
result_list = []


def funcOperator():
	content = entry_box.get()
	print(content)
	result = eval(content)
	print(result)
	entry_box.delete(0, END)
	entry_box.insert(0, str(result))

	result_list.append((content))
	result_list.reverse()
	statusBar.configure(text='History: ' + '|'.join(result_list[:5]), font="calibri 11 bold")


def funcDelete():
	length = len(entry_box.get())
	entry_box.delete(length - 1, 'end')
	if length == 1:
		entry_box.insert(0, 'O')


##########EntryBox#############################
entry_box = Entry(font='calibri 12 bold', width=31, bd=5, justify=RIGHT, bg='#F3ECDB')
entry_box.insert(0, 'O')
entry_box.place(x=20, y=10)

###########Klawiatura#########################
klawiatura_liczby = []
for i in range(10):
	klawiatura_liczby.append(Button(width=4, text=str(i), font='calibri 12 bold', bd=3, bg='#F5F5DC',
	                                command=lambda x=i: enterNumber(x)))

klawiatura_text = 1
for i in range(0, 3):
	for j in range(0, 3):
		klawiatura_liczby[klawiatura_text].place(x=25 + j * 90, y=70 + i * 70)
		klawiatura_text += 1
############klawiszeOperatorów###########################
klawisz_operatora = []
for i in range(4):
	klawisz_operatora.append(Button(width=4, font='calibri 12 bold', bd=3, bg='#F5F5DC',
	                                command=lambda x=i: enterOperator(x)))
klawisz_operatora[0]['text'] = '+'
klawisz_operatora[1]['text'] = '-'
klawisz_operatora[2]['text'] = '*'
klawisz_operatora[3]['text'] = '/'

for i in range(4):
	klawisz_operatora[i].place(x=290, y=70 + i * 70)
###########pozostałeKlawisze#############################
klawisz_zero = Button(width=19, text='0', font='calibri 12 bold', bd=3, bg='#F5F5DC',
                      command=lambda x=0: enterNumber(x))
klawisz_wyczysc = Button(width=4, text='C', font='calibri 12 bold', bd=3, bg='#F5F5DC',
                         command=funcClear)
klawisz_wyczysc.place(x=25, y=340)
klawisz_zero.place(x=25, y=280)
klawisz_dot = Button(width=4, text='.', font='calibri 12 bold', bd=3, bg='#F5F5DC',
                     command=lambda x=".": enterNumber(x))
klawisz_dot.place(x=110, y=340)
klawisz_equal = Button(width=4, text='=', font='calibri 12 bold', bd=3, bg='#F5F5DC',
                       command=funcOperator)
klawisz_equal.place(x=200, y=340)
icon = PhotoImage(file='Obrazy/return.png')
klawisz_usun = Button(width=50, height=35, font='calibri 12 bold', bd=3, bg='#F5F5DC',
                      command=funcDelete, image=icon)
klawisz_usun.place(x=305, y=340)

statusBar = Label(root, text='History: ', relief=SUNKEN, height=3, anchor=W, font='calibri 11 bold')
statusBar.pack(side=BOTTOM, fill=X)

root.mainloop()
