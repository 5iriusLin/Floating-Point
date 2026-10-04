	.file	"kernels.cpp"
	.text
	.section	.text._Z6kernelIfET_mS0_S0_S0_S0_9Operationb,"axG",@progbits,_Z6kernelIfET_mS0_S0_S0_S0_9Operationb,comdat
	.p2align 4
	.weak	_Z6kernelIfET_mS0_S0_S0_S0_9Operationb
	.type	_Z6kernelIfET_mS0_S0_S0_S0_9Operationb, @function
_Z6kernelIfET_mS0_S0_S0_S0_9Operationb:
.LFB16:
	.cfi_startproc
	movss	.LC0(%rip), %xmm4
	movss	%xmm0, -16(%rsp)
	addss	%xmm0, %xmm4
	movss	%xmm4, -12(%rsp)
	movss	.LC1(%rip), %xmm4
	addss	%xmm0, %xmm4
	addss	.LC2(%rip), %xmm0
	movss	%xmm4, -8(%rsp)
	movss	%xmm0, -4(%rsp)
	testb	%dl, %dl
	jne	.L2
	cmpl	$1, %esi
	je	.L3
	cmpl	$2, %esi
	je	.L45
	testl	%esi, %esi
	jne	.L42
	movss	-16(%rsp), %xmm0
	xorl	%eax, %eax
	testq	%rdi, %rdi
	je	.L42
	.p2align 5
	.p2align 4
	.p2align 3
.L11:
	addss	%xmm1, %xmm0
	addq	$1, %rax
	subss	%xmm1, %xmm0
	cmpq	%rax, %rdi
	jne	.L11
	movss	%xmm0, -16(%rsp)
.L42:
	movss	-16(%rsp), %xmm0
	ret
	.p2align 4,,10
	.p2align 3
.L2:
	cmpl	$1, %esi
	je	.L15
	cmpl	$2, %esi
	je	.L46
	testl	%esi, %esi
	jne	.L40
	testq	%rdi, %rdi
	je	.L40
	movss	-16(%rsp), %xmm4
	movss	-12(%rsp), %xmm3
	xorl	%eax, %eax
	movss	-8(%rsp), %xmm2
	movss	-4(%rsp), %xmm0
	.p2align 6
	.p2align 4
	.p2align 3
.L24:
	addss	%xmm1, %xmm4
	addss	%xmm1, %xmm3
	addq	$1, %rax
	addss	%xmm1, %xmm2
	addss	%xmm1, %xmm0
	subss	%xmm1, %xmm4
	subss	%xmm1, %xmm3
	subss	%xmm1, %xmm2
	subss	%xmm1, %xmm0
	cmpq	%rax, %rdi
	jne	.L24
	movss	%xmm4, -16(%rsp)
	movss	%xmm3, -12(%rsp)
	movss	%xmm2, -8(%rsp)
	movss	%xmm0, -4(%rsp)
	jmp	.L18
	.p2align 4,,10
	.p2align 3
.L40:
.L18:
	movss	-16(%rsp), %xmm0
	addss	-12(%rsp), %xmm0
	addss	-8(%rsp), %xmm0
	addss	-4(%rsp), %xmm0
	ret
	.p2align 4,,10
	.p2align 3
.L15:
	testq	%rdi, %rdi
	je	.L40
	movss	-16(%rsp), %xmm5
	movss	-12(%rsp), %xmm4
	xorl	%eax, %eax
	movss	-8(%rsp), %xmm1
	movss	-4(%rsp), %xmm0
	.p2align 6
	.p2align 4
	.p2align 3
.L25:
	mulss	%xmm2, %xmm5
	addq	$1, %rax
	mulss	%xmm2, %xmm4
	mulss	%xmm2, %xmm1
	mulss	%xmm2, %xmm0
	mulss	%xmm3, %xmm5
	mulss	%xmm3, %xmm4
	mulss	%xmm3, %xmm1
	mulss	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L25
.L41:
	movss	%xmm5, -16(%rsp)
	movss	%xmm4, -12(%rsp)
	movss	%xmm1, -8(%rsp)
	movss	%xmm0, -4(%rsp)
	jmp	.L18
	.p2align 4,,10
	.p2align 3
.L3:
	movss	-16(%rsp), %xmm0
	xorl	%eax, %eax
	testq	%rdi, %rdi
	je	.L42
	.p2align 5
	.p2align 4
	.p2align 3
.L13:
	mulss	%xmm2, %xmm0
	addq	$1, %rax
	mulss	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L13
	movss	%xmm0, -16(%rsp)
	jmp	.L42
	.p2align 4,,10
	.p2align 3
.L46:
	testq	%rdi, %rdi
	je	.L40
	movss	-16(%rsp), %xmm5
	movss	-12(%rsp), %xmm4
	xorl	%eax, %eax
	movss	-8(%rsp), %xmm1
	movss	-4(%rsp), %xmm0
	.p2align 6
	.p2align 4
	.p2align 3
.L26:
	divss	%xmm2, %xmm5
	addq	$1, %rax
	divss	%xmm2, %xmm4
	divss	%xmm2, %xmm1
	divss	%xmm2, %xmm0
	divss	%xmm3, %xmm5
	divss	%xmm3, %xmm4
	divss	%xmm3, %xmm1
	divss	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L26
	jmp	.L41
	.p2align 4,,10
	.p2align 3
.L45:
	movss	-16(%rsp), %xmm0
	xorl	%eax, %eax
	testq	%rdi, %rdi
	je	.L42
	.p2align 5
	.p2align 4
	.p2align 3
.L14:
	divss	%xmm2, %xmm0
	addq	$1, %rax
	divss	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L14
	movss	%xmm0, -16(%rsp)
	jmp	.L42
	.cfi_endproc
.LFE16:
	.size	_Z6kernelIfET_mS0_S0_S0_S0_9Operationb, .-_Z6kernelIfET_mS0_S0_S0_S0_9Operationb
	.section	.text._Z6kernelIdET_mS0_S0_S0_S0_9Operationb,"axG",@progbits,_Z6kernelIdET_mS0_S0_S0_S0_9Operationb,comdat
	.p2align 4
	.weak	_Z6kernelIdET_mS0_S0_S0_S0_9Operationb
	.type	_Z6kernelIdET_mS0_S0_S0_S0_9Operationb, @function
_Z6kernelIdET_mS0_S0_S0_S0_9Operationb:
.LFB17:
	.cfi_startproc
	movsd	.LC3(%rip), %xmm4
	movsd	%xmm0, -32(%rsp)
	addsd	%xmm0, %xmm4
	movsd	%xmm4, -24(%rsp)
	movsd	.LC4(%rip), %xmm4
	addsd	%xmm0, %xmm4
	addsd	.LC5(%rip), %xmm0
	movsd	%xmm4, -16(%rsp)
	movsd	%xmm0, -8(%rsp)
	testb	%dl, %dl
	jne	.L48
	cmpl	$1, %esi
	je	.L49
	cmpl	$2, %esi
	je	.L90
	testl	%esi, %esi
	jne	.L88
	movsd	-32(%rsp), %xmm0
	xorl	%eax, %eax
	testq	%rdi, %rdi
	je	.L88
	.p2align 5
	.p2align 4
	.p2align 3
.L57:
	addsd	%xmm1, %xmm0
	addq	$1, %rax
	subsd	%xmm1, %xmm0
	cmpq	%rax, %rdi
	jne	.L57
	movsd	%xmm0, -32(%rsp)
.L88:
	movsd	-32(%rsp), %xmm0
	ret
	.p2align 4,,10
	.p2align 3
.L48:
	cmpl	$1, %esi
	je	.L61
	cmpl	$2, %esi
	je	.L91
	testl	%esi, %esi
	jne	.L86
	testq	%rdi, %rdi
	je	.L86
	movsd	-32(%rsp), %xmm4
	movsd	-24(%rsp), %xmm3
	xorl	%eax, %eax
	movsd	-16(%rsp), %xmm2
	movsd	-8(%rsp), %xmm0
	.p2align 6
	.p2align 4
	.p2align 3
.L70:
	addsd	%xmm1, %xmm4
	addsd	%xmm1, %xmm3
	addq	$1, %rax
	addsd	%xmm1, %xmm2
	addsd	%xmm1, %xmm0
	subsd	%xmm1, %xmm4
	subsd	%xmm1, %xmm3
	subsd	%xmm1, %xmm2
	subsd	%xmm1, %xmm0
	cmpq	%rax, %rdi
	jne	.L70
	movsd	%xmm4, -32(%rsp)
	movsd	%xmm3, -24(%rsp)
	movsd	%xmm2, -16(%rsp)
	movsd	%xmm0, -8(%rsp)
	jmp	.L64
	.p2align 4,,10
	.p2align 3
.L86:
.L64:
	movsd	-32(%rsp), %xmm0
	addsd	-24(%rsp), %xmm0
	addsd	-16(%rsp), %xmm0
	addsd	-8(%rsp), %xmm0
	ret
	.p2align 4,,10
	.p2align 3
.L61:
	testq	%rdi, %rdi
	je	.L86
	movsd	-32(%rsp), %xmm5
	movsd	-24(%rsp), %xmm4
	xorl	%eax, %eax
	movsd	-16(%rsp), %xmm1
	movsd	-8(%rsp), %xmm0
	.p2align 6
	.p2align 4
	.p2align 3
.L71:
	mulsd	%xmm2, %xmm5
	addq	$1, %rax
	mulsd	%xmm2, %xmm4
	mulsd	%xmm2, %xmm1
	mulsd	%xmm2, %xmm0
	mulsd	%xmm3, %xmm5
	mulsd	%xmm3, %xmm4
	mulsd	%xmm3, %xmm1
	mulsd	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L71
.L87:
	movsd	%xmm5, -32(%rsp)
	movsd	%xmm4, -24(%rsp)
	movsd	%xmm1, -16(%rsp)
	movsd	%xmm0, -8(%rsp)
	jmp	.L64
	.p2align 4,,10
	.p2align 3
.L49:
	movsd	-32(%rsp), %xmm0
	xorl	%eax, %eax
	testq	%rdi, %rdi
	je	.L88
	.p2align 5
	.p2align 4
	.p2align 3
.L59:
	mulsd	%xmm2, %xmm0
	addq	$1, %rax
	mulsd	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L59
	movsd	%xmm0, -32(%rsp)
	jmp	.L88
	.p2align 4,,10
	.p2align 3
.L91:
	testq	%rdi, %rdi
	je	.L86
	movsd	-32(%rsp), %xmm5
	movsd	-24(%rsp), %xmm4
	xorl	%eax, %eax
	movsd	-16(%rsp), %xmm1
	movsd	-8(%rsp), %xmm0
	.p2align 6
	.p2align 4
	.p2align 3
.L72:
	divsd	%xmm2, %xmm5
	addq	$1, %rax
	divsd	%xmm2, %xmm4
	divsd	%xmm2, %xmm1
	divsd	%xmm2, %xmm0
	divsd	%xmm3, %xmm5
	divsd	%xmm3, %xmm4
	divsd	%xmm3, %xmm1
	divsd	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L72
	jmp	.L87
	.p2align 4,,10
	.p2align 3
.L90:
	movsd	-32(%rsp), %xmm0
	xorl	%eax, %eax
	testq	%rdi, %rdi
	je	.L88
	.p2align 5
	.p2align 4
	.p2align 3
.L60:
	divsd	%xmm2, %xmm0
	addq	$1, %rax
	divsd	%xmm3, %xmm0
	cmpq	%rax, %rdi
	jne	.L60
	movsd	%xmm0, -32(%rsp)
	jmp	.L88
	.cfi_endproc
.LFE17:
	.size	_Z6kernelIdET_mS0_S0_S0_S0_9Operationb, .-_Z6kernelIdET_mS0_S0_S0_S0_9Operationb
	.section	.text._Z6kernelIeET_mS0_S0_S0_S0_9Operationb,"axG",@progbits,_Z6kernelIeET_mS0_S0_S0_S0_9Operationb,comdat
	.p2align 4
	.weak	_Z6kernelIeET_mS0_S0_S0_S0_9Operationb
	.type	_Z6kernelIeET_mS0_S0_S0_S0_9Operationb, @function
_Z6kernelIeET_mS0_S0_S0_S0_9Operationb:
.LFB18:
	.cfi_startproc
	fldt	8(%rsp)
	fldt	24(%rsp)
	fldt	40(%rsp)
	fldt	56(%rsp)
	fxch	%st(3)
	fld	%st(0)
	fstpt	-72(%rsp)
	fld	%st(0)
	fadds	.LC0(%rip)
	fstpt	-56(%rsp)
	fld	%st(0)
	fadds	.LC1(%rip)
	fstpt	-40(%rsp)
	fadds	.LC2(%rip)
	fstpt	-24(%rsp)
	testb	%dl, %dl
	jne	.L93
	cmpl	$1, %esi
	je	.L94
	cmpl	$2, %esi
	je	.L133
	fstp	%st(0)
	fstp	%st(1)
	testl	%esi, %esi
	jne	.L136
	testq	%rdi, %rdi
	je	.L137
	fldt	-72(%rsp)
	xorl	%eax, %eax
	.p2align 4
	.p2align 4
	.p2align 3
.L102:
	fadd	%st(1), %st
	addq	$1, %rax
	fsub	%st(1), %st
	cmpq	%rax, %rdi
	jne	.L102
	fstp	%st(1)
	fstpt	-72(%rsp)
	jmp	.L131
	.p2align 4,,10
	.p2align 3
.L136:
	fstp	%st(0)
	jmp	.L131
	.p2align 4,,10
	.p2align 3
.L137:
	fstp	%st(0)
	jmp	.L131
	.p2align 4,,10
	.p2align 3
.L143:
	fstp	%st(0)
	fstp	%st(0)
	jmp	.L131
	.p2align 4,,10
	.p2align 3
.L146:
	fstp	%st(0)
	fstp	%st(0)
.L131:
	fldt	-72(%rsp)
	ret
	.p2align 4,,10
	.p2align 3
.L93:
	cmpl	$1, %esi
	je	.L106
	cmpl	$2, %esi
	je	.L134
	fstp	%st(0)
	fstp	%st(1)
	testl	%esi, %esi
	jne	.L138
	testq	%rdi, %rdi
	je	.L139
	fldt	-72(%rsp)
	xorl	%eax, %eax
	fldt	-56(%rsp)
	fldt	-40(%rsp)
	fldt	-24(%rsp)
	fxch	%st(3)
	jmp	.L115
	.p2align 6
	.p2align 4,,10
	.p2align 3
.L140:
	fxch	%st(3)
	fxch	%st(1)
	fxch	%st(2)
.L115:
	fadd	%st(4), %st
	addq	$1, %rax
	fsub	%st(4), %st
	fxch	%st(2)
	fadd	%st(4), %st
	fsub	%st(4), %st
	fxch	%st(1)
	fadd	%st(4), %st
	fsub	%st(4), %st
	fxch	%st(3)
	fadd	%st(4), %st
	fsub	%st(4), %st
	cmpq	%rax, %rdi
	jne	.L140
	fstp	%st(4)
	fxch	%st(1)
	fxch	%st(2)
	fxch	%st(3)
	fxch	%st(2)
	fstpt	-72(%rsp)
	fstpt	-56(%rsp)
	fxch	%st(1)
	fstpt	-40(%rsp)
	fstpt	-24(%rsp)
	jmp	.L109
	.p2align 4,,10
	.p2align 3
.L138:
	fstp	%st(0)
	jmp	.L128
	.p2align 4,,10
	.p2align 3
.L139:
	fstp	%st(0)
	jmp	.L128
	.p2align 4,,10
	.p2align 3
.L141:
	fstp	%st(0)
	fstp	%st(0)
	jmp	.L128
	.p2align 4,,10
	.p2align 3
.L144:
	fstp	%st(0)
	fstp	%st(0)
	.p2align 4
	.p2align 3
.L128:
.L109:
	fldt	-72(%rsp)
	fldt	-56(%rsp)
	faddp	%st, %st(1)
	fldt	-40(%rsp)
	faddp	%st, %st(1)
	fldt	-24(%rsp)
	faddp	%st, %st(1)
	ret
	.p2align 4,,10
	.p2align 3
.L106:
	fstp	%st(1)
	testq	%rdi, %rdi
	je	.L141
	fldt	-72(%rsp)
	xorl	%eax, %eax
	fldt	-56(%rsp)
	fldt	-40(%rsp)
	fldt	-24(%rsp)
	fxch	%st(3)
	jmp	.L116
	.p2align 6
	.p2align 4,,10
	.p2align 3
.L142:
	fxch	%st(3)
	fxch	%st(1)
	fxch	%st(2)
.L116:
	fmul	%st(4), %st
	addq	$1, %rax
	fmul	%st(5), %st
	fxch	%st(2)
	fmul	%st(4), %st
	fmul	%st(5), %st
	fxch	%st(1)
	fmul	%st(4), %st
	fmul	%st(5), %st
	fxch	%st(3)
	fmul	%st(4), %st
	fmul	%st(5), %st
	cmpq	%rax, %rdi
	jne	.L142
	fstp	%st(4)
	fstp	%st(4)
	fxch	%st(1)
	fxch	%st(3)
	fxch	%st(1)
	fstpt	-72(%rsp)
	fstpt	-56(%rsp)
	fxch	%st(1)
	fstpt	-40(%rsp)
	fstpt	-24(%rsp)
	jmp	.L109
	.p2align 4,,10
	.p2align 3
.L94:
	fstp	%st(1)
	testq	%rdi, %rdi
	je	.L143
	fldt	-72(%rsp)
	xorl	%eax, %eax
	.p2align 4
	.p2align 4
	.p2align 3
.L104:
	fmul	%st(1), %st
	addq	$1, %rax
	fmul	%st(2), %st
	cmpq	%rax, %rdi
	jne	.L104
	fstp	%st(1)
	fstp	%st(1)
	fstpt	-72(%rsp)
.L135:
	fldt	-72(%rsp)
	ret
	.p2align 4,,10
	.p2align 3
.L134:
	fstp	%st(1)
	testq	%rdi, %rdi
	je	.L144
	fldt	-72(%rsp)
	xorl	%eax, %eax
	fldt	-56(%rsp)
	fldt	-40(%rsp)
	fldt	-24(%rsp)
	fxch	%st(3)
	jmp	.L117
	.p2align 6
	.p2align 4,,10
	.p2align 3
.L145:
	fxch	%st(3)
	fxch	%st(1)
	fxch	%st(2)
.L117:
	addq	$1, %rax
	fdiv	%st(4), %st
	fdiv	%st(5), %st
	fxch	%st(2)
	fdiv	%st(4), %st
	fdiv	%st(5), %st
	fxch	%st(1)
	fdiv	%st(4), %st
	fdiv	%st(5), %st
	fxch	%st(3)
	fdiv	%st(4), %st
	fdiv	%st(5), %st
	cmpq	%rax, %rdi
	jne	.L145
	fstp	%st(4)
	fstp	%st(4)
	fxch	%st(1)
	fxch	%st(3)
	fxch	%st(1)
	fstpt	-72(%rsp)
	fstpt	-56(%rsp)
	fxch	%st(1)
	fstpt	-40(%rsp)
	fstpt	-24(%rsp)
	jmp	.L109
	.p2align 4,,10
	.p2align 3
.L133:
	fstp	%st(1)
	testq	%rdi, %rdi
	je	.L146
	fldt	-72(%rsp)
	xorl	%eax, %eax
	.p2align 4
	.p2align 4
	.p2align 3
.L105:
	addq	$1, %rax
	fdiv	%st(1), %st
	fdiv	%st(2), %st
	cmpq	%rax, %rdi
	jne	.L105
	fstp	%st(1)
	fstp	%st(1)
	fstpt	-72(%rsp)
	jmp	.L135
	.cfi_endproc
.LFE18:
	.size	_Z6kernelIeET_mS0_S0_S0_S0_9Operationb, .-_Z6kernelIeET_mS0_S0_S0_S0_9Operationb
	.section	.rodata.cst4,"aM",@progbits,4
	.align 4
.LC0:
	.long	1048576000
	.align 4
.LC1:
	.long	1056964608
	.align 4
.LC2:
	.long	1061158912
	.section	.rodata.cst8,"aM",@progbits,8
	.align 8
.LC3:
	.long	0
	.long	1070596096
	.align 8
.LC4:
	.long	0
	.long	1071644672
	.align 8
.LC5:
	.long	0
	.long	1072168960
	.ident	"GCC: (HW2 local GCC 16.2.0) 16.2.0"
	.section	.note.GNU-stack,"",@progbits
