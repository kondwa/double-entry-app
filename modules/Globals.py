import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables


accounts = anvil.server.call('get_accounts')
