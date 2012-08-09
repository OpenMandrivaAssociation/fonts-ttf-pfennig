%define pkgname pfennig

Summary:	Humanist sans-serif font family
Name:		fonts-ttf-pfennig
Version:	20120410
Release:	%mkrel 1
License:	OFL
Group:		System/Fonts/True type
URL:		http://io.debian.net/~danielj/
Source0:	%{pkgname}.zip
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
%__mkdir_p %{buildroot}%{_xfontdir}/TTF/pfennig

%__install -m 644 *.ttf %{buildroot}%{_xfontdir}/TTF/pfennig
ttmkfdir %{buildroot}%{_xfontdir}/TTF/pfennig -o %{buildroot}%{_xfontdir}/TTF/pfennig/fonts.dir
%__ln_s fonts.dir %{buildroot}%{_xfontdir}/TTF/pfennig/fonts.scale

%__mkdir_p %{buildroot}%_sysconfdir/X11/fontpath.d/
%__ln_s ../../..%{_xfontdir}/TTF/pfennig \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-pfennig:pri=50

%files
%defattr(0644,root,root,0755)
%doc FONTLOG.txt OFL.txt
%dir %{_xfontdir}/TTF/pfennig
%{_xfontdir}/TTF/pfennig/*.ttf
%verify(not mtime) %{_datadir}/fonts/TTF/pfennig/fonts.dir
%{_xfontdir}/TTF/pfennig/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-pfennig:pri=50
