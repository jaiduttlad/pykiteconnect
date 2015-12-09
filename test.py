import pprint 
from kiteclient import Kite
import pprint
pp = pprint.PrettyPrinter(indent=4)

# initialize kite for the first time
# if the user has already logged in, 'token' has to be passed
token = "3984358472"

kite = Kite("DK3411", token=token, debug=True)

if not token:
	# login and get the 2fa questions
	questions = kite.login(password="zerozero123", ip="127.0.0.1")

	# there will be two 2fa questions
	questions = questions["questions"]

	# set 2fa
	#print kite.update_2fa({
	#	questions[0]["id"]: "a", questions[1]["id"]: "a"
	#})

	# for testing, both answers are set to 'a'
	user = kite.do2fa([questions[0]["id"], questions[1]["id"]], ["a", "a"])

	# logged in, we have the token now
	kite.set_token(user["token"])

# send an order
try:
	print kite.order_place(
		exchange="NSE",
		tradingsymbol="RELIANCE-EQ",
		transaction_type="BUY",
		quantity=1,
		price=930,
		order_type="LIMIT",
		trigger_price="",
		product="MIS",
	)
except Exception as e:
	print e.code

# normal order = 141119000062604, amo = 141119000077821
"""
pp.pprint(kite.product_modify(
	tradingsymbol="asdad",
	exchange="adsds",
	transaction_type="BUY",
	quantity=25,
	old_product="MIS",
	new_product="NRML"
))
"""