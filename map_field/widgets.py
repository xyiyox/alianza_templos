
from django.conf import settings
from django.forms import widgets
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe
from django.forms.utils import flatatt



class MapsGeoPointhWidget(widgets.TextInput):
    
    class Media:
        css = {'all': (
            settings.STATIC_URL + 'main/leaflet/leaflet.css?v=0-7-7',
            settings.STATIC_URL + 'map_field/css/map_field.css',
        ),}
        js = (
            '//ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js',
            settings.STATIC_URL + 'main/leaflet/leaflet.js?v=0-7-7',
            settings.STATIC_URL + 'map_field/js/map_field.js?v=5',
        )

    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_text(self._format_value(value))
        return mark_safe(u'<div class="map_canvas_wrapper"><div id="map_canvas"></div><input %s/></div>' % ( flatatt(final_attrs)) )