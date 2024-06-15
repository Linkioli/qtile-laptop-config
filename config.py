#
# LINKIO'S QTILE CONFIG
#

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "i", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "n", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "e", lazy.layout.up(), desc="Move focus up"),
    Key([mod, "shift"], "h", lazy.layout.shrink_main(), desc="Decrease ratio"),
    Key([mod, "shift"], "i", lazy.layout.grow_main(), desc="Increase ratio"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    Key([mod], "m", lazy.layout.swap_main(),
        desc="Promote focused window to master"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(),
        desc="Toggle floating state of focused window"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "r", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

colors = {
    'red1': '#cc241d',
    'red2': '#fb4934',
    'green1': '#98971a',
    'green2': '#b8bb26',
    'yellow1': '#d79921',
    'yellow2': '#fabd2f',
    'blue1': '#458588',
    'blue2': '#83a598',
    'purple1': '#b16286',
    'purple2': '#d3869b',
    'aqua1': '#689d6a',
    'aqua2': '#8ec07c',
    'orange1': '#d65s0e',
    'orange2': '#fe8019',
    'gray1': '#a89984',
    'gray2': '#928374',

    'bg0': '#282828',
    'bg0_h': '#1d2021',
    'bg1': '#3c3836',
    'bg2': '#504945',
    'bg3': '665c54',
    'bg4': '#7c6f64',

    'fg0': '#fbf1c7',
    'fg1': '#ebdbb2',
    'fg2': '#d5c4a1',
    'fg3': '#bdae93',
    'fg4': '#a89984',
}

# Function for Powerline affect taken from: https://github.com/hiimsergey/qtile-gruvbox-material/blob/main/config.py


def pline(rl, fg, bg):
    if rl == 0:
        uc = ''
    else:
        uc = ''
    return widget.TextBox(text=uc, padding=0, fontsize=22, foreground=fg, background=bg)


def init_group_names():
    return [('I', {'layout': 'monadtall'}),
            ('II', {'layout': 'monadtall'}),
            ('III', {'layout': 'monadtall'}),
            ('IV', {'layout': 'monadtall'}),
            ('V', {'layout': 'monadtall'}),]


def init_groups():
    return [Group(name, **kwargs) for name, kwargs in group_names]


if __name__ in ["config", "__main__"]:
    group_names = init_group_names()
    groups = init_groups()

for i, (name, kwargs) in enumerate(group_names, 1):
    # Switch to another group
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))
    # Send current window to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layouts = [
    layout.MonadTall(
        border_focus=colors['fg1'],
        border_normal=colors['bg0'],
        border_width=2,
        margin=5,
        ratio=0.55,
    ),
    # layout.Max(),
    layout.Floating(
        border_focus='#ebdbb2',
        border_normal='#282828',
        border_width=2,
    ),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Columns(),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.Spiral(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.GroupBox(
                    background=colors['bg2'],
                    highlight_method='text',
                    this_current_screen_border=colors['orange2'],
                    hide_unused=True,
                    disable_drag=True,
                    use_mouse_wheel=False,
                ),
                pline(0, colors['bg2'], colors['bg0_h']),
                widget.WindowName(background=colors['bg0_h']),
                widget.Systray(background=colors['bg0_h']),
                pline(1, colors['purple1'], colors['bg0_h']),
                widget.TextBox("⌨", background=colors['purple1']),
                widget.KeyboardLayout(
                    background=colors['purple1'],
                    configured_keyboards=['us colemak', 'us'],
                ),
                pline(1, colors['yellow1'], colors['purple1']),
                widget.TextBox("🔉", background=colors['yellow1']),
                widget.PulseVolume(background=colors['yellow1']),
                pline(1, colors['blue1'], colors['yellow1']),
                widget.TextBox("🔅", background=colors['blue1']),
                widget.OpenWeather(
                    background=colors['blue1'],
                    zip='23185',
                    metric=False,
                    format='{location_city}: {temp} °{units_temperature} {icon} {weather_details}'
                ),
                pline(1, colors['orange2'], colors['blue1']),
                widget.TextBox("⏰", background=colors['orange2']),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p",
                             background=colors['orange2']),
                pline(1, colors['red1'], colors['orange2']),
                widget.CurrentLayoutIcon(background=colors['red1']),
            ],

            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    border_focus=colors['fg1'],
    border_normal=colors['bg0'],
    border_width=2,
    margin=5,
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

wmname = "Qtile"
