import subprocess
import py.config 

status = "pass"

project_folder =  py.config.var["project_folder"]

program_list = [project_folder + '/py/0.py', project_folder + '/py/1.py', project_folder + '/py/2.py', project_folder + '/py/3.py']

for program in program_list:
    subprocess.run(['python', program])
    print("### Finished:" + program)
exit(0)