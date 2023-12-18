from anvil import *
import anvil.server
import anvil.tables as tables
from anvil.tables import app_tables

class Home(HomeTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    
    # Start off on the "Account History" page
    self.bs_link_click()
    
  def select_link(self, lnk):
    for link in self.sidebar_pnl.get_components():
      link.role = None
    lnk.role = "selected"
    self.content_panel.clear()

  def hist_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.select_link(self.hist_link)
    from AccountHistory import AccountHistory
    self.content_panel.add_component(AccountHistory())

  def new_tx_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.select_link(self.new_tx_link)
    from NewTransaction import NewTransaction
    self.content_panel.add_component(NewTransaction())
    
  def bs_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.select_link(self.bs_link)
    from BalanceSheet import BalanceSheet
    self.content_panel.add_component(BalanceSheet())

  def pl_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.select_link(self.pl_link)
    from ProfitAndLoss import ProfitAndLoss
    self.content_panel.add_component(ProfitAndLoss())


  

  


  

