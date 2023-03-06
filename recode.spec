# TODO: package python extension
#
# Conditional build:
%bcond_without  tests	# unit tests
#
Summary:	Utility for converting text between multiple character sets
Summary(pl.UTF-8):	Uniwersalny konwerter między zestawami znaków
Name:		recode
Version:	3.7.14
Release:	1
License:	LGPL v2+ (library), GPL v2+ (utility)
Group:		Applications/Text
Source0:        https://github.com/rrthomas/recode/releases/download/v%{version}/recode-%{version}.tar.gz
# Source0-md5:	d88b41fd27549123a0822e5a3fae98a8
Patch0:         %{name}-info.patch
Patch1:		%{name}-pl.po-update.patch
URL:		https://github.com/rrthomas/recode
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake
BuildRequires:	flex
BuildRequires:	gettext-tools >= 0.19
BuildRequires:	help2man
BuildRequires:	libtool >= 2:2
BuildRequires:	texinfo
BuildRequires:	python3 >= 1:3.5
BuildRequires:	python3-Cython
BuildRequires:	python3-modules >= 1:3.5
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Free `recode' converts files between various character sets and
surfaces. It supports more than 200 different character sets and
surfaces, including well known ISO-8859, CP-XXXX and Unicode.

%description -l pl.UTF-8
Program `recode' konwertuje pliki pomiędzy różnymi zestawami znaków i
kodowaniami. Obsługuje ponad 200 różnych zestawów znaków oraz sposobów
kodowania, włącznie z popularnymi ISO-8859, CP-XXXX oraz Unicode.

%package devel
Summary:	Header files and documentations for librecode
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do librecode
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files and documentations for librecode.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do librecode.

%package static
Summary:	Static librecode library
Summary(pl.UTF-8):	Biblioteka statyczna librecode
License:	LGPL v2+
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static librecode library.

%description static -l pl.UTF-8
Biblioteka statyczna librecode.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i '1 i @documentencoding ISO-8859-1' doc/recode.texi

%{__rm} po/stamp-po

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%if %{with tests}
%{__make} check
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/recode
%attr(755,root,root) %{_libdir}/librecode.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/librecode.so.3
%{_infodir}/recode.info*
%{_mandir}/man1/recode.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/librecode.so
%{_libdir}/librecode.la
%{_includedir}/recode.h
%{_includedir}/recodext.h

%files static
%defattr(644,root,root,755)
%{_libdir}/librecode.a
