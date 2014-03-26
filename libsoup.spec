Summary:	SOAP (Simple Object Access Protocol) implementation in C
Name:		libsoup
Version:	2.46.0
Release:	1
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libsoup/2.46/%{name}-%{version}.tar.xz
# Source0-md5:	86765c0093efaf3006fa2960d170d097
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel >= 1:2.40.0
BuildRequires:	gnutls-devel
BuildRequires:	gobject-introspection-devel >= 1.40.0
BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	libgnome-keyring-devel >= 3.12.0
BuildRequires:	libgpg-error-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel
BuildRequires:	pkg-config
BuildRequires:	sqlite3-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver	2.4

%description
It provides an queued asynchronous callback-based mechanism for
sending and servicing SOAP requests, and a WSDL (Web Service
Definition Language) to C compiler which generates client stubs and
server skeletons for easily calling and implementing SOAP methods.

%package devel
Summary:	Include files etc to develop SOAP applications
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files, etc you can use to develop SOAP applications.

%package gnome
Summary:	GNOME bindings to libsoup
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gnome
GNOME bindings to libsoup.

%package gnome-devel
Summary:	Include files etc to develop SOAP applications
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Requires:	%{name}-gnome = %{version}-%{release}

%description gnome-devel
Header files, etc you can use to develop SOAP applications.

%package apidocs
Summary:	libsoup API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libsoup API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules		\
	--disable-static		\
	--disable-tls-check		\
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	pkgconfigdir=%{_pkgconfigdir} \
	m4datadir=%{_aclocaldir} \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%post   gnome -p /usr/sbin/ldconfig
%postun gnome -p /usr/sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %ghost %{_libdir}/libsoup-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libsoup-%{apiver}.so.*.*.*
%{_libdir}/girepository-1.0/Soup-2.4.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-%{apiver}.so
%{_includedir}/libsoup-%{apiver}
%{_pkgconfigdir}/libsoup-%{apiver}.pc
%{_datadir}/gir-1.0/Soup-2.4.gir

%files gnome
%defattr(644,root,root,755)
%attr(755,root,root) %ghost %{_libdir}/libsoup-gnome-%{apiver}.so.?
%attr(755,root,root) %{_libdir}/libsoup-gnome-%{apiver}.so.*.*.*
%{_libdir}/girepository-1.0/SoupGNOME-2.4.typelib

%files gnome-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsoup-gnome-%{apiver}.so
%{_includedir}/libsoup-gnome-%{apiver}
%{_pkgconfigdir}/libsoup-gnome-%{apiver}.pc
%{_datadir}/gir-1.0/SoupGNOME-2.4.gir

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libsoup-*

