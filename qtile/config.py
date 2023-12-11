# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import subprocess

mod = "mod4"
terminal = guess_terminal()

gruv_mat = {
    "black": "#000000",
    "dark": "#1d2021",
    "disabled": "#504945",
    "red": "#ea6962",
    "red-alt": "#b22222",
    "orange": "#e78a4e",
    "yellow": "#d8a657",
    "green": "#a9a665",
    "aqua": "#89b482",
    "blue": "#7daea3",
    "grey": "#a89984",
    "dark-grey": "#303030",
    "cream": "#d4be98",
    "white": "#FFFFFF",
    "transparent": "#00000000",
}

gruvbox = {
    "black": "#000000",
    "dark": "#141617",
    "disabled": "#504945",
    "red": "#fb4934",
    "red-alt": "#cc241d",
    "orange": "#fe8019",
    "orange-alt": "#d65d0e",
    "yellow": "#fabd2f",
    "yellow-alt": "#d79921",
    "green": "#b8bb26",
    "green-alt": "#98971a",
    "aqua": "#8ec07c",
    "aqua-alt": "#689d6a",
    "blue": "#83a598",
    "blue-alt": "#458588",
    "grey": "#504945",
    "dark-grey": "#1d2021",
    "cream": "#ebdbb2",
    "cream-alt": "#bdae93",
    "white": "#FFFFFF",
    "transparent": "#00000000",
}

colors = [
    ["#282c34ee", "#282c34cc"], #transparent    
    ["#eee8d5", "#eee8d5"], # bg
    ["#657b83", "#657b83"], # fg
    ["#ece5ac", "#ece5ac"], # color01
    ["#dc322f", "#dc322f"], # color02
    ["#859900", "#859900"], # color03
    ["#b58900", "#b58900"], # color04
    ["#268bd2", "#268bd2"], # color05
    ["#d33682", "#d33682"], # color06
    ["#2aa198", "#2aa198"]  # color15
    ]



keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show run"), desc="Spawn a command using a prompt widget"),
    Key([mod, "control", "shift"], "r", lazy.restart()),
    Key([mod, "control"], "b", lazy.group["scratchpad"].dropdown_toggle("term")),

]

groups = [

ScratchPad("scratchpad", [
    DropDown("term", "/usr/bin/alacritty", height = 0.7, width = 0.3, x = 0.35, y = 0.15)
            
    ]
),
Group("1"),
Group("2"),
Group("3"),
Group("4"),
Group("5"),
Group("6"),
Group("7"),
Group("8"),
Group("9"),
]
for i in groups:
    if i.name != "scratchpad":
        keys.extend(
            [
                # mod1 + letter of group = switch to group
                Key(
                    [mod],
                    i.name,
                    lazy.group[i.name].toscreen(),
                    desc="Switch to group {}".format(i.name),
                ),
                # mod1 + shift + letter of group = switch to & move focused window to group
                #Key(
                #    [mod, "shift"],
                #    i.name,
                #    lazy.window.togroup(i.name, switch_group=True),
                #    desc="Switch to & move focused window to group {}".format(i.name),
                #),
                # Or, use below if you prefer not to switch to that group.
                # # mod1 + shift + letter of group = move focused window to group
                Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                    desc="move focused window to group {}".format(i.name)),
            ]
        )

layouts = [
    layout.Columns(
        border_focus_stack=["#175f50", "#1f3d3d"],
        border_width=3,
        margin = 15,
        border_focus = gruv_mat["grey"],
        border_normal = gruv_mat["dark"],
        num_columns = 3, 
        grow_amount = 1.5,
        ),
    layout.Max(
        border_width = 2,
        margin = 6, 
        border_focus = gruv_mat["grey"]
        ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=14,
    padding=3,
    foreground=gruv_mat["white"],
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
               
                widget.GroupBox(
                    fontsize = 14,
                     margin_y = 3,
                     margin_x = 4,
                     padding_y = 9,
                     padding_x = 3,
                     borderwidth = 3,
                     active = gruvbox["cream"],
                     inactive = gruvbox["blue-alt"],
                     rounded = False,
                     center_align = True,
                     highlight_color = gruvbox["black"],
                     highlight_method = "line",
                     this_current_screen_border = gruv_mat["yellow"],
                     this_screen_border=gruv_mat["disabled"],
                other_screen_border=gruv_mat["red"],
                    other_current_screen_border=gruv_mat["red"],
                    background=gruvbox["black"],
                    foreground=gruv_mat["disabled"],
                    ),
                widget.TaskList(
                    margin=0,
                    padding=6,
                    icon_size=0,
                    fontsize=14,
                    borderwidth=1,
                    rounded=False,
                    highlight_method="block",
                    title_width_method="uniform",
                    urgent_alert_methond="border",
                    foreground=gruv_mat["black"],
                    background=gruvbox["cream"],
                    border=gruvbox["cream"],
                    urgent_border=gruv_mat["red-alt"],
                    txt_floating=" ",
                    txt_maximized=" ",
                    txt_minimized=" ",
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.CPU(
                    padding=5,
                    format="  {freq_current}GHz {load_percent}%",
                    foreground=gruvbox["cream"],
                    background=gruvbox["dark-grey"],
                ),
                widget.Memory(
                    padding=5,
                    format="󰈀 {MemUsed:.0f}{mm}",
                    background=gruvbox["cream"],
                    foreground=gruvbox["dark-grey"],
                ),
                widget.Clock(
                    padding=5,
                    format="  %a %d %b %H:%M:%S",
                    foreground=gruvbox["yellow"],
                    background=gruvbox["dark-grey"],
                ),
                widget.Volume(
                    fmt="󰕾 {}",
                    foreground=gruvbox["dark"],
                    background=gruvbox["yellow"],
                    padding=10,
                ),
                widget.Systray(
                    padding=7,
                    icon_size=15,
                ),
                widget.QuickExit(
                    foreground=colors[1],
                    ),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),

    Screen(
        top=bar.Bar(
            [
               
                widget.GroupBox(
                    fontsize = 14,
                     margin_y = 3,
                     margin_x = 4,
                     padding_y = 9,
                     padding_x = 3,
                     borderwidth = 3,
                     active = gruvbox["cream"],
                     inactive = gruvbox["blue-alt"],
                     rounded = False,
                     center_align = True,
                     highlight_color = gruvbox["black"],
                     highlight_method = "line",
                     this_current_screen_border = gruv_mat["yellow"],
                     this_screen_border=gruv_mat["disabled"],
                other_screen_border=gruv_mat["red"],
                    other_current_screen_border=gruv_mat["red"],
                    background=gruvbox["black"],
                    foreground=gruv_mat["disabled"],
                    ),
                widget.TaskList(
                    margin=0,
                    padding=6,
                    icon_size=0,
                    fontsize=14,
                    borderwidth=1,
                    rounded=False,
                    highlight_method="block",
                    title_width_method="uniform",
                    urgent_alert_methond="border",
                    foreground=gruv_mat["black"],
                    background=gruvbox["cream"],
                    border=gruvbox["cream"],
                    urgent_border=gruv_mat["red-alt"],
                    txt_floating=" ",
                    txt_maximized=" ",
                    txt_minimized=" ",
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.CPU(
                    padding=5,
                    format="  {freq_current}GHz {load_percent}%",
                    foreground=gruvbox["cream"],
                    background=gruvbox["dark-grey"],
                ),
                widget.Memory(
                    padding=5,
                    format="󰈀 {MemUsed:.0f}{mm}",
                    background=gruvbox["cream"],
                    foreground=gruvbox["dark-grey"],
                ),
                widget.Clock(
                    padding=5,
                    format="  %a %d %b %H:%M:%S",
                    foreground=gruvbox["yellow"],
                    background=gruvbox["dark-grey"],
                ),
                widget.Volume(
                    fmt="󰕾 {}",
                    foreground=gruvbox["dark"],
                    background=gruvbox["yellow"],
                    padding=10,
                ),
                widget.QuickExit(
                    foreground=colors[1],
                    ),
            ],
            30,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

@hook.subscribe.startup_once
def start_once():
    subprocess.Popen('/home/david/.scripts/autostart.sh')

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
