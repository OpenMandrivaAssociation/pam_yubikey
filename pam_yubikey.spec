Summary:	Provides support for One Time Passwords (OTP) authentication
Name:		pam_yubikey
Version:	1.0.4
Release:	7
License:	GPLv2
Group:		System/Libraries
URL:		http://www.securixlive.com/yubikey/
Source0:	http://www.securixlive.com/download/yubikey/YubiPAM-%{version}.tar.gz
Patch1:		pam_yubikey-rlimit.patch
BuildRequires:  pam-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
YubiPAM is a module for PAM that provides support for One Time Passwords (OTP)
authentication. It supports the OTPs generated from a Yubikey authentication
token. YubiPAM aims to be a simple, easy to configure, module for the Yubikey.

%prep

%setup -q -n YubiPAM-%{version}
%patch1 -p1

%build
%serverbuild
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
    --with-pam-dir=/%{_lib}/security \
    --with-authdb=%{_sysconfdir}/yubikey

%make

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_sysconfdir}/yubikey

%makeinstall_std

# cleanup
rm -f %{buildroot}/%{_lib}/security/*.*a

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING README RELEASE.NOTES
%dir %attr(0711,root,root) %{_sysconfdir}/yubikey
%attr(0755,root,root) /sbin/ykpasswd
%attr(0755,root,root) /sbin/yk_chkpwd
%attr(0755,root,root) %{_bindir}/ykvalidate
%attr(0755,root,root) /%{_lib}/security/pam_yubikey.so



%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-5mdv2011.0
+ Revision: 666983
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-4mdv2011.0
+ Revision: 607065
- rebuild

* Sun Mar 14 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-3mdv2010.1
+ Revision: 519050
- rebuild

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.4-2mdv2010.0
+ Revision: 426354
- rebuild

* Wed Mar 18 2009 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-1mdv2009.1
+ Revision: 357407
- 1.0.4

* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2009.0
+ Revision: 285181
- import pam_yubikey


* Tue Sep 16 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-1mdv2009.0
- initial Mandriva package
