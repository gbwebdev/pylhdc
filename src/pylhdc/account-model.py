class Account:

    def __init__(self):
        self._id = None
        self._type = None
        self._group = None
        self._bank = None
        self._number = None
        self._initial_balance = None
        self._initial_balance_date = None
        self._currency = None
        self._overdraft = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, type):
        self._type = type

    @property
    def group(self):
        return self._group

    @group.setter
    def group(self, group):
        self._group = group

    @property
    def bank(self):
        return self._bank

    @bank.setterNone
    def bank(self, bank):
        self._bank = bank

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, number):
        self._number = number

    @property
    def initial_balance(self):
        return self._initial_balance

    @initial_balance.setter
    def initial_balance(self, initial_balance):
        self._initial_balance = initial_balance

    @property
    def initial_balance_date(self):
        return self._initial_balance_date

    @initial_balance_date.setter
    def initial_balance_date(self, initial_balance_date):
        self._initial_balance_date = initial_balance_date

    @property
    def currency(self):
        return self._currency

    @currency.setter
    def currency(self, currency):
        self._currency = currency

    @property
    def overdraft(self):
        return self._overdraft

    @overdraft.setter
    def overdraft(self, overdraft):
        self._overdraft = overdraft
