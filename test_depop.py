import pytest
import depop as d

def test_generate_url_mens():
    """Function to test if mens generates the appropriate url"""
    url = d.generate_url('mens')
    assert url == 'https://www.depop.com/category/mens/'

def test_generate_url_womens():
    """Function to test if womens generates the appropriate url"""
    url = d.generate_url('womens')
    assert url == 'https://www.depop.com/category/womens/'

def test_filter_data_size():
    """Function to test the filtering function for the size"""
    sample_products = [
        {'link': 'depop.com/mens', 'price': 20.0, 'size': 'L'},
        {'link': 'depop.com/womens', 'price': 30.0, 'size': 'L'},
        {'link': 'depop.com/mens', 'price': 25.0, 'size': 'US 10.5'}
    ]

    filtered = d.filter_data_size(sample_products, 'L')
    assert len(filtered) == 2

    filtered = d.filter_data_size(sample_products, '10.5')
    assert len(filtered) == 1

    filtered = d.filter_data_size(sample_products, 'XXL')
    assert len(filtered) == 0    

def test_filter_data_size():
    """Function to test the filtering function for the price"""
    sample_products = [
        {'link': 'depop.com/mens', 'price': 20.0, 'size': 'L'},
        {'link': 'depop.com/womens', 'price': 30.0, 'size': 'M'},
        {'link': 'depop.com/mens', 'price': 25.0, 'size': '10.5'}
    ]

    filtered = d.filter_data_price(sample_products, 20)
    assert len(filtered) == 1

    for f in filtered:      
        assert f['price'] == 20

