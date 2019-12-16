Summary:	A chroot-like wrapper for non-privileged users
Name:		fakechroot
Version:	2.20.1
Release:	1
Group:		File tools
License:	GPLv2+
URL:		https://github.com/dex4er/fakechroot
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
# Required for manpage
BuildRequires:	/usr/bin/pod2man
# ldd.fakechroot
Requires:	/usr/bin/objdump
# rpm5 and rpm4 < 4.11 export glob(3) when they shouldn't...
Conflicts:	rpm < 2:4.14.0

%description
fakechroot runs a command in an environment were is additional possibility
to use chroot(8) command without root privileges. This is useful for
allowing users to create own chrooted environment with possibility to
install another packages without need for root privileges.

%prep
%autosetup -p1
# For %%doc dependency-clean.
chmod -x scripts/{relocatesymlinks,restoremode,savemode}.sh

%build
autoreconf -vfi
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install
# Drop libtool files
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%check
%make_build check

%files
%doc scripts/{relocatesymlinks,restoremode,savemode}.sh
%doc NEWS.md README.md THANKS.md
%license COPYING LICENSE
%{_bindir}/%{name}
%{_bindir}/env.%{name}
%{_bindir}/ldd.%{name}
%{_sbindir}/chroot.%{name}
%dir %{_sysconfdir}/%{name}/
%config(noreplace) %{_sysconfdir}/%{name}/chroot.env
%config(noreplace) %{_sysconfdir}/%{name}/debootstrap.env
%config(noreplace) %{_sysconfdir}/%{name}/rinse.env
%{_mandir}/man1/%{name}.1*
%{_libdir}/%{name}/*.so
