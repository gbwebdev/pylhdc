class Transaction:

    def __init__(self):
        self._id = None
        self._parent = None
        self._date = None
        self._source_account = None
        self._destination_account = None
        self._amount = None
        self._title = None
        self._mean_of_payment = None
        self._third_party = None
        self._info = None
        self._category = None
        self._validation = None
        self._status = None

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent):
        self._parent = parent

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        self._date = date

    @property
    def source_account(self):
        return self._source_account

    @source_account.setter
    def source_account(self, source_account):
        self._source_account = source_account

    @property
    def destination_account(self):
        return self._destination_account

    @destination_account.setter
    def destination_account(self, destination_account):
        self._destination_account = destination_account

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, amount):
        self._amount = amount

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title
    @property
    def mean_of_payment(self):
        return self._mean_of_payment

    @mean_of_payment.setter
    def mean_of_payment(self, mean_of_payment):
        self._mean_of_payment = mean_of_payment

    @property
    def third_party(self):
        return self._third_party

    @third_party.setter
    def third_party(self, third_party):
        self._third_party = third_party

    @property
    def info(self):
        return self._info

    @info.setter
    def info(self, info):
        self._info = info

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        self._category = category

    @property
    def validation(self):
        return self._validation

    @validation.setter
    def validation(self, validation):
        self._validation = validation

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status