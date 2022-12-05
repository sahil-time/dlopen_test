import os

DEBUG = True

######################### UTILS #########################

obj_files_list = []

# Wrapper on os.system for debug info
def sys_call(cmd):
    if DEBUG == True:
        print(cmd)
    os.system(cmd)

# Remove object file
def remove_obj(obj):
    sys_call("rm " + obj)

# Removes all created Object files
def remove_all_obj():
    for obj in obj_files_list:
        remove_obj(obj)

# Creates a shared lib with a single C file and ".so" dependency
def create_shared_lib(c_file, so_dep=""):
    lib_name = c_file.split('.')[0].upper()
    obj_name = c_file.split('.')[0]

    sys_call("gcc -fPIC -c " + c_file + " -o " + obj_name + ".o")
    obj_files_list.append(obj_name + ".o")

    if so_dep == "":
        sys_call("gcc -shared -o lib" + lib_name + ".so " + obj_name + ".o")
    else:
        sys_call("gcc -shared -o lib" + lib_name + ".so " + obj_name + ".o -Wl,-rpath,. -L . -l" + so_dep.replace("lib",""))

    obj_files_list.append("lib" + lib_name + ".so")

# Creates executable from C file and shared dependencies
def create_executable(c_file, args = "", so_dep=[]):
    exec_name = c_file.split('.')[0]
    
    if len(so_dep) == 0:
        sys_call("gcc -Wall " + c_file + " -o " + exec_name + " " + args)
    else:
        dep_str = ""
        for dep in so_dep:
            dep_str = dep_str + "-l" + dep.replace("lib","") + " "
        sys_call("gcc -Wall " + c_file + " -o " + exec_name + " " + args + " -L . " + dep_str)

######################### TEST #########################

create_shared_lib("b1.c")
create_shared_lib("b2.c")
create_shared_lib("c.c")
create_shared_lib("a.c", "libB1")
create_executable("dlopen.c", "-ldl", ["libA"])
sys_call("./" + "dlopen")

#remove_all_obj()
