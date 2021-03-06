#
# __init__.py  - Service wrapper
# Copyright (C) 2011 René Köcher <shirk@bitspin.org>
#
# This program is free software; you can redistribute it and/or modify it 
# under the terms of the GNU General Public License as published by the 
# Free Software Foundation; either version 2 of the License, or 
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but 
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY 
# or FITNESS FOR A PARTICULAR PURPOSE. 
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
#

from EyeTVLive import EyeTVLive

def Start():
    global eyetv_live_service
    eyetv_live_service = EyeTVLive()
    
    Plugin.AddPrefixHandler('/video/eyetv-live', eyetv_live_service.gui_main_menu, 'EyeTVLive', 'icon-default.png', 'background.png')
    Plugin.AddViewGroup('Category', viewMode='List', mediaType='items')
    Plugin.AddViewGroup('Details', viewMode='InfoList', mediaType='items')
    
    HTTP.Headers['Cache-Control'] = 'no-cache'
    ObjectContainer.title1 = 'EyeTVLive'
    ObjectContainer.content = ContainerContent.GenericVideos
    ObjectContainer.art = R('background.png')
    
    MediaContainer.art = R('background.png')
    
    DirectoryObject.thumb = R('icon-default.png')
    DirectoryObject.art = R('background.png')
    VideoClipObject.art = R('background.png')
    
    try:
        ObjectContainer.no_cache = True
    except Framework.FrameworkException:
        pass

def ValidatePrefs():
    global eyetv_live_service
    return eyetv_live_service.validate_prefs()
