#
# Conditional build:
%bcond_without	apidocs		# gi-docgen based API documentation
%bcond_without	broadway	# Broadway target
%bcond_without	wayland		# Wayland target
%bcond_without	vulkan		# Vulkan graphics support
%bcond_without	ffmpeg		# FFmpeg media backend
%bcond_without	gstreamer	# GStreamer media backend
%bcond_without	cups		# CUPS print backend
%bcond_without	cloudproviders	# cloudproviders support
%bcond_without	static_libs	# static library
%bcond_with	sysprof		# sysprof tracing support
%bcond_with	tracker		# Tracker3 filechooser search

Summary:	The GIMP Toolkit
Summary(cs.UTF-8):	Sada nástrojů pro GIMP
Summary(de.UTF-8):	Der GIMP-Toolkit
Summary(fi.UTF-8):	GIMP-työkalukokoelma
Summary(fr.UTF-8):	Le toolkit de GIMP
Summary(it.UTF-8):	Il toolkit per GIMP
Summary(pl.UTF-8):	GIMP Toolkit
Summary(tr.UTF-8):	GIMP ToolKit arayüz kitaplığı
Name:		gtk4
Version:	4.6.4
Release:	1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	https://download.gnome.org/sources/gtk/4.6/gtk-%{version}.tar.xz
# Source0-md5:	1a118b965febe60fa9a2734ec0ddc5c5
Patch0:		%{name}-lpr.patch
URL:		https://www.gtk.org/
%{?with_vulkan:BuildRequires:	Vulkan-Loader-devel}
# cairo-gobject + cairo-pdf,cairo-ps,cairo-svg
BuildRequires:	cairo-gobject-devel >= 1.14.0
BuildRequires:	colord-devel >= 0.1.9
%if %{with cups}
BuildRequires:	cups-devel >= 1:2.0
%endif
BuildRequires:	docbook-dtd412-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	fontconfig-devel
# libavfilter >= 6.47.100, libavformat >= 57.41.100, libavcodec >= 57.48.101, libavutil >= 55.28.100, libswscale >= 4.6.100
%{?with_ffmpeg:BuildRequires:	ffmpeg-devel >= 3.1.1}
BuildRequires:	freetype-devel >= 1:2.7.1
BuildRequires:	fribidi-devel >= 0.19.7
BuildRequires:	gdk-pixbuf2-devel >= 2.31.0
BuildRequires:	gettext-tools >= 0.19.7
%{?with_apidocs:BuildRequires:	gi-docgen >= 2021.1}
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gobject-introspection-devel >= 1.39.0
BuildRequires:	graphene-devel >= 1.9.1
%{?with_gstreamer:BuildRequires:	gstreamer-devel >= 1.12.3}
# pkgconfig(gstreamer-player-1.0)
%{?with_gstreamer:BuildRequires:	gstreamer-plugins-bad-devel >= 1.12.3}
BuildRequires:	harfbuzz-devel >= 2.1.0
BuildRequires:	iso-codes
%{?with_cloudproviders:BuildRequires:	libcloudproviders-devel >= 0.3.1}
BuildRequires:	libepoxy-devel >= 1.4
BuildRequires:	libjpeg-turbo-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel >= 4
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libxml2-progs >= 1:2.6.31
BuildRequires:	libxslt-progs >= 1.1.20
BuildRequires:	meson >= 0.59
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.50.0
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.752
# glslc required to rebuild some files from source
%{?with_vulkan:BuildRequires:	shaderc}
BuildRequires:	sqlite3-devel
%{?with_sysprof:BuildRequires:	sysprof-devel >= 3.38.0}
BuildRequires:	tar >= 1:1.22
%{?with_tracker:BuildRequires:	tracker3-devel >= 3.0}
BuildRequires:	xorg-lib-libX11-devel >= 1.5.0
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.8
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5.0
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xz
%{?with_broadway:BuildRequires:	zlib-devel}
%if %{with wayland}
# wayland-client, wayland-cursor, wayland-scanner
BuildRequires:	wayland-devel >= 1.20.0
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.23
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.2.0
%endif
Requires:	xorg-lib-libX11 >= 1.5.0
Requires(post,postun):	glib2 >= 1:2.66.0
Requires:	cairo-gobject >= 1.14.0
Requires:	freetype >= 1:2.7.1
Requires:	gdk-pixbuf2 >= 2.31.0
Requires:	glib2 >= 1:2.66.0
Requires:	graphene >= 1.9.1
Requires:	harfbuzz >= 2.1.0
Requires:	iso-codes
%{?with_cloudproviders:Requires:	libcloudproviders >= 0.3.1}
Requires:	libepoxy >= 1.4
Requires:	pango >= 1:1.50.0
Requires:	xorg-lib-libXi >= 1.8
Requires:	xorg-lib-libXrandr >= 1.5.0
%if %{with wayland}
Requires:	wayland >= 1.20.0
Requires:	xorg-lib-libxkbcommon >= 0.2.0
%endif
# evince is used as gtk-print-preview-command by default
Suggests:	evince-backend-pdf
%if %{with cups}
# cups is used by default if gtk is built with cups
Suggests:	%{name}-cups = %{version}-%{release}
%endif
Obsoletes:	gtk+4 < 3.95
Obsoletes:	gtk+4-papi < 3.94
Obsoletes:	gtk+4-cloudprint < 3.95
Obsoletes:	gtk4-cloudprint < 4.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		abivers	4.0.0

%if "%{_lib}" != "lib"
%define		libext		%(lib="%{_lib}"; echo ${lib#lib})
%define		pqext		-%{libext}
%else
%define		pqext		%{nil}
%endif

%description
GTK, which stands for the GIMP ToolKit, is a library for creating
graphical user interfaces for the X Window System. It is designed to
be small, efficient, and flexible. GTK is written in C with a very
object-oriented approach. GDK (part of GTK) is a drawing toolkit
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
GTK, która to biblioteka stała się podstawą programu GIMP, zawiera
funkcje do tworzenia graficznego interfejsu użytkownika pod X Window.
Była tworzona z założeniem żeby była mała, efektywna i wygodna. GTK
jest napisane w C z podejściem zorientowanym bardzo obiektowo. GDK
(część GTK) jest warstwą pośrednią pomiędzy Xlib a właściwym GTK
zapewniającą pracę niezależnie od głębi koloru (ilości bitów na
piksel). GTK (druga część GTK) jest natomiast już zbiorem różnego
rodzaju kontrolek służących do tworzenia interfejsu użytkownika.

%description -l tr.UTF-8
Başlangıçta GIMP için yazılmış X kitaplıkları. Şu anda başka
programlarca da kullanılmaktadır.

%package update-icon-cache
Summary:	Utility to update icon cache used by GTK library
Summary(pl.UTF-8):	Narzędzie do uaktualniania cache'a ikon używanego przez bibliotekę GTK
Group:		Applications/System
Requires:	gdk-pixbuf2 >= 2.31.0
Requires:	glib2 >= 1:2.66.0
Obsoletes:	gtk+4-update-icon-cache < 3.95

%description update-icon-cache
Utility to update icon cache used by GTK library.

%description update-icon-cache -l pl.UTF-8
Narzędzie do uaktualniania cache'a ikon używanego przez bibliotekę
GTK.

%package devel
Summary:	GTK header files and development documentation
Summary(cs.UTF-8):	Sada nástrojů GIMP a kreslící kit GIMP
Summary(da.UTF-8):	GIMP Toolkit og GIMP Tegnings-værktøj
Summary(de.UTF-8):	GIMP Toolkit und GIMP Drawing Kit
Summary(fi.UTF-8):	Gimp-työkalukokoelma ja Gimp-piirtotyökalut
Summary(fr.UTF-8):	Toolkit de GIMP (GTK) et Kit de dessin de GIMP (GDK)
Summary(it.UTF-8):	GIMP Toolkit and GIMP Drawing Kit
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do GTK
Summary(tr.UTF-8):	GIMP araç takımı ve çizim takımı
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
%{?with_vulkan:Requires:	Vulkan-Loader-devel}
Requires:	cairo-gobject-devel >= 1.14.0
Requires:	fontconfig-devel
Requires:	gdk-pixbuf2-devel >= 2.31.0
Requires:	glib2-devel >= 1:2.65.0
Requires:	graphene-devel >= 1.9.1
Requires:	libepoxy-devel >= 1.4
Requires:	pango-devel >= 1:1.50.0
Requires:	shared-mime-info
Requires:	xorg-lib-libX11-devel >= 1.5.0
Requires:	xorg-lib-libXcomposite-devel
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXi-devel >= 1.8
Requires:	xorg-lib-libXinerama-devel
Requires:	xorg-lib-libXrandr-devel >= 1.5.0
%if %{with wayland}
Requires:	wayland-devel >= 1.20.0
Requires:	wayland-egl-devel
Requires:	wayland-protocols >= 1.23
Requires:	xorg-lib-libxkbcommon-devel >= 0.2.0
%endif
Requires:	zlib-devel
Obsoletes:	gtk+4-devel < 3.95

%description devel
Header files and development documentation for the GTK libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do bibliotek GTK.

%package static
Summary:	GTK static libraries
Summary(pl.UTF-8):	Biblioteki statyczne GTK
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gtk+4-static < 3.95

%description static
GTK static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne GTK

%package apidocs
Summary:	GTK API documentation
Summary(pl.UTF-8):	Dokumentacja API GTK
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	gtk+4-apidocs < 3.95
BuildArch:	noarch

%description apidocs
GTK API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API GTK.

%package examples
Summary:	GTK - example programs
Summary(pl.UTF-8):	GTK - programy przykładowe
Group:		X11/Development/Libraries
Requires(post,postun):	glib2 >= 1:2.65.0
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	gtk+4-examples < 3.95

%description examples
GTK - example programs.

%description examples -l pl.UTF-8
GTK - przykładowe programy.

%package media-ffmpeg
Summary:	FFmpeg media backend for GTK
Summary(pl.UTF-8):	Backend multimedialny FFmpeg dla GTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ffmpeg-libs >= 3.1.1

%description media-ffmpeg
FFmpeg media backend for GTK.

%description media-ffmpeg -l pl.UTF-8
Backend multimedialny FFmpeg dla GTK.

%package media-gstreamer
Summary:	GStreamer media backend for GTK
Summary(pl.UTF-8):	Backend multimedialny GStreamer dla GTK
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gstreamer >= 1.12.3

%description media-gstreamer
GStreamer media backend for GTK.

%description media-gstreamer -l pl.UTF-8
Backend multimedialny GStreamer dla GTK.

%package cups
Summary:	CUPS printing module for GTK
Summary(pl.UTF-8):	Moduł GTK do drukowania przez CUPS
Group:		X11/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cups-lib >= 2.0
Obsoletes:	gtk+4-cups < 3.95

%description cups
CUPS printing module for GTK.

%description cups -l pl.UTF-8
Moduł GTK do drukowania przez CUPS.

%prep
%setup -q -n gtk-%{version}
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/env python3,%{__python3},' demos/gtk-demo/geninclude.py
%{__sed} -i -e '1s,/usr/bin/env .* gjs,/usr/bin/gjs,' examples/labels.js
%{__sed} -i -e '1s,/usr/bin/env .* python3,%{__python3},' examples/squares.py

%if %{with static_libs}
%{__sed} -i -e '/^libgtk = / s/shared_library/library/' gtk/meson.build
%endif

# FIXME: common location for gi-docgen generated docs
%{__sed} -i -e "/^docs_dir =/ s,gtk_datadir / 'doc','%{_gtkdocdir}'," docs/reference/meson.build

%build
%meson build \
	%{?with_broadway:-Dbroadway-backend=true} \
	%{?with_cloudproviders:-Dcloudproviders=enabled} \
	-Dcolord=enabled \
	%{?with_apidocs:-Dgtk_doc=true} \
	-Dinstall-tests=false \
	-Dman-pages=true \
	%{?with_ffmpeg:-Dmedia-ffmpeg=enabled} \
	%{!?with_gstreamer:-Dmedia-gstreamer=disabled} \
	%{!?with_cups:-Dprint-cups=disabled} \
	-Dprint-lpr=true \
	%{?with_sysprof:-Dsysprof=enabled} \
	%{?with_tracker:-Dtracker=enabled} \
	%{!?with_vulkan:-Dvulkan=disabled} \
	%{!?with_wayland:-Dwayland-backend=false}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

install -d $RPM_BUILD_ROOT%{_libdir}/gtk-4.0/%{abivers}/{immodules,inspector}

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a demos examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__mv} $RPM_BUILD_ROOT%{_localedir}/{sr@ije,sr@ijekavian}
# unsupported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/io

# gtk40 and gtk40-properties domains
%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig
%glib_compile_schemas
umask 022
gio-querymodules %{_libdir}/gtk-4.0/%{abivers}/immodules
gio-querymodules %{_libdir}/gtk-4.0/%{abivers}/printbackends
exit 0

%postun
/sbin/ldconfig
if [ "$1" != "0" ]; then
	umask 022
	gio-querymodules %{_libdir}/gtk-4.0/%{abivers}/immodules
	gio-querymodules %{_libdir}/gtk-4.0/%{abivers}/printbackends
else
	%glib_compile_schemas
fi
exit 0

%post examples
%glib_compile_schemas
%update_desktop_database
%update_icon_cache hicolor

%postun examples
%glib_compile_schemas
%update_desktop_database
%update_icon_cache hicolor

%post cups
umask 022
gio-querymodules %{_libdir}/gtk-4.0/%{abivers}/printbackends

%postun cups
if [ "$1" != "0" ]; then
	umask 022
	gio-querymodules %{_libdir}/gtk-4.0/%{abivers}/printbackends
fi
exit 0

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%{?with_broadway:%attr(755,root,root) %{_bindir}/gtk4-broadwayd}
%attr(755,root,root) %{_bindir}/gtk4-launch
%attr(755,root,root) %{_libdir}/libgtk-4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgtk-4.so.1

%dir %{_libdir}/gtk-4.0
%dir %{_libdir}/gtk-4.0/%{abivers}
%dir %{_libdir}/gtk-4.0/%{abivers}/immodules
%dir %{_libdir}/gtk-4.0/%{abivers}/inspector
%dir %{_libdir}/gtk-4.0/%{abivers}/media
%dir %{_libdir}/gtk-4.0/%{abivers}/printbackends
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-file.so
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-lpr.so
%{_libdir}/girepository-1.0/Gdk-4.0.typelib
%if %{with wayland}
%{_libdir}/girepository-1.0/GdkWayland-4.0.typelib
%endif
%{_libdir}/girepository-1.0/GdkX11-4.0.typelib
%{_libdir}/girepository-1.0/Gsk-4.0.typelib
%{_libdir}/girepository-1.0/Gtk-4.0.typelib

%{_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.ColorChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.Debug.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.EmojiChooser.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gtk.gtk4.Settings.FileChooser.gschema.xml
%{?with_broadway:%{_mandir}/man1/gtk4-broadwayd.1*}
%{_mandir}/man1/gtk4-launch.1*

%files update-icon-cache
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk4-encode-symbolic-svg
%attr(755,root,root) %{_bindir}/gtk4-update-icon-cache
%{_mandir}/man1/gtk4-encode-symbolic-svg.1*
%{_mandir}/man1/gtk4-update-icon-cache.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk4-builder-tool
%attr(755,root,root) %{_bindir}/gtk4-query-settings
%attr(755,root,root) %{_libdir}/libgtk-4.so
%{_includedir}/gtk-4.0
%{_pkgconfigdir}/gtk4.pc
%{_pkgconfigdir}/gtk4-unix-print.pc
%{_pkgconfigdir}/gtk4-x11.pc
%if %{with broadway}
%{_pkgconfigdir}/gtk4-broadway.pc
%endif
%if %{with wayland}
%{_pkgconfigdir}/gtk4-wayland.pc
%endif
%{_datadir}/gettext/its/gtk4builder.its
%{_datadir}/gettext/its/gtk4builder.loc
%{_datadir}/gtk-4.0
%{_datadir}/gir-1.0/Gdk-4.0.gir
%if %{with wayland}
%{_datadir}/gir-1.0/GdkWayland-4.0.gir
%endif
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
%{_gtkdocdir}/gdk4-wayland
%{_gtkdocdir}/gdk4-x11
%{_gtkdocdir}/gsk4
%{_gtkdocdir}/gtk4
%endif

%files examples
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gtk4-demo
%attr(755,root,root) %{_bindir}/gtk4-demo-application
%attr(755,root,root) %{_bindir}/gtk4-icon-browser
%attr(755,root,root) %{_bindir}/gtk4-print-editor
%attr(755,root,root) %{_bindir}/gtk4-widget-factory
%{_datadir}/glib-2.0/schemas/org.gtk.Demo4.gschema.xml
%{_datadir}/metainfo/org.gtk.Demo4.appdata.xml
%{_datadir}/metainfo/org.gtk.IconBrowser4.appdata.xml
%{_datadir}/metainfo/org.gtk.PrintEditor4.appdata.xml
%{_datadir}/metainfo/org.gtk.WidgetFactory4.appdata.xml
%{_desktopdir}/org.gtk.Demo4.desktop
%{_desktopdir}/org.gtk.IconBrowser4.desktop
%{_desktopdir}/org.gtk.PrintEditor4.desktop
%{_desktopdir}/org.gtk.WidgetFactory4.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gtk.Demo4.svg
%{_iconsdir}/hicolor/scalable/apps/org.gtk.IconBrowser4.svg
%{_iconsdir}/hicolor/scalable/apps/org.gtk.PrintEditor4.svg
%{_iconsdir}/hicolor/scalable/apps/org.gtk.PrintEditor4.Devel.svg
%{_iconsdir}/hicolor/scalable/apps/org.gtk.WidgetFactory4.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gtk.Demo4-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gtk.IconBrowser4-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gtk.PrintEditor4-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gtk.WidgetFactory4-symbolic.svg
%{_mandir}/man1/gtk4-demo.1*
%{_mandir}/man1/gtk4-demo-application.1*
%{_mandir}/man1/gtk4-icon-browser.1*
%{_mandir}/man1/gtk4-widget-factory.1*
%{_examplesdir}/%{name}-%{version}

%if %{with ffmpeg}
%files media-ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/media/libmedia-ffmpeg.so
%endif

%if %{with gstreamer}
%files media-gstreamer
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/media/libmedia-gstreamer.so
%endif

%if %{with cups}
%files cups
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gtk-4.0/%{abivers}/printbackends/libprintbackend-cups.so
%endif
