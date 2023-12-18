from ._anvil_designer import NewTransactionTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables
import Globals
from datetime import date

class NewTransaction(NewTransactionTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    account_options = [("Select account", None)] + [(r['name'], r) for r in Globals.accounts]
    self.from_dd.items = self.to_dd.items = account_options
    self.date_picker.date = date.today()
    
    

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    
    anvil.server.call('add_new_transaction', self.date_picker.date,
                                             self.from_dd.selected_value,
                                             self.to_dd.selected_value,
                                             self.amount_box.text,
                                             self.description_box.text)
    alert("Transaction added.")
    self.amount_box.text = None
    self.description_box.text = ''
