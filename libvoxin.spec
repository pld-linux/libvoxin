# TODO: (fake) libibmeci, voxind (32-bit only?)
Summary:	Library to ease the integration of voxin on 64-bit architectures
Summary(pl.UTF-8):	Biblioteka ułatwiająca integrację voxina na architeksturach 64-bitowych
Name:		libvoxin
Version:	1.6.0
Release:	1
License:	LGPL v2.1+, MIT, BSD
Group:		Libraries
#Source0Download: https://github.com/Oralux/libvoxin/tags
Source0:	https://github.com/Oralux/libvoxin/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6c233a303568d66bf283f88329905cde
URL:		https://oralux.org/
BuildRequires:	gcc >= 6:4.7
BuildRequires:	inih-devel
BuildRequires:	libinote-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libvoxin library eases the integration of voxin on 64-bit
architectures.

%description -l pl.UTF-8
Biblioteka libvoxin ułatwia integrowanie voxina na architekaturach
64-bitowych.

%package devel
Summary:	Header files for libvoxin library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libvoxin
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libvoxin library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libvoxin.

%prep
%setup -q

%build
CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
%{__make} -C src/common

CC="%{__cc}" \
CFLAGS="%{rpmcflags} %{rpmcppflags}" \
LDFLAGS="%{rpmldflags} %{rpmcflags} -L$(pwd)/src/common" \
STRIP=: \
%{__make} -C src/libvoxin

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install src/libvoxin/libvoxin.so.0.0.1 $RPM_BUILD_ROOT%{_libdir}
ln -sf libvoxin.so.0.0.1 $RPM_BUILD_ROOT%{_libdir}/libvoxin.so.0
ln -sf libvoxin.so.0.0.1 $RPM_BUILD_ROOT%{_libdir}/libvoxin.so
cp -p src/api/*.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README.org
%attr(755,root,root) %{_libdir}/libvoxin.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libvoxin.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libvoxin.so
%{_includedir}/eci.h
%{_includedir}/voxin.h
