import os
import sys
import time
file_path = os.path.dirname(__file__)
sys.path.append(file_path)
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import webbrowser
import Functions as fs
import Weblogo as iweb
import Reduce as ired

def gui_open():
	# choose file
	Filepath = filedialog.askopenfilename()
	if Filepath != '':
		with open(Filepath, 'r', encoding='UTF-8') as f:
			content = f.read()
		root =  tk.Toplevel(window)
		root.title(Filepath)
		root.geometry('700x300')
		root.iconbitmap(os.path.join(os.path.join(file_path, 'bin'), 'Logo.ico'))
		#display box
		sb = tk.Scrollbar(root)
		sb.pack(side="right", fill="y")
		mhp = tk.Text(root)
		mhp.pack(fill="both")
		sb.config(command=mhp.yview)
		mhp.insert('end', content)
		mhp.configure(state='disabled')

def gui_webup1_file():
	Filepath = filedialog.askopenfilename()
	e_weblogo1_i.delete(0,'end')
	e_weblogo1_i.insert(0, Filepath)
	e_weblogo1_o.delete(0,'end')
	e_weblogo1_o.insert(0, os.path.join(os.path.join(file_path, 'data'), os.path.split(Filepath)[-1].split('.')[0] + '.svg'))


def gui_webup2_file():
	Filepath = filedialog.askdirectory()
	e_weblogo2_i.delete(0,'end')
	e_weblogo2_i.insert(0, Filepath)
	e_weblogo2_o.delete(0,'end')
	e_weblogo2_o.insert(0, os.path.join(os.path.join(file_path, 'data'), os.path.split(Filepath)[-1].split('.')[0] + '.svg'))

def gui_redup_file():
	Filepath = filedialog.askopenfilename()
	e_reduce1_i.delete(0,'end')
	e_reduce1_i.insert(0, Filepath)
	e_reduce1_o.delete(0,'end')
	e_reduce1_o.insert(0, os.path.join(os.path.join(file_path, 'data'), os.path.split(Filepath)[-1].split('.')[0]))

def gui_about():
	#new window
	root =  tk.Toplevel(window)
	root.title('About EasyBioPlot')
	root.geometry('470x83')
	root.iconbitmap(os.path.join(os.path.join(file_path, 'bin'), 'Logo.ico'))
	#display box
	mha = tk.Text(root)
	mha.pack(fill="both")
	mha.insert('end', fs.about())
	mha.configure(state='disabled')

def gui_documentation():
	webbrowser.open_new(fs.documentation())

def gui_log():
	with open(os.path.join(os.path.join(file_path, 'bin'), 'Logs.txt'), 'r', encoding='UTF-8') as f:
		content = f.read()
	root =  tk.Toplevel(window)
	root.title('RunningLog')
	root.geometry('700x300')
	root.iconbitmap(os.path.join(os.path.join(file_path, 'bin'), 'Logo.ico'))
	#display box
	sb = tk.Scrollbar(root)
	sb.pack(side="right", fill="y")
	mhp = tk.Text(root)
	mhp.pack(fill="both")
	sb.config(command=mhp.yview)
	mhp.insert('end', content)
	mhp.configure(state='disabled')

def gui_weblogo_single():
	var.set(fs.description_weblogo_signle())
	weblogo_i = e_weblogo1_i.get()
	weblogo_o = e_weblogo1_o.get()
	weblogo_t = e_weblogo1_t.get()
	if len(weblogo_i) != 0 and len(weblogo_o) != 0 and len(weblogo_t) != 0:
		v_command = fs.commands('weblogo', {'-d':weblogo_i, '-o':weblogo_o, '-tp':weblogo_t})
		var.set(v_command)
		cmd.insert('end', '\n>>>Drawing Weblogo...')
		iweb.weblogo(file=weblogo_i, out=weblogo_o, tp=weblogo_t)
		cmd.insert('end', '\n>>>Weblogo created successfully!')
		fs.save(v_command, file_path)
		os.startfile(os.path.join(file_path, 'data'))

def gui_weblogo_mulity():
	var.set(fs.description_weblogo_mulity())
	weblogo_i = e_weblogo2_i.get()
	weblogo_o = e_weblogo2_o.get()
	weblogo_t = e_weblogo2_t.get()
	weblogo_l = e_weblogo2_l.get()
	if len(weblogo_i) != 0 and len(weblogo_o) != 0 and len(weblogo_t) != 0:
		if len(weblogo_l) != 0:
			v_command = fs.commands('weblogo', {'-f':weblogo_i, '-o':weblogo_o, '-tp':weblogo_t, '-label':weblogo_l})
			var.set(v_command)
			cmd.insert('end', '\n>>>Drawing Weblogo...')
			iweb.weblogo_multy(folder=weblogo_i, out=weblogo_o, tp=weblogo_t, label=weblogo_l.split(','))
			cmd.insert('end', '\n>>>Weblogo created successfully!')
		else:
			v_command = fs.commands('weblogo', {'-f':weblogo_i, '-o':weblogo_o, '-tp':weblogo_t})
			var.set(v_command)
			cmd.insert('end', '\n>>>Drawing Weblogo...')
			iweb.weblogo_multy(folder=weblogo_i, out=weblogo_o, tp=weblogo_t)
			cmd.insert('end', '\n>>>Weblogo created successfully!')
		fs.save(v_command, file_path)
		os.startfile(os.path.join(file_path, 'data'))

def gui_reduce_file():
	var.set(fs.description_reduce_mulity())
	reduce_i = e_reduce1_i.get()
	reduce_r = e_reduce1_r.get()
	reduce_o = e_reduce1_o.get()
	if len(reduce_r) != 0 and len(reduce_o) != 0 and len(reduce_i) != 0:
		v_command = fs.commands('reduce', {'-d':reduce_i, '-raa':reduce_r, '-o':reduce_o})
		var.set(v_command)
		cmd.insert('end', '\n>>>Drawing ReduceSequence...')
		ired.reduce(file=reduce_i, out=reduce_o, raa=reduce_r)
		cmd.insert('end', '\n>>>ReduceSequence created successfully!')
		fs.save(v_command, file_path)
		os.startfile(os.path.join(file_path, 'data'))

def gui_reduce_sq():
	var.set(fs.description_reduce_mulity())
	reduce_r = e_reduce2_r.get()
	reduce_o = e_reduce2_o.get()
	reduce_s = e_reduce2_s.get()
	if len(reduce_r) != 0 and len(reduce_o) != 0 and len(reduce_s) != 0:
		v_command = fs.commands('reduce', {'-sq':reduce_s, '-raa':reduce_r, '-o':reduce_o})
		var.set(v_command)
		cmd.insert('end', '\n>>>Drawing ReduceSequence...')
		ired.reduce(sq=reduce_s, out=reduce_o, raa=reduce_r)
		cmd.insert('end', '\n>>>ReduceSequence created successfully!')
		fs.save(v_command, file_path)
		os.startfile(os.path.join(file_path, 'data'))

# load logo
fs.load(file_path)

# windows
window = tk.Tk()
window.title('EasyBioPlot')
window.geometry('700x410')
window.resizable(0,0)
window.iconbitmap(os.path.join(os.path.join(file_path, 'bin'), 'Logo.ico'))
window.configure() 

# frame
frame = tk.Frame(window)
frame.pack(fill="both",padx=20,pady=10) 
frame_1 = tk.Frame(frame)
frame_2 = tk.Frame(frame)
frame_1.pack(side='top',fill="x")
frame_2.pack(side='bottom',fill="x")
frame_1_1 = tk.Frame(frame_1,bg='DarkTurquoise')
frame_1_2 = tk.Frame(frame_1)
frame_2_1 = tk.Frame(frame_2)
frame_2_2 = tk.Frame(frame_2)
frame_1_1.pack(side='top',fill="both")
frame_1_2.pack(side='bottom',fill="both")
frame_2_1.pack(side='top',fill="both")
frame_2_2.pack(side='bottom',fill="both")

# title
tilogo = tk.PhotoImage(file=(os.path.join(os.path.join(file_path, 'bin'), 'Title.gif')))
tilogo_label = tk.Label(frame_1_1,image=tilogo,bg='DarkTurquoise',anchor='center')
tilogo_label.pack(side='left')
tk.Label(frame_1_1,text=fs.title(),bg='DarkTurquoise',font=('SimHei', 16), width=60, height=3,anchor='center').pack()

# tabline
tabControl = ttk.Notebook(frame_1_2)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text=' Weblogo ')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text=' Reduce ')
tabControl.pack(expand=1, fill="x")

# weblogo single
weblogo_fuc1 = ttk.LabelFrame(tab1, text='Single Weblogo')
weblogo_fuc1.pack(fill='x',padx=8,pady=4)
######input
tk.Label(weblogo_fuc1,text='input',width=6,anchor='w').pack(side='left')
e_weblogo1_i = tk.Entry(weblogo_fuc1,show=None,width=10,font=('SimHei', 11))
e_weblogo1_i.pack(side='left')
tk.Label(weblogo_fuc1,text='',width=1,anchor='w').pack(side='left')
b_weblogo1_i = tk.Button(weblogo_fuc1,text='✉',font=('SimHei', 11),width=2,height=1,command=gui_webup1_file)
b_weblogo1_i.pack(side='left')
tk.Label(weblogo_fuc1,text='',width=2,anchor='w').pack(side='left')
######output
tk.Label(weblogo_fuc1,text='output',width=7,anchor='w').pack(side='left')
e_weblogo1_o = tk.Entry(weblogo_fuc1,show=None,width=10,font=('SimHei', 11))
e_weblogo1_o.pack(side='left')
tk.Label(weblogo_fuc1,text='',width=2,anchor='w').pack(side='left')
e_weblogo1_o.insert(0, os.path.join(os.path.join(file_path, 'data'), 'test.svg'))
######type
tk.Label(weblogo_fuc1,text='type',width=5,anchor='w').pack(side='left')
comvalue1 = tk.StringVar()
e_weblogo1_t = ttk.Combobox(weblogo_fuc1,width=5,textvariable=comvalue1)
e_weblogo1_t["values"]=("p","n","d")
e_weblogo1_t.current(0)
e_weblogo1_t.pack(side='left')
tk.Label(weblogo_fuc1,text='',width=2,anchor='w').pack(side='left')
######button
b_weblogo1 = tk.Button(weblogo_fuc1,text='Plot',font=('SimHei', 11),width=5,height=1,command=gui_weblogo_single)
b_weblogo1.pack(side='right')

# weblogo mulity
weblogo_fuc2 = ttk.LabelFrame(tab1, text='Mulity Weblogo')
weblogo_fuc2.pack(fill='x',padx=8,pady=4)
######input
tk.Label(weblogo_fuc2,text='input',width=6,anchor='w').pack(side='left')
e_weblogo2_i = tk.Entry(weblogo_fuc2,show=None,width=10,font=('SimHei', 11))
e_weblogo2_i.pack(side='left')
tk.Label(weblogo_fuc2,text='',width=1,anchor='w').pack(side='left')
b_weblogo2_i = tk.Button(weblogo_fuc2,text='✉',font=('SimHei', 11),width=2,height=1,command=gui_webup2_file)
b_weblogo2_i.pack(side='left')
tk.Label(weblogo_fuc2,text='',width=2,anchor='w').pack(side='left')
######output
tk.Label(weblogo_fuc2,text='output',width=7,anchor='w').pack(side='left')
e_weblogo2_o = tk.Entry(weblogo_fuc2,show=None,width=10,font=('SimHei', 11))
e_weblogo2_o.pack(side='left')
tk.Label(weblogo_fuc2,text='',width=2,anchor='w').pack(side='left')
e_weblogo2_o.insert(0, os.path.join(os.path.join(file_path, 'data'), 'test.svg'))
######type
tk.Label(weblogo_fuc2,text='type',width=5,anchor='w').pack(side='left')
comvalue2 = tk.StringVar()
e_weblogo2_t = ttk.Combobox(weblogo_fuc2,width=5,textvariable=comvalue2)
e_weblogo2_t["values"]=("p","n","d")
e_weblogo2_t.current(0)
e_weblogo2_t.pack(side='left')
tk.Label(weblogo_fuc2,text='',width=2,anchor='w').pack(side='left')
######label
tk.Label(weblogo_fuc2,text='label',width=6,anchor='w').pack(side='left')
e_weblogo2_l = tk.Entry(weblogo_fuc2,show=None,width=5,font=('SimHei', 11))
e_weblogo2_l.pack(side='left')
tk.Label(weblogo_fuc2,text='',width=2,anchor='w').pack(side='left')
######button
b_weblogo2 = tk.Button(weblogo_fuc2,text='Plot',font=('SimHei', 11),width=5,height=1,command=gui_weblogo_mulity)
b_weblogo2.pack(side='right')

# reduce FASTA file
reduce_fuc1 = ttk.LabelFrame(tab2, text='Reduce FASTA file')
reduce_fuc1.pack(fill='x',padx=8,pady=4)
######input
tk.Label(reduce_fuc1,text='input',width=6,anchor='w').pack(side='left')
e_reduce1_i = tk.Entry(reduce_fuc1,show=None,width=10,font=('SimHei', 11))
e_reduce1_i.pack(side='left')
tk.Label(reduce_fuc1,text='',width=1,anchor='w').pack(side='left')
b_reduce1_i = tk.Button(reduce_fuc1,text='✉',font=('SimHei', 11),width=2,height=1,command=gui_redup_file)
b_reduce1_i.pack(side='left')
tk.Label(reduce_fuc1,text='',width=1,anchor='w').pack(side='left')
######raacode
tk.Label(reduce_fuc1,text='raacode',width=8,anchor='w').pack(side='left')
e_reduce1_r = tk.Entry(reduce_fuc1,show=None,width=22,font=('SimHei', 11))
e_reduce1_r.pack(side='left')
tk.Label(reduce_fuc1,text='',width=2,anchor='w').pack(side='left')
e_reduce1_r.insert(0, 'LVIMCAGSTPFYW-EDNQKRH')
######out
tk.Label(reduce_fuc1,text='out',width=5,anchor='w').pack(side='left')
e_reduce1_o = tk.Entry(reduce_fuc1,show=None,width=5,font=('SimHei', 11))
e_reduce1_o.pack(side='left')
tk.Label(reduce_fuc1,text='',width=2,anchor='w').pack(side='left')
e_reduce1_o.insert(0, 'test')
######button
b_reduce1 = tk.Button(reduce_fuc1,text='Plot',font=('SimHei', 11),width=5,height=1,command=gui_reduce_file)
b_reduce1.pack(side='right')

# reduce sequence
reduce_fuc2 = ttk.LabelFrame(tab2, text='Reduce sequence')
reduce_fuc2.pack(fill='x',padx=8,pady=4)
######sequence
tk.Label(reduce_fuc2,text='sequence',width=9,anchor='w').pack(side='left')
e_reduce2_s = tk.Entry(reduce_fuc2,show=None,width=11,font=('SimHei', 11))
e_reduce2_s.pack(side='left')
tk.Label(reduce_fuc2,text='',width=2,anchor='w').pack(side='left')
######raacode
tk.Label(reduce_fuc2,text='raacode',width=8,anchor='w').pack(side='left')
e_reduce2_r = tk.Entry(reduce_fuc2,show=None,width=22,font=('SimHei', 11))
e_reduce2_r.pack(side='left')
tk.Label(reduce_fuc2,text='',width=2,anchor='w').pack(side='left')
e_reduce2_r.insert(0, 'LVIMCAGSTPFYW-EDNQKRH')
######out
tk.Label(reduce_fuc2,text='out',width=5,anchor='w').pack(side='left')
e_reduce2_o = tk.Entry(reduce_fuc2,show=None,width=5,font=('SimHei', 11))
e_reduce2_o.pack(side='left')
tk.Label(reduce_fuc2,text='',width=2,anchor='w').pack(side='left')
e_reduce2_o.insert(0, 'test')
######button
b_reduce2 = tk.Button(reduce_fuc2,text='Plot',font=('SimHei', 11),width=5,height=1,command=gui_reduce_sq)
b_reduce2.pack(side='right')

# menu
root_menu = tk.Menu(window)
# file
filemenu = tk.Menu(root_menu,tearoff=0)
root_menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open',command=gui_open)
filemenu.add_command(label='Exit',command=window.quit)
# help
editmenu = tk.Menu(root_menu, tearoff=0)
root_menu.add_cascade(label='Help',menu=editmenu)
editmenu.add_command(label='About',command=gui_about)
editmenu.add_command(label='Documentation',command=gui_documentation)
editmenu.add_command(label='RunningLog',command=gui_log)
window.config(menu=root_menu)

# log
cmd = tk.Text(frame_2_1,height=10,bg='black',fg='snow')
cmd.pack(fill='x')
fs.save('>>>' + os.getcwd() + '\t' + fs.detal_time(), file_path)
cmd.insert('end', '>>>' + os.getcwd())

# detals
var = tk.StringVar()
detal = tk.Label(frame_2_2,textvariable=var,anchor='w',bg='Snow')
detal.pack(fill='x')
var.set('Now time: ' + fs.detal_time())
# flash
window.mainloop()
