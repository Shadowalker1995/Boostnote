# Enable tap to click in i3 WM

When switching from Gnome or KDE to using i3 tiling window manager on a laptop, you might be frustrated to discover that tap-to-click on your touchpad no longer functions. This is how to re-enable tap-to-click in i3 by properly using X11 configuration.

## Doing it the X11 config way

X11 provides configurations in a directory “X11/xorg.conf.d/” this directory could live in various places on your system depending on your distribution.

However, X11 will always attempt to also load configurations from /etc/X11/xorg.conf.d/ when present.

To ensure the directory exists, run:

```bash
sudo mkdir -p /etc/X11/xorg.conf.d
```

Next we’ll create a new file `90-touchpad.conf`. The configuration file names end with .conf and are read in ASCII order—by convention file names begin with two digits followed by a dash.

```bash
sudo touch /etc/X11/xorg.conf.d/90-touchpad.conf
```

Now open up the file your editor of choice (with suitable write permission of course) and paste the following:

```Xorg
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "Tapping" "on"
EndSection
```

## Additional libinput options

Libinput support additional options beyond tapping, you can add and configure each one by adding them on new lines after `Option "Tapping" "on"` in your /etc/X11/xorg.conf.d/90-touchpad.conf, for example:

```Xorg
Section "InputClass"
        Identifier "touchpad"
        MatchIsTouchpad "on"
        Driver "libinput"
        Option "Tapping" "on"
        Option "TappingButtonMap" "lrm"
        Option "NaturalScrolling" "on"
        Option "ScrollMethod" "twofinger"
EndSection
```

### Two and three finger tap

Two and three finger tap configurations can be set with to have two finger tap to cause a right-click and three finger tap to cause a middle-click with:

```Xorg
        Option "TappingButtonMap" "lrm"
```

Or two make a two finger tap do a middle-click and a three finger tap to cause a right-click:

```Xorg
        Option "TappingButtonMap" "lmr"
```

### Natural scrolling

Natural scrolling can be enabled with:

```Xorg
        Option "NaturalScrolling" "on"
```

### Scroll method

Two scroll with two fingers, the default:

```Xorg
        Option "ScrollMethod" "twofinger"
```

If you prefer to use the edge of your touchpad:

```Xorg
        Option "ScrollMethod" "edge"
```