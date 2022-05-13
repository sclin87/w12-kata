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
