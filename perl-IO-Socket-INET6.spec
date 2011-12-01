Name:           perl-IO-Socket-INET6
Version:        2.56
Release:        4%{?dist}
Summary:        Perl Object interface for AF_INET|AF_INET6 domain sockets

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/~mondejar/IO-Socket-INET6/
Source0:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/IO-Socket-INET6-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Socket6)
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:  perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Perl Object interface for AF_INET|AF_INET6 domain sockets 

%prep
%setup -q -n IO-Socket-INET6-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


#%check
#make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc README ChangeLog
%{perl_vendorlib}/*
%{_mandir}/man3/*.3*

%changelog
* Wed Jan 27 2010 Stepan Kasal <skasal@redhat.com> - 2.56-4
- fix the source url

* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 2.56-3
- rebuild against perl 5.10.1

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.56-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 13 2009 Warren Togami <wtogami@redhat.com> - 2.56-1
- 2.56

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.54-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Mar 26 2008 Warren Togami <wtogami@redhat.com> - 2.54-1
- 2.54

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.51-5
- Rebuild for perl 5.10 (again)

* Thu Jan 31 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.51-4
- rebuild for new perl

* Fri Nov 16 2007 Parag Nemade <panemade@gmail.com> - 2.51-3
- Merge Review(#226263) Spec cleanup

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 2.51-2.1
- correct license tag
- add BR: perl(ExtUtils::MakeMaker)

* Thu Jul 06 2006 Warren Togami <wtogami@redhat.com> 2.51-2
- minor spec fixes (#197821)

* Thu Jul 06 2006 Warren Togami <wtogami@redhat.com> 2.51-1
- initial Fedora package
