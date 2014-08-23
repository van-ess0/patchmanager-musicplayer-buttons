Name:          patchmanager-musicplayer-buttons
Version:       1.3
Release:       1
Summary:       Set of MPB patches
#Group:         System/Tools
Vendor:        Van-ess0
Distribution:  SailfisfOS
Packager: van-ess0 <van-ess0@mail.ru>
URL:           github.com/van-ess0
Requires: patchmanager

License:       TODO

%description
This package contains the set of patches, adding musicplayer buttons to the lockscreen.\n\nList of patches:\n-Mediaplayer D-Bus Add\n-Lockscreen Musicplayer 
Buttons\n

%files

%defattr(-,root,root,-)
/usr/share/patchmanager/patches/mpb-*


%postun
rm -rf /usr/share/patchmanager/patches/mpb-*

#%changelog
#*
#- First public build.
