	.file	"operations.cpp"
	.text
	.p2align 4
	.globl	_Z12left_groupedddd
	.type	_Z12left_groupedddd, @function
_Z12left_groupedddd:
.LFB3:
	.cfi_startproc
	addsd	%xmm1, %xmm0
	addsd	%xmm2, %xmm0
	ret
	.cfi_endproc
.LFE3:
	.size	_Z12left_groupedddd, .-_Z12left_groupedddd
	.p2align 4
	.globl	_Z13right_groupedddd
	.type	_Z13right_groupedddd, @function
_Z13right_groupedddd:
.LFB4:
	.cfi_startproc
	addsd	%xmm2, %xmm1
	addsd	%xmm1, %xmm0
	ret
	.cfi_endproc
.LFE4:
	.size	_Z13right_groupedddd, .-_Z13right_groupedddd
	.p2align 4
	.globl	_Z15self_inequalityd
	.type	_Z15self_inequalityd, @function
_Z15self_inequalityd:
.LFB5:
	.cfi_startproc
	ucomisd	%xmm0, %xmm0
	setp	%al
	ret
	.cfi_endproc
.LFE5:
	.size	_Z15self_inequalityd, .-_Z15self_inequalityd
	.ident	"GCC: (HW2 local GCC 16.2.0) 16.2.0"
	.section	.note.GNU-stack,"",@progbits
