# -*- coding:utf-8 -*-

import idc
import idautils
import re
import idaapi

SN_FORCE = 0x800

mips_func = {}
__NR_Linux = 4000
mips_func.update({__NR_Linux+0: "_WPe_syscall"})
mips_func.update({__NR_Linux+1: "_WPe_exit"})
mips_func.update({__NR_Linux+2: "_WPe_fork"})
mips_func.update({__NR_Linux+3: "_WPe_read"})
mips_func.update({__NR_Linux+4: "_WPe_write"})
mips_func.update({__NR_Linux+5: "_WPe_open"})
mips_func.update({__NR_Linux+6: "_WPe_close"})
mips_func.update({__NR_Linux+7: "_WPe_waitpid"})
mips_func.update({__NR_Linux+8: "_WPe_creat"})
mips_func.update({__NR_Linux+9: "_WPe_link"})
mips_func.update({__NR_Linux+10: "_WPe_unlink"})
mips_func.update({__NR_Linux+11: "_WPe_execve"})
mips_func.update({__NR_Linux+12: "_WPe_chdir"})
mips_func.update({__NR_Linux+13: "_WPe_time"})
mips_func.update({__NR_Linux+14: "_WPe_mknod"})
mips_func.update({__NR_Linux+15: "_WPe_chmod"})
mips_func.update({__NR_Linux+16: "_WPe_lchown"})
mips_func.update({__NR_Linux+17: "_WPe_break"})
mips_func.update({__NR_Linux+18: "_WPe_unused18"})
mips_func.update({__NR_Linux+19: "_WPe_lseek"})
mips_func.update({__NR_Linux+20: "_WPe_getpid"})
mips_func.update({__NR_Linux+21: "_WPe_mount"})
mips_func.update({__NR_Linux+22: "_WPe_umount"})
mips_func.update({__NR_Linux+23: "_WPe_setuid"})
mips_func.update({__NR_Linux+24: "_WPe_getuid"})
mips_func.update({__NR_Linux+25: "_WPe_stime"})
mips_func.update({__NR_Linux+26: "_WPe_ptrace"})
mips_func.update({__NR_Linux+27: "_WPe_alarm"})
mips_func.update({__NR_Linux+28: "_WPe_unused28"})
mips_func.update({__NR_Linux+29: "_WPe_pause"})
mips_func.update({__NR_Linux+30: "_WPe_utime"})
mips_func.update({__NR_Linux+31: "_WPe_stty"})
mips_func.update({__NR_Linux+32: "_WPe_gtty"})
mips_func.update({__NR_Linux+33: "_WPe_access"})
mips_func.update({__NR_Linux+34: "_WPe_nice"})
mips_func.update({__NR_Linux+35: "_WPe_ftime"})
mips_func.update({__NR_Linux+36: "_WPe_sync"})
mips_func.update({__NR_Linux+37: "_WPe_kill"})
mips_func.update({__NR_Linux+38: "_WPe_rename"})
mips_func.update({__NR_Linux+39: "_WPe_mkdir"})
mips_func.update({__NR_Linux+40: "_WPe_rmdir"})
mips_func.update({__NR_Linux+41: "_WPe_dup"})
mips_func.update({__NR_Linux+42: "_WPe_pipe"})
mips_func.update({__NR_Linux+43: "_WPe_times"})
mips_func.update({__NR_Linux+44: "_WPe_prof"})
mips_func.update({__NR_Linux+45: "_WPe_brk"})
mips_func.update({__NR_Linux+46: "_WPe_setgid"})
mips_func.update({__NR_Linux+47: "_WPe_getgid"})
mips_func.update({__NR_Linux+48: "_WPe_signal"})
mips_func.update({__NR_Linux+49: "_WPe_geteuid"})
mips_func.update({__NR_Linux+50: "_WPe_getegid"})
mips_func.update({__NR_Linux+51: "_WPe_acct"})
mips_func.update({__NR_Linux+52: "_WPe_umount2"})
mips_func.update({__NR_Linux+53: "_WPe_lock"})
mips_func.update({__NR_Linux+54: "_WPe_ioctl"})
mips_func.update({__NR_Linux+55: "_WPe_fcntl"})
mips_func.update({__NR_Linux+56: "_WPe_mpx"})
mips_func.update({__NR_Linux+57: "_WPe_setpgid"})
mips_func.update({__NR_Linux+58: "_WPe_ulimit"})
mips_func.update({__NR_Linux+59: "_WPe_unused59"})
mips_func.update({__NR_Linux+60: "_WPe_umask"})
mips_func.update({__NR_Linux+61: "_WPe_chroot"})
mips_func.update({__NR_Linux+62: "_WPe_ustat"})
mips_func.update({__NR_Linux+63: "_WPe_dup2"})
mips_func.update({__NR_Linux+64: "_WPe_getppid"})
mips_func.update({__NR_Linux+65: "_WPe_getpgrp"})
mips_func.update({__NR_Linux+66: "_WPe_setsid"})
mips_func.update({__NR_Linux+67: "_WPe_sigaction"})
mips_func.update({__NR_Linux+68: "_WPe_sgetmask"})
mips_func.update({__NR_Linux+69: "_WPe_ssetmask"})
mips_func.update({__NR_Linux+70: "_WPe_setreuid"})
mips_func.update({__NR_Linux+71: "_WPe_setregid"})
mips_func.update({__NR_Linux+72: "_WPe_sigsuspend"})
mips_func.update({__NR_Linux+73: "_WPe_sigpending"})
mips_func.update({__NR_Linux+74: "_WPe_sethostname"})
mips_func.update({__NR_Linux+75: "_WPe_setrlimit"})
mips_func.update({__NR_Linux+76: "_WPe_getrlimit"})
mips_func.update({__NR_Linux+77: "_WPe_getrusage"})
mips_func.update({__NR_Linux+78: "_WPe_gettimeofday"})
mips_func.update({__NR_Linux+79: "_WPe_settimeofday"})
mips_func.update({__NR_Linux+80: "_WPe_getgroups"})
mips_func.update({__NR_Linux+81: "_WPe_setgroups"})
mips_func.update({__NR_Linux+82: "_WPe_reserved82"})
mips_func.update({__NR_Linux+83: "_WPe_symlink"})
mips_func.update({__NR_Linux+84: "_WPe_unused84"})
mips_func.update({__NR_Linux+85: "_WPe_readlink"})
mips_func.update({__NR_Linux+86: "_WPe_uselib"})
mips_func.update({__NR_Linux+87: "_WPe_swapon"})
mips_func.update({__NR_Linux+88: "_WPe_reboot"})
mips_func.update({__NR_Linux+89: "_WPe_readdir"})
mips_func.update({__NR_Linux+90: "_WPe_mmap"})
mips_func.update({__NR_Linux+91: "_WPe_munmap"})
mips_func.update({__NR_Linux+92: "_WPe_truncate"})
mips_func.update({__NR_Linux+93: "_WPe_ftruncate"})
mips_func.update({__NR_Linux+94: "_WPe_fchmod"})
mips_func.update({__NR_Linux+95: "_WPe_fchown"})
mips_func.update({__NR_Linux+96: "_WPe_getpriority"})
mips_func.update({__NR_Linux+97: "_WPe_setpriority"})
mips_func.update({__NR_Linux+98: "_WPe_profil"})
mips_func.update({__NR_Linux+99: "_WPe_statfs"})
mips_func.update({__NR_Linux+100: "_WPe_fstatfs"})
mips_func.update({__NR_Linux+101: "_WPe_ioperm"})
mips_func.update({__NR_Linux+102: "_WPe_socketcall"})
mips_func.update({__NR_Linux+103: "_WPe_syslog"})
mips_func.update({__NR_Linux+104: "_WPe_setitimer"})
mips_func.update({__NR_Linux+105: "_WPe_getitimer"})
mips_func.update({__NR_Linux+106: "_WPe_stat"})
mips_func.update({__NR_Linux+107: "_WPe_lstat"})
mips_func.update({__NR_Linux+108: "_WPe_fstat"})
mips_func.update({__NR_Linux+109: "_WPe_unused109"})
mips_func.update({__NR_Linux+110: "_WPe_iopl"})
mips_func.update({__NR_Linux+111: "_WPe_vhangup"})
mips_func.update({__NR_Linux+112: "_WPe_idle"})
mips_func.update({__NR_Linux+113: "_WPe_vm86"})
mips_func.update({__NR_Linux+114: "_WPe_wait4"})
mips_func.update({__NR_Linux+115: "_WPe_swapoff"})
mips_func.update({__NR_Linux+116: "_WPe_sysinfo"})
mips_func.update({__NR_Linux+117: "_WPe_ipc"})
mips_func.update({__NR_Linux+118: "_WPe_fsync"})
mips_func.update({__NR_Linux+119: "_WPe_sigreturn"})
mips_func.update({__NR_Linux+120: "_WPe_clone"})
mips_func.update({__NR_Linux+121: "_WPe_setdomainname"})
mips_func.update({__NR_Linux+122: "_WPe_uname"})
mips_func.update({__NR_Linux+123: "_WPe_modify_ldt"})
mips_func.update({__NR_Linux+124: "_WPe_adjtimex"})
mips_func.update({__NR_Linux+125: "_WPe_mprotect"})
mips_func.update({__NR_Linux+126: "_WPe_sigprocmask"})
mips_func.update({__NR_Linux+127: "_WPe_create_module"})
mips_func.update({__NR_Linux+128: "_WPe_init_module"})
mips_func.update({__NR_Linux+129: "_WPe_delete_module"})
mips_func.update({__NR_Linux+130: "_WPe_get_kernel_syms"})
mips_func.update({__NR_Linux+131: "_WPe_quotactl"})
mips_func.update({__NR_Linux+132: "_WPe_getpgid"})
mips_func.update({__NR_Linux+133: "_WPe_fchdir"})
mips_func.update({__NR_Linux+134: "_WPe_bdflush"})
mips_func.update({__NR_Linux+135: "_WPe_sysfs"})
mips_func.update({__NR_Linux+136: "_WPe_personality"})
mips_func.update({__NR_Linux+137: "_WPe_afs_syscall"})
mips_func.update({__NR_Linux+138: "_WPe_setfsuid"})
mips_func.update({__NR_Linux+139: "_WPe_setfsgid"})
mips_func.update({__NR_Linux+140: "_WPe__llseek"})
mips_func.update({__NR_Linux+141: "_WPe_getdents"})
mips_func.update({__NR_Linux+142: "_WPe__newselect"})
mips_func.update({__NR_Linux+143: "_WPe_flock"})
mips_func.update({__NR_Linux+144: "_WPe_msync"})
mips_func.update({__NR_Linux+145: "_WPe_readv"})
mips_func.update({__NR_Linux+146: "_WPe_writev"})
mips_func.update({__NR_Linux+147: "_WPe_cacheflush"})
mips_func.update({__NR_Linux+148: "_WPe_cachectl"})
mips_func.update({__NR_Linux+149: "_WPe_sysmips"})
mips_func.update({__NR_Linux+150: "_WPe_unused150"})
mips_func.update({__NR_Linux+151: "_WPe_getsid"})
mips_func.update({__NR_Linux+152: "_WPe_fdatasync"})
mips_func.update({__NR_Linux+153: "_WPe__sysctl"})
mips_func.update({__NR_Linux+154: "_WPe_mlock"})
mips_func.update({__NR_Linux+155: "_WPe_munlock"})
mips_func.update({__NR_Linux+156: "_WPe_mlockall"})
mips_func.update({__NR_Linux+157: "_WPe_munlockall"})
mips_func.update({__NR_Linux+158: "_WPe_sched_setparam"})
mips_func.update({__NR_Linux+159: "_WPe_sched_getparam"})
mips_func.update({__NR_Linux+160: "_WPe_sched_setscheduler"})
mips_func.update({__NR_Linux+161: "_WPe_sched_getscheduler"})
mips_func.update({__NR_Linux+162: "_WPe_sched_yield"})
mips_func.update({__NR_Linux+163: "_WPe_sched_get_priority_max"})
mips_func.update({__NR_Linux+164: "_WPe_sched_get_priority_min"})
mips_func.update({__NR_Linux+165: "_WPe_sched_rr_get_interval"})
mips_func.update({__NR_Linux+166: "_WPe_nanosleep"})
mips_func.update({__NR_Linux+167: "_WPe_mremap"})
mips_func.update({__NR_Linux+168: "_WPe_accept"})
mips_func.update({__NR_Linux+169: "_WPe_bind"})
mips_func.update({__NR_Linux+170: "_WPe_connect"})
mips_func.update({__NR_Linux+171: "_WPe_getpeername"})
mips_func.update({__NR_Linux+172: "_WPe_getsockname"})
mips_func.update({__NR_Linux+173: "_WPe_getsockopt"})
mips_func.update({__NR_Linux+174: "_WPe_listen"})
mips_func.update({__NR_Linux+175: "_WPe_recv"})
mips_func.update({__NR_Linux+176: "_WPe_recvfrom"})
mips_func.update({__NR_Linux+177: "_WPe_recvmsg"})
mips_func.update({__NR_Linux+178: "_WPe_send"})
mips_func.update({__NR_Linux+179: "_WPe_sendmsg"})
mips_func.update({__NR_Linux+180: "_WPe_sendto"})
mips_func.update({__NR_Linux+181: "_WPe_setsockopt"})
mips_func.update({__NR_Linux+182: "_WPe_shutdown"})
mips_func.update({__NR_Linux+183: "_WPe_socket"})
mips_func.update({__NR_Linux+184: "_WPe_socketpair"})
mips_func.update({__NR_Linux+185: "_WPe_setresuid"})
mips_func.update({__NR_Linux+186: "_WPe_getresuid"})
mips_func.update({__NR_Linux+187: "_WPe_query_module"})
mips_func.update({__NR_Linux+188: "_WPe_poll"})
mips_func.update({__NR_Linux+189: "_WPe_nfsservctl"})
mips_func.update({__NR_Linux+190: "_WPe_setresgid"})
mips_func.update({__NR_Linux+191: "_WPe_getresgid"})
mips_func.update({__NR_Linux+192: "_WPe_prctl"})
mips_func.update({__NR_Linux+193: "_WPe_rt_sigreturn"})
mips_func.update({__NR_Linux+194: "_WPe_rt_sigaction"})
mips_func.update({__NR_Linux+195: "_WPe_rt_sigprocmask"})
mips_func.update({__NR_Linux+196: "_WPe_rt_sigpending"})
mips_func.update({__NR_Linux+197: "_WPe_rt_sigtimedwait"})
mips_func.update({__NR_Linux+198: "_WPe_rt_sigqueueinfo"})
mips_func.update({__NR_Linux+199: "_WPe_rt_sigsuspend"})
mips_func.update({__NR_Linux+200: "_WPe_pread64"})
mips_func.update({__NR_Linux+201: "_WPe_pwrite64"})
mips_func.update({__NR_Linux+202: "_WPe_chown"})
mips_func.update({__NR_Linux+203: "_WPe_getcwd"})
mips_func.update({__NR_Linux+204: "_WPe_capget"})
mips_func.update({__NR_Linux+205: "_WPe_capset"})
mips_func.update({__NR_Linux+206: "_WPe_sigaltstack"})
mips_func.update({__NR_Linux+207: "_WPe_sendfile"})
mips_func.update({__NR_Linux+208: "_WPe_getpmsg"})
mips_func.update({__NR_Linux+209: "_WPe_putpmsg"})
mips_func.update({__NR_Linux+210: "_WPe_mmap2"})
mips_func.update({__NR_Linux+211: "_WPe_truncate64"})
mips_func.update({__NR_Linux+212: "_WPe_ftruncate64"})
mips_func.update({__NR_Linux+213: "_WPe_stat64"})
mips_func.update({__NR_Linux+214: "_WPe_lstat64"})
mips_func.update({__NR_Linux+215: "_WPe_fstat64"})
mips_func.update({__NR_Linux+216: "_WPe_pivot_root"})
mips_func.update({__NR_Linux+217: "_WPe_mincore"})
mips_func.update({__NR_Linux+218: "_WPe_madvise"})
mips_func.update({__NR_Linux+219: "_WPe_getdents64"})
mips_func.update({__NR_Linux+220: "_WPe_fcntl64"})
mips_func.update({__NR_Linux+221: "_WPe_reserved221"})
mips_func.update({__NR_Linux+222: "_WPe_gettid"})
mips_func.update({__NR_Linux+223: "_WPe_readahead"})
mips_func.update({__NR_Linux+224: "_WPe_setxattr"})
mips_func.update({__NR_Linux+225: "_WPe_lsetxattr"})
mips_func.update({__NR_Linux+226: "_WPe_fsetxattr"})
mips_func.update({__NR_Linux+227: "_WPe_getxattr"})
mips_func.update({__NR_Linux+228: "_WPe_lgetxattr"})
mips_func.update({__NR_Linux+229: "_WPe_fgetxattr"})
mips_func.update({__NR_Linux+230: "_WPe_listxattr"})
mips_func.update({__NR_Linux+231: "_WPe_llistxattr"})
mips_func.update({__NR_Linux+232: "_WPe_flistxattr"})
mips_func.update({__NR_Linux+233: "_WPe_removexattr"})
mips_func.update({__NR_Linux+234: "_WPe_lremovexattr"})
mips_func.update({__NR_Linux+235: "_WPe_fremovexattr"})
mips_func.update({__NR_Linux+236: "_WPe_tkill"})
mips_func.update({__NR_Linux+237: "_WPe_sendfile64"})
mips_func.update({__NR_Linux+238: "_WPe_futex"})
mips_func.update({__NR_Linux+239: "_WPe_sched_setaffinity"})
mips_func.update({__NR_Linux+240: "_WPe_sched_getaffinity"})
mips_func.update({__NR_Linux+241: "_WPe_io_setup"})
mips_func.update({__NR_Linux+242: "_WPe_io_destroy"})
mips_func.update({__NR_Linux+243: "_WPe_io_getevents"})
mips_func.update({__NR_Linux+244: "_WPe_io_submit"})
mips_func.update({__NR_Linux+245: "_WPe_io_cancel"})
mips_func.update({__NR_Linux+246: "_WPe_exit_group"})
mips_func.update({__NR_Linux+247: "_WPe_lookup_dcookie"})
mips_func.update({__NR_Linux+248: "_WPe_epoll_create"})
mips_func.update({__NR_Linux+249: "_WPe_epoll_ctl"})
mips_func.update({__NR_Linux+250: "_WPe_epoll_wait"})
mips_func.update({__NR_Linux+251: "_WPe_remap_file_pages"})
mips_func.update({__NR_Linux+252: "_WPe_set_tid_address"})
mips_func.update({__NR_Linux+253: "_WPe_restart_syscall"})
mips_func.update({__NR_Linux+254: "_WPe_fadvise64"})
mips_func.update({__NR_Linux+255: "_WPe_statfs64"})
mips_func.update({__NR_Linux+256: "_WPe_fstatfs64"})
mips_func.update({__NR_Linux+257: "_WPe_timer_create"})
mips_func.update({__NR_Linux+258: "_WPe_timer_settime"})
mips_func.update({__NR_Linux+259: "_WPe_timer_gettime"})
mips_func.update({__NR_Linux+260: "_WPe_timer_getoverrun"})
mips_func.update({__NR_Linux+261: "_WPe_timer_delete"})
mips_func.update({__NR_Linux+262: "_WPe_clock_settime"})
mips_func.update({__NR_Linux+263: "_WPe_clock_gettime"})
mips_func.update({__NR_Linux+264: "_WPe_clock_getres"})
mips_func.update({__NR_Linux+265: "_WPe_clock_nanosleep"})
mips_func.update({__NR_Linux+266: "_WPe_tgkill"})
mips_func.update({__NR_Linux+267: "_WPe_utimes"})
mips_func.update({__NR_Linux+268: "_WPe_mbind"})
mips_func.update({__NR_Linux+269: "_WPe_get_mempolicy"})
mips_func.update({__NR_Linux+270: "_WPe_set_mempolicy"})
mips_func.update({__NR_Linux+271: "_WPe_mq_open"})
mips_func.update({__NR_Linux+272: "_WPe_mq_unlink"})
mips_func.update({__NR_Linux+273: "_WPe_mq_timedsend"})
mips_func.update({__NR_Linux+274: "_WPe_mq_timedreceive"})
mips_func.update({__NR_Linux+275: "_WPe_mq_notify"})
mips_func.update({__NR_Linux+276: "_WPe_mq_getsetattr"})
mips_func.update({__NR_Linux+277: "_WPe_vserver"})
mips_func.update({__NR_Linux+278: "_WPe_waitid"})
mips_func.update({__NR_Linux+280: "_WPe_add_key"})
mips_func.update({__NR_Linux+281: "_WPe_request_key"})
mips_func.update({__NR_Linux+282: "_WPe_keyctl"})
mips_func.update({__NR_Linux+283: "_WPe_set_thread_area"})
mips_func.update({__NR_Linux+284: "_WPe_inotify_init"})
mips_func.update({__NR_Linux+285: "_WPe_inotify_add_watch"})
mips_func.update({__NR_Linux+286: "_WPe_inotify_rm_watch"})
mips_func.update({__NR_Linux+287: "_WPe_migrate_pages"})
mips_func.update({__NR_Linux+288: "_WPe_openat"})
mips_func.update({__NR_Linux+289: "_WPe_mkdirat"})
mips_func.update({__NR_Linux+290: "_WPe_mknodat"})
mips_func.update({__NR_Linux+291: "_WPe_fchownat"})
mips_func.update({__NR_Linux+292: "_WPe_futimesat"})
mips_func.update({__NR_Linux+293: "_WPe_fstatat64"})
mips_func.update({__NR_Linux+294: "_WPe_unlinkat"})
mips_func.update({__NR_Linux+295: "_WPe_renameat"})
mips_func.update({__NR_Linux+296: "_WPe_linkat"})
mips_func.update({__NR_Linux+297: "_WPe_symlinkat"})
mips_func.update({__NR_Linux+298: "_WPe_readlinkat"})
mips_func.update({__NR_Linux+299: "_WPe_fchmodat"})
mips_func.update({__NR_Linux+300: "_WPe_faccessat"})
mips_func.update({__NR_Linux+301: "_WPe_pselect6"})
mips_func.update({__NR_Linux+302: "_WPe_ppoll"})
mips_func.update({__NR_Linux+303: "_WPe_unshare"})
mips_func.update({__NR_Linux+304: "_WPe_splice"})
mips_func.update({__NR_Linux+305: "_WPe_sync_file_range"})
mips_func.update({__NR_Linux+306: "_WPe_tee"})
mips_func.update({__NR_Linux+307: "_WPe_vmsplice"})
mips_func.update({__NR_Linux+308: "_WPe_move_pages"})
mips_func.update({__NR_Linux+309: "_WPe_set_robust_list"})
mips_func.update({__NR_Linux+310: "_WPe_get_robust_list"})
mips_func.update({__NR_Linux+311: "_WPe_kexec_load"})
mips_func.update({__NR_Linux+312: "_WPe_getcpu"})
mips_func.update({__NR_Linux+313: "_WPe_epoll_pwait"})
mips_func.update({__NR_Linux+314: "_WPe_ioprio_set"})
mips_func.update({__NR_Linux+315: "_WPe_ioprio_get"})
mips_func.update({__NR_Linux+316: "_WPe_utimensat"})
mips_func.update({__NR_Linux+317: "_WPe_signalfd"})
mips_func.update({__NR_Linux+318: "_WPe_timerfd"})
mips_func.update({__NR_Linux+319: "_WPe_eventfd"})
mips_func.update({__NR_Linux+320: "_WPe_fallocate"})
mips_func.update({__NR_Linux+321: "_WPe_timerfd_create"})
mips_func.update({__NR_Linux+322: "_WPe_timerfd_gettime"})
mips_func.update({__NR_Linux+323: "_WPe_timerfd_settime"})
mips_func.update({__NR_Linux+324: "_WPe_signalfd4"})
mips_func.update({__NR_Linux+325: "_WPe_eventfd2"})
mips_func.update({__NR_Linux+326: "_WPe_epoll_create1"})
mips_func.update({__NR_Linux+327: "_WPe_dup3"})
mips_func.update({__NR_Linux+328: "_WPe_pipe2"})
mips_func.update({__NR_Linux+329: "_WPe_inotify_init1"})
mips_func.update({__NR_Linux+330: "_WPe_preadv"})
mips_func.update({__NR_Linux+331: "_WPe_pwritev"})
mips_func.update({__NR_Linux+332: "_WPe_rt_tgsigqueueinfo"})
mips_func.update({__NR_Linux+333: "_WPe_perf_event_open"})
mips_func.update({__NR_Linux+334: "_WPe_accept4"})
mips_func.update({__NR_Linux+335: "_WPe_recvmmsg"})
mips_func.update({__NR_Linux+336: "_WPe_fanotify_init"})
mips_func.update({__NR_Linux+337: "_WPe_fanotify_mark"})
mips_func.update({__NR_Linux+338: "_WPe_prlimit64"})
mips_func.update({__NR_Linux+339: "_WPe_name_to_handle_at"})
mips_func.update({__NR_Linux+340: "_WPe_open_by_handle_at"})
mips_func.update({__NR_Linux+341: "_WPe_clock_adjtime"})
mips_func.update({__NR_Linux+342: "_WPe_syncfs"})
mips_func.update({__NR_Linux+343: "_WPe_sendmmsg"})
mips_func.update({__NR_Linux+344: "_WPe_setns"})
mips_func.update({__NR_Linux+345: "_WPe_process_vm_readv"})
mips_func.update({__NR_Linux+346: "_WPe_process_vm_writev"})
mips_func.update({__NR_Linux+347: "_WPe_kcmp"})
mips_func.update({__NR_Linux+348: "_WPe_finit_module"})
mips_func.update({__NR_Linux+349: "_WPe_sched_setattr"})
mips_func.update({__NR_Linux+350: "_WPe_sched_getattr"})
mips_func.update({__NR_Linux+351: "_WPe_renameat2"})
mips_func.update({__NR_Linux+352: "_WPe_seccomp"})
mips_func.update({__NR_Linux+353: "_WPe_getrandom"})
mips_func.update({__NR_Linux+354: "_WPe_memfd_create"})
mips_func.update({__NR_Linux+355: "_WPe_bpf"})
mips_func.update({__NR_Linux+356: "_WPe_execveat"})
mips_func.update({__NR_Linux+357: "_WPe_userfaultfd"})
mips_func.update({__NR_Linux+358: "_WPe_membarrier"})
mips_func.update({__NR_Linux+359: "_WPe_mlock2"})
mips_func.update({__NR_Linux+360: "_WPe_copy_file_range"})
mips_func.update({__NR_Linux+361: "_WPe_preadv2"})
mips_func.update({__NR_Linux+362: "_WPe_pwritev2"})
mips_func.update({__NR_Linux+363: "_WPe_pkey_mprotect"})
mips_func.update({__NR_Linux+364: "_WPe_pkey_alloc"})
mips_func.update({__NR_Linux+365: "_WPe_pkey_free"})
mips_func.update({__NR_Linux+366: "_WPe_statx"})
mips_func.update({__NR_Linux+367: "_WPe_rseq"})
mips_func.update({__NR_Linux+368: "_WPe_io_pgetevents"})
mips_func.update({__NR_Linux+393: "_WPe_semget"})
mips_func.update({__NR_Linux+394: "_WPe_semctl"})
mips_func.update({__NR_Linux+395: "_WPe_shmget"})
mips_func.update({__NR_Linux+396: "_WPe_shmctl"})
mips_func.update({__NR_Linux+397: "_WPe_shmat"})
mips_func.update({__NR_Linux+398: "_WPe_shmdt"})
mips_func.update({__NR_Linux+399: "_WPe_msgget"})
mips_func.update({__NR_Linux+400: "_WPe_msgsnd"})
mips_func.update({__NR_Linux+401: "_WPe_msgrcv"})
mips_func.update({__NR_Linux+402: "_WPe_msgctl"})
mips_func.update({__NR_Linux+403: "_WPe_clock_gettime64"})
mips_func.update({__NR_Linux+404: "_WPe_clock_settime64"})
mips_func.update({__NR_Linux+405: "_WPe_clock_adjtime64"})
mips_func.update({__NR_Linux+406: "_WPe_clock_getres_time64"})
mips_func.update({__NR_Linux+407: "_WPe_clock_nanosleep_time64"})
mips_func.update({__NR_Linux+408: "_WPe_timer_gettime64"})
mips_func.update({__NR_Linux+409: "_WPe_timer_settime64"})
mips_func.update({__NR_Linux+410: "_WPe_timerfd_gettime64"})
mips_func.update({__NR_Linux+411: "_WPe_timerfd_settime64"})
mips_func.update({__NR_Linux+412: "_WPe_utimensat_time64"})
mips_func.update({__NR_Linux+413: "_WPe_pselect6_time64"})
mips_func.update({__NR_Linux+414: "_WPe_ppoll_time64"})
mips_func.update({__NR_Linux+416: "_WPe_io_pgetevents_time64"})
mips_func.update({__NR_Linux+417: "_WPe_recvmmsg_time64"})
mips_func.update({__NR_Linux+418: "_WPe_mq_timedsend_time64"})
mips_func.update({__NR_Linux+419: "_WPe_mq_timedreceive_time64"})
mips_func.update({__NR_Linux+420: "_WPe_semtimedop_time64"})
mips_func.update({__NR_Linux+421: "_WPe_rt_sigtimedwait_time64"})
mips_func.update({__NR_Linux+422: "_WPe_futex_time64"})
mips_func.update({__NR_Linux+423: "_WPe_sched_rr_get_interval_time64"})
mips_func.update({__NR_Linux+424: "_WPe_pidfd_send_signal"})
mips_func.update({__NR_Linux+425: "_WPe_io_uring_setup"})
mips_func.update({__NR_Linux+426: "_WPe_io_uring_enter"})
mips_func.update({__NR_Linux+427: "_WPe_io_uring_register"})
mips_func.update({__NR_Linux+428: "_WPe_open_tree"})
mips_func.update({__NR_Linux+429: "_WPe_move_mount"})
mips_func.update({__NR_Linux+430: "_WPe_fsopen"})
mips_func.update({__NR_Linux+431: "_WPe_fsconfig"})
mips_func.update({__NR_Linux+432: "_WPe_fsmount"})
mips_func.update({__NR_Linux+433: "_WPe_fspick"})
mips_func.update({__NR_Linux+434: "_WPe_pidfd_open"})
mips_func.update({__NR_Linux+435: "_WPe_clone3"})
mips_func.update({__NR_Linux+436: "_WPe_close_range"})
mips_func.update({__NR_Linux+437: "_WPe_openat2"})
mips_func.update({__NR_Linux+438: "_WPe_pidfd_getfd"})
mips_func.update({__NR_Linux+439: "_WPe_faccessat2"})
mips_func.update({__NR_Linux+440: "_WPe_process_madvise"})

def TestSyscall():
    startAddr = idc.get_name_ea_simple("start")
    if startAddr != 0xFFFFFFFF:
        flagLine = idc.next_head(startAddr)
        disasmLine = idc.generate_disasm_line(flagLine, 0)
        if disasmLine == "move    $fp, $zero":
            return 2
        else:
            return 1
    else:
        startAddr = idc.get_name_ea_simple("_start")
        flagLine = idc.next_head(startAddr)
        disasmLine = idc.generate_disasm_line(flagLine, 0)
        if disasmLine == "move    $fp, $zero":
            return 2
        else:
            return 1

def ReName_DirectCall():
    sum = 0
    for func in idautils.Functions():
        dism_addr = list(idautils.FuncItems(func))
        for line in dism_addr:
            m = idc.print_insn_mnem(line)
            if m == 'syscall':
                op = idc.GetDisasm(line - 4)
                op = re.findall('(?<=0x).*$', op)
                opString = ''.join(op)
                if len(opString) == 0:
                    print("Error：请确认调用规则是否正确！")
                    return
                callNumber = int(opString, 16)
                address = idc.get_name_ea_simple(idc.get_func_name(line))
                flag = 0
                for func in idautils.Functions():
                    name = idc.get_func_name(func)
                    if name == mips_func[callNumber]:
                        flag = 1
                if flag == 0:
                    print(mips_func[callNumber])
                    idc.set_name(address, mips_func[callNumber], idc.SN_CHECK)
                    sum += 1
        continue
    print("LinuxFuncFinder_Mips32_DirectCall finished！总共重命名%d个函数" % sum)

def ReName_IndirectCall():
    sum = 0
    for func in idautils.Functions():
        dism_addr = list(idautils.FuncItems(func))
        for line in dism_addr:
            m = idc.print_insn_mnem(line)
            if m == 'syscall':
                lastline = idc.prev_head(line)
                op = idc.print_operand(lastline, 0)
                funcStartAddr = idc.get_func_attr(line, idc.FUNCATTR_START)
                if "v0" in op:
                    Mnem_lastline = idc.print_insn_mnem(lastline)
                    if Mnem_lastline == "li":
                        opString = idc.print_operand(lastline, 1)
                        callNumber = int(opString, 16)
                        funcAddr = funcStartAddr
                        idc.set_name(funcAddr, mips_func[callNumber], SN_FORCE)
                        print(mips_func[callNumber])
                        sum += 1
                    elif Mnem_lastline == "move":
                        xrefs = list(idautils.XrefsTo(funcStartAddr))
                        for xrefAddr in xrefs:
                            uptoFindNrLine = idc.prev_head(xrefAddr.frm)
                            op_uptoFindNrLine = idc.print_operand(uptoFindNrLine, 0)
                            while "a0" not in op_uptoFindNrLine:
                                uptoFindNrLine = idc.prev_head(uptoFindNrLine)
                                op_uptoFindNrLine = idc.print_operand(uptoFindNrLine, 0)
                            opString = idc.print_operand(uptoFindNrLine, 1)
                            callNumber = int(opString, 16)
                            funcAddr = idc.get_func_attr(uptoFindNrLine, idc.FUNCATTR_START)
                            idc.set_name(funcAddr, mips_func[callNumber], SN_FORCE)
                            print(mips_func[callNumber])
                            sum += 1
                            break
                    elif Mnem_lastline == "lw":
                        xrefs = list(idautils.XrefsTo(funcStartAddr))
                        for xrefAddr in xrefs:
                            uptoFindNrLine = idc.prev_head(xrefAddr.frm)
                            op_uptoFindNrLine = idc.print_operand(uptoFindNrLine, 0)
                            while "a0" not in op_uptoFindNrLine:
                                uptoFindNrLine = idc.prev_head(uptoFindNrLine)
                                op_uptoFindNrLine = idc.print_operand(uptoFindNrLine, 0)
                                Mnem = idc.print_insn_mnem(uptoFindNrLine)
                            if Mnem == "lw" and "a0" in op_uptoFindNrLine:
                                funcStartAddrTemp = idc.get_func_attr(uptoFindNrLine, idc.FUNCATTR_START)
                                xrefsTemp = list(idautils.XrefsTo(funcStartAddrTemp))
                                for xrefAddrTemp in xrefsTemp:
                                    MnemSegment = idc.print_insn_mnem(xrefAddrTemp.frm)
                                    if MnemSegment == "jalr":
                                        xrefs.append(xrefAddrTemp)
                            if Mnem == "li" and "a0" in op_uptoFindNrLine:
                                opString = idc.print_operand(uptoFindNrLine, 1)
                                callNumber = int(opString, 16)
                                funcAddr = idc.get_func_attr(uptoFindNrLine, idc.FUNCATTR_START)
                                idc.set_name(funcAddr, mips_func[callNumber], SN_FORCE)
                                print(mips_func[callNumber])
                                sum += 1
        continue
    print("LinuxFuncFinder_Mips32_IndirectCall finished！总共重命名%d个函数" % sum)

def GetMainFunc(func):
    start = func.start_ea
    tmpMainAddr = idc.next_head(idc.next_head(idc.next_head(idc.next_head(idc.next_head(idc.next_head(start))))))
    mainOP = idc.print_operand(tmpMainAddr, 1)
    if "sub" in mainOP:
        mainAddr = int(mainOP.split("sub_")[1], 16)
        end = idc.prev_head(func.end_ea)
        tmpInitMainAddr = idc.prev_head(idc.prev_head(idc.prev_head(idc.prev_head(idc.prev_head(end)))))
        initMainOP = idc.print_operand(tmpInitMainAddr, 1)
        initMainAddr = int(initMainOP.split("sub_")[1], 16)
        print("main address = 0x%x" %mainAddr)
        idc.set_name(initMainAddr, "Init_Main", SN_FORCE)
        idc.set_name(mainAddr, "main", SN_FORCE)
    elif "loc" in mainOP:
        mainAddr = int(mainOP.split("loc_")[1], 16)
        end = idc.prev_head(func.end_ea)
        tmpInitMainAddr = idc.prev_head(idc.prev_head(idc.prev_head(idc.prev_head(idc.prev_head(end)))))
        initMainOP = idc.print_operand(tmpInitMainAddr, 1)
        initMainAddr = int(initMainOP.split("sub_")[1], 16)
        print("main address = 0x%x" %mainAddr)
        idc.set_name(initMainAddr, "Init_Main", SN_FORCE)
        idc.set_name(mainAddr, "main", SN_FORCE)
    elif "unk" in mainOP:
        mainAddr = int(mainOP.split("unk_")[1], 16)
        end = idc.prev_head(func.end_ea)
        tmpInitMainAddr = idc.prev_head(idc.prev_head(idc.prev_head(idc.prev_head(idc.prev_head(end)))))
        initMainOP = idc.print_operand(tmpInitMainAddr, 1)
        initMainAddr = int(initMainOP.split("sub_")[1], 16)
        print("main address = 0x%x" %mainAddr)
        idc.set_name(initMainAddr, "Init_Main", SN_FORCE)
        idc.set_name(mainAddr, "main", SN_FORCE)

def RenameStartFunc():
    startAddr = idc.get_name_ea_simple("start")
    func = idaapi.get_func(startAddr)
    if func != None:
        GetMainFunc(func)
    else:
        startAddr = idc.get_name_ea_simple("_start")
        func = idaapi.get_func(startAddr)
        if func != None:
            GetMainFunc(func)

def main():
    TS = TestSyscall()
    if TS == 1:
        ReName_DirectCall()
    elif TS == 2:
        ReName_IndirectCall()
    RenameStartFunc()

if __name__ == "__main__":
    main()
