import logging
_logger = logging.getLogger(__name__)

try:
    import feedparser
except ImportError:
    pass

def rate_retrieve():
    banxico_rss_url = "http://www.banxico.org.mx/rsscb/rss?BMXC_canal=pagos&BMXC_idioma=es" 
    feed = feedparser.parse(banxico_rss_url)
    rate = 0.0
    for f in feed.entries:
        rate = f and f.cb_exchangerate or 0.0
    return rate

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: