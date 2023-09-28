import subprocess
import py.config 

status = "pass"

project_folder =  py.config.var["project_folder"]

program_list = [project_folder + '/py/0_health_bot.py', project_folder + '/py/1_main_playwright.py', project_folder + '/py/2_process_excel.py', project_folder + '/py/3_send_email_outlook.py']

for program in program_list:
    subprocess.run(['python', program])
    print("### Finished:" + program)
exit(0)