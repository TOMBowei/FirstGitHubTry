import linecache
import tkinter as tk

dataset = []
the_line = linecache.getline('/Users/wubowei/Documents/毕业设计源代码/friend.csv', 47)
print (the_line)
the_line = the_line.strip('\n')
dataset= the_line.split(',')
print(dataset)

window = tk.Tk()
window.title('个人基本信息')
window.geometry('500x300')

list1 = tk.Listbox(window,height=14)
for item in dataset:
    list1.insert(0,item)
list1.grid(row=1,column=2,padx=(10,5),pady=10)
# list1.pack()

list2 = tk.Listbox(window,height=14)
basic_top=['QQ账号','QQ昵称','QQ空间名称','性别','星座','年龄','出生年份','生日','现居国家','现居省份','现居城市','故乡国家','故乡城市','添加时间']
for item in basic_top:
    list2.insert(0,item)
list2.grid(row=1,column=1,padx=(5,10),pady=10)

# list2.pack()
window.mainloop()