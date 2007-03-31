#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-DefaultEnd
Summary:	Catalyst::Plugin::DefaultEnd - Sensible default end action
Summary(pl.UTF-8):	Catalyst::Plugin::DefaultEnd - sensowna domyślna akcja kończąca
Name:		perl-Catalyst-Plugin-DefaultEnd
Version:	0.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	af50b78732e8e2b2461698f8e0ac8598
URL:		http://search.cpan.org/dist/Catalyst-Plugin-DefaultEnd/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.2
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This action implements a sensible default end action, which will
forward to the first available view, unless status is set to 3xx, or
there is a response body. It also allows you to pass dump_info=1 to
the URL in order to force a debug screen, while in debug mode.

%description -l pl.UTF-8
Ta akcja implementuje sensowną domyślną akcję kończącą,
przekierowującą na pierwszy dostępny widok, chyba że status ustawiono
na 3xx lub istnieje ciało odpowiedzi. Pozwala także przekazać
dump_info=1 do URL-a w celu wymuszenia ekranu diagnostycznego w
przypadku włączonego trybu śledzenia (debug mode).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	destdir=$RPM_BUILD_ROOT \
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Catalyst/Plugin/*.pm
%{_mandir}/man3/*
