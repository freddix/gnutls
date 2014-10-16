Summary:	The GNU Transport Layer Security Library
Name:		gnutls
Version:	3.3.9
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/gcrypt/gnutls/v3.3/%{name}-%{version}.tar.xz
# Source0-md5:	ff61b77e39d09f1140ab5a9cf52c58b6
Patch0:		%{name}-link.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtasn1-devel
BuildRequires:	libtool
BuildRequires:	nettle-devel >= 2.7
BuildRequires:	p11-kit-devel >= 0.20.7
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuTLS is a project that aims to develop a library which provides a
secure layer, over a reliable transport layer (ie. TCP/IP). Currently
the gnuTLS library implements the proposed standards by the IETF's TLS
working group.

%package libs
Summary:	GnuTLS libraries
Group:		Libraries

%description libs
GnuTLS libraries.

%package devel
Summary:	Header files etc to develop gnutls applications
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Header files etc to develop gnutls applications.

%package c++
Summary:	libgnutlsxx - C++ interface to gnutls library
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name}-libs = %{version}-%{release}

%description c++
libgnutlsxx - C++ interface to gnutls library.

%package c++-devel
Summary:	Header files for libgnutlsxx, a C++ interface to gnutls library
License:	LGPL v2.1+
Group:		Development/Libraries
Requires:	%{name}-c++ = %{version}-%{release}
Requires:	%{name}-devel = %{version}-%{release}
Requires:	libstdc++-devel

%description c++-devel
Header files for libgnutlsxx, a C++ interface to gnutls library.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4 -I gl/m4 -I src/gl/m4 -I src/libopts/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-guile		\
	--disable-silent-rules	\
	--disable-static	\
	--with-zlib
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	m4datadir=%{_aclocaldir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	libs -p /usr/sbin/ldconfig
%postun	libs -p /usr/sbin/ldconfig

%post	c++ -p /usr/sbin/ldconfig
%postun	c++ -p /usr/sbin/ldconfig

%files -f gnutls.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/crywrap
%attr(755,root,root) %{_bindir}/danetool
%attr(755,root,root) %{_bindir}/gnutls*
%attr(755,root,root) %{_bindir}/ocsptool
%attr(755,root,root) %{_bindir}/p11tool
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool
%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*
%{_mandir}/man1/ocsptool.1*
%{_mandir}/man1/p11tool.1*
%{_mandir}/man1/psktool.1*
%{_mandir}/man1/srptool.1*
%{_infodir}/*.info*
%{_infodir}/*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgnutls-openssl.so.27
%attr(755,root,root) %ghost %{_libdir}/libgnutls.so.28
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%attr(755,root,root) %{_libdir}/libgnutls.so
%{_includedir}/gnutls
%exclude %{_includedir}/gnutls/gnutlsxx.h
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*gnutls*.3*

%files c++
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libgnutlsxx.so.??
%attr(755,root,root) %{_libdir}/libgnutlsxx.so.*.*.*

%files c++-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutlsxx.so
%{_includedir}/gnutls/gnutlsxx.h

