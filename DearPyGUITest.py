import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='RocketLaunchCountdown', width=600, height=400)

TLToggle = False

def start():
    print("Start pressed")
    if TLToggle:
        dpg.set_value("text item", "00:00:00")
    else: dpg.set_value("text item", "00:00:01")

def hold():
    print("Hold pressed")

def scrub():
    print("Scrub pressed")
    dpg.set_value("text item", "SCRUB")

def Ttoggle():
    global TLToggle
    if TLToggle:
        TLToggle = False
    else: TLToggle = True
    print(TLToggle)

with dpg.window(tag="Primary Window"):
    dpg.add_text("T- 00:00:00", tag="text item")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="Start", callback=start)
        dpg.add_button(label="Hold", callback=hold)
        dpg.add_button(label="Scrub", callback=scrub)
        dpg.add_button(label="Toggle T- L-", callback=Ttoggle)
    

dpg.show_metrics()
dpg.show_style_editor()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()