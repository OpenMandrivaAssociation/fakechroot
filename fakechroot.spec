Summary:	A chroot-like wrapper for non-privileged users
Name:		fakechroot
Version:	2.14
Release:	%mkrel 1
Group:		File tools
License:	GPLv2+
URL:		https://github.com/fakechroot/fakechroot/wiki
Source0:	https://github.com/downloads/%{name}/%{name}/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
rm -rf %{buildroot}

%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README NEWS LICENSE
%{_bindir}/%{name}
%{_bindir}/ldd.%{name}
%{_bindir}/ldconfig.%{name}
%{_mandir}/man1/%{name}*
%{_libdir}/%name/*.so
%{_libdir}/%name/*.la
