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
BuildRequires:  meta-generic
BuildRequires:  meta-%{_profile}

%description
Create Configuration files to build Tizen images

%prep
%setup -q
cp %{SOURCE1001} .


%build

# merge the configuration files from generic and the current profile
# in the same input dir to make kickstarter aware of the generic scripts.
mkdir -p input
for profile in generic %_profile; do
	pdir=%{_datadir}/image-configurations/$profile
	[ -d $pdir ] && cp -a $pdir/* input/
done

kickstarter -c input/%_profile.yaml \
    -e input/configs \
    -r input/%_profile-repos.yaml \
    -T input/%_profile-targets.yaml \
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
