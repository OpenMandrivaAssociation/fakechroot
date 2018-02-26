Summary:	A chroot-like wrapper for non-privileged users
Name:		fakechroot
Version:	2.19
Release:	1
Group:		File tools
License:	GPLv2+
URL:		https://github.com/fakechroot/fakechroot/wiki
Source0:	https://github.com/downloads/%{name}/%{name}/%{name}_%{version}.orig.tar.gz
# https://github.com/dex4er/fakechroot/pull/50
Patch0:		0001-Add-support-of-LFS-compatible-fts-functions.patch
Patch1:		fakechroot-rpm-glob64.patch
# Required for patch0:
BuildRequires:	autoconf
BuildRequires:	automake >= 1.10
BuildRequires:	libtool

%description
fakechroot runs a command in an environment were is additional possibility
to use chroot(8) command without root privileges. This is useful for
allowing users to create own chrooted environment with possibility to
install another packages without need for root privileges.

%prep
%setup -q
%apply_patches

# Patch0 updates autoconf, so rerun this:
./autogen.sh

%build
%configure
%make

%install
%makeinstall_std
find %{buildroot} -type f -name "*.la" -exec rm -f {} ';'

%files
%doc LICENSE scripts/restoremode.sh scripts/savemode.sh
%{_bindir}/%{name}
%{_bindir}/ldd.%{name}
%{_sbindir}/chroot.%{name}
%{_mandir}/man1/%{name}*
%{_libdir}/%{name}/*.so
%{_sysconfdir}/%{name}/
