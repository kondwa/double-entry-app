from ._anvil_designer import AccountHistoryRowTemplateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

class AccountHistoryRowTemplate(AccountHistoryRowTemplateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.