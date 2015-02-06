%define pkgname pfennig

Summary:	Humanist sans-serif font family
Name:		fonts-ttf-pfennig
Version:	20110924
Release:	2
License:	OFL
Group:		System/Fonts/True type
URL:		http://io.debian.net/~danielj/
Source0:	http://io.debian.net/~danielj/pfennig/%{pkgname}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch:	noarch
BuildRequires:	freetype-tools
BuildRequires:	dos2unix

%description
Pfennig is a humanist sans-serif font with support for Latin, Cyrillic, Greek
and Hebrew character sets. It contains sufficient characters for Latin-0
through Latin-10, as well as glyphs for all modern Cyrillic orthographies,
the full Vietnamese range, modern Greek, modern Hebrew, and the Pan-African
Alphabet. It supports the standard Roman ligatures and uses OpenType tables
for diacritic placement. The italic faces are true italics, not just oblique.

%prep
%setup -q -c -n %{pkgname}-%{version}
dos2unix *.txt

%build

%install
%__rm -rf %{buildroot}

%__mkdir_p %{buildroot}%{_xfontdir}/TTF/pfennig

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/pfennig
ttmkfdir %{buildroot}%{_xfontdir}/TTF/pfennig -o %{buildroot}%{_xfontdir}/TTF/pfennig/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/pfennig/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/pfennig \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-pfennig:pri=50

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc FONTLOG.txt OFL.txt
%dir %{_xfontdir}/TTF/pfennig
%{_xfontdir}/TTF/pfennig/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/pfennig/fonts.dir
%{_xfontdir}/TTF/pfennig/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-pfennig:pri=50


%changelog
* Fri Dec 09 2011 Dmitry Mikhirev <dmikhirev@mandriva.org> 20110924-1mdv2012.0
+ Revision: 739433
- Added new tarball
- Update to 20110924

* Sat Jul 23 2011 Sergey Zhemoitel <serg@mandriva.org> 20100831-1
+ Revision: 691278
- imported package fonts-ttf-pfennig

