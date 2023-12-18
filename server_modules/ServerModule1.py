import anvil.tables as tables
from anvil.tables import app_tables
import anvil.tables.query as q
import anvil.server

###############################################################################
##  This code implements a double-entry bookkeeping system. To learn more,   ##
##  read our blog post:                                                      ##
##                                                                           ##
##      https://anvil.works/blog/double-entry-accounting-for-engineers       ##
##                                                                           ##
###############################################################################


@anvil.server.callable
def get_accounts():
  return app_tables.accounts.search()


@anvil.server.callable
@tables.in_transaction
def add_new_transaction(date, from_ac, to_ac, amount, description):
  txn = app_tables.transactions.add_row(description=description, date=date)
  
  app_tables.journal_entries.add_row(account=to_ac, change=amount, date=date, transaction=txn)
  app_tables.journal_entries.add_row(account=from_ac, change=-amount, date=date, transaction=txn)  


def get_balance_for_account(account, date):
  balance = 0

  for entry in app_tables.journal_entries.search(account=account,
                                                 date=q.less_than(date)):
    balance += entry['change']

  return balance

  
@anvil.server.callable
def get_balance_sheet(date):
  # Total up transactions for all balance-sheet accounts
  # up to the specified date
  
  return [{'name': account['name'], 'balance': get_balance_for_account(account, date)}
          for account in app_tables.accounts.search(tables.order_by('name'), balance_sheet=True)]


def get_profit_for_account(account, from_date, to_date):
  profit = 0

  for entry in app_tables.journal_entries.search(account=account,
                                                 date=q.between(from_date, to_date)):
    # Subtract, because any money going out of a P&L account
    # is a gain for us, and any money going in is a loss for us.
    profit -= entry['change']

  return profit


@anvil.server.callable
def get_profit_and_loss(from_date, to_date):
  # Total up all transactions for profit-and-loss accounts
  # up to the specified date

  return [{'name': account['name'], 'profit': get_profit_for_account(account, from_date, to_date)}
          for account in app_tables.accounts.search(tables.order_by('name'), balance_sheet=False)]


@anvil.server.callable
def get_account_history(account):
  bal = 0
  hist = []
  for r in app_tables.journal_entries.search(tables.order_by('date'), account=account):
    bal += r['change']
    hist.append({'date': r['date'], 'description': r['transaction']['description'], 'change': r['change'], 'balance': bal if account['balance_sheet'] else None})
    
  return hist

