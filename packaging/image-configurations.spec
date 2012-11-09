%define baseline tizen-3.0
Summary:	Create kickstart files for Tizen images
Name:		image-configurations
Version:	100
Release:	1
License:	GPLv2
Group:		System/Base
URL:		http://www.tizen.org
Source:		image-configurations-%{version}.tar.bz2

BuildArch:	noarch
BuildRequires:  kickstarter >= 0.15
BuildRequires:  meta-base

%description
Create Configuration files to build Tizen images 

%prep
%setup -q


%build
kickstarter -c /usr/share/image-configurations/base/base.yaml -r /usr/share/image-configurations/base/base-repos.yaml -i image-configs.xml

%install

mkdir -p %{buildroot}/usr/share/image-configurations
cp %{baseline}/*.ks %{buildroot}/usr/share/image-configurations
cp image-configs.xml %{buildroot}/usr/share/image-configurations

%files
#%dir %_datadir/image-configurations
%_datadir/image-configurations/*.ks
%_datadir/image-configurations/image-configs.xml
