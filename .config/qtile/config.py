from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, ScratchPad, DropDown
from libqtile.lazy import lazy
from screens import screens
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
  
  # Mover entre grupos
  Key([mod], "Tab", lazy.screen.next_group(), desc="Cambiar al siguiente grupo"),
  Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="Cambiar al grupo anterior"),

  # Mover entre pantallas
  Key([mod], "space", lazy.next_screen(), desc="Siguiente monitor"),

  # Mover entre programas
  Key(["mod1"], "Tab", lazy.spawn("rofi -show windowcd -theme ~/.config/rofi/launcher.rasi"), desc="Menu programas"),

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
  Key([mod], "r", lazy.spawn("rofi -show drun -theme ~/.config/rofi/launcher.rasi"), desc="Rofi"),
  Key([mod], "d", lazy.spawn("discord"), desc="Discord"),
  Key([mod], "s", lazy.spawn("steam"), desc="Steam"),
  Key([mod, "shift"], "s", lazy.spawn("lutris"), desc="Lutris"),
  Key([mod], "c", lazy.spawn("code"), desc="Code"),
  Key([mod, "shift"], "m", lazy.spawn("/usr/bin/prismlauncher --launch Tormekia"), desc="Minecraft"),
]

# groups = [Group(i) for i in "123456789"]
groups = []

group_names = ["1","2","3","4","5","6"]

group_labels = ["壱","弐","参","四","五","六"]

for i in range(len(group_names)):
  groups.append(
    Group(
      name = group_names[i],
      label = group_labels[i],
    )
  )

for i in groups:
  keys.extend([
    # super + numero para cambiar al grupo
    Key([mod], i.name, lazy.group[i.name].toscreen(),
      desc="Cambiar al grupo {}".format(i.name)),

    # super + shift + numero para mover ventana al grupo
    Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
      desc="Mover ventana al grupo {}".format(i.name)),

  ])

layouts = [
  layout.Columns(
    margin=6,
    border_focus="#4abaaf",
    border_normal="#2e324c",
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
  font="Noto Sans Bold",
  fontsize=14,
  padding=3,
  foreground="#cdd6f4",
  background="#11111b",
)
extension_defaults = widget_defaults.copy()

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
  border_focus="#4abaaf",
  border_normal="#2e324c",
  border_width=2,
  float_rules=[
    *layout.Floating.default_float_rules,
    Match(wm_class="confirmreset"),  # gitk
    Match(wm_class="makebranch"),  # gitk
    Match(wm_class="maketag"),  # gitk
    Match(wm_class="ssh-askpass"),  # ssh-askpass
    Match(title="branchdialog"),  # gitk
    Match(title="pinentry"),  # GPG key password entry
    Match(wm_class="gnome-calculator"),
  ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
wmname = "Qtile"

# Scratchpad groups
groups.append(ScratchPad("scratchpad", [
  DropDown("terminal", "kitty", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
  DropDown("sistema", "kitty -e btop", width=0.8, height=0.9, x=0.1, y=0.05, opacity=1),
  DropDown("musica", "kitty -e cmus", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
  DropDown("keys", "secrets", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
  DropDown("correo", "thunderbird", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
  DropDown("explorador", "thunar", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
  DropDown("sonido", "pavucontrol", width=0.8, height=0.8, x=0.1, y=0.1, opacity=1),
]))

# Scratchpad keybindings
keys.extend([
  Key([mod, "shift"], "Return", lazy.group["scratchpad"].dropdown_toggle("terminal")),
  Key([mod], "n", lazy.group["scratchpad"].dropdown_toggle("musica")),
  Key([mod], "k", lazy.group["scratchpad"].dropdown_toggle("keys")),
  Key([mod], "a", lazy.group["scratchpad"].dropdown_toggle("correo")),
  Key([mod], "z", lazy.group["scratchpad"].dropdown_toggle("sistema")),
  Key([mod, "shift"], "e", lazy.group["scratchpad"].dropdown_toggle("explorador")),
  Key([mod, "shift"], "n", lazy.group["scratchpad"].dropdown_toggle("sonido")),
])

# Arrancar con el sistema
@hook.subscribe.startup_once
def autostart():
  home = os.path.expanduser("~/.config/qtile/autostart.sh")
  subprocess.call([home])

# Hacer mpv tiled
@hook.subscribe.client_new
def disable_floating(window):
    rules = [
        Match(wm_class="mpv")
    ]

    if any(window.match(rule) for rule in rules):
        window.togroup(qtile.current_group.name)
        window.cmd_disable_floating()
