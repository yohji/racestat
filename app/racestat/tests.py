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
from unittest2 import TestCase;

from app.racestat.models import Pilot;
from app.racestat.models import Vehicle;
from app.racestat.models import Raceway; 
from app.racestat.core.motec import MotecLoader;


class TestCaseUnit(TestCase):
	
	test_pilot = None;
	test_vehicle = None;
	test_raceway = None;
	
	def setUp(self):
		
		self.test_pilot = Pilot();
		self.test_pilot.name = "Marco Merli";
		self.test_pilot.save();
		
		self.test_vehicle = Vehicle();
		self.test_vehicle.name = "Osella";
		self.test_vehicle.save();
		
		self.test_raceway = Raceway();
		self.test_raceway.name = "Prato - Full GP";
		self.test_raceway.save();


class MotecLoaderTest(TestCaseUnit):
	
	def test_load(self):

		motec = MotecLoader(
			self.test_pilot,
			self.test_vehicle,
			self.test_raceway);
			
		fname = "data/motec.csv.gz";
		fcsv = gzip.open(fname);
		motec.load(fcsv);

