# coding:utf-8 
import logging
import json
import urllib.request  
import urllib.parse  
import http.cookiejar
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
DOMAIN = 'se7en_voice'
CONF_USERNAME = 'username'
CONF_PASSWORD = 'password'
ATTR_TEXT = 'text'
DEFAULT_TEXT = '0648'
ATTR_MOBILE = 'mobile'
DEFAULT_MOBILE = '18627899544'
voice_send_url = "http://api.vm.ihuyi.com/webservice/voice.php?method=Submit"
_LOGGER = logging.getLogger(__name__)
CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_USERNAME): cv.string,
        vol.Required(CONF_PASSWORD): cv.string,
    }),
}, extra=vol.ALLOW_EXTRA)
def setup(hass, config):
    def handle_hello(call):
        conf = config[DOMAIN]
        params = urllib.parse.urlencode({'account': conf.get(CONF_USERNAME), 'password': conf.get(CONF_PASSWORD), 'content': call.data.get(ATTR_TEXT, DEFAULT_TEXT), 'mobile':call.data.get(ATTR_MOBILE, DEFAULT_MOBILE)	,'format':'json'}).encode('utf-8')
        headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        req = urllib.request.Request(voice_send_url,params,headers)
        urllib.request.urlopen(req).read().decode('utf-8')
    hass.services.register(DOMAIN, 'send_voice', handle_hello)
    
    return True

