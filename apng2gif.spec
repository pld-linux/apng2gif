Summary:	Convert APNG animations into animated GIF format
Summary(pl.UTF-8):	Konwerter animacji APNG do animowanego formatu GIF
Name:		apng2gif
Version:	1.7
Release:	1
License:	Zlib (BSD-like)
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/apng2gif/%{name}-%{version}-src.zip
# Source0-md5:	9877249603e7d01bc1970130a40cd035
URL:		http://apng2gif.sourceforge.net/
BuildRequires:	libpng-devel >= 2:1.6.17
BuildRequires:	libstdc++-devel
BuildRequires:	zlib-devel >= 1.2.8
Requires:	libpng >= 2:1.6.17
Requires:	zlib >= 1.2.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program converts APNG animations into animated GIF format. Wu
quantizer is used for true-color files.

%description -l pl.UTF-8
Ten program przekształca animacje APNG do animowanego formatu GIF. W
przypadku plików true-color używany jest kwantyzator Wu.

%prep
%setup -q -c

%build
%{__cxx} %{rpmldflags} %{rpmcxxflags} %{rpmcppflags} -Wall -o apng2gif apng2gif.cpp -lpng -lz -lm

%install
rm -rf $RPM_BUILD_ROOT

install -D apng2gif $RPM_BUILD_ROOT%{_bindir}/apng2gif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/apng2gif
