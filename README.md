# JSON Key/Value Pair Storage Script

This script allows for easy persistent storiage of Keys and Values into a JSON file.

## Commands

It supports the following commands

### View

`[-v] <KeyName>` Flag isn't required for this

View a Value from a given Key

### Save

`-w <NewValue>` flag

Save a new Value with a given Key

### Delete

`-d <KeyName>` flag

Delete a Value and Key Pair

### Search

`-s <SearchString>` flag

Search for keys with a given search value

## Usage

`kv.py <JSON File> [<Key> [-w <New Value>] | -s <SearchString> | -d <Key>]`