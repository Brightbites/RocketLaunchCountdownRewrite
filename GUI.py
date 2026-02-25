import dearpygui.dearpygui as dpg
import backend
import time

if __name__ == '__main__':
    dpg.create_context()
    dpg.create_viewport(title='RocketLaunchCountdown', min_width=600, min_height=400, width=600, height=400)

    with dpg.font_registry():
        # first argument ids the path to the .ttf or .otf file
        default_font = dpg.add_font("OpenSans-Medium.ttf", 128)
        second_font = dpg.add_font("OpenSans-Medium.ttf", 36)

    with dpg.window(tag="Primary Window"):
        timer = dpg.add_button(label="T- 00:00:00", tag="text item")
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
            dpg.add_button(label="Toggle Date Till", tag="toggleDate", callback="toggledateview")
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
    
        with dpg.tooltip("Day"):
            dpg.add_text("Day")
    
        with dpg.tooltip("Month"):
            dpg.add_text("Month")
    
        with dpg.tooltip("Year"):
            dpg.add_text("Year")
    
        dpg.bind_font(second_font)
        dpg.bind_item_font(timer, default_font)

    dpg.show_metrics()

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.set_primary_window("Primary Window", True)

    currentViewportSize = 0
    seccondPassed = 0

    while dpg.is_dearpygui_running(): # on every frame
        if not dpg.get_viewport_client_width() == currentViewportSize: # has it been resized
            currentViewportSize = dpg.get_viewport_client_width()
            dpg.configure_item("text item", width=int(currentViewportSize - 16))
            dpg.configure_item("Start", width=int((currentViewportSize / 4) - 10))
            dpg.configure_item("Hold", width=int((currentViewportSize / 4) - 10))
            dpg.configure_item("Scrub", width=int((currentViewportSize / 4) - 10))
            dpg.configure_item("toggle", width=int((currentViewportSize / 4) - 10))
            dpg.configure_item("Day", width=int((currentViewportSize / 3) - 11))
            dpg.configure_item("Month", width=int((currentViewportSize / 3) - 11))
            dpg.configure_item("Year", width=int((currentViewportSize / 3) - 11))
            dpg.configure_item("Hours", width=int((currentViewportSize / 4) - 10))
            dpg.configure_item("Minutes", width=int((currentViewportSize / 4) - 10))
            dpg.configure_item("Seconds", width=int((currentViewportSize / 4) - 10))
            dpg.configure_item("toggleDate",width=int((currentViewportSize / 4) - 10))
            
        #if seccondPassed == abs(time.monotonic()): # has a seccond passed since last run
        #    seccondPassed = abs(time.monotonic() + 1)
        #    if not onHold:
        #        countTime = backend.countTime(countTime)
        #        displayTime = abs(countTime)
        #        holdTime = 0
        #    else:
        #        holdTime = backend.holdTime(holdTime)
        #        displayTime = abs(countTime)
        
        #update button to display time

        dpg.render_dearpygui_frame()

    dpg.destroy_context()

def toggledateview(sender, app_data):
    if dateInputVisable:
        dateInputVisable = False
        dpg.configure_item("Day", enabled=False)
        dpg.configure_item("Month", enabled=False)
        dpg.configure_item("Year", enabled=False)
    else:
        dateInputVisable = True
        dpg.configure_item("Day", enabled=True)
        dpg.configure_item("Month", enabled=True)
        dpg.configure_item("Year", enabled=True) 
