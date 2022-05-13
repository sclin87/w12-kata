from bookStore import Customer


def testBasics():
    customer = Customer()
    customer.buyList([])
    assert 0 == customer.checkout()
    customer.buyList([1])
    assert 8 == customer.checkout()
    customer.buyList([2])
    assert 8 == customer.checkout()
    customer.buyList([3])
    assert 8 == customer.checkout()
    customer.buyList([4])
    assert 8 == customer.checkout()
    customer.buyList([1, 1, 1])
    assert 8 * 3 == customer.checkout()


def testSimpleDiscounts():
    customer = Customer()
    customer.buyList([0, 1])
    assert 8 * 2 * 0.95 == customer.checkout()
    customer.buyList([0, 2, 4])
    assert 8 * 3 * 0.9 == customer.checkout()
    customer.buyList([0, 1, 2, 4])
    assert 8 * 4 * 0.8 == customer.checkout()
    customer.buyList([0, 1, 2, 3, 4])
    assert 8 * 5 * 0.75 == customer.checkout()


def testSeveralDiscounts():
    customer = Customer()
    customer.buyList([0, 0, 1])
    assert 8 + (8 * 2 * 0.95) == customer.checkout()
    customer.buyList([0, 0, 1, 1])
    assert 2 * (8 * 2 * 0.95) == customer.checkout()
    customer.buyList([0, 0, 1, 2, 2, 3])
    assert (8 * 4 * 0.8) + (8 * 2 * 0.95) == customer.checkout()
    customer.buyList([0, 1, 1, 2, 3, 4])
    assert 8 + (8 * 5 * 0.75) == customer.checkout()


def testEdgeCases():
    customer = Customer()
    customer.buyList([0, 0, 1, 1, 2, 2, 3, 4])
    assert 2 * (8 * 4 * 0.8) == customer.checkout()
    customer.buyList([0, 0, 0, 0, 0,
                      1, 1, 1, 1, 1,
                      2, 2, 2, 2,
                      3, 3, 3, 3, 3,
                      4, 4, 4, 4])
    assert 3 * (8 * 5 * 0.75) + 2 * (8 * 4 * 0.8) == customer.checkout()
