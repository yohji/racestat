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

import os;
from time import time;

from django.template import RequestContext;
from django.shortcuts import render_to_response;
from django.shortcuts import redirect;

from app.racestat.web.models import LoadForm;
from app.racestat.loader.motec import MotecLoader;


def load_motec(request):

	form = None;
	if (request.method == "POST"):
		form = LoadForm(request.POST, request.FILES);
		if (form.is_valid()):
			
			pilot = form.cleaned_data["pilot"];
			vehicle = form.cleaned_data["vehicle"];
			raceway = form.cleaned_data["raceway"];
			motec = MotecLoader(
				pilot,
				vehicle,
				raceway);
			
			ftemp = request.FILES["csv"];
			fname = "/tmp/racestat-%s.tmp" % str(int(time()));
			fwrite = open(fname, "wb+");
			for chunk in ftemp.chunks():
				fwrite.write(chunk);
			fwrite.flush();
			
			fread = open(fname, "rb")
			motec.load(fread);
			os.remove(fname);
	else:
		form = LoadForm();
	
	return render_to_response("load/motec.html", 
		{"form": form}, 
		context_instance=RequestContext(request));
