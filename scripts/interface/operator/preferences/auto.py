
# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or modify it
#  under the terms of the GNU General Public License as published by the Free
#  Software Foundation; either version 2 of the License, or (at your option)
#  any later version.
#
#  This program is distributed in the hope that it will be useful, but WITHOUT
#  ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
#  FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for
#  more details.
#
#  You should have received a copy of the GNU General Public License along with
#  this program; if not, write to the Free Software Foundation, Inc.,
#  51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

# imports
import bpy
from bpy.types import Operator
from .. import shared
from ....function import options
from ....function.preferences import auto

# addon
addon = bpy.context.user_preferences.addons.get(__name__.partition('.')[0])

# name
class name(Operator):
  '''
    Default settings for the auto name operator.
  '''
  bl_idname = 'wm.auto_name_defaults'
  bl_label = 'Auto Name Defaults'
  bl_description = 'Current settings for the auto name operator.'
  bl_options = {'INTERNAL'}

  # check
  def check(self, context):
    return True

  # draw
  def draw(self, context):
    '''
      Draw the operator panel/menu.
    '''

    from ..auto import name
    name.draw(self, context)

  # execute
  def execute(self, context):
    '''
      Execute the operator.
    '''

    return {'FINISHED'}

  # invoke
  def invoke(self, context, event):
    '''
      Invoke the operator panel/menu, control its width.
    '''
    size = 330 if not context.window_manager.BatchShared.largePopups else 460
    context.window_manager.invoke_props_dialog(self, width=size)
    return {'RUNNING_MODAL'}
