##############################################
#                 CREDITS                    #
#              Made By Novex                 #
#         github.com/NovexTheRizzler         #         
##############################################

##############################################
#                DISCLAIMER                  #
#            EDUCATIONAL PURPOSES            #
#                   ONLY!                    #         
##############################################

from Helper import *



def fake_ddos():
    width_px = 930
    height_px = 340

    char_width = width_px // 8
    char_height = height_px // 16

    os.system(f"mode con: cols={char_width} lines={char_height}")
    ctypes.windll.kernel32.SetConsoleTitleW(f'''DDoS | discord.gg/subscribers | Developer - Novex ''')

    print(banner1)
    ip = input(f"{hash} Enter Victom Ip >  ")
    print(f"{hash} Choose DDoS Method > ")
    methods = [f" PyFlooder", f" Botnet Server", f" TCP"]
    for i, method in enumerate(methods, 1):
        print(f"{i}. {method}")

    method_choice = int(input(f"{minus} Enter the number of the method: "))
    if method_choice not in range(1, len(methods) + 1):
        print(f"{mark} [WRONG OPTION] ")
        return

    print(f"{hash} Starting DDoS attack on {ip} using{methods[method_choice - 1]} method...")
    
    # Fake ahh loading
    for _ in range(10):
        print(".", end="", flush=True)
        time.sleep(random.uniform(0.1, 0.5))

    os.system("cls")  
    ctypes.windll.kernel32.SetConsoleTitleW(f'''DDOS ATTACK STARTED ON {ip} ''')  
    print(banner1)
    print(f"\n{mark} DDoS attack started!")
    
    # Fake ahh data sending
    sent_data = 0
    units = ["MB", "GB", "TB"]
    while True:
        time.sleep(1)
        data_sent = random.randint(1, 100)
        sent_data += data_sent
        unit_index = 0
        display_data = sent_data
        while display_data >= 1000 and unit_index < len(units) - 1:
            display_data /= 1000
            unit_index += 1
        print(f"{hash} Sent {data_sent} MB... Total: {display_data:.2f} {units[unit_index]}")
        if sent_data > 10000:  # Stop after 1000mb of data fr
            print(f"{hash} Stopping DDoS attack...")
            break

if __name__ == "__main__":
    fake_ddos()
