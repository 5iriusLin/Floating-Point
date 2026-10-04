	.arch armv8.5-a
	.build_version macos,  27, 0
	.text
	.align	2
	.p2align 5,,15
	.globl __Z10add_doubledd
__Z10add_doubledd:
LFB0:
	fadd	d0, d0, d1
	ret
LFE0:
	.align	2
	.p2align 5,,15
	.globl __Z21increment_long_doubleee
__Z21increment_long_doubleee:
LFB1:
	fadd	d1, d0, d1
	sub	sp, sp, #16
LCFI0:
	str	d1, [sp, 8]
	ldr	d31, [sp, 8]
	add	sp, sp, 16
LCFI1:
	fsub	d0, d31, d0
	ret
LFE1:
	.section __TEXT,__eh_frame,coalesced,no_toc+strip_static_syms+live_support
EH_frame1:
	.set L$set$0,LECIE1-LSCIE1
	.long L$set$0
LSCIE1:
	.long	0
	.byte	0x3
	.ascii "zR\0"
	.uleb128 0x1
	.sleb128 -8
	.uleb128 0x1e
	.uleb128 0x1
	.byte	0x10
	.byte	0xc
	.uleb128 0x1f
	.uleb128 0
	.align	3
LECIE1:
LSFDE1:
	.set L$set$1,LEFDE1-LASFDE1
	.long L$set$1
LASFDE1:
	.long	LASFDE1-EH_frame1
	.quad	LFB0-.
	.set L$set$2,LFE0-LFB0
	.quad L$set$2
	.uleb128 0
	.align	3
LEFDE1:
LSFDE3:
	.set L$set$3,LEFDE3-LASFDE3
	.long L$set$3
LASFDE3:
	.long	LASFDE3-EH_frame1
	.quad	LFB1-.
	.set L$set$4,LFE1-LFB1
	.quad L$set$4
	.uleb128 0
	.byte	0x4
	.set L$set$5,LCFI0-LFB1
	.long L$set$5
	.byte	0xe
	.uleb128 0x10
	.byte	0x4
	.set L$set$6,LCFI1-LCFI0
	.long L$set$6
	.byte	0xe
	.uleb128 0
	.align	3
LEFDE3:
	.ident	"GCC: (Homebrew GCC 16.2.0) 16.2.0"
	.subsections_via_symbols
