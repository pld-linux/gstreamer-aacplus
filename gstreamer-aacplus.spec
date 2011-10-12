Summary:	GStreamer plugin to encode audio to mp4 AAC+/eAAC+ audio codecs
Summary(pl.UTF-8):	Wtyczka GStreamera kodująca dźwięk do formatu mp4 AAC+/eAAC+
Name:		gstreamer-aacplus
Version:	0.10.0
Release:	1
License:	LGPL v2+
Group:		Libraries
Source0:	http://tipok.ath.cx/downloads/media/aac+/libaacplus-simple-sample/gstreamer/gst-aacplus-%{version}.tar.gz
# Source0-md5:	20a221b0f35fe02fad4cfcf64a40ac7e
URL:		http://tipok.org.ua/node/17
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.10
BuildRequires:	gstreamer-devel >= 0.10.16
BuildRequires:	gstreamer-plugins-base-devel >= 0.10.16
BuildRequires:	libaacplus-devel >= 2.0.2
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	pkgconfig
Requires:	gstreamer-plugins-base >= 0.10.16
Requires:	libaacplus >= 2.0.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains GStreamer plugin to encode audio to modern mp4
audio codec: AAC+ and eAAC+. The specific mode (SBR or SBR+PS) - is
selected automatically, depending on channels number, samplerate and
bitrate of input stream.

This plugin is based on libaacplus library, that also depends on
proprietary 3GPP's code, so you have to be very careful with this
plugin usage, because the encoding logic part is not free.

%description -l pl.UTF-8
Ten pakiet zawiera wtyczkę GStreamera służącą do kodowania dźwięku do
współczesnego kodeka mp4: AAC+ i eAAC+. Konkretny tryb (SBR lub
SBR+PS) wybierany automatycznie, w zależności od liczby kanałów,
częstotliwości próbkowania i szybkości strumienia wejściowego.

Ta wtyczka jest oparta na bibliotece libaacplus, która zależy od
własnościowego kodu 3GPP, więc trzeba być ostrożnym przy używaniu
niniejszej wtyczki - część logiczna kodowania nie jest wolnodostępna.

%prep
%setup -q -n gst-aacplus-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# gstreamer module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/gstreamer-0.10/libgst*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/gstreamer-0.10/libgstaacplus.so
