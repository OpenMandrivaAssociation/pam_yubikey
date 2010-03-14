Summary:	Provides support for One Time Passwords (OTP) authentication
Name:		pam_yubikey
Version:	1.0.4
Release:	%mkrel 3
License:	GPLv2
Group:		System/Libraries
URL:		http://www.securixlive.com/yubikey/
Source0:	http://www.securixlive.com/download/yubikey/YubiPAM-%{version}.tar.gz
BuildRequires:  pam-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
YubiPAM is a module for PAM that provides support for One Time Passwords (OTP)
authentication. It supports the OTPs generated from a Yubikey authentication
token. YubiPAM aims to be a simple, easy to configure, module for the Yubikey.

%prep

%setup -q -n YubiPAM-%{version}

%build
%serverbuild

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

