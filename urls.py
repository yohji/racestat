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

from django.conf.urls.defaults import *
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('app.racestat.web',

	(r'^$', 'home.index'),
	(r'^session/$', 'session.sessions'),
	(r'^session/(?P<session_id>\d+)/$', 'session.laps'),
	(r'^load/$', 'load.show'),
	(r'^load/submit/$', 'load.submit'),
	(r'^test/$', 'home.test'),

	(r'^admin/', include(admin.site.urls)),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)

urlpatterns += patterns('',
	url(r'^(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_DOC_ROOT, 'show_indexes': True}),
)
