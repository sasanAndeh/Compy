segment .text
global _start
_start:
    ret

;winget install nasm -i
;nasm -f win32 assembly.asm -o test.o
;ld -m i386pe -s -o file.exe a.o
