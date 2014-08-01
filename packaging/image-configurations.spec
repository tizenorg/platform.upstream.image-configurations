%if %{defined profile}
%define _profile %profile
%else
%define _profile base
%endif

%define baseline tizen-3.0

Summary:	Create kickstart files for Tizen images
Name:		image-configurations
Version:	101
Release:	1
License:	GPL-2.0
Group:		System/Base
URL:		http://www.tizen.org
Source:		image-configurations-%{version}.tar.bz2
Source1001: 	image-configurations.manifest

BuildArch:	noarch
BuildRequires:  kickstarter >= 0.15
BuildRequires:  meta-%{_profile}

%description
Create Configuration files to build Tizen images 

%prep
%setup -q
cp %{SOURCE1001} .


%build
kickstarter -c /usr/share/image-configurations/%_profile/%_profile.yaml \
    -e /usr/share/image-configurations/%_profile/configs \
    -r /usr/share/image-configurations/%_profile/%_profile-repos.yaml \
    -T /usr/share/image-configurations/%_profile/%_profile-targets.yaml \
    -t %{_repository} \
    -i image-configs.xml

%install

mkdir -p %{buildroot}/usr/share/image-configurations
[ -n "$(ls -A %{baseline}/*.ks 2>/dev/null)" ] &&  cp %{baseline}/*.ks %{buildroot}/usr/share/image-configurations
cp image-configs.xml %{buildroot}/usr/share/image-configurations

%files
%manifest %{name}.manifest
#%dir %_datadir/image-configurations
%_datadir/image-configurations/*
