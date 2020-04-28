# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:07:28 2020

@author: Yugar
"""

import file_operation

import tkinter as tk
from tkinter import Tk
from tkinter import ttk
from tkinter import filedialog
import os

class Root(Tk):
    
    def __init__(self):
        super(Root,self).__init__()
        
        # initiate variables
        self.initVar()
        
        self.title("Tkinter Dialog Widget")
        # self.minsize(800,200)
        self.geometry("800x200+550+350")
#        self.wm_iconbitmap('icon.ico')
        self.columnconfigure([0,2],minsize=15)
        self.columnconfigure([1],minsize=15)
        self.rowconfigure([0,1],minsize=10)


        self.frm_main = ttk.Frame(self)
        self.frm_main.pack()
        #
        self.lbl_source = ttk.Label(self.frm_main, text = '请选择源文件夹路径')
        self.lbl_source.grid(row=0,column=0,padx=10,sticky='e')
        
        self.ent_source = ttk.Entry(self.frm_main,width=50)
        self.ent_source.grid(row=0,column=1,padx=10,sticky='e')
        
        self.btn_sltsrc = ttk.Button(self.frm_main,text="browse",command=self.fileDialogSource)
        self.btn_sltsrc.grid(row=0,column=2,padx=10,sticky='e')
        
        # row 1  
        self.lbl_output = ttk.Label(self.frm_main, text = '请选择输出文件夹路径')
        self.lbl_output.grid(row=1,column=0,padx=10,sticky='e')
        
        self.ent_output = ttk.Entry(self.frm_main,width=50)
        self.ent_output.grid(row=1,column=1,padx=10,sticky='e')
        
        self.btn_sltout = ttk.Button(self.frm_main,text="browse",command=self.fileDialogOutput)
        self.btn_sltout.grid(row=1,column=2,padx=10,sticky='e')

        # row 2
        self.cbtn_current = ttk.Checkbutton(self.frm_main, variable=self.outputvar,
                                            text='输出到源文件夹下的output文件夹')
        self.cbtn_current.grid(row=2,column=1,padx=10,sticky='w')
        self.cbtn_current.invoke()
        self.cbtn_current.invoke()
        
        # row 3
        self.lbl_warning = ttk.Label(self.frm_main, text = '请确保文件夹为空！')
        self.lbl_warning.grid(row=3,column=1,padx=10,sticky='w')
        
        # row 4
        self.lbl_tip = ttk.Label(self.frm_main)
        self.lbl_tip.grid(row=4,column=1,padx=10,sticky='w')
        
        
        # frm_buttons
        self.frm_buttons = ttk.Frame(self)
        self.frm_buttons.pack(fill=tk.BOTH)
        
        self.btn_commit = ttk.Button(self.frm_buttons,text="确认", command=self.commitSort)
        self.btn_commit.pack()
        
    def fileDialogSource(self):
        self.ent_source.delete(0, tk.END)
        self.ent_source.insert(0, filedialog.askdirectory(initialdir= os.getcwd(), 
              title = "Select A Folder", mustexist=True))
        
    def fileDialogOutput(self):
        '''
        the folder needn't to be existed
        
        mustexist=False

        Returns
        -------
        None.

        '''
        self.ent_output.delete(0, tk.END)
        self.ent_output.insert(0, filedialog.askdirectory(initialdir= os.getcwd(), 
              title = "Select A Folder", mustexist=False))
    
    def commitSort(self):
        self.source_path = self.ent_source.get()
        self.output_path = self.ent_output.get()
        
        # if os.path.isdir(self.source_path):
        if not os.path.isdir(self.source_path):
            # self.warning = tk.Tk()
            # self.warning.geometry("200x50+850+300")
            # ttk.Label(self.warning, text='源文件夹路径不能为空！').pack(padx=10,pady=5)
            self.lbl_tip['text'] = '源文件夹路径无效！'
            
        else:
            if self.outputvar.get() == 1 or self.output_path == None:
                self.output_path = self.source_path + '/output'
                
            try:
                os.mkdir(self.output_path)
            except FileExistsError: # if the folder existed
                try:
                    os.removedirs(self.output_path)
                except OSError: # not empty, throw error
                    self.lbl_tip['text'] = '输出文件夹需要为空文件夹！'
                else: # empty, exec sort
                    os.mkdir(self.output_path)
                    file_operation.sort_files(self.source_path, self.output_path)
                    print(self.source_path)
                    print(self.output_path)
            else: # not existed, exec sort
                file_operation.sort_files(self.source_path, self.output_path)
                print(self.source_path)
                print(self.output_path)
                
        
    def initVar(self):
        self.source_path = None
        self.output_path = None
        
        self.outputvar = tk.IntVar()
        

if __name__ == '__main__':
    root = Root()
    root.mainloop()