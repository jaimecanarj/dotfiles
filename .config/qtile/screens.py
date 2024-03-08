from libqtile import bar, widget
from libqtile.config import Screen
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration
from nvidiaSensors2 import NvidiaSensors2

screens = [
  Screen(
    top= bar.Bar([
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
        fontsize=16,
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
        scroll_delay=1,
        scroll_interval=0.05,
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
      widget.Volume(
        background="#11111baa",
        foreground="#9a7ecc",
        padding=6,
        emoji=True,
        emoji_list=["󰖁","󰕿","󰖀","󰕾"],
        fontsize=20,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      ),],),
      widget.Volume(
        background="#11111baa",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      ),],),
      widget.TextBox(
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#4e5173",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        foreground="#4abaaf",
        background="#11111baa",
        fontsize=16,
        device="/dev_E8_EE_CC_88_45_7A",
        symbol_connected="󰋋",
        symbol_paired="󰟎",
        device_format="{symbol}",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        background="#11111baa",
        device="/dev_E8_EE_CC_88_45_7A",
        device_battery_format="{battery}%",
        device_format=" {battery_level}  - ",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        foreground="#e0af68",
        background="#11111baa",
        fontsize=16,
        device="/dev_E7_F3_5C_89_B8_72",
        symbol_connected="󰍽",
        symbol_paired="󰍾",
        device_format="{symbol}",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        background="#11111baa",
        device="/dev_E7_F3_5C_89_B8_72",
        device_battery_format="{battery}%",
        device_format=" {battery_level}",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Sep(
        background="#11111baa",
        linewidth=0,
        padding=8,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Spacer(background="#00000000", length=8),
      widget.TextBox(
        text="  ",
        font="JetBrainsMono Nerd Font",
        fontsize=16,
        padding=0,
        foreground="#7aa2f7",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.CPU(
        background="#11111baa",
        format="{load_percent: .0f}% - ",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.ThermalSensor(
        background="#11111baa",
        format="{temp: .0f}ºC",
        tag_sensor="Tctl",
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
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#4e5173",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text="󰢮 ",
        font="JetBrainsMono Nerd Font",
        fontsize=17,
        padding=0,
        foreground="#9ece6a",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      NvidiaSensors2(
        background="#11111baa",
        foreground="#cdd6f4",
        format="{utilization_gpu}% - {temperature_gpu}°C",
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
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#4e5173",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text="󰘚",
        font="JetBrainsMono Nerd Font",
        fontsize=17,
        foreground="#e0af68",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Memory(
        background="#11111baa",
        format="{MemUsed: .2f}{mm}b",
        measure_mem="G",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Sep(
        background="#11111baa",
        linewidth=0,
        padding=10,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
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
            padding_y=0,
      ),],),
      widget.Clock(
        format="%H:%M",
        foreground="#11111b",
        background="#9ece6a",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      ),],),
      widget.TextBox(
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#11111b",
        background="#9ece6a",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text="󰸗 ",
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
            padding_y=0,
      ),],),
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
            padding_y=0,
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
            padding_y=0,
      ),],),],
      30,
      background="#11111b00",
      margin=6,
  )),
  Screen(
    top= bar.Bar([
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
        this_screen_border="#4abaaf",
        this_current_screen_border="#4abaaf",
        other_screen_border="#9a7ecc",
        other_current_screen_border="#9a7ecc",
        highlight_color=["#9a7ecc","#4abaaf"],
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
        fontsize=16,
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
        scroll_delay=1,
        scroll_interval=0.05,
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
      widget.Volume(
        background="#11111baa",
        foreground="#9a7ecc",
        padding=6,
        emoji=True,
        emoji_list=["󰖁","󰕿","󰖀","󰕾"],
        fontsize=20,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      ),],),
      widget.Volume(
        background="#11111baa",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      ),],),
      widget.TextBox(
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#4e5173",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        foreground="#4abaaf",
        background="#11111baa",
        fontsize=16,
        device="/dev_E8_EE_CC_88_45_7A",
        symbol_connected="󰋋",
        symbol_paired="󰟎",
        device_format="{symbol}",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        background="#11111baa",
        device="/dev_E8_EE_CC_88_45_7A",
        device_battery_format="{battery}%",
        device_format=" {battery_level}  - ",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        foreground="#e0af68",
        background="#11111baa",
        fontsize=16,
        device="/dev_E7_F3_5C_89_B8_72",
        symbol_connected="󰍽",
        symbol_paired="󰍾",
        device_format="{symbol}",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Bluetooth(
        background="#11111baa",
        device="/dev_E7_F3_5C_89_B8_72",
        device_battery_format="{battery}%",
        device_format=" {battery_level}",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Sep(
        background="#11111baa",
        linewidth=0,
        padding=8,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Spacer(background="#00000000", length=8),
      widget.TextBox(
        text="  ",
        font="JetBrainsMono Nerd Font",
        fontsize=16,
        padding=0,
        foreground="#7aa2f7",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.CPU(
        background="#11111baa",
        format="{load_percent: .0f}% - ",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.ThermalSensor(
        background="#11111baa",
        format="{temp: .0f}ºC",
        tag_sensor="Tctl",
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
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#4e5173",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text="󰢮 ",
        font="JetBrainsMono Nerd Font",
        fontsize=17,
        padding=0,
        foreground="#9ece6a",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      NvidiaSensors2(
        background="#11111baa",
        foreground="#cdd6f4",
        format="{utilization_gpu}% - {temperature_gpu}°C",
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
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#4e5173",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text="󰘚",
        font="JetBrainsMono Nerd Font",
        fontsize=17,
        foreground="#e0af68",
        background="#11111baa",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Memory(
        background="#11111baa",
        format="{MemUsed: .2f}{mm}b",
        measure_mem="G",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.Sep(
        background="#11111baa",
        linewidth=0,
        padding=10,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
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
            padding_y=0,
      ),],),
      widget.Clock(
        format="%H:%M",
        foreground="#11111b",
        background="#9ece6a",
        padding=0,
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      ),],),
      widget.TextBox(
        text="",
        font="JetBrainsMono Nerd Font",
        fontsize=27,
        padding=10,
        foreground="#11111b",
        background="#9ece6a",
        decorations=[
          RectDecoration(
            group=True,
            use_widget_background=True,
            radius=4,
            filled=True,
            padding_y=0,
      )],),
      widget.TextBox(
        text="󰸗 ",
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
            padding_y=0,
      ),],),
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
            padding_y=0,
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
            padding_y=0,
      ),],),],
      30,
      background="#11111b00",
      margin=6,
  ))
]

# Cosas a añadir a la barra
#   notificaciones acceso (widget eww)