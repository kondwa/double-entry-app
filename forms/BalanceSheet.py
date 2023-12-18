from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import date

class BalanceSheet(BalanceSheetTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.date_picker.date = date.today()
    self.date_picker_change()

  def date_picker_change(self, **event_args):
    """This method is called when the selected date changes"""
    if self.date_picker.date is None:
      self.data_grid_1.visible = False
    else:
      self.data_grid_1.visible = True
      balance_sheet = anvil.server.call('get_balance_sheet', self.date_picker.date)
      self.repeating_panel_1.items = balance_sheet
      self.total_lbl.text = "$ %1.02f" % sum((acc['balance'] for acc in balance_sheet))


