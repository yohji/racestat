#
#	Copyright (c) 2011 Marco Merli <yohji@marcomerli.net>
#
#	This program is free software; you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation; either version 2 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program; if not, write to the Free Software Foundation,
#	Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

from django.contrib import admin

from app.racestat.models import Pilot
from app.racestat.models import Vehicle
from app.racestat.models import Raceway
from app.racestat.models import Session
from app.racestat.models import Lap
from app.racestat.models import Data

admin.site.register(Pilot)
admin.site.register(Vehicle)
admin.site.register(Raceway)
admin.site.register(Session)
admin.site.register(Lap)
admin.site.register(Data)

