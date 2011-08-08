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

from django.db import models


class Pilot(models.Model):
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name


class Raceway(models.Model):
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name
	

class Vehicle(models.Model):
	name = models.CharField(max_length=64)

	def __unicode__(self):
		return self.name
	

class Session(models.Model):
	pilot = models.ForeignKey(Pilot)
	vehicle = models.ForeignKey(Vehicle)
	raceway = models.ForeignKey(Raceway)
	date = models.DateTimeField()
	duration = models.TimeField()

	def __unicode__(self):
		return "%s" % (self.date)


class Lap(models.Model):
	session = models.ForeignKey(Session)
	number = models.IntegerField()
	time = models.TimeField()
	distance = models.FloatField(null=True)
	max_speed = models.FloatField(null=True)
	avg_speed = models.FloatField(null=True)
	max_glat = models.FloatField(null=True)
	max_glon= models.FloatField(null=True)
	avg_gas = models.FloatField(null=True)
	avg_brake = models.FloatField(null=True)
	avg_gear = models.FloatField(null=True)

	def __unicode__(self):
		return "%s|%s|%s" % (self.session, self.number, self.time)


class Data(models.Model):
	lap = models.ForeignKey(Lap)
	time = models.TimeField()
	distance = models.FloatField()
	glat = models.FloatField()
	yawrate = models.FloatField()
	steerangle = models.FloatField()
	speed = models.FloatField()
	glon = models.FloatField()
	gaspedal = models.FloatField()
	brakepedal = models.FloatField()
	gear = models.FloatField()

	def __unicode__(self):
		return "%s|%s" % (self.lap, self.time)

