#
#    Copyright (c) 2011 Marco Merli <yohji@marcomerli.net>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software Foundation,
#    Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import gzip;
from time import time;

from django.http import HttpResponse;

from mod.core.models import Pilot;
from mod.core.models import Vehicle;
from mod.core.models import Raceway;
from mod.core.models import Session;
from mod.core.models import Lap;
from mod.core.models import Data;
from mod.core.load.motec import MotecLoader;


def index(request):

    return HttpResponse("Racestat is running.. ;)");

def load(request):
    
    timer = time();
    
    Data.objects.all().delete();
    Lap.objects.all().delete();
    Session.objects.all().delete();
    Raceway.objects.all().delete();
    Vehicle.objects.all().delete();
    Pilot.objects.all().delete();
    
    test_pilot = Pilot();
    test_pilot.id = 1;
    test_pilot.name = "Marco Merli";
    test_pilot.save();
    
    test_vehicle = Vehicle();
    test_vehicle.id = 1;
    test_vehicle.name = "Osella";
    test_vehicle.save();
    
    test_raceway = Raceway();
    test_raceway.id = 1;
    test_raceway.name = "Prato - Full GP";
    test_raceway.save();
    
    motec = MotecLoader(
        test_pilot,
        test_vehicle,
        test_raceway);
    
    fname = "data/motec.csv.gz";
    fcsv = gzip.open(fname);
    motec.load(fcsv);
    
    return HttpResponse("Completed! ;) Time: %g sec" % (time() - timer));
