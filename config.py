import tomllib

toml_str = """
[Appearance]
Background_Color = "#484D66"
Text_Color = "#FFFFFF"
Font = "Consolas"
Mission_Font_Size = 24
Timer_Font_Size = 80

[Go_No-Go_Appearance]
Background_Color = "#111111"
Border_Color = "#FFFFFF"
Go_Color = "#00FF00"
No-Go_Color = "#FF0000"
Caution_Color = "#FFA500"
Font_Size = 20

[Other]
Mode = "Spreadsheet"
# Sheet_Link = ""
Range_Row = 2
Weather_Row = 3
Vehicle_Row = 4
Major_Concerns_Row = 9
Column = 12
Hide_Mission_Name = true
Timezone = "System" # timezone used, example: UTC, Europe/Paris
"""

data = tomllib.loads(toml_str)