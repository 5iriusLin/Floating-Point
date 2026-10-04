	.file	"operations.cpp"
	.text
	.p2align 4
	.globl	_Z10add_doubledd
	.type	_Z10add_doubledd, @function
_Z10add_doubledd:
.LFB0:
	.cfi_startproc
	addsd	%xmm1, %xmm0
	ret
	.cfi_endproc
.LFE0:
	.size	_Z10add_doubledd, .-_Z10add_doubledd
	.p2align 4
	.globl	_Z21increment_long_doubleee
	.type	_Z21increment_long_doubleee, @function
_Z21increment_long_doubleee:
.LFB1:
	.cfi_startproc
	fldt	8(%rsp)
	fldt	24(%rsp)
	fadd	%st(1), %st
	fstpt	-24(%rsp)
	fldt	-24(%rsp)
	fsubp	%st, %st(1)
	ret
	.cfi_endproc
.LFE1:
	.size	_Z21increment_long_doubleee, .-_Z21increment_long_doubleee
	.ident	"GCC: (HW2 local GCC 16.2.0) 16.2.0"
	.section	.note.GNU-stack,"",@progbits
