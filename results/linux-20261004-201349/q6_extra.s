	.file	"operations.cpp"
	.text
	.p2align 4
	.globl	_Z16multiply_runtimeff
	.type	_Z16multiply_runtimeff, @function
_Z16multiply_runtimeff:
.LFB0:
	.cfi_startproc
	mulss	%xmm1, %xmm0
	ret
	.cfi_endproc
.LFE0:
	.size	_Z16multiply_runtimeff, .-_Z16multiply_runtimeff
	.p2align 4
	.globl	_Z16multiply_runtimedd
	.type	_Z16multiply_runtimedd, @function
_Z16multiply_runtimedd:
.LFB1:
	.cfi_startproc
	mulsd	%xmm1, %xmm0
	ret
	.cfi_endproc
.LFE1:
	.size	_Z16multiply_runtimedd, .-_Z16multiply_runtimedd
	.p2align 4
	.globl	_Z16multiply_runtimeee
	.type	_Z16multiply_runtimeee, @function
_Z16multiply_runtimeee:
.LFB2:
	.cfi_startproc
	fldt	8(%rsp)
	fldt	24(%rsp)
	fmulp	%st, %st(1)
	ret
	.cfi_endproc
.LFE2:
	.size	_Z16multiply_runtimeee, .-_Z16multiply_runtimeee
	.ident	"GCC: (HW2 local GCC 16.2.0) 16.2.0"
	.section	.note.GNU-stack,"",@progbits
