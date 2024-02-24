from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
import subprocess
import os

mod = "mod4"
terminal = "kitty"

keys = [
  # Cambiar foco entre ventanas
  Key([mod], "Left", lazy.layout.left(), desc="Mover foco a la izquierda"),
  Key([mod], "Right", lazy.layout.right(), desc="Mover foco a la derecha"),
  Key([mod], "Down", lazy.layout.down(), desc="Mover foco abajo"),
  Key([mod], "Up", lazy.layout.up(), desc="Mover foco arriba"),

  # Mover ventanas
  Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Mover ventana a la izquierda"),
  Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Mover ventana a la derecha"),
  Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Mover ventana abajo"),
  Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Mover ventana arriba"),

  # Redimensionar ventanas
  Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Redimensionar a la izquierda"),
  Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Redimensionar a la derecha"),
  Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Reducir tamaño vertical"),
  Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Aumentar tamaño vertical"),
  Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Cambiar entre stack partido y completo"),
  
  # Mover entre pantallas
  Key([mod], "space", lazy.next_screen(), desc="Siguiente monitor"),

  # Cerrar ventanas
  Key([mod], "w", lazy.window.kill(), desc="Cerrar ventana"),

  # Pantalla completa
  Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Ventana en pantalla completa"),

  # Ventana flotante
  Key([mod], "t", lazy.window.toggle_floating(), desc="Ventana en modo flotante"),

  # Maximinar ventana
  Key([mod], "m", lazy.next_layout(), desc="Maximizar ventana"),

  # Recargar qtile
  Key([mod, "control"], "r", lazy.restart(), desc="Reiniciar Qtile"),

  # Cerrar  qtile
  Key([mod, "control"], "q", lazy.shutdown(), desc="Cerrar Qtile"),

  # Multimedia
  Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 2%+"), desc="Aumentar volumen"),
  Key([], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 2%-"), desc="Reducir volumen"),
  Key([], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="Silenciar volumen"),

  Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Reproducir música"),
  Key([], "XF86AudioPrev", lazy.spawn("playerctl previous"), desc="Siguiente canción"),
  Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Anterior canción"),
  
  # Screenshot
  Key([], "Print", lazy.spawn("flameshot gui"), desc="Hacer recorte"),
  Key([mod], "Print", lazy.spawn("flameshot screen"), desc="Pantallazo pantalla actual"),
  Key([mod, "shift"], "Print", lazy.spawn("flameshot full"), desc="Pantallazo ambas pantallas"),

  # Programas
  Key([mod], "Return", lazy.spawn(terminal), desc="Terminal"),
  Key([mod], "b", lazy.spawn("firefox"), desc="Firefox"),
  Key([mod, "shift"], "b", lazy.spawn("firefox --private-window"), desc="Firefox privado"),
  Key([mod], "e", lazy.spawn("thunar"), desc="Thunar"),
  Key([mod], "r", lazy.spawn("rofi -show drun"), desc="Rofi"),
  Key([mod], "d", lazy.spawn("discord"), desc="Discord"),
  Key([mod], "s", lazy.spawn("steam"), desc="Steam"),
  Key([mod], "c", lazy.spawn("code"), desc="Code"),
  # Key([mod], "a", lazy.spawn("thunderbird"), desc="Correo"),
  Key([mod, "shift"], "m", lazy.spawn("/usr/bin/prismlauncher '--launch' 'Tormekia'"), desc="Minecraft"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
  keys.extend([
    # super + numero para cambiar al grupo
    Key([mod], i.name, lazy.group[i.name].toscreen(),
      desc="Cambiar al grupo {}".format(i.name)),

    # super + tab para cambiar al grupo siguiente
    Key([mod], "Tab", lazy.screen.next_group(),
      desc="Cambiar al siguiente grupo"),

    # super + shift + tab para cambiar al grupo anterior
    Key([mod, "shift"], "Tab", lazy.screen.prev_group(),
      desc="Cambiar al grupo anterior"),

    # super + shift + numero para mover ventana al grupo
    Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
      desc="Mover ventana al grupo {}".format(i.name)),

  ])

layouts = [
  layout.Columns(
    margin=6,
    border_focus='#32467f',
    border_normal='#2e324c',
    border_focus_stack='#a6e3a1',
    border_normal_stack='#94e2d5',
    border_on_single=True
  ),
  layout.Max(),
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
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.TextBox("default config", name="default"),
                widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(),
                widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
                widget.QuickExit(),
            ],
            24,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

mouse = [
  # Mover ventana flotante
  Drag([mod], "Button1", lazy.window.set_position_floating(),
    start=lazy.window.get_position()),

  # Redimensionar ventana flotante
  Drag([mod], "Button3", lazy.window.set_size_floating(),
    start=lazy.window.get_size()),

  # Enfocar ventana flotante
  Click([mod], "Button2", lazy.window.bring_to_front()),

  # Cerrar ventana
  Click([], "Button8", lazy.window.kill()),

  # Abrir overlay
  Click([], "Button9", lazy.spawn("eww open --toggle overlay"))

]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
  border_focus='#32467f',
  border_normal='#2e324c',
  border_width=2,
  float_rules=[
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
wmname = "Qtile"

# Scratchpad groups
groups.append(ScratchPad("scratchpad", [
  DropDown("terminal", "kitty", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1)
  DropDown("sistema", "kitty -e btop", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1)
  DropDown("musica", "kitty -e cmus", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1)
  DropDown("keys", "secrets", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1)
  DropDown("correo", "thuderbird", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1)
  DropDown("explorador", "thunar", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1)
  DropDown("sonido", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1)
]))

# Scratchpad keybindings
keys.extend([
  Key([mod, "shift"], 'Return', lazy.group['scratchpad'].dropdown_toggle('terminal')),
  Key([mod], 'n', lazy.group['scratchpad'].dropdown_toggle('musica')),
  Key([mod], 'k', lazy.group['scratchpad'].dropdown_toggle('keys')),
  Key([mod], 'a', lazy.group['scratchpad'].dropdown_toggle('correo')),
  Key([mod], 'z', lazy.group['scratchpad'].dropdown_toggle('sistema')),
  Key([mod, "shift"], 'e', lazy.group['scratchpad'].dropdown_toggle('explorador')),
  Key([mod, "shift"], 'n', lazy.group['scratchpad'].dropdown_toggle('sonido')),
])

# Arrancar con el sistema
@hook.subscribe.startup_once
def autostart():
  home = os.path.expanduser('~/.config/qtile/autostart.sh')
  subprocess.call([home])