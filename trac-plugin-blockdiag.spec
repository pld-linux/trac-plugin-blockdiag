%define		trac_ver	0.12
%define		plugin		blockdiag
Summary:	TracBlockDiag Plugin for Trac
Name:		trac-plugin-%{plugin}
Version:	0.5.0
Release:	1
License:	GPL
Group:		Applications/WWW
Source0:	http://trac-hacks.org/changeset/latest/tracblockdiagplugin?old_path=/&filename=blockdiagplugin&format=zip#/%{plugin}-%{version}.zip
# Source0-md5:	add894ae5601a469ed9f4236a1203eb1
URL:		http://trac-hacks.org/wiki/TracBlockDiagPlugin
BuildRequires:	python-devel
Requires:	python-blockdiag
Requires:	trac >= %{trac_ver}
Suggests:	python-actdiag
Suggests:	python-nwdiag
Suggests:	python-seqdiag
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
blockdiag and seqdiag is a powerful utility to generate diagrams from
simple text format. This plugin provided wiki-processors which allow
you to embed blockdiag diagrams to wiki page.

%prep
%setup -q -n trac%{plugin}plugin
mv %{trac_ver}/* .

%build
%{__python} setup.py build
%{__python} setup.py egg_info

ver=$(awk '$1 == "Version:" {print $2}' *.egg-info/PKG-INFO)
test "$ver" = %{version}

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--single-version-externally-managed \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%post
trac-enableplugin "blockdiagplugin.web_ui.*"

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{plugin}plugin
%{py_sitescriptdir}/*-*.egg-info
