import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='RocketLaunchCountdown', width=600, height=400)

def start():
    print("Start pressed")

def hold():
    print("Hold pressed")

def scrub():
    print("Scrub pressed")


with dpg.window(tag="Primary Window"):
    dpg.add_text("T- " + "00:00:00")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="Start", callback=start)
        dpg.add_button(label="Hold", callback=hold)
        dpg.add_button(label="Scrub", callback=scrub)
        with dpg.group() as group1:
            pass

dpg.show_metrics()
dpg.show_style_editor()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()