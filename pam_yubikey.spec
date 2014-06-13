Summary:	Provides support for One Time Passwords (OTP) authentication
Name:		pam_yubikey
Version:	1.0.4
Release:	12
License:	GPLv2
Group:		System/Libraries
Url:		http://www.securixlive.com/yubikey/
Source0:	http://www.securixlive.com/download/yubikey/YubiPAM-%{version}.tar.gz
Patch1:		pam_yubikey-rlimit.patch
BuildRequires:	pam-devel

%description
YubiPAM is a module for PAM that provides support for One Time Passwords (OTP)
authentication. It supports the OTPs generated from a Yubikey authentication
token. YubiPAM aims to be a simple, easy to configure, module for the Yubikey.

%prep
%setup -qn YubiPAM-%{version}
%apply_patches

%build
%serverbuild
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--disable-static \
	--with-pam-dir=/%{_lib}/security \
	--with-authdb=%{_sysconfdir}/yubikey

%make

%install
install -d %{buildroot}%{_sysconfdir}/yubikey
%makeinstall_std

%files
%doc COPYING README RELEASE.NOTES
%dir %attr(0711,root,root) %{_sysconfdir}/yubikey
/sbin/ykpasswd
/sbin/yk_chkpwd
%{_bindir}/ykvalidate
/%{_lib}/security/pam_yubikey.so

