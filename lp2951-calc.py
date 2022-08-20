import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print("\nLP2951 CALC ")
print("-----------------------\n")
vref = 1.235
voutmin = float(input("[-] VOut Minimum (v): "))
voutmax = float(input("[-] VOut Maximum (v): "))
cvmax = float(input("[-] CV maximum (v): "))
R3 = int(input("[-] R3 Value (Ω): "))
print("\n(reference voltage = 1.235v)\n\n")
print("COMPONENT VALUES:\n-------------------------------\n")


#-------------------------------------------#


k1 = vref * (voutmax - voutmin) 
k2 = vref * (voutmin - cvmax - voutmax) + (cvmax * voutmax)
K = k1 / k2

print("[+] K =", bcolors.OKBLUE, K, bcolors.ENDC)


#------------------------------------------#


r11 = K * R3 * (voutmax - vref)
r12 = vref * K + 1
R1 = r11 // r12
print("[+] R1 Value:", bcolors.OKBLUE, round(R1, 2), bcolors.ENDC, "Ω")


#------------------------------------------#


R2 = K * R3
print("[+] R2 Value:", bcolors.OKBLUE, round(R2, 2), bcolors.ENDC, "Ω\n")


#-------------------------------------------#


c1 = cvmax * voutmax / vref
c2 = voutmin - cvmax - voutmax

if c1 > c2:
    print("[+]", bcolors.OKGREEN,"CONDITIONS MET\n" + bcolors.ENDC)
else:
    print("\n[x]CONDITIONS UNMET\n")