Name:		texlive-gustprog
Version:	54074
Release:	2
Summary:	TeXLive gustprog package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gustprog.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gustprog.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
TeXLive gustprog package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/support/gustprog/README
%doc %{_texmfdistdir}/doc/support/gustprog/l2h-examples.zip
%doc %{_texmfdistdir}/doc/support/gustprog/normtext.awk
%doc %{_texmfdistdir}/doc/support/gustprog/plmindex.zip
%doc %{_texmfdistdir}/doc/support/gustprog/porzadki.pl
%doc %{_texmfdistdir}/doc/support/gustprog/slim.zip

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
