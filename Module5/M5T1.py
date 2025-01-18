import numpy as np
from colorama import Fore, Back, Style, init

init(autoreset=True)
A = np.arange(1, 16).reshape(3, 5)
B = np.arange(16, 31).reshape(3, 5)

print(Fore.BLUE + "Matrix A:")
print(Fore.BLUE + str(A))

A_transposed = A.T
print(Fore.GREEN + "\nMatrix A Transposed (5x3):")
print(Fore.GREEN + str(A_transposed))

A_rotated_180 = np.rot90(A, 2)
print(Fore.RED + "\nMatrix A Rotated 180 Degrees:")
print(Fore.RED + str(A_rotated_180))

A_mirrored = np.fliplr(A)
print(Fore.YELLOW + "\nMatrix A Mirrored Horizontally:")
print(Fore.YELLOW + str(A_mirrored))

print(Fore.WHITE + "\nMatrix B:")
print(Fore.WHITE + str(B))

AB_hstack = np.hstack((A, B))
print(Fore.BLUE + "\n[A, B] Horizontally Stacked (4x10):")
print(Fore.BLUE + str(AB_hstack))

AB_vstack = np.vstack((A, B))
print(Fore.CYAN + "\n[A; B] Vertically Stacked (6x5):")
print(Fore.CYAN + str(AB_vstack))

AB_8x10 = np.vstack((AB_hstack, np.hstack((B, A))))
print(Fore.MAGENTA + "\n[A, B; B, A] Stacked (8x10):")
print(Fore.MAGENTA + str(AB_8x10))

AB_mult = A @ B.T
print(Fore.GREEN + "\nMatrix Multiplication (A @ B.T):")
print(Fore.GREEN + str(AB_mult))
