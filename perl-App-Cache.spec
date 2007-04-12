%define realname   App-Cache

Name:		perl-%{realname}
Version:    0.31
Release:    %mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
Summary:    Module for easy application-level caching
Source0:    ftp://ftp.perl.org/pub/CPAN/modules/by-module/App/%{realname}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{realname}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	perl-devel
BuildRequires:  perl(Path::Class)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(Test::Pod)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl-libwww-perl
BuildRequires:  perl(Class::Accessor::Chained)
BuildArch:      noarch

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
%setup -q -n %{realname}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
rm -rf $RPM_BUILD_ROOT/%{perl_vendorarch}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/*
%{_mandir}/man3/*

