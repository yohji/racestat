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

from django.db import models


class Pilot(models.Model):
    name = models.CharField(max_length=200);
    

class Raceway(models.Model):
    name = models.CharField(max_length=200);
    

class Vehicle(models.Model):
    name = models.CharField(max_length=200);
    

class Session(models.Model):
    pilot = models.ForeignKey(Pilot);
    vehicle = models.ForeignKey(Vehicle);
    raceway = models.ForeignKey(Raceway);
    date = models.DateTimeField();
    duration = models.TimeField();


class Lap(models.Model):
    session = models.ForeignKey(Session);
    time = models.TimeField();


class Data(models.Model):
    lap = models.ForeignKey(Lap);
    time = models.TimeField();
    distance = models.FloatField();
    glat = models.FloatField();
    yawrate = models.FloatField();
    steerangle = models.FloatField();
    speed = models.FloatField();
    glon = models.FloatField();
    gaspedal = models.FloatField();
    brakepedal = models.FloatField();
    gear = models.FloatField();
