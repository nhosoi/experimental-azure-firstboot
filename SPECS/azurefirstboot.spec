Name:		azurefirstboot
Version:	0.4
Release:	1
Summary:	runs ansible playbooks after firstboot

Group:		Tools
License:	GPL v3
URL:		http://github.com/rhmk/firstboot
Source0:	%{name}-%{version}.tar.gz
BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch:	noarch

Requires:	/bin/bash
Requires:	ansible

%description
This is a first boot startup service that runs a couple of ansible-playbooks

%prep
%setup -q


%build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p ${RPM_BUILD_ROOT}/etc/init.d
install -m 755  rootfs/etc/init.d/azfirstboot.sh ${RPM_BUILD_ROOT}/etc/init.d/azfirstboot.sh
chcon -u system_u -t initrc_exec_t ${RPM_BUILD_ROOT}/etc/init.d/azfirstboot.sh
mkdir -p ${RPM_BUILD_ROOT}/etc/systemd/system
install -m 644  rootfs/etc/systemd/system/azfirstboot.service ${RPM_BUILD_ROOT}/etc/systemd/system/azfirstboot.service
chcon -u system_u -t systemd_unit_file_t ${RPM_BUILD_ROOT}/etc/systemd/system/azfirstboot.service
#mkdir -p ${RPM_BUILD_ROOT}/etc/azfirstboot.d

%clean
rm -rf $RPM_BUILD_ROOT

%preun
systemctl disable azfirstboot

%post
systemctl enable azfirstboot

%files
%defattr(-,root,root,-)
/etc/init.d/azfirstboot.sh
/etc/systemd/system/azfirstboot.service

%doc



%changelog
* Fri Jan 18 2019 Markus Koch |mkoch@redhat.com> - 0.4
- bugfixes
* Fri Dec 21 2018 Markus Koch |mkoch@redhat.com> - 0.1
- initial build

