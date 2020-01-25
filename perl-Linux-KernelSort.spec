#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Linux
%define		pnam	KernelSort
Summary:	Linux::KernelSort - Perl extension for sorting and comparing Linux kernel versions
Summary(pl.UTF-8):	Linux::KernelSort - rozszerzenie Perla do sortowania i porównywania wersji jądra Linuksa
Name:		perl-Linux-KernelSort
Version:	0.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Linux/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2d789b0c1eb296ea4a5ff70810ddd563
URL:		http://search.cpan.org/dist/Linux-KernelSort/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Linux::KernelSort is intended to sort a list of kernel versions into
ascending order.  It also provides the capability to compare
two kernel versions and determine if one version is newer, older,
or the same as the other version.

%description -l pl.UTF-8
Linux::KernelSort jest przeznaczone do sortowania wersji jądra Linuksa
Umożliwia również porównywanie wersji jądra.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Linux/*.pm
%{_mandir}/man3/*
