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

import csv;
from datetime import datetime;
from datetime import timedelta;
from time import time;

from django.db import transaction;

from app.racestat.loader import Loader;
from app.racestat.models import Session;
from app.racestat.models import Lap;
from app.racestat.models import Data; 


class MotecLoader(Loader):
	
	session = None;
	timelaps = list();
	datalaps = list();

	clap = None;
	cidx = 0;
	cclock = 1;
	
	def load(self, fcsv):
		
		timer = time();
		rcsv = csv.reader(fcsv, delimiter=",", quotechar='"');
		
		self.session = Session();
		self.session.pilot = self.pilot;
		self.session.vehicle = self.vehicle;
		self.session.raceway = self.raceway;
		
		sdate = stime = sdur = None;
		nline = 1;

		for line in rcsv:

			if (nline == 18):
				self.__load_session(sdate, stime, sdur);
			
			elif (nline >= 19):
				self.__load_laps(line);
			
			else:
				if (nline == 7):
					sdate = line[1];
				elif (nline == 8):
					stime = line[1];
				elif (nline == 10):
					sdur = line[1];
				elif (nline == 12):
					l = line[1].split(",");
					i = 0;
					while (i < len(l)):
						if (i == 0):
							n = float(l[i]);
							self.timelaps.append(n);
						else:
							n = float(l[i]) - float(l[i - 1]);
							self.timelaps.append(n);
						i += 1;

			nline += 1;

		print("metadata: %g sec" % (time() - timer));
		timer = time();
		
		self.__write_data();
		print("data: %g sec" % (time() - timer));
					 
		fcsv.close();
		
	def __load_session(self, sdate, stime, sdur):
		
		t = sdate + " " + stime;
		self.session.date = datetime.strptime(t, "%m/%d/%y %H:%M:%S");
		self.session.duration = timedelta(0, float(sdur));
		self.session.save();
	
	def __load_laps(self, line):
		
		t = float(line[0]);
		if (t < self.cclock):
			self.clap = Lap();
			self.clap.session = self.session;
			self.clap.time = timedelta(0, self.timelaps[self.cidx]);
			self.clap.save();
			self.cidx += 1;
			
		d = Data();
		d.lap = self.clap;
		d.time = timedelta(0, float(line[0]));
		d.distance = float(line[1]);
		d.glat = float(line[2]);
		d.yawrate = float(line[3]);
		d.steerangle = float(line[4]);
		d.speed = float(line[5]);
		d.glon = float(line[6]);
		d.gaspedal = float(line[7]);
		d.brakepedal = float(line[8]);
		d.gear = float(line[9]);
		self.datalaps.append(d);

		self.cclock = t;
		
	@transaction.commit_manually
	def __write_data(self):
		
		for data in self.datalaps:
			data.save();
		
		transaction.commit();
