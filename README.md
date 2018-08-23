# JTrans

Non-official [Yahoo!(R) Transit Search](https://transit.yahoo.co.jp/) on command line.

# Installation

    pip install jtrans

# Example

    $ jtrans-cli route 大島 高尾山口 --date 2018-01-01 --time 08:00

This will get you several routes from 大島 to 高尾山口 departing at 08:00 on 2018-01-01.

The options `--date` and `--time` can be omit as to search routes for the current time. (For now it only accept JST +9 timezone)

Feel free to try any other routes or time point.

# Note

Requires Python3.

Only part of options are supported for now.

`Yahoo!` is the trademark owned by [Yahoo! Japan](https://www.yahoo.co.jp/) in Japan.
