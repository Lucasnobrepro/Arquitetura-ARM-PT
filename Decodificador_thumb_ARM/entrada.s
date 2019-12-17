.thumb


strh r5, [r4, r2]

ldr r5, [r4, #3]
str r4, [r1, #2]


ldr r3, [pc, #100]

ldr r0, [r4, r6]
str r0, [r4, r6]


strb r5, [r7, r6]
ldrb r5, [r7, r6]
bx r40

blx r11

add r8, r9
cmp r8, r9
mov r8, r9

asr r7, r5
and r0, r3
mul r4, r3
cmp r1, r2

mov r0, #3
mov r1, #5

main:

add r2, r1, #5
push {r2}
swi #10
pop {r2}
sub r2, #1
cmp r2, #0
beq fim
mov r0, r2
b main

fim:
b 