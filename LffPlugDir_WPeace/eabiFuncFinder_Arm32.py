# -*- coding:utf-8 -*-
import idc
import idautils
import re

SN_FORCE = 0x800

linux_func = [];
linux_func += ['_WPe_restart_syscall']
linux_func += ['_WPe_exit']
linux_func += ['_WPe_fork']
linux_func += ['_WPe_read']
linux_func += ['_WPe_write']
linux_func += ['_WPe_open']
linux_func += ['_WPe_close']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_creat']
linux_func += ['_WPe_link']
linux_func += ['_WPe_unlink']
linux_func += ['_WPe_execve']
linux_func += ['_WPe_chdir']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_mknod']
linux_func += ['_WPe_chmod']
linux_func += ['_WPe_lchown']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_lseek']
linux_func += ['_WPe_getpid']
linux_func += ['_WPe_mount']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_setuid']
linux_func += ['_WPe_getuid']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_ptrace']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_pause']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_access']
linux_func += ['_WPe_nice']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_sync']
linux_func += ['_WPe_kill']
linux_func += ['_WPe_rename']
linux_func += ['_WPe_mkdir']
linux_func += ['_WPe_rmdir']
linux_func += ['_WPe_dup']
linux_func += ['_WPe_pipe']
linux_func += ['_WPe_times']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_brk']
linux_func += ['_WPe_setgid']
linux_func += ['_WPe_getgid']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_geteuid']
linux_func += ['_WPe_getegid']
linux_func += ['_WPe_acct']
linux_func += ['_WPe_umount2']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_ioctl']
linux_func += ['_WPe_fcntl']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_setpgid']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_umask']
linux_func += ['_WPe_chroot']
linux_func += ['_WPe_ustat']
linux_func += ['_WPe_dup2']
linux_func += ['_WPe_getppid']
linux_func += ['_WPe_getpgrp']
linux_func += ['_WPe_setsid']
linux_func += ['_WPe_sigaction']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_setreuid']
linux_func += ['_WPe_setregid']
linux_func += ['_WPe_sigsuspend']
linux_func += ['_WPe_sigpending']
linux_func += ['_WPe_sethostname']
linux_func += ['_WPe_setrlimit']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_getrusage']
linux_func += ['_WPe_gettimeofday']
linux_func += ['_WPe_settimeofday']
linux_func += ['_WPe_getgroups']
linux_func += ['_WPe_setgroups']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_symlink']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_readlink']
linux_func += ['_WPe_uselib']
linux_func += ['_WPe_swapon']
linux_func += ['_WPe_reboot']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_munmap']
linux_func += ['_WPe_truncate']
linux_func += ['_WPe_ftruncate']
linux_func += ['_WPe_fchmod']
linux_func += ['_WPe_fchown']
linux_func += ['_WPe_getpriority']
linux_func += ['_WPe_setpriority']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_statfs']
linux_func += ['_WPe_fstatfs']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_syslog']
linux_func += ['_WPe_setitimer']
linux_func += ['_WPe_getitimer']
linux_func += ['_WPe_stat']
linux_func += ['_WPe_lstat']
linux_func += ['_WPe_fstat']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_vhangup']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_wait4']
linux_func += ['_WPe_swapoff']
linux_func += ['_WPe_sysinfo']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_fsync']
linux_func += ['_WPe_sigreturn']
linux_func += ['_WPe_clone']
linux_func += ['_WPe_setdomainname']
linux_func += ['_WPe_uname']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_adjtimex']
linux_func += ['_WPe_mprotect']
linux_func += ['_WPe_sigprocmask']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_init_module']
linux_func += ['_WPe_delete_module']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_quotactl']
linux_func += ['_WPe_getpgid']
linux_func += ['_WPe_fchdir']
linux_func += ['_WPe_bdflush']
linux_func += ['_WPe_sysfs']
linux_func += ['_WPe_personality']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_setfsuid']
linux_func += ['_WPe_setfsgid']
linux_func += ['_WPe__llseek']
linux_func += ['_WPe_getdents']
linux_func += ['_WPe__newselect']
linux_func += ['_WPe_flock']
linux_func += ['_WPe_msync']
linux_func += ['_WPe_readv']
linux_func += ['_WPe_writev']
linux_func += ['_WPe_getsid']
linux_func += ['_WPe_fdatasync']
linux_func += ['_WPe__sysctl']
linux_func += ['_WPe_mlock']
linux_func += ['_WPe_munlock']
linux_func += ['_WPe_mlockall']
linux_func += ['_WPe_munlockall']
linux_func += ['_WPe_sched_setparam']
linux_func += ['_WPe_sched_getparam']
linux_func += ['_WPe_sched_setscheduler']
linux_func += ['_WPe_sched_getscheduler']
linux_func += ['_WPe_sched_yield']
linux_func += ['_WPe_sched_get_priority_max']
linux_func += ['_WPe_sched_get_priority_min']
linux_func += ['_WPe_sched_rr_get_interval']
linux_func += ['_WPe_nanosleep']
linux_func += ['_WPe_mremap']
linux_func += ['_WPe_setresuid']
linux_func += ['_WPe_getresuid']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_poll']
linux_func += ['_WPe_nfsservctl']
linux_func += ['_WPe_setresgid']
linux_func += ['_WPe_getresgid']
linux_func += ['_WPe_prctl']
linux_func += ['_WPe_rt_sigreturn']
linux_func += ['_WPe_rt_sigaction']
linux_func += ['_WPe_rt_sigprocmask']
linux_func += ['_WPe_rt_sigpending']
linux_func += ['_WPe_rt_sigtimedwait']
linux_func += ['_WPe_rt_sigqueueinfo']
linux_func += ['_WPe_rt_sigsuspend']
linux_func += ['_WPe_pread64']
linux_func += ['_WPe_pwrite64']
linux_func += ['_WPe_chown']
linux_func += ['_WPe_getcwd']
linux_func += ['_WPe_capget']
linux_func += ['_WPe_capset']
linux_func += ['_WPe_sigaltstack']
linux_func += ['_WPe_sendfile']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_vfork']
linux_func += ['_WPe_ugetrlimit']
linux_func += ['_WPe_mmap2']
linux_func += ['_WPe_truncate64']
linux_func += ['_WPe_ftruncate64']
linux_func += ['_WPe_stat64']
linux_func += ['_WPe_lstat64']
linux_func += ['_WPe_fstat64']
linux_func += ['_WPe_lchown32']
linux_func += ['_WPe_getuid32']
linux_func += ['_WPe_getgid32']
linux_func += ['_WPe_geteuid32']
linux_func += ['_WPe_getegid32']
linux_func += ['_WPe_setreuid32']
linux_func += ['_WPe_setregid32']
linux_func += ['_WPe_getgroups32']
linux_func += ['_WPe_setgroups32']
linux_func += ['_WPe_fchown32']
linux_func += ['_WPe_setresuid32']
linux_func += ['_WPe_getresuid32']
linux_func += ['_WPe_setresgid32']
linux_func += ['_WPe_getresgid32']
linux_func += ['_WPe_chown32']
linux_func += ['_WPe_setuid32']
linux_func += ['_WPe_setgid32']
linux_func += ['_WPe_setfsuid32']
linux_func += ['_WPe_setfsgid32']
linux_func += ['_WPe_getdents64']
linux_func += ['_WPe_pivot_root']
linux_func += ['_WPe_mincore']
linux_func += ['_WPe_madvise']
linux_func += ['_WPe_fcntl64']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_gettid']
linux_func += ['_WPe_readahead']
linux_func += ['_WPe_setxattr']
linux_func += ['_WPe_lsetxattr']
linux_func += ['_WPe_fsetxattr']
linux_func += ['_WPe_getxattr']
linux_func += ['_WPe_lgetxattr']
linux_func += ['_WPe_fgetxattr']
linux_func += ['_WPe_listxattr']
linux_func += ['_WPe_llistxattr']
linux_func += ['_WPe_flistxattr']
linux_func += ['_WPe_removexattr']
linux_func += ['_WPe_lremovexattr']
linux_func += ['_WPe_fremovexattr']
linux_func += ['_WPe_tkill']
linux_func += ['_WPe_sendfile64']
linux_func += ['_WPe_futex']
linux_func += ['_WPe_sched_setaffinity']
linux_func += ['_WPe_sched_getaffinity']
linux_func += ['_WPe_io_setup']
linux_func += ['_WPe_io_destroy']
linux_func += ['_WPe_io_getevents']
linux_func += ['_WPe_io_submit']
linux_func += ['_WPe_io_cancel']
linux_func += ['_WPe_exit_group']
linux_func += ['_WPe_lookup_dcookie']
linux_func += ['_WPe_epoll_create']
linux_func += ['_WPe_epoll_ctl']
linux_func += ['_WPe_epoll_wait']
linux_func += ['_WPe_remap_file_pages']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_NotImplemented']
linux_func += ['_WPe_set_tid_address']
linux_func += ['_WPe_timer_create']
linux_func += ['_WPe_timer_settime']
linux_func += ['_WPe_timer_gettime']
linux_func += ['_WPe_timer_getoverrun']
linux_func += ['_WPe_timer_delete']
linux_func += ['_WPe_clock_settime']
linux_func += ['_WPe_clock_gettime']
linux_func += ['_WPe_clock_getres']
linux_func += ['_WPe_clock_nanosleep']
linux_func += ['_WPe_statfs64']
linux_func += ['_WPe_fstatfs64']
linux_func += ['_WPe_tgkill']
linux_func += ['_WPe_utimes']
linux_func += ['_WPe_arm_fadvise64_64']
linux_func += ['_WPe_pciconfig_iobase']
linux_func += ['_WPe_pciconfig_read']
linux_func += ['_WPe_pciconfig_write']
linux_func += ['_WPe_mq_open']
linux_func += ['_WPe_mq_unlink']
linux_func += ['_WPe_mq_timedsend']
linux_func += ['_WPe_mq_timedreceive']
linux_func += ['_WPe_mq_notify']
linux_func += ['_WPe_mq_getsetattr']
linux_func += ['_WPe_waitid']
linux_func += ['_WPe_socket']
linux_func += ['_WPe_bind']
linux_func += ['_WPe_connect']
linux_func += ['_WPe_listen']
linux_func += ['_WPe_accept']
linux_func += ['_WPe_getsockname']
linux_func += ['_WPe_getpeername']
linux_func += ['_WPe_socketpair']
linux_func += ['_WPe_send']
linux_func += ['_WPe_sendto']
linux_func += ['_WPe_recv']
linux_func += ['_WPe_recvfrom']
linux_func += ['_WPe_shutdown']
linux_func += ['_WPe_setsockopt']
linux_func += ['_WPe_getsockopt']
linux_func += ['_WPe_sendmsg']
linux_func += ['_WPe_recvmsg']
linux_func += ['_WPe_semop']
linux_func += ['_WPe_semget']
linux_func += ['_WPe_semctl']
linux_func += ['_WPe_msgsnd']
linux_func += ['_WPe_msgrcv']
linux_func += ['_WPe_msgget']
linux_func += ['_WPe_msgctl']
linux_func += ['_WPe_shmat']
linux_func += ['_WPe_shmdt']
linux_func += ['_WPe_shmget']
linux_func += ['_WPe_shmctl']
linux_func += ['_WPe_add_key']
linux_func += ['_WPe_request_key']
linux_func += ['_WPe_keyctl']
linux_func += ['_WPe_semtimedop']
linux_func += ['_WPe_vserver']
linux_func += ['_WPe_ioprio_set']
linux_func += ['_WPe_ioprio_get']
linux_func += ['_WPe_inotify_init']
linux_func += ['_WPe_inotify_add_watch']
linux_func += ['_WPe_inotify_rm_watch']
linux_func += ['_WPe_mbind']
linux_func += ['_WPe_get_mempolicy']
linux_func += ['_WPe_set_mempolicy']
linux_func += ['_WPe_openat']
linux_func += ['_WPe_mkdirat']
linux_func += ['_WPe_mknodat']
linux_func += ['_WPe_fchownat']
linux_func += ['_WPe_futimesat']
linux_func += ['_WPe_fstatat64']
linux_func += ['_WPe_unlinkat']
linux_func += ['_WPe_renameat']
linux_func += ['_WPe_linkat']
linux_func += ['_WPe_symlinkat']
linux_func += ['_WPe_readlinkat']
linux_func += ['_WPe_fchmodat']
linux_func += ['_WPe_faccessat']
linux_func += ['_WPe_pselect6']
linux_func += ['_WPe_ppoll']
linux_func += ['_WPe_unshare']
linux_func += ['_WPe_set_robust_list']
linux_func += ['_WPe_get_robust_list']
linux_func += ['_WPe_splice']
linux_func += ['_WPe_arm_sync_file_range']
linux_func += ['_WPe_tee']
linux_func += ['_WPe_vmsplice']
linux_func += ['_WPe_move_pages']
linux_func += ['_WPe_getcpu']
linux_func += ['_WPe_epoll_pwait']
linux_func += ['_WPe_kexec_load']
linux_func += ['_WPe_utimensat']
linux_func += ['_WPe_signalfd']
linux_func += ['_WPe_timerfd_create']
linux_func += ['_WPe_eventfd']
linux_func += ['_WPe_fallocate']
linux_func += ['_WPe_timerfd_settime']
linux_func += ['_WPe_timerfd_gettime']
linux_func += ['_WPe_signalfd4']
linux_func += ['_WPe_eventfd2']
linux_func += ['_WPe_epoll_create1']
linux_func += ['_WPe_dup3']
linux_func += ['_WPe_pipe2']
linux_func += ['_WPe_inotify_init1']
linux_func += ['_WPe_preadv']
linux_func += ['_WPe_pwritev']
linux_func += ['_WPe_rt_tgsigqueueinfo']
linux_func += ['_WPe_perf_event_open']
linux_func += ['_WPe_recvmmsg']
linux_func += ['_WPe_accept4']
linux_func += ['_WPe_fanotify_init']
linux_func += ['_WPe_fanotify_mark']
linux_func += ['_WPe_prlimit64']
linux_func += ['_WPe_name_to_handle_at']
linux_func += ['_WPe_open_by_handle_at']
linux_func += ['_WPe_clock_adjtime']
linux_func += ['_WPe_syncfs']
linux_func += ['_WPe_sendmmsg']
linux_func += ['_WPe_setns']
linux_func += ['_WPe_process_vm_readv']
linux_func += ['_WPe_process_vm_writev']
linux_func += ['_WPe_kcmp']
linux_func += ['_WPe_finit_module']
linux_func += ['_WPe_sched_setattr']
linux_func += ['_WPe_sched_getattr']
linux_func += ['_WPe_renameat2']
linux_func += ['_WPe_seccomp']
linux_func += ['_WPe_getrandom']
linux_func += ['_WPe_memfd_create']
linux_func += ['_WPe_bpf']
linux_func += ['_WPe_execveat']
linux_func += ['_WPe_userfaultfd']
linux_func += ['_WPe_membarrier']
linux_func += ['_WPe_mlock2']
linux_func += ['_WPe_copy_file_range']
linux_func += ['_WPe_preadv2']
linux_func += ['_WPe_pwritev2']
linux_func += ['_WPe_pkey_mprotect']
linux_func += ['_WPe_pkey_alloc']
linux_func += ['_WPe_pkey_free']
linux_func += ['_WPe_statx']

def ReName():
    sum = 0;
    for func in idautils.Functions():
        dism_addr = list(idautils.FuncItems(func));
        for line in dism_addr:
            op = idc.print_insn_mnem(line);
            if op == 'SVC':
                lastline = idc.prev_head(line)
                op_last = idc.print_insn_mnem(lastline);
                if op_last == 'MOV' and idc.get_operand_value(lastline, 0) == 7:
                    callnumber = idc.get_operand_value(lastline, 1)
                    address = idc.get_name_ea_simple(idc.get_func_name(line));
                    funcName = idc.get_func_name(address)
                    if funcName != "start" and funcName != "_WPe_fork":
                        if "clone" in funcName and callnumber == 0xF0:
                            idc.set_name(address, "_WPe_fork", SN_FORCE);
                            print("_WPe_fork")
                        else:
                            idc.set_name(address, linux_func[callnumber], SN_FORCE);
                            print(linux_func[callnumber])
                        sum += 1
                elif op_last == 'LDR' and idc.get_operand_value(lastline, 0) == 7:
                    op = idc.GetDisasm(lastline);
                    op = re.findall('=.*$', op);
                    if op:
                        try:
                            opString = ''.join(op[0].replace('=',''));
                            callnumber = int(opString, 16);
                            address = idc.get_name_ea_simple(idc.get_func_name(line));
                            funcName = idc.get_func_name(address)
                            if funcName != "start" and funcName != "_WPe_fork":
                                if "clone" in funcName and callnumber == 0xF0:
                                    idc.set_name(address, "_WPe_fork", SN_FORCE);
                                    print("_WPe_fork")
                                else:
                                    idc.set_name(address, linux_func[callnumber], SN_FORCE);
                                    print(linux_func[callnumber])
                                sum += 1
                        except Exception as e:
                            pass
    print("eabiFuncFinder_Arm32 finished！总共重命名%d个函数" %sum);

def main():
    ReName();

if __name__ == "__main__":
    main();