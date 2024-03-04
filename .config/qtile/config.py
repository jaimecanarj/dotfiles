from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
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

screens = [
  Screen(
    top=bar.Bar([
      widget.Image(
        filename="~/.config/qtile/tokyoflag.png",
        margin=6,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),

      widget.GroupBox(
        padding=6,
        highlight_method="line",
        font="Noto Sans CJK JP Black",
        fontsize = 16,
        this_screen_border="#9a7ecc",
        this_current_screen_border="#9a7ecc",
        other_screen_border="#4abaaf",
        other_current_screen_border="#4abaaf",
        highlight_color=["#4abaaf","#9a7ecc"],
        fontshadow=["#1a1b26"],
        active="#cdd6f4",
        inactive="#4e5173",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Spacer(
        background="#00000000",
        length=8,
      ),
      widget.TextBox(
        text="  ",
        font="JetBrainsMono Nerd Font",
        fontsize=14,
        foreground="#11111b",
        background="#e0af68",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.CheckUpdates(
        fmt=' {} ',
        distro='Arch_yay',
        font="JetBrainsMono Nerd Font SemiBold",
        display_format='Updates: {updates} ',
        no_update_string='Sistema actualizado ',
        colour_have_updates="#11111b",
        colour_no_updates="#11111b",
        background="#e0af68",
        update_interval=60,  # in seconds
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text='',
        font="JetBrainsMono Nerd Font",
        fontsize=24,
        foreground="#4abaaf",
        background="#e0af68",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text='',
        font="JetBrainsMono Nerd Font",
        fontsize=24,
        foreground="#7aa2f7",
        background="#4abaaf",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text='',
        font="JetBrainsMono Nerd Font",
        fontsize=24,
        foreground="#9a7ecc",
        background="#7aa2f7",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Cmus(
        font="JetBrainsMono Nerd Font SemiBold",
        background="#9a7ecc",
        noplay_color="#11111b",
        play_color="#cdd6f4",
        width=200,
        scroll=True,
        scroll_fixed_width=True,
        padding=6,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      ),],),
      widget.Spacer(background="#00000000"),
      widget.Volume(), 
      widget.CPU(), 
      widget.Spacer(background="#00000000", length=8),
      widget.TextBox(
        text=" 󰥔 ",
        font="JetBrainsMono Nerd Font",
        fontsize=16,
        padding=0,
        foreground="#11111b",
        background="#9ece6a",
      decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
         ),],),
      widget.Clock(
        format="%H:%M |",
        foreground="#11111b",
        background="#9ece6a",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
         ),],),
      widget.TextBox(
        text=" 󰸗 ",
        font="JetBrainsMono Nerd Font",
        fontsize=16,
        padding=0,
        foreground="#11111b",
        background="#9ece6a",
      decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
         ),],),
    #   widget.GenPollCommand(
    #     fontsize = 16,
    #     padding=0,
    #     foreground="#11111b",
    #     background="#9ece6a",
    #     update_interval=1,
    #     cmd="~/.config/qtile/weekday.sh",
    #     shell=True,
    #     decorations=[
    #       RectDecoration(
    #         group=True,
    #         use_widget_background=True,
    #         radius=4,
    #         filled=True,
    #      ),],),
      widget.Clock(
        format="%d de %B",
        foreground="#11111b",
        background="#9ece6a",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
         ),],),
      widget.Sep(
        padding=6,
        linewidth=0,
        background="#9ece6a",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
         ),],),
    ],
    30,
    background="#11111b00",
    margin=6,
    ),
  ),
  Screen(
    top=bar.Bar([
      widget.Sep(padding=6, linewidth=0,),
      widget.Image(filename="~/.config/qtile/tokyoflag.png", margin=6, mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")}),
      widget.Sep(padding=6, linewidth=0,),
      widget.Clock(format="%H:%M | %A, %d de %B",
      foreground="#cdd6f4"),
      widget.Sep(padding=6, linewidth=0,),
      widget.GroupBox(
          highlight_method="line",
          font="Noto Sans CJK JP Black",
          fontsize = 16,
          this_screen_border="#4abaaf",
          this_current_screen_border="#4abaaf",
          other_screen_border="#9a7ecc",
          other_current_screen_border="#9a7ecc",
          highlight_color=["#9a7ecc","#4abaaf"],
          fontshadow=["#1a1b26"],
          active="#cdd6f4",
          inactive="#4e5173"),
    ],
    30,  # height in px
    background="#11111b"  # background color
    ),
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
  border_focus="#32467f",
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

# Cosas a añadir a la barra
#   bluetooth y ethernet accesos
#   notificaciones acceso (widget eww)
#   información sistema (widget eww?)
#   volumen icono