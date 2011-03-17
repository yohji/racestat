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

from django.shortcuts import render_to_response;

from app.racestat.models import Session;
from app.racestat.models import Lap;


def sessions(request):
	
	l = Session.objects.all().order_by('-date');
	return render_to_response("session/sessions.html", {"session_list" : l});


def laps(request, session_id):
	
	l = Lap.objects.all().filter(session=session_id).order_by('number');
	return render_to_response("session/laps.html", {"lap_list" : l});
