Summary:	Programs that show the differences between files or directories
Name:		diffutils
Version:	3.7
Release:	1%{?dist}
License:	GPLv3+
URL:		http://www.gnu.org/software/diffutils
Group:		System Environment/Base
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnu.org/gnu/diffutils/%{name}-%{version}.tar.xz
%define sha1 diffutils=ad4e0a05ee2e7f5529db6cb84474f45e086e609b
BuildRequires:  coreutils
Conflicts:      toybox < 0.8.2-2

%description
The Diffutils package contains programs that show the
differences between files or directories.
%prep
%setup -q
sed -i 's:= @mkdir_p@:= /bin/mkdir -p:' po/Makefile.in.in

%build

%configure --disable-silent-rules

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
rm -rf %{buildroot}%{_infodir}

%find_lang %{name}

%check
sed -i 's/test-update-copyright.sh //' gnulib-tests/Makefile
make %{?_smp_mflags} check

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/*/*

%changelog
*       Wed Jul 08 2020 Gerrit Photon <photon-checkins@vmware.com> 3.7-1
-       Automatic Version Bump
*       Thu Apr 16 2020 Alexey Makhalov <amakhalov@vmware.com> 3.6-3
-       Do not conflict with toybox >= 0.8.2-2
*       Tue Oct 2 2018 Michelle Wang <michellew@vmware.com> 3.6-2
-       Add conflicts toybox.
*       Fri Aug 03 2018 Srivatsa S. Bhat <srivatsa@csail.mit.edu> 3.6-1
-       Update to version 3.6 to get it to build with gcc 7.3.
*       Wed Apr 19 2017 Bo Gan <ganb@vmware.com> 3.5-1
-       Update to 3.5.
*       Wed Oct 05 2016 ChangLee <changlee@vmware.com> 3.3-4
-       Modified %check.
*       Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 3.3-3
-       GA Bump release of all rpms.
*       Wed Jun 3 2015 Divya Thaluru <dthaluru@vmware.com> 3.3-2
-       Adding coreutils package to build requires.
*       Wed Nov 5 2014 Divya Thaluru <dthaluru@vmware.com> 3.3-1
-       Initial build First version.
