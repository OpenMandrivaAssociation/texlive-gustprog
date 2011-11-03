# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-gustprog
Version:	20111103
Release:	1
Summary:	TeXLive gustprog package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gustprog.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gustprog.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
