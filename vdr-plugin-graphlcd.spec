
%define plugin	graphlcd
%define name	vdr-plugin-%plugin
%define version	0.1.5
%define rel	3

Summary:	VDR plugin: Output to graphic LCD
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://graphlcd.berlios.de/
Source:		vdr-%plugin-%version-stripped.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
BuildRequires:	glcddrivers-devel
BuildRequires:	glcdgraphics-devel
Requires:	vdr-abi = %vdr_abi

%description
graphlcd is a plugin for the Video Disc Recorder and shows information
about the current state of VDR on displays supported by the GraphLCD
driver library.

%prep
%setup -q -n %plugin-%version

rm -f graphlcd/logonames.alias graphlcd/logonames.alias.1.2
mv graphlcd/logonames.alias.1.3 graphlcd/logonames.alias
chmod -R a+r graphlcd

%vdr_plugin_params_begin %plugin
# use alternative driver config file
var=CONFIG_FILE
param="-c CONFIG_FILE"
# use display DISPLAY for output
var=DISPLAY
param="-d DISPLAY"
%vdr_plugin_params_end

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}
cp -a graphlcd %{buildroot}%{_vdr_plugin_cfgdir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY COPYING
%dir %{_vdr_plugin_cfgdir}/graphlcd
%{_vdr_plugin_cfgdir}/graphlcd/fonts
%{_vdr_plugin_cfgdir}/graphlcd/logos
%config(noreplace) %{_vdr_plugin_cfgdir}/graphlcd/*.alias
%config(noreplace) %{_vdr_plugin_cfgdir}/graphlcd/fonts.conf*


