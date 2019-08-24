# JSON Key/Value Pair Storage Script

This script allows for easy persistent storiage of Keys and Values into a JSON file.

This program is designed to __NOT FAIL__. This means that if a bad key is supplied, then the program will print nothing and exit.

## Commands

It supports the following commands

### View

`[-v] <KeyName>` Flag isn't required for this

View a Value from a given Key. If the key does not exist, then nothing will print out (It fails silently).

### Save

`-w <NewValue>` flag

Save a new Value with a given Key. If the key doesn't exist, then one will be created.

### Delete

`-d <KeyName>` flag

Delete a Value and Key Pair. If the key doesn't exist, then nothing will happen.

### Search

`-s <SearchString>` flag

Search for keys with a given search value.

## Usage

`kv.py <JSON File> [<Key> [-w <New Value>] | -s <SearchString> | -d <Key>]`

KV Supports performing multiple operations on the JSON File, but only for certain ones. If a Strictly-Single Operation, then the first one found will be used and then the program will exit.

`kv.py <JSON File> ...`

Strictly-Single Operations:

`[-s <SearchString>]` - Search for a string in the keys

For Multiple Operations: There are a few separate blocks that are supported...

`[<Key> -w <New Value>]`

`[-d <Key>]`

`[-v <Key>]`
