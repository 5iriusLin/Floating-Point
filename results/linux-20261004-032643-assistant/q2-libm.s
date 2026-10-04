	.file	"sqrt_paths.cpp"
	.text
	.p2align 4
	.globl	_Z9sqrt_pathf
	.type	_Z9sqrt_pathf, @function
_Z9sqrt_pathf:
.LFB1273:
	.cfi_startproc
	movq	$sqrtf, -16(%rsp)
	jmp	*-16(%rsp)
	.cfi_endproc
.LFE1273:
	.size	_Z9sqrt_pathf, .-_Z9sqrt_pathf
	.p2align 4
	.globl	_Z9sqrt_pathd
	.type	_Z9sqrt_pathd, @function
_Z9sqrt_pathd:
.LFB1274:
	.cfi_startproc
	movq	$sqrt, -16(%rsp)
	jmp	*-16(%rsp)
	.cfi_endproc
.LFE1274:
	.size	_Z9sqrt_pathd, .-_Z9sqrt_pathd
	.p2align 4
	.globl	_Z9sqrt_pathe
	.type	_Z9sqrt_pathe, @function
_Z9sqrt_pathe:
.LFB1275:
	.cfi_startproc
	movq	$sqrtl, -16(%rsp)
	jmp	*-16(%rsp)
	.cfi_endproc
.LFE1275:
	.size	_Z9sqrt_pathe, .-_Z9sqrt_pathe
	.ident	"GCC: (HW2 local GCC 16.2.0) 16.2.0"
	.section	.note.GNU-stack,"",@progbits
