%define upstream_name    App-Cache
%define upstream_version 0.37

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Module for easy application-level caching
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/App/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor::Chained)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::HomeDir)
BuildRequires:	perl-libwww-perl
BuildRequires:	perl(Path::Class)
BuildRequires:	perl(Test::Pod)

BuildArch:	noarch

%description
The App::Cache module lets an application cache data locally. There are a few 
times an application would need to cache data: when it is retrieving 
information from the network or when it has to complete a large calculation.

For example, the Parse::BACKPAN::Packages module downloads a file off the net 
and parses it, creating a data structure. Only then can it actually provide 
any useful information for the programmer. Parse::BACKPAN::Packages uses 
App::Cache to cache both the file download and data structures, providing 
much faster use when the data is cached.

This module stores data in the home directory of the user, in a dot directory. 
For example, the Parse::BACKPAN::Packages cache isactually stored 
underneath "~/.parse_backpan_packages/cache/". This is so that permisssions 
are not a problem - it is a per-user, per-application cache.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}

%files
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.370.0-2mdv2011.0
+ Revision: 680470
- mass rebuild

* Wed Dec 09 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.370.0-1mdv2011.0
+ Revision: 475395
- update to 0.37

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.360.0-1mdv2010.0
+ Revision: 405954
- rebuild using %%perl_convert_version

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2010.0
+ Revision: 389772
- update to new version 0.36

* Thu Sep 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.0
+ Revision: 283882
- update to new version 0.35

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2009.0
+ Revision: 272257
- update to new version 0.34

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.33-3mdv2009.0
+ Revision: 255288
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2008.1
+ Revision: 97362
- update to new version 0.33

  + Michael Scherer <misc@mandriva.org>
    - rebuild


* Thu Apr 27 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.31-5mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL

* Tue Dec 27 2005 Michael Scherer <misc@mandriva.org> 0.31-4mdk
- Do not ship empty dir

* Mon Oct 10 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.31-3mdk
- Fix BuildRequires

* Fri Sep 30 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.31-2mdk
- Buildrequires fix

* Wed Sep 21 2005 Michael Scherer <misc@mandriva.org> 0.31-1mdk
- First mandriva package

