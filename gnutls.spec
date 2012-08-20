Summary:	The GNU Transport Layer Security Library
Name:		gnutls
Version:	3.0.21
Release:	1
License:	LGPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/%{name}-%{version}.tar.xz
# Source0-md5:	7480dff7115e5af85215893c06b3ac5c
Patch0:		%{name}-link.patch
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libtasn1-devel
BuildRequires:	libtool
BuildRequires:	nettle-devel
BuildRequires:	p11-kit-devel
BuildRequires:	readline-devel
BuildRequires:	texinfo
BuildRequires:	zlib-devel
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GnuTLS is a project that aims to develop a library which provides a
secure layer, over a reliable transport layer (ie. TCP/IP). Currently
the gnuTLS library implements the proposed standards by the IETF's TLS
working group.

%package devel
Summary:	Header files etc to develop gnutls applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc to develop gnutls applications.

%package c++
Summary:	libgnutlsxx - C++ interface to gnutls library
Summary(pl.UTF-8):	libgnutlsxx - interfejs C++ do biblioteki gnutls
License:	LGPL v2.1+
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

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
%{__aclocal} -I m4 -I gl/m4 -I src/libopts/m4
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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%post	c++ -p /sbin/ldconfig
%postun	c++ -p /sbin/ldconfig

%files -f gnutls.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_bindir}/certtool
%attr(755,root,root) %{_bindir}/gnutls*
%attr(755,root,root) %{_bindir}/ocsptool
%attr(755,root,root) %{_bindir}/p11tool
%attr(755,root,root) %{_bindir}/psktool
%attr(755,root,root) %{_bindir}/srptool

%attr(755,root,root) %ghost %{_libdir}/libgnutls-openssl.so.??
%attr(755,root,root) %ghost %{_libdir}/libgnutls.so.??
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so.*.*.*
%attr(755,root,root) %{_libdir}/libgnutls.so.*.*.*

%{_mandir}/man1/certtool.1*
%{_mandir}/man1/gnutls-*
%{_mandir}/man1/ocsptool.1*
%{_mandir}/man1/p11tool.1*
%{_mandir}/man1/psktool.1*
%{_mandir}/man1/srptool.1*
%{_infodir}/*.info*
%{_infodir}/*.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnutls-openssl.so
%attr(755,root,root) %{_libdir}/libgnutls.so
%{_libdir}/libgnutls-openssl.la
%{_libdir}/libgnutls.la
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
%{_libdir}/libgnutlsxx.la
%{_includedir}/gnutls/gnutlsxx.h

