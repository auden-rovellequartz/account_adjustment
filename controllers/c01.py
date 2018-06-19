# -*- coding: utf-8 -*-

def home():
	amount = 0
	balance_rows = db(db.balance.id > 0).select()
	for x in balance_rows:
		amount = x.cash
	form = FORM(
		INPUT(
			_type = "text",
			_name = "spent",
			),
		INPUT(
			_type = "submit",
			_value = "Spend",
			)
		)
	if (form.process().accepted):
		new_balance = int(amount) - int(form.vars.spent)
		balance_rows[0].update_record(
			cash = new_balance,
			)
		db.commit()
		redirect(
			URL(
				a = "account_adjustment",
				c = "c01",
				f = "home",
				)
			)
	return dict(
		amount = amount,
		form = form,
		)
