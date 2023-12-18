from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
import Globals

class AccountHistory(AccountHistoryTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.account_dd.items = [("Select account", None)] + [(r['name'], r) for r in Globals.accounts]

  def account_dd_change(self, **event_args):
    """This method is called when an item is selected"""
    
    account = self.account_dd.selected_value
    if account is None:
      self.account_history_pnl.visible = False
    else:
      self.account_history_pnl.visible = True
      self.type_lbl.text = "Balance Sheet" if account['balance_sheet'] else "Profit and Loss"
      self.repeating_panel_1.items = anvil.server.call('get_account_history', account)

