"""
the following operation/ methods can be used along with XPATH

1. and             - both xpath used should be matched
eg: //*[@id='search_query_top' and @name='search_query']

2. or              - one of the xpath used should be matched
eg: //*[@id='search_query_top' or @name='search_query']

3. contains()      - match the elements contains the given text
eg: //*[contains(@id,'st')]

4. starts-with()   - match the elements starts-with the given text
eg: //*[starts-with(@id,'st')]

5. text()          - used when a element contains any text
eg: //*[text()='Women']
"""
