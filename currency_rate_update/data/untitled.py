import oerplib
env = oerplib.OERP('localhost', protocol='xmlrpc', port=8069)
user = env.login('admin', 'admin', 'dbname')

currency_obj = env.get('res.currency')
print 'currency_obj', currency_obj.run_currency_update([])