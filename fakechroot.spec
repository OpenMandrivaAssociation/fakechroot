Summary:	A chroot-like wrapper for non-privileged users
Name:		fakechroot
Version:	2.20.1
Release:	3
Group:		File tools
License:	GPLv2+
URL:		https://github.com/dex4er/fakechroot
Source0:	%{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0:		https://github.com/dex4er/fakechroot/commit/b42d1fb9538f680af2f31e864c555414ccba842a.patch
Patch1:		https://github.com/dex4er/fakechroot/pull/80.patch
Patch2:		https://github.com/dex4er/fakechroot/pull/104.patch
Patch3:		https://src.fedoraproject.org/rpms/fakechroot/raw/rawhide/f/disable_cp.t.patch
Patch4:		https://src.fedoraproject.org/rpms/fakechroot/raw/rawhide/f/autoupdate.patch

BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
# Required for manpage
BuildRequires:	/usr/bin/pod2man
# ldd.fakechroot
Requires:	/usr/bin/objdump

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
# FIXME Building with clang causes 6 tests in "make check" to fail
# Last verified with fakechroot 2.20.1, clang 17.0.5
export CC=gcc
%configure --disable-static --disable-silent-rules
%make_build

%install
%make_install

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
