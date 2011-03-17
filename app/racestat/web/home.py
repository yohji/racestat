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

import gzip;
from time import time;

from django.http import HttpResponse;
from django.shortcuts import render_to_response;

from app.racestat.models import Pilot;
from app.racestat.models import Vehicle;
from app.racestat.models import Raceway;
from app.racestat.models import Session;
from app.racestat.models import Lap;
from app.racestat.models import Data;
from app.racestat.loader.motec import MotecLoader;


def index(request):

	return render_to_response("home.html");

def test(request):
	
	timer = time();
	
	Data.objects.all().delete();
	Lap.objects.all().delete();
	Session.objects.all().delete();
	Raceway.objects.all().delete();
	Vehicle.objects.all().delete();
	Pilot.objects.all().delete();
	
	pilot = Pilot();
	pilot.id = 1;
	pilot.name = "Marco Merli";
	pilot.save();
	
	vehicle = Vehicle();
	vehicle.id = 1;
	vehicle.name = "F3";
	vehicle.save();
	
	raceway = Raceway();
	raceway.id = 1;
	raceway.name = "Interlagos";
	raceway.save();

	motec = MotecLoader(
		pilot=pilot,
		vehicle=vehicle,
		raceway=raceway);
	
	fname = "data/motec.csv.gz";
	fcsv = gzip.open(fname);
	motec.load(fcsv);
	
	exec_time = "%g" % (time() - timer);
	model = {'exec_time': exec_time};
	
	return render_to_response("home.html", model);
