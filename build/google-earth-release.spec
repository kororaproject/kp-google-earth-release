Name:   google-earth-release
Version:  1.0
Release:  2%{?dist}
Summary:  Google Earth repository configuration

Group:  System Environment/Base
License:  BSD
URL:    http://google.com/earth
Source0:  %{name}-%{version}.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildArch: noarch

%description
Google Earth repository configuration.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 $RPM_BUILD_ROOT/etc/yum.repos.d
install -m 644 google-earth.repo $RPM_BUILD_ROOT/etc/yum.repos.d/

install -d -m 755 $RPM_BUILD_ROOT/etc/pki/rpm-gpg
install -m 644 RPM-GPG-KEY-google-earth $RPM_BUILD_ROOT/etc/pki/rpm-gpg/

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
/etc/pki/rpm-gpg/RPM-GPG-KEY-google-earth
%config(noreplace) /etc/yum.repos.d/google-earth.repo

%changelog
* Sat Sep 7 2013 Chris Smart <csmart@kororaproject.org> - 1.0-2
- Disable repo by default, this way we include it in ks, but users
- just need to enable it to work

* Mon Dec 26 2011 Chris Smart <chris@kororaa.org> - 1.0-1
- Initial package.
