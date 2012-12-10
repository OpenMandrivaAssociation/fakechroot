Summary:	A chroot-like wrapper for non-privileged users
Name:		fakechroot
Version:	2.16
Release:	1
Group:		File tools
License:	GPLv2+
URL:		https://github.com/fakechroot/fakechroot/wiki
Source0:	https://github.com/downloads/%{name}/%{name}/%{name}-%{version}.tar.gz

%description 
fakechroot runs a command in an environment were is additional possibility
to use chroot(8) command without root privileges. This is useful for
allowing users to create own chrooted environment with possibility to
install another packages without need for root privileges.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'


%files
%doc README NEWS LICENSE
%{_bindir}/%{name}
%{_bindir}/ldd.%{name}
%{_sbindir}/chroot.%{name}
%{_mandir}/man1/%{name}*
%{_libdir}/%name/*.so
%{_sysconfdir}/%name/


%changelog
* Sun Dec 18 2011 Alexander Khrukin <akhrukin@mandriva.org> 2.16-1
+ Revision: 743623
- update version 2.16

* Wed Feb 02 2011 Bogdano Arendartchuk <bogdano@mandriva.com> 2.14-1
+ Revision: 634945
- imported package fakechroot

