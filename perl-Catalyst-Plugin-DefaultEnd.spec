#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-DefaultEnd
Summary:	Catalyst::Plugin::DefaultEnd - Sensible default end action
Summary(pl):	Catalyst::Plugin::DefaultEnd - sensowna domy¶lna akcja koñcz±ca
Name:		perl-Catalyst-Plugin-DefaultEnd
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	96a211646bc1e734a464eff360af8825
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

%description -l pl
Ta akcja implementuje sensown± domy¶ln± akcjê koñcz±c±,
przekierowuj±c± na pierwszy dostêpny widok, chyba ¿e status ustawiono
na 3xx lub istnieje cia³o odpowiedzi. Pozwala tak¿e przekazaæ
dump_info=1 do URL-a w celu wymuszenia ekranu diagnostycznego w
przypadku w³±czonego trybu ¶ledzenia (debug mode).

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
