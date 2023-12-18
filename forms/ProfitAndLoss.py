from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
from datetime import date

class ProfitAndLoss(ProfitAndLossTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.to_date_picker.date = date.today()
    self.update_date()

  def update_date(self, **event_args):
    """This method is called when the selected date changes"""
    
    from_date = self.from_date_picker.date
    to_date = self.to_date_picker.date
    
    if from_date is None or to_date is None:
      self.data_grid_1.visible = False
      
    else:
      self.data_grid_1.visible = True
      pnl = anvil.server.call('get_profit_and_loss', from_date, to_date)
      self.repeating_panel_1.items = pnl
      self.total_lbl.text = "$ %1.02f" % sum((acc['profit'] for acc in pnl))


