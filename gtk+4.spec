# TODO: vulkan+glslc
#
# Conditional build:
%bcond_without	apidocs		# gtk-doc build
%bcond_without	cloudprint	# cloudprint print backend
%bcond_without	cups		# CUPS print backend
%bcond_without	papi		# PAPI print backend
%bcond_without	broadway	# Broadway target
%bcond_with	mir		# Mir target
%bcond_without	wayland		# Wayland target
%bcond_without	static_libs	# static library build

Summary:	The GIMP Toolkit
Summary(cs.UTF-8):	Sada nástrojů pro GIMP
Summary(de.UTF-8):	Der GIMP-Toolkit
Summary(fi.UTF-8):	GIMP-työkalukokoelma
Summary(fr.UTF-8):	Le toolkit de GIMP
Summary(it.UTF-8):	Il toolkit per GIMP
Summary(pl.UTF-8):	GIMP Toolkit
Summary(tr.UTF-8):	GIMP ToolKit arayüz kitaplığı
Name:		gtk+4
Version:	3.90.0
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gtk+/3.90/gtk+-%{version}.tar.xz
# Source0-md5:	38df8442d7a5b96fe02e245c4f03a5e1
Patch0:		%{name}-papi.patch
URL:		http://www.gtk.org/
BuildRequires:	at-spi2-atk-devel >= 2.6.0
BuildRequires:	atk-devel >= 1:2.16.0
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
# cairo-gobject + cairo-pdf,cairo-ps,cairo-svg
BuildRequires:	cairo-gobject-devel >= 1.14.0
BuildRequires:	colord-devel >= 0.1.9
%if %{with cups} || %{with papi}
BuildRequires:	cups-devel >= 1:1.2
%endif
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gdk-pixbuf2-devel >= 2.31.0
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.51.5
BuildRequires:	gobject-introspection-devel >= 1.39.0
BuildRequires:	graphene-devel >= 1.5.1
%if %{with apidocs}
BuildRequires:	gtk-doc >= 1.25-2
BuildRequires:	gtk-doc-automake >= 1.25-2
%endif
BuildRequires:	harfbuzz-devel >= 0.9
%{?with_cloudprint:BuildRequires:	json-glib-devel >= 1.0}
BuildRequires:	libepoxy-devel >= 1.0
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-progs >= 1:2.6.31
BuildRequires:	libxslt-progs >= 1.1.20
# mirclient >= 0.22.0, mircookie >= 0.17.0
%{?with_mir:BuildRequires:	mir-devel >= 0.22.0}
BuildRequires:	pango-devel >= 1:1.38.0
%{?with_papi:BuildRequires:	papi-devel}
BuildRequires:	perl-base
BuildRequires:	pkgconfig
%{?with_cloudprint:BuildRequires:	rest-devel >= 0.7}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.592
BuildRequires:	sqlite3-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libX11-devel >= 1.5.0
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5.0
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xz
%{?with_broadway:BuildRequires:	zlib-devel}
%if %{with wayland}
BuildRequires:	Mesa-libwayland-egl-devel
# wayland-client, wayland-cursor, wayland-scanner
BuildRequires:	wayland-devel >= 1.9.91
BuildRequires:	wayland-protocols >= 1.7
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.2.0
%endif
Requires:	xorg-lib-libX11 >= 1.5.0
Requires(post,postun):	glib2 >= 1:2.51.5
Requires:	atk >= 1:2.16.0
Requires:	cairo-gobject >= 1.14.0
Requires:	gdk-pixbuf2 >= 2.31.0
Requires:	glib2 >= 1:2.51.5
Requires:	graphene >= 1.5.1
Requires:	libepoxy >= 1.0
Requires:	pango >= 1:1.38.0
Requires:	xorg-lib-libXi >= 1.3.0
Requires:	xorg-lib-libXrandr >= 1.5.0
%if %{with wayland}
Requires:	wayland >= 1.9.91
Requires:	xorg-lib-libxkbcommon >= 0.2.0
%endif
# evince is used as gtk-print-preview-command by default
Suggests:	evince-backend-pdf
%if %{with cups}
# cups is used by default if gtk+ is built with cups
Suggests:	%{name}-cups = %{version}-%{release}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abivers	4.0.0

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		pqext		-%{libext}
%else
%define		pqext		%{nil}
%endif

%description
GTK+, which stands for the GIMP ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK+ is written in C with a very
object-oriented approach. GDK (part of GTK+) is a drawing toolkit
which provides a thin layer over Xlib to help automate things like
dealing with different color depths, and GTK is a widget set for
creating user interfaces.

%description -l cs.UTF-8
Knihovny X původně psané pro GIMP, které nyní používá také řada jiných
programů.

%description -l da.UTF-8
X biblioteker, oprindeligt udviklet til GIMP, men anvendes nu af flere
forskellige programmer.

%description -l de.UTF-8
Die X-Libraries, die ursprünglich für GIMP geschrieben wurden und
mittlerweile für eine ganze Reihe anderer Programme benutzt werden.

%description -l fr.UTF-8
X-kirjastot, jotka alunperin kirjoitettiin GIMP:lle, mutta joita
käytetään nyt myös useissa muissakin ohjelmissa.

%description -l it.UTF-8
Libreria X scritta per GIMP. Viene usata da diversi programmi.

%description -l pl.UTF-8
GTK+, która to biblioteka stała się podstawą programu GIMP, zawiera
funkcje do tworzenia graficznego interfejsu użytkownika pod X Window.
Była tworzona z założeniem żeby była mała, efektywna i wygodna. GTK+
jest napisane w C z podejściem zorientowanym bardzo obiektowo. GDK
(część GTK+) jest warstwą pośrednią pomiędzy Xlib a właściwym GTK
zapewniającą pracę niezależnie od głębi koloru (ilości bitów na
piksel). GTK (druga część GTK+) jest natomiast już zbiorem różnego
rodzaju kontrolek służących do tworzenia interfejsu użytkownika.

%description -l tr.UTF-8
Başlangıçta GIMP için yazılmış X kitaplıkları. Şu anda başka
programlarca da kullanılmaktadır.

%package update-icon-cache
Summary:	Utility to update icon cache used by GTK+ library
Summary(pl.UTF-8):	Narzędzie do uaktualniania cache'a ikon używanego przez bibliotekę GTK+
Group:		Applications/System
Requires:	gdk-pixbuf2 >= 2.31.0
Requires:	glib2 >= 1:2.51.5

%description update-icon-cache
Utility to update icon cache used by GTK+ library.

%description update-icon-cache -l pl.UTF-8
Narzędzie do uaktualniania cache'a ikon używanego przez bibliotekę
GTK+.

%package devel
Summary:	GTK+ header files and development documentation
Summary(cs.UTF-8):	Sada nástrojů GIMP a kreslící kit GIMP
Summary(da.UTF-8):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de.UTF-8):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi.UTF-8):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr.UTF-8):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it.UTF-8):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do GTK+
Summary(tr.UTF-8):	GIMP araç takımı ve çizim takımı
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	at-spi2-atk-devel >= 2.6.0
Requires:	atk-devel >= 1:2.16.0
Requires:	cairo-gobject-devel >= 1.14.0
Requires:	gdk-pixbuf2-devel >= 2.31.0
Requires:	glib2-devel >= 1:2.51.5
Requires:	graphene-devel >= 1.5.1
Requires:	pango-devel >= 1:1.38.0
Requires:	shared-mime-info

%description devel
Header files and development documentation for the GTK+ libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek GTK+.

%package static
Summary:	GTK+ static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GTK+
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
GTK+ static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GTK+

%package apidocs
Summary:	GTK+ API documentation
Summary(pl.UTF-8):	Dokumentacja API GTK+
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
GTK+ API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GTK+.

%package examples
Summary:	GTK+ - example programs
Summary(pl.UTF-8):	GTK+ - programy przykładowe
Group:		X11/Development/Libraries
Requires(post,postun):	glib2 >= 1:2.51.5
Requires:	%{name}-devel = %{version}-%{release}

%description examples
GTK+ - example programs.

%description examples -l pl.UTF-8
GTK+ - przykładowe programy.

%package cloudprint
Summary:	Cloudprint printing module for GTK+
Summary(pl.UTF-8):	Moduł GTK+ do drukowania przez Cloudprint
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description cloudprint
Cloudprint printing module for GTK+.

%description cloudprint -l pl.UTF-8
Moduł GTK+ do drukowania przez Cloudprint.

%package cups
Summary:	CUPS printing module for GTK+
Summary(pl.UTF-8):	Moduł GTK+ do drukowania przez CUPS
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}

%description cups
CUPS printing module for GTK+.

%description cups -l pl.UTF-8
Moduł GTK+ do drukowania przez CUPS.

%package papi
Summary:	PAPI printing module for GTK+
Summary(pl.UTF-8):	Moduł GTK+ do drukowania przez PAPI
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	papi

%description papi
PAPI printing module for GTK+.

%description papi -l pl.UTF-8
Moduł GTK+ do drukowania przez PAPI.

%prep
%setup -q -n gtk+-%{version}
%patch0 -p1

# for packaging clean examples
# TODO: add am patch to do it like demos/gtk-demo via some configurable dir
# NOTE: make install so far installs only demos/gtk-demo
install -d _examples
cp -a demos examples _examples

# upstream used too new wayland for make dist in 3.10.6 - force regeneration
touch gdk/wayland/protocol/gtk-shell.xml

%build
CPPFLAGS="%{rpmcppflags}%{?with_papi: -I/usr/include/papi}"
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules \
	%{!?with_cloudprint:--disable-cloudprint} \
	%{__disable cups} \
	%{!?with_papi:--disable-papi} \
	%{?debug:--enable-debug=yes} \
	%{__enable_disable apidocs gtk-doc} \
	--enable-man \
	%{__enable_disable static_libs static} \
	%{?with_broadway:--enable-broadway-backend} \
	%{?with_mir:--enable-mir-backend} \
	%{?with_wayland:--enable-wayland-backend} \
	--enable-x11-backend \
	--enable-xinerama \
	--enable-xkb \
	--with-html-dir=%{_gtkdocdir}

%{__make} \
	democodedir=%{_examplesdir}/%{name}-%{version}/demos/gtk-demo

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/%{abivers}/engines
install -d $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/%{abivers}/theming-engines

%{__make} install \
	democodedir=%{_examplesdir}/%{name}-%{version}/demos/gtk-demo \
	DESTDIR=$RPM_BUILD_ROOT

touch $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/%{abivers}/gtk.immodules
install -d $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/modules

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a _examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

# shut up check-files (static modules and *.la for modules)
%{__rm} -r $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/%{abivers}/*/*.la \
	%{?with_static_libs:$RPM_BUILD_ROOT%{_libdir}/gtk-4.0/%{abivers}/*/*.a}

%if "%{_lib}" != "lib"
# We need to have 32-bit and 64-bit binaries as they have hardcoded LIBDIR.
# (needed when multilib is used)
%{__mv} $RPM_BUILD_ROOT%{_bindir}/gtk4-query-immodules{,%{pqext}}
%endif

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}
# unsupported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/io

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name} --all-name

%{!?with_apidocs:%{__rm} -r $RPM_BUILD_ROOT%{_gtkdocdir}/{gdk4,gtk4}}

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas
umask 022
%{_bindir}/gtk4-query-immodules%{pqext} --update-cache
exit 0

%postun
/sbin/ldconfig
if [ "$1" != "0" ]; then
	umask 022
	%{_bindir}/gtk4-query-immodules%{pqext} --update-cache
else
	%glib_compile_schemas
fi
exit 0

%post examples
%glib_compile_schemas

%postun examples
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%{?with_broadway:%attr(755,root,root) %{_bindir}/gtk4-broadwayd}
%attr(755,root,root) %{_bindir}/gtk4-launch
%attr(755,root,root) %{_bindir}/gtk4-query-immodules%{pqext}
%attr(755,root,root) %{_libdir}/libgtk-4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-4.so.0

%dir %{_libdir}/gtk-4.0
%dir %{_libdir}/gtk-4.0/modules
%dir %{_libdir}/gtk-4.0/%{abivers}
%dir %{_libdir}/gtk-4.0/%{abivers}/engines
%dir %{_libdir}/gtk-4.0/%{abivers}/theming-engines
%dir %{_libdir}/gtk-4.0/%{abivers}/immodules
%dir %{_libdir}/gtk-4.0/%{abivers}/printbackends
%ghost %{_libdir}/gtk-4.0/%{abivers}/gtk.immodules
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-file.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-lpr.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-am-et.so
%{?with_broadway:%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-broadway.so}
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-cedilla.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-cyrillic-translit.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-inuktitut.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-ipa.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-multipress.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-thai.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-ti-er.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-ti-et.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-viqr.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/immodules/im-xim.so
%{_libdir}/girepository-1.0/Gdk-4.0.typelib
%{_libdir}/girepository-1.0/GdkX11-4.0.typelib
%{_libdir}/girepository-1.0/Gsk-4.0.typelib
%{_libdir}/girepository-1.0/Gtk-4.0.typelib

%dir %{_sysconfdir}/gtk-4.0
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/gtk-4.0/im-multipress.conf
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.ColorChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.Debug.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.Settings.FileChooser.gschema.xml
%dir %{_datadir}/themes/Default/gtk-4.0
%{_datadir}/themes/Default/gtk-4.0/gtk-keys.css
%dir %{_datadir}/themes/Emacs
%dir %{_datadir}/themes/Emacs/gtk-4.0
%{_datadir}/themes/Emacs/gtk-4.0/gtk-keys.css
%{?with_broadway:%{_mandir}/man1/gtk4-broadwayd.1*}
%{_mandir}/man1/gtk4-launch.1*
%{_mandir}/man1/gtk4-query-immodules.1*

%files update-icon-cache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk4-encode-symbolic-svg
%attr(755,root,root) %{_bindir}/gtk4-update-icon-cache
%{_mandir}/man1/gtk4-encode-symbolic-svg.1*
%{_mandir}/man1/gtk4-update-icon-cache.1*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/gtk4-builder-tool
%attr(755,root,root) %{_bindir}/gtk4-query-settings
%attr(755,root,root) %{_libdir}/libgtk-4.so
%{_includedir}/gtk-4.0
%{_pkgconfigdir}/gail-4.0.pc
%{_pkgconfigdir}/gtk+-4.0.pc
%{_pkgconfigdir}/gtk+-unix-print-4.0.pc
%{_pkgconfigdir}/gtk+-x11-4.0.pc
%if %{with broadway}
%{_pkgconfigdir}/gtk+-broadway-4.0.pc
%endif
%if %{with mir}
%{_pkgconfigdir}/gtk+-mir-4.0.pc
%endif
%if %{with wayland}
%{_pkgconfigdir}/gtk+-wayland-4.0.pc
%endif
%{_datadir}/gettext/its/gtkbuilder.its
%{_datadir}/gettext/its/gtkbuilder.loc
%{_datadir}/gtk-4.0
%{_datadir}/gir-1.0/Gdk-4.0.gir
%{_datadir}/gir-1.0/GdkX11-4.0.gir
%{_datadir}/gir-1.0/Gsk-4.0.gir
%{_datadir}/gir-1.0/Gtk-4.0.gir
%{_mandir}/man1/gtk4-builder-tool.1*
%{_mandir}/man1/gtk4-query-settings.1*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgtk-4.a
%endif

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/gdk4
%{_gtkdocdir}/gsk4
%{_gtkdocdir}/gtk4
%endif

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk4-demo
%attr(755,root,root) %{_bindir}/gtk4-demo-application
%attr(755,root,root) %{_bindir}/gtk4-icon-browser
%attr(755,root,root) %{_bindir}/gtk4-widget-factory
%{_datadir}/glib-2.0/schemas/org.gtk.Demo.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.exampleapp.gschema.xml
%{_desktopdir}/gtk4-demo.desktop
%{_desktopdir}/gtk4-icon-browser.desktop
%{_desktopdir}/gtk4-widget-factory.desktop
%{_iconsdir}/hicolor/*/apps/gtk4-demo-symbolic.symbolic.png
%{_iconsdir}/hicolor/*/apps/gtk4-demo.png
%{_iconsdir}/hicolor/*/apps/gtk4-widget-factory-symbolic.symbolic.png
%{_iconsdir}/hicolor/*/apps/gtk4-widget-factory.png
%{_mandir}/man1/gtk4-demo.1*
%{_mandir}/man1/gtk4-demo-application.1*
%{_mandir}/man1/gtk4-icon-browser.1*
%{_mandir}/man1/gtk4-widget-factory.1*
%{_examplesdir}/%{name}-%{version}

%if %{with cloudprint}
%files cloudprint
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-cloudprint.so
%endif

%if %{with cups}
%files cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-cups.so
%endif

%if %{with papi}
%files papi
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-papi.so
%endif