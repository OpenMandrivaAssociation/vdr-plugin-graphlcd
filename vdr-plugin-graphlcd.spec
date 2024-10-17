
%define plugin	graphlcd
%define name	vdr-plugin-%plugin
%define version	0.1.5
%define rel	12

Summary:	VDR plugin: Output to graphic LCD
Name:		%name
Version:	%version
Release:	%rel
Group:		Video
License:	GPL+
URL:		https://graphlcd.berlios.de/
Source:		vdr-%plugin-%version-stripped.tar.bz2
Patch0:		graphlcd-0.1.5-i18n-1.6.patch
Patch1:		90_graphlcd-0.1.5-1.5.3.dpatch
BuildRequires:	vdr-devel >= 1.6.0
BuildRequires:	graphlcd-devel
Requires:	vdr-abi = %vdr_abi

%description
graphlcd is a plugin for the Video Disc Recorder and shows information
about the current state of VDR on displays supported by the GraphLCD
driver library.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

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
%vdr_plugin_install

install -d -m755 %{buildroot}%{vdr_plugin_cfgdir}
cp -a graphlcd %{buildroot}%{vdr_plugin_cfgdir}

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY COPYING
%dir %{vdr_plugin_cfgdir}/graphlcd
%{vdr_plugin_cfgdir}/graphlcd/fonts
%{vdr_plugin_cfgdir}/graphlcd/logos
%config(noreplace) %{vdr_plugin_cfgdir}/graphlcd/*.alias
%config(noreplace) %{vdr_plugin_cfgdir}/graphlcd/fonts.conf*




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.1.5-10mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.1.5-9mdv2009.1
+ Revision: 359324
- rebuild for new vdr
- backportability buildrequires

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.1.5-8mdv2009.0
+ Revision: 197936
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.1.5-7mdv2009.0
+ Revision: 197678
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.3 (P1 from e-tobi)
- apply new license policy
- simplify buildrequires

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.1.5-6mdv2008.1
+ Revision: 145102
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.1.5-5mdv2008.1
+ Revision: 103142
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.1.5-4mdv2008.0
+ Revision: 50007
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 3mdv2008.0-current
+ Revision: 42093
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.1.5-2mdv2008.0
+ Revision: 22691
- rebuild for new vdr


* Fri Mar 02 2007 Anssi Hannula <anssi@mandriva.org> 0.1.5-1mdv2007.0
+ Revision: 131161
- 0.1.5

* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3-5mdv2007.1
+ Revision: 90930
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3-4mdv2007.1
+ Revision: 74021
- rebuild for new vdr
- Import vdr-plugin-graphlcd

* Tue Sep 12 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3-3mdv2007.0
- strip non-free stuff from tarball

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3-2mdv2007.0
- rebuild for new vdr

* Sat Aug 19 2006 Anssi Hannula <anssi@mandriva.org> 0.1.3-1mdv2007.0
- initial Mandriva release

