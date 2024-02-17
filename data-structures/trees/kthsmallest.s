	.section	__TEXT,__text,regular,pure_instructions
	.build_version macos, 12, 0	sdk_version 12, 1
	.globl	_createTreeNode                 ## -- Begin function createTreeNode
	.p2align	4, 0x90
_createTreeNode:                        ## @createTreeNode
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	movl	%edi, -4(%rbp)
	movl	$24, %edi
	callq	_malloc
	movq	%rax, -16(%rbp)
	movl	-4(%rbp), %ecx
	movq	-16(%rbp), %rax
	movl	%ecx, (%rax)
	movq	-16(%rbp), %rax
	movq	$0, 8(%rax)
	movq	-16(%rbp), %rax
	movq	$0, 16(%rax)
	movq	-16(%rbp), %rax
	addq	$16, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_inorderTraversal               ## -- Begin function inorderTraversal
	.p2align	4, 0x90
_inorderTraversal:                      ## @inorderTraversal
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movq	%rdi, -8(%rbp)
	movq	%rsi, -16(%rbp)
	movq	%rdx, -24(%rbp)
	cmpq	$0, -8(%rbp)
	jne	LBB1_2
## %bb.1:
	jmp	LBB1_3
LBB1_2:
	movq	-8(%rbp), %rax
	movq	8(%rax), %rdi
	movq	-16(%rbp), %rsi
	movq	-24(%rbp), %rdx
	callq	_inorderTraversal
	movq	-8(%rbp), %rax
	movl	(%rax), %edx
	movq	-16(%rbp), %rax
	movq	-24(%rbp), %rsi
	movl	(%rsi), %ecx
	movl	%ecx, %edi
	addl	$1, %edi
	movl	%edi, (%rsi)
	movslq	%ecx, %rcx
	movl	%edx, (%rax,%rcx,4)
	movq	-8(%rbp), %rax
	movq	16(%rax), %rdi
	movq	-16(%rbp), %rsi
	movq	-24(%rbp), %rdx
	callq	_inorderTraversal
LBB1_3:
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_kthSmallest                    ## -- Begin function kthSmallest
	.p2align	4, 0x90
_kthSmallest:                           ## @kthSmallest
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$32, %rsp
	movq	%rdi, -8(%rbp)
	movl	%esi, -12(%rbp)
	movl	$400, %edi                      ## imm = 0x190
	callq	_malloc
	movq	%rax, -24(%rbp)
	movl	$0, -28(%rbp)
	movq	-8(%rbp), %rdi
	movq	-24(%rbp), %rsi
	leaq	-28(%rbp), %rdx
	callq	_inorderTraversal
	movq	-24(%rbp), %rax
	movl	-12(%rbp), %ecx
	subl	$1, %ecx
	movslq	%ecx, %rcx
	movl	(%rax,%rcx,4), %eax
	movl	%eax, -32(%rbp)
	movq	-24(%rbp), %rdi
	callq	_free
	movl	-32(%rbp), %eax
	addq	$32, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.globl	_main                           ## -- Begin function main
	.p2align	4, 0x90
_main:                                  ## @main
	.cfi_startproc
## %bb.0:
	pushq	%rbp
	.cfi_def_cfa_offset 16
	.cfi_offset %rbp, -16
	movq	%rsp, %rbp
	.cfi_def_cfa_register %rbp
	subq	$16, %rsp
	movl	$0, -4(%rbp)
	movl	$20, %edi
	callq	_createTreeNode
	movq	%rax, -16(%rbp)
	movl	$10, %edi
	callq	_createTreeNode
	movq	%rax, %rcx
	movq	-16(%rbp), %rax
	movq	%rcx, 8(%rax)
	movl	$9, %edi
	callq	_createTreeNode
	movq	%rax, %rcx
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rcx, 8(%rax)
	movl	$11, %edi
	callq	_createTreeNode
	movq	%rax, %rcx
	movq	-16(%rbp), %rax
	movq	8(%rax), %rax
	movq	%rcx, 16(%rax)
	movl	$30, %edi
	callq	_createTreeNode
	movq	%rax, %rcx
	movq	-16(%rbp), %rax
	movq	%rcx, 16(%rax)
	movl	$22, %edi
	callq	_createTreeNode
	movq	%rax, %rcx
	movq	-16(%rbp), %rax
	movq	16(%rax), %rax
	movq	%rcx, 8(%rax)
	movl	$40, %edi
	callq	_createTreeNode
	movq	%rax, %rcx
	movq	-16(%rbp), %rax
	movq	16(%rax), %rax
	movq	%rcx, 16(%rax)
	movq	-16(%rbp), %rdi
	movl	$3, %esi
	callq	_kthSmallest
	movl	%eax, %esi
	leaq	L_.str(%rip), %rdi
	movb	$0, %al
	callq	_printf
	xorl	%eax, %eax
	addq	$16, %rsp
	popq	%rbp
	retq
	.cfi_endproc
                                        ## -- End function
	.section	__TEXT,__cstring,cstring_literals
L_.str:                                 ## @.str
	.asciz	"The 3rd smallest element is: %d\n"

.subsections_via_symbols
