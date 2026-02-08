import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='RocketLaunchCountdown', min_width=600, min_height=400, width=600, height=400)

with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("OpenSans-Medium.ttf", 128)
    second_font = dpg.add_font("OpenSans-Medium.ttf", 36)


with dpg.window(tag="Primary Window"):
    BIG = dpg.add_button(label="T- 00:00:00", tag="text item")
    dpg.add_separator()
    with dpg.group(horizontal=True):
        dpg.add_button(label="Start", tag="Start")
        dpg.add_button(label="Hold", tag="Hold")
        dpg.add_button(label="Scrub", tag="Scrub")
        dpg.add_button(label="Toggle T- L-", tag="toggle")
    with dpg.group(horizontal=True):

        dpg.add_input_int(min_value=0, max_value=23, min_clamped=True, max_clamped=True, step=0, tag="Hours")
        dpg.add_input_int(min_value=0, max_value=59, min_clamped=True, max_clamped=True, step=0, tag="Minutes")
        dpg.add_input_int(min_value=0, max_value=59, min_clamped=True, max_clamped=True, step=0, tag="Seconds")
    with dpg.group(horizontal=True):
        dpg.add_input_int(min_value=1, max_value=31, min_clamped=True, max_clamped=True, step=0, tag="Day")
        dpg.add_input_int(min_value=1, max_value=12, min_clamped=True, max_clamped=True, step=0, tag="Month")
        dpg.add_input_int(min_value=1970, max_value=2038, min_clamped=True, max_clamped=True, step=0, tag="Year")
    
    with dpg.tooltip("Hours"):
        dpg.add_text("Hours")
    
    with dpg.tooltip("Minutes"):
        dpg.add_text("Minutes")
    
    with dpg.tooltip("Seconds"):
        dpg.add_text("Seconds")

    dpg.bind_font(second_font)
    dpg.bind_item_font(BIG, default_font)

dpg.show_style_editor()

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.set_primary_window("Primary Window", True)

while dpg.is_dearpygui_running():
    dpg.configure_item("text item", width=int(dpg.get_viewport_width() - 16))
    dpg.configure_item("Start", width=int((dpg.get_viewport_client_width() / 4) - 10))
    dpg.configure_item("Hold", width=int((dpg.get_viewport_client_width() / 4) - 10))
    dpg.configure_item("Scrub", width=int((dpg.get_viewport_client_width() / 4) - 10))
    dpg.configure_item("toggle", width=int((dpg.get_viewport_client_width() / 4) - 10))
    dpg.configure_item("Day", width=int((dpg.get_viewport_client_width() / 3) - 11))
    dpg.configure_item("Month", width=int((dpg.get_viewport_client_width() / 3) - 11))
    dpg.configure_item("Year", width=int((dpg.get_viewport_client_width() / 3) - 11))
    dpg.configure_item("Hours", width=int((dpg.get_viewport_client_width() / 4) - 10))
    dpg.configure_item("Minutes", width=int((dpg.get_viewport_client_width() / 4) - 10))
    dpg.configure_item("Seconds", width=int((dpg.get_viewport_client_width() / 4) - 10))
    #dpg.configure_item("toggleDate",width=int((dpg.get_viewport_client_width() / 4) - 11))
    dpg.render_dearpygui_frame()

dpg.destroy_context()