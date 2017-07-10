import bpy

from bpy.types import AddonPreferences
from bpy.props import *

from .config import defaults
from .utilities import get

class name_panel(AddonPreferences):
    bl_idname = __name__.partition('.')[0]

    default = defaults['preferences']

    mode = EnumProperty(
        name = 'Mode',
        description = 'Preference Mode',
        items = [
            ('GENERAL', 'General', 'Adjust general preferences'),
            ('PANEL', 'Name Panel', 'Adjust preferences related to the name stack'),
            ('NAMER', 'Namer', 'Adjust preferences related to namer')
        ],
        default = default['mode']
    )

    keep_session_settings = BoolProperty(
        name = 'Keep Session Settings',
        description = 'Remember common settings values related to this addon consistent across blend files',
        default = default['keep_session_settings']
    )

    location = EnumProperty(
        name = 'Location',
        description = 'The 3D view shelf to use for the name panel',
        items = [
            ('TOOLS', 'Tool Shelf', 'Places the name panel in the tool shelf under the tab labeled \'Name\''),
            ('UI', 'Property Shelf', 'Places the name panel in the property shelf.')
        ],
        default = default['location']
    )

    pin_active = BoolProperty(
        name = 'Pin Active',
        description = 'Keep the active object/bone at the top of the name stack.',
        default = default['pin_active']
    )

    click_through = BoolProperty(
        name = 'Click Through',
        description = 'Do not activate the pop-up when clicking a datablock icon',
        default = default['click_through']
    )

    remove_item = BoolProperty(
        name = 'Remove Item Panel',
        description = 'Remove the item panel from the properties shelf when this addon is active',
        default = default['remove_item']
    )

    popup_width = IntProperty(
        name = 'Width',
        description = 'Width of the pop-up panels in pixels',
        min = 200,
        max = 1000,
        subtype = 'PIXEL',
        default = default['popup_width']
    )

    use_last = BoolProperty(
        name = 'Use Last Settings',
        description = 'When adding a naming operation use the previous settings',
        default = default['use_last']
    )

    auto_name_operations = BoolProperty(
        name = 'Auto Name Operations',
        description = 'Automatically name operation entries based on operation modes',
        default = default['auto_name_operations']
    )

    namer_popup_width = IntProperty(
        name = 'Width',
        description = 'Width of the pop-up panel in pixels',
        min = 200,
        max = 1000,
        subtype = 'PIXEL',
        default = default['namer_popup_width']
    )


    def draw(self, context):

        web_links = [
            ('Thread', ''),
            ('Blender Market', ''),
            ('Github', ''),
            ('Report Bug', ''),
            ('Donate', ''),
        ]

        self.preference = get.preferences(context)

        row = self.layout.row()
        row.prop(self.preference, 'mode', expand=True)

        getattr(self, self.preference.mode.lower())(context)

        row = self.layout.row(align=True)
        row.scale_y = 1.5
        for name, url in web_links:
            row.operator('wm.url_open', text=name).url = url


    def general(self, context):

        box = self.layout.box()

        row = box.row()
        row.prop(self.preference, 'keep_session_settings')


    def panel(self, context):

        box = self.layout.box()

        row = box.row()
        row.label(text='Location:')
        row.prop(self.preference, 'location', expand=True)

        row = box.row()
        row.prop(self.preference, 'pin_active')
        row.prop(self.preference, 'remove_item')

        row = box.row()
        row.prop(self.preference, 'click_through')

        row = box.row()
        row.label(text='Pop-up Width:')
        row.prop(self.preference, 'popup_width')

    def namer(self, context):

        box = self.layout.box()

        row = box.row()
        row.prop(self.preference, 'use_last')
        row.prop(self.preference, 'auto_name_operations')

        row = box.row()
        row.label(text='Namer Pop-up Width:')
        row.prop(self.preference, 'namer_popup_width')
