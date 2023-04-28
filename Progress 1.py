import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt

import JointClass as jc

app = tk.Tk()
app.title('Node application')

app.geometry('600x400')
app.config(bg="skyblue")

def save():
    num_joints = int(num_joints_entry.get())
    joint_coordinates = []
    for i in range(num_joints):
        x_coord = float(joint_x_entries[i].get())
        y_coord = float(joint_y_entries[i].get())
        joint_coordinates.append((x_coord, y_coord))
    print(joint_coordinates)
    plot_coordinates(joint_coordinates)
    
    num_members = int(num_members_entry.get())
    member_info = []
    for i in range(num_members):
        start_joint = (member_start_entries[i].get())
        end_joint = (member_end_entries[i].get())
        member_info.append((start_joint, end_joint))
    print(member_info)
    
    num_supports = int(num_supports_entry.get())
    support_info = []
    for i in range(num_supports):
        support_joint = support_joint_entries[i].get()
        support_type = support_type_entries[i].get()
        support_info.append((support_joint,support_type))
    print(support_info)
        
    num_loads = int(num_loads_entry.get())
    load_info = []
    for i in range(num_loads):
        load_joint = int(load_joint_entries[i].get())
        load_intensity = load_intensity_entries[i].get()
        load_info.append((load_joint, load_intensity))
    print(load_info)
    

def plot_coordinates(coordinates):
    x_values = [coord[0] for coord in coordinates]
    y_values = [coord[1] for coord in coordinates]
    plt.scatter(x_values, y_values)
    plt.show()

root = tk.Tk()
root.title("TRUSS")

jointlabelframe=ttk.LabelFrame(root,text='Joint')
jointlabelframe.grid(row=0,column=0)

memlabelframe=ttk.LabelFrame(root,text='Member')
memlabelframe.grid(row=0,column=1)

loadlabelframe=ttk.LabelFrame(root,text='Load')
loadlabelframe.grid(row=2,column=0)

supportslabelframe = ttk.LabelFrame(root,text='Support')
supportslabelframe.grid(row=2,column=1)


num_joints_label = ttk.Label(jointlabelframe, text="Number of joints:")
num_joints_label.grid(column=0, row=0)

num_joints_entry = ttk.Entry(jointlabelframe)
num_joints_entry.grid(column=1, row=0)

joint_x_labels = []
joint_y_labels = []
joint_x_entries = []
joint_y_entries = []

def add_joint_entries():
    num_joints = int(num_joints_entry.get())

    for i in range(num_joints):
        joint_label = ttk.Label(jointlabelframe, text=f"Joint {i+1}")
        joint_label.grid(column=0, row=i+1)

        joint_x_label = ttk.Label(jointlabelframe, text="X-coord:")
        joint_x_label.grid(column=1, row=i+1)
        joint_x_labels.append(joint_x_label)

        joint_x_entry = ttk.Entry(jointlabelframe)
        joint_x_entry.grid(column=2, row=i+1)
        joint_x_entries.append(joint_x_entry)

        joint_y_label = ttk.Label(jointlabelframe, text="Y-coord:")
        joint_y_label.grid(column=3, row=i+1)
        joint_y_labels.append(joint_y_label)

        joint_y_entry = ttk.Entry(jointlabelframe)
        joint_y_entry.grid(column=4, row=i+1)
        joint_y_entries.append(joint_y_entry)
        
def add_member_entries():        
    global num_members_entry
    num_members_label = ttk.Label(memlabelframe, text="Number of members:")
    num_members_label.grid(column=0, row=0)
    num_members_entry = ttk.Entry(memlabelframe)
    num_members_entry.grid(column=1, row= 0)    
    num_members = (num_members_entry.get())
    
    num_members_btn=ttk.Button(memlabelframe, text='OK' , command=member_info)
    num_members_btn.grid(row=0,column=3)

    
def member_info():
    global member_start_entries
    global member_end_entries
    num_members = int(num_members_entry.get())
    member_start_entries = []
    member_end_entries = []
    for i in range(num_members):
        member_start_label = ttk.Label(memlabelframe, text=f"Member {i+1} Start:")
        member_start_label.grid(column=0, row=len(joint_x_entries)+1+i)

        member_start_entry = ttk.Entry(memlabelframe)
        member_start_entry.grid(column=1, row=len(joint_x_entries)+1+i)
        member_start_entries.append(member_start_entry)

        member_end_label = ttk.Label(memlabelframe, text=f"Member {i+1} End:")
        member_end_label.grid(column=2, row=len(joint_x_entries)+1+i)

        member_end_entry = ttk.Entry(memlabelframe)
        member_end_entry.grid(column=3, row=len(joint_x_entries)+1+i)
        member_end_entries.append(member_end_entry)

def add_support_entries():
    num_spport_label = ttk.Label(supportslabelframe, text='Number of Support')
    num_spport_label.grid(row=0,column=0)
    
    global num_supports_entry
    num_supports_entry =ttk.Entry(supportslabelframe)
    num_supports_entry.grid(row=0,column= 1)
    
    num_supports_bttn = ttk.Button(supportslabelframe,text='OK',command=support_info)
    num_supports_bttn.grid(row=0,column=2)
    
def support_info():
    global support_joint_entries
    global support_type_entries
    support_joint_entries = []
    support_type_entries = []
    for i in range(int(num_supports_entry.get())):
        support_joint_label = ttk.Label(supportslabelframe, text=f"Support {i+1} Joint:")
        support_joint_label.grid(column=0, row=len(joint_x_entries)+len(member_start_entries)+2+i)

        support_joint_entry = ttk.Entry(supportslabelframe)
        support_joint_entry.grid(column=1, row=len(joint_x_entries)+len(member_start_entries)+2+i)
        support_joint_entries.append(support_joint_entry)

        support_type_label = ttk.Label(supportslabelframe, text=f"Support {i+1} Type:")
        support_type_label.grid(column=2, row=len(joint_x_entries)+len(member_start_entries)+2+i)

        support_type_entry = ttk.Combobox(supportslabelframe, values=['Pin','Roller','Fixed'])
        support_type_entry.grid(column=3, row=len(joint_x_entries)+len(member_start_entries)+2+i)
        support_type_entries.append(support_type_entry)


def add_load_entries():
    num_loads_label = ttk.Label(loadlabelframe, text="Number of loads:")
    num_loads_label.grid(column=0, row=0)

    global num_loads_entry
    num_loads_entry = ttk.Entry(loadlabelframe)
    num_loads_entry.grid(column=1, row=0)
    
    num_load_bttn=ttk.Button(loadlabelframe,text="Ok",command=load_info)
    num_load_bttn.grid(column=2, row=0)
    
    
def load_info():
    global load_joint_entries
    global load_intensity_entries
    load_joint_entries = []
    load_intensity_entries = []
    for i in range(int(num_loads_entry.get())):
        load_joint_label = ttk.Label(loadlabelframe, text=f"Load {i+1} Joint:")
        load_joint_label.grid(column=0, row=i+4)

        load_joint_entry = ttk.Entry(loadlabelframe)
        load_joint_entry.grid(column=1, row=i+4)
        load_joint_entries.append(load_joint_entry)

        load_intensity_label = ttk.Label(loadlabelframe, text=f"Load {i+1} Intensity:")
        load_intensity_label.grid(column=2, row=len(joint_x_entries)+4+i)
        load_intensity_entry = ttk.Entry(loadlabelframe)
        load_intensity_entry.grid(column=3, row=len(joint_x_entries)+4+i)
        load_intensity_entries.append(load_intensity_entry)

    save_button = ttk.Button(root, text="Save", command=save)
    save_button.grid(column=i, row=i)

add_joints_button = ttk.Button(jointlabelframe, text="Add Joints Coord", command=add_joint_entries)
add_joints_button.grid(column=2, row=0)

add_member_entries_button = ttk.Button(memlabelframe, text="Add Member", command=add_member_entries)
add_member_entries_button.grid(column=3, row=0)

add_support_entries_bttn = ttk.Button(supportslabelframe,text='Add Support',command=add_support_entries)
add_support_entries_bttn.grid(row=0,column=2)

add_load_button = ttk.Button(loadlabelframe, text="Add Load", command=add_load_entries)
add_load_button.grid(column=2, row=0)



app.mainloop()
